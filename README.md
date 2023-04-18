##  This is a GPT3 Fine Tuned Employee Performance Data evaluation project.
> Essentially we're creating a custom Fine Tuned model that evaluates Employee Performance Data based on employee/manager evaluations. 

Given the employee data which we find under datasets/DATASET_dummy_employee_data.json <br/>
A company executive needs to be able to prompt GPT-3 in the following manner in order to get employee/manager evaluations based on their performance reviews for the quarter:

Potential questions he may be interested in asking:

Who is the lowest-rated employee this quarter and why?
> John Williams is the lowest-rated employee this quarter, with an overall rating of 2.5. His manager evaluation indicates he needs improvement in multiple competencies and is not meeting expectations.

How does Jane Smith handle organization and planning?
> she thinks she excels, rating herself a 5 with her own self evaluation being 'I excel in providing effective management, motivation, and leadership to my team. I am skilled at setting clear expectations, providing constructive feedback, and empowering team members to achieve their best performance. I am recognized for my ability to inspire and lead by example.'but she is a poor leader according to her manager

Who is the weakest performing employee this quarter and why?
> John Williams, he has the lowest manager rating of all the employees in this quarter, rating on average 2.5 overall.

What is the sentiment score for the marketing team this quarter?
> The sentiment score for the marketing team this quarter is 0.8, which indicates a positive sentiment overall.

Who is the lowest-rated employee this quarter and why?
> John Williams is the lowest-rated employee this quarter, with an overall rating of 2.5. His manager evaluation indicates he needs improvement in multiple competencies and is not meeting expectations.


Given the wanted input/output requirements above, the training data we need to provide openai for Fine Tuning should look as follows:
```
{Prompt: "Describe Jane Lane Doe's performance in customer focus."
Completion: "she has a low rating, her manager says she has room to improve"}

{Prompt: "How does Jane Lane Doe handle organization and planning?"
Completion: "she thinks she excels, rating herself a 5 with her own self evaluation being 'I excel in providing effective management, motivation, and leadership to my team. I am skilled at setting clear expectations, providing constructive feedback, and empowering team members to achieve their best performance. I am recognized for my ability to inspire and lead by example.'but she is a poor leader according to her manager"}

{Prompt: "what rating did Jane Doe give herself for customer focus"
Completion: "she gave herself a 2"}
```



# Step 1: 
Create prompt/completion pairs based off the original data

# Step 2: 
Convert the prompt completion pair files into jsonl format


# Step 3: 
train the model on the json l file


# Step 4: 
test the model

Fine_Tune_custom_
