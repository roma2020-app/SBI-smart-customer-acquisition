def analyze_profile(age: int, occupation: str, income: int, goal: str):

    if occupation == "Student":
        segment = "Student"

    elif occupation == "Business":
        segment = "Business Owner"

    elif income >= 100000:
        segment = "Premium Customer"

    elif income >= 50000:
        segment = "Young Professional"

    else:
        segment = "General Customer"

    return {
        "segment": segment,
        "age": age,
        "occupation": occupation,
        "income": income,
        "goal": goal,
    }