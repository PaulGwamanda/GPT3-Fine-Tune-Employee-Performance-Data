##  This is a GPT3 Fine Tuned Employee Performance Data evaluation project.
### Essentially we're creating a custom Fine Tuned model that evaluates Employee Performance based on employee/manager evaluations. 
<br/>

A company executive wants to use natural language to get insights into his employee/manager evaluations based on their performance reviews that quarter:

<br/>

*"Who is the lowest-rated employee this quarter and why?"*
> *John Williams is the lowest-rated employee this quarter, with an overall rating of 2.5. His manager evaluation indicates he needs improvement in multiple competencies and is not meeting expectations.*

*"How does Jane Smith handle organization and planning?"*
> *she thinks she excels, rating herself a 5 with her own self evaluation being 'I excel in providing effective management, motivation, and leadership to my team. I am skilled at setting clear expectations, providing constructive feedback, and empowering team members to achieve their best performance. I am recognized for my ability to inspire and lead by example.'but she is a poor leader according to her manager*

*"How does Brad Wilson rate in terms of Leadership skills according to his employee evaluation?"*
> *Brad Wilson has a rating of 3 for the competency Leadership according to his employee evaluation.*

*"What is the sentiment score for the marketing team this quarter?"*
> *The sentiment score for the marketing team this quarter is 0.8, which indicates a positive sentiment overall.*

*"Who is the lowest-rated employee this quarter and why?"*
> *John Williams is the lowest-rated employee this quarter, with an overall rating of 2.5. His manager evaluation indicates he needs improvement in multiple competencies and is not meeting expectations.*

<br/>

### Given the wanted input/output requirements above, the training data we need to provide openai for finetuning should therefore look like this:

<br/>

```ruby
{Prompt: "Describe Jane Lane Doe's performance in customer focus."
Completion: "she has a low rating, her manager says she has room to improve"}

{Prompt: "How does Jane Lane Doe handle organization and planning?"
Completion: "she thinks she excels, rating herself a 5 with her own self evaluation being 'I excel in providing effective management, motivation, and leadership to my team. I am skilled at setting clear expectations, providing constructive feedback, and empowering team members to achieve their best performance. I am recognized for my ability to inspire and lead by example.'but she is a poor leader according to her manager"}

{Prompt: "what rating did Jane Doe give herself for customer focus"
Completion: "she gave herself a 2"}
```

### ...generated from our dataset under 'datasets/DATASET_dummy_employee_data.json' which looks like this: 
<br/>

```ruby
{
    "DisplayName": "John Smith",
    "department": "data science",
    "job_title": "HR Manager",
    "manager": "John Williams",
    "quarter": "1",
    "CombinedF": [
      {
        "competency": "Customer Focus",
        "employee_evaluation": {
          "rating": 2,
          "comment": "Needs improvement in meeting customer needs and displaying a customer-centric attitude."
        },
        "manager_evaluation": {
          "rating": 1.5,
          "comment": "Rarely meets expectations in customer focus and needs to improve."
        }
      },
    ]
  }
```

### ...we should be able to extract the features we want for finetuning by prompting ChatGPT like this:

```
Give me 10 prompt/completion pairs based on the following:
The prompts or questions must be asked as if coming from a CEO or high level company executive interested in the performance of his employees and relevant departments this quarter based on the Employee_dataset file.

An example of a prompt/completion format would be like this:
{"Prompt": "How does Jane Thunder rate in terms of customer focus?", "completion": "Jane Thunder has a low rating for customer focus, with her manager indicating she has room for improvement in this area."}
{Prompt: "Describe Jane Lane Doe's performance in customer focus." Completion: "She has a low rating, her manager says she has room to improve"}
{Prompt: "How does Jane Lane Doe handle organization and planning?"Completion: "she thinks she excels, rating herself a 5 with her own self evaluation being 'I excel in providing effective management, motivation, and leadership to my team. I am skilled at setting clear expectations, providing constructive feedback, and empowering team members to achieve their best performance. I am recognized for my ability to inspire and lead by example.'but she is a poor leader according to her manager"}
{Prompt: "What rating did Jane Doe give herself for customer focus" Completion: "She gave herself a 2, saying she could do a lot more in providing good customer service."}

Employee_dataset:

{
  "QueryResponse": {
  "Employees": [
              {
        "DisplayName": "John Smith",
        "department": "data science",
        "job_title": "HR Manager",
        "manager": "John Williams",
        "quarter": "1",
         "CombinedF": [
         {
        "competency": "Customer Focus",
        "employee_evaluation": {
          "rating": 2,
          "comment": "I need improvement in meeting customer needs and displaying a customer-centric attitude."
        },
        "manager_evaluation": {
          "rating": 1.5,
          "comment": "Rarely meets expectations in customer focus and needs to improve."
        }
      }
  ]
}
```


** *The full prompt file can be found under /prompts. Copy the contents of GENERATE_prompt_completion_pairs.txt and paste it into ChatGpt.**

The output format should be in jsonl format like this: 
<br/>
```{"prompt": "What is John Smith's department?", "completion": "data science"}``` <br />
```{"prompt": "Is jane smith a good employee?", "completion": "Yes, she has scored above average in her manager evaluation"}``` <br />
```{"prompt": "Who is John Smith's manager?", "completion": "John Williams"}``` <br />
```{"prompt": "What is John Smith's competency rating for Customer Focus according to his manager?", "completion": "1.5"}``` <br />


***Train the model:*** 

```openai api fine_tunes.create -t 'training\final.jsonl' -m currie --n_epochs 100```

*Running this command will finetune your custom training data on the "currie" model and train for 100 epochs (https://platform.openai.com/docs/guides/fine-tuning/advanced-usage)

***Test the model:*** 

```openai api completions.create -m curie:ft-personal-2023-04-18-19-01-44 -p 'How does John Doe rank in the Customer Focus category?'```
<sub> *Replace "curie:ft-personal-2023-04-18-19-01-44" with your actual model name </sub>
