from pprint import pprint

# Nested hashmap initialization
employees = {
    "employee_1": {
        "name": "John",
        "role": "Developer",
        "salary": 5000,
        "coin": "USD"
    },
    "employee_2": {
        "name": "Susan",
        "role": "Business Analyst",
        "salary": 4000,
        "coin": "USD"
    },
    "employee_3": {
        "name": "Edward",
        "role": "UX Designer",
        "salary": 5300,
        "coin": "USD"
    }
}

# Printing the hashmap
pprint(employees)

# Looping through every child hashmap
for employee in employees.values():
    print(employee["name"], "is", employee["role"])