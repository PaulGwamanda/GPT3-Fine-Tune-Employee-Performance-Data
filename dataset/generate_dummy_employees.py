import json
import random

# List of possible values for each field
DEPARTMENTS = ["Web development", "Data science", "Marketing", "Human resources", "Risk Management Department", "Compliance Department", "Design department",
               "IT and Technology Department", "Call Center Department", "Sales and Marketing Department", "Research and Analysis Department", "Finance"]
DISPLAY_NAMES = ["Bongani Dlamini", "Thabo Ndlovu", "Jabulani Mthembu", "Lerato Kgosi", "Perd Engelbrecht", "Doos Du Plessis", "Johan Erasmus", "John Steenhuisen", "Lerato Kgosi", "Peter Mulder", "Faf de Klerk", "Jane Celliers"]
MANAGERS = {
    "John Williams": "Marketing",
    "Sarah Thompson": "Data science",
    "David Lee": "Human resources",
    "Jennifer Miller": "Web development",
    "Adriaan van Heerden": "Risk Management Department",
    "Hennie Nel": "Compliance Department",
    "Koos Scheepers": "Design department",
    "Sakkie Fourie": "IT and Technology Department",
    "Sampie Smit": "Call Center Department",
    "Jaco du Toit": "Sales and Marketing Department",
    "Stoffel van der Merwe": "Research and Analysis Department",
    "Wilhelm Snyman": "Finance"
}
JOB_TITLES = ["Software Developer", "Digital Marketer", "Graphic Designer", "Accountant", "Support Specialist",
              "Fraud Analyst", "Copywriter", "IT Technician", "QA", "Risk analyst", "Affiliate manager", "Product Owner","Gaming Specialist"]
QUARTERS = ["1"]


# Function to generate random evaluation ratings and comments
def generate_evaluation():
    rating = round(random.choice([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]), 1)
    comment = ""
    return {"rating": rating, "comment": comment}


# Generate random data for each competency
def generate_competency(competency):
    employee_evaluation = generate_evaluation()
    manager_evaluation = generate_evaluation()
    return {
        "competency": competency,
        "employee_evaluation": employee_evaluation,
        "manager_evaluation": manager_evaluation
    }


# Generate random data for all employees
def generate_employee():
    department = random.choice(DEPARTMENTS)
    display_name = random.choice(DISPLAY_NAMES)
    manager = random.choice(list(MANAGERS.keys()))
    job_title = random.choice(JOB_TITLES)
    quarter = random.choice(QUARTERS)
    competencies = [
        generate_competency("Customer Focus"),
        generate_competency("Organisation & Planning"),
        generate_competency("Management, Motivation & Leadership"),
        generate_competency("Bottom Line Focus"),
        generate_competency("Initiative"),
        generate_competency("Innovation"),
        generate_competency("Numbers"),
        generate_competency("Effectiveness & Delivery"),
        generate_competency("For the love of the game")
    ]
    return {
        "displayName": display_name,
        "department": MANAGERS[manager],
        "job_title": job_title,
        "manager": manager,
        "quarter": quarter,
        "combinedF": competencies
    }


# Generate JSON data
data = {
    "QueryResponse": {
        "employees": [generate_employee() for _ in range(10)]  # Generate 10 employees
    }
}

# Write JSON data to file
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
