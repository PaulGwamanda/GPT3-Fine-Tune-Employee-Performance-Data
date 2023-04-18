##  This is a GPT3 Fine Tuned Employee Performance Data evaluation project.
> Essential we're creating a custom Fine Tuned model that evaluates Employee Performance Data based on employee/manager evaluations. 

Given the employee data which we find under datasets/DATASET_dummy_employee_data.json
We need to be able to prompt GPT-3 in the following manner in order to get employee/manager evaluations:

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
