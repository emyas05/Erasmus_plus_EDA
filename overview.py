import pandas as pd

def load_bank_variables():
    data = {
        "Variable Name": [
            "age", "job", "marital", "education", "default", "balance", "housing", "loan", "contact",
            "day_of_week", "month", "duration", "campaign", "pdays", "previous", "poutcome", "y"
        ],
        "Description": [
            "Age",
            "Type of job (e.g., 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')",
            "Marital status (e.g., 'divorced','married','single','unknown'; 'divorced' means divorced or widowed)",
            "Education level (e.g., 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')",
            "Has credit in default?",
            "Average yearly balance (euros)",
            "Has housing loan?",
            "Has personal loan?",
            "Contact communication type (e.g., 'cellular','telephone')",
            "Last contact day of the week",
            "Last contact month of year (e.g., 'jan', 'feb', 'mar', ..., 'nov', 'dec')",
            "Last contact duration in seconds (only for benchmarks, discard for real prediction)",
            "Number of contacts during this campaign (includes last contact)",
            "Number of days since last contact from previous campaign (-1 means not contacted)",
            "Number of contacts before this campaign",
            "Outcome of previous campaign (e.g., 'failure','nonexistent','success')",
            "Has the client subscribed to a term deposit?"
        ]
    }

    df = pd.DataFrame(data)
    return df
