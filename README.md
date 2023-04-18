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

> * "Given the data below of employee/manager performance evaluation, give me several generated samples in the same json format using the same competency categories ("Customer Focus", "Organisation & Planning", "Management Motivation & Leadership", "Bottom Line Focus", "Initiative", "Innovation", "Numbers", "Effectiveness & Delivery", "For the love of the game").*
> * It is important to keep the context of the generated samples in similar alignment with the rating structure and competency categories structure.*

```
dataset to use as an example to model:
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
      },
      {
        "competency": "Organisation & Planning",
        "employee_evaluation": {
          "rating": 4,
          "comment": "I maintain an organized approach to work."
        },
        "manager_evaluation": {
          "rating": 4.5,
          "comment": "Consistently demonstrates effective organization and planning skills."
        }
      },
```

## Steps

<br/>

***Step 1:*** 
Generate prompt completion pairs:
*Under /prompts, copy the contents of GENERATE_prompt_completion_pairs.txt and paste it into ChatGpt.

The output format should be in jsonl format like this: 
<br/>
```{"prompt": "What is John Smith's department?", "completion": "data science"}``` <br />
```{"prompt": "Is jane smith a good employee?", "completion": "Yes, she has scored above average in her manager evaluation"}``` <br />
```{"prompt": "Who is John Smith's manager?", "completion": "John Williams"}``` <br />
```{"prompt": "What is John Smith's competency rating for Customer Focus according to his manager?", "completion": "1.5"}``` <br />


***Step 2:*** 
Convert the prompt completion pair files into jsonl format


***Step 3:*** 
train the model on the json l file


***Step 4:*** 
test the model

Fine_Tune_custom_
