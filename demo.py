def get_demo_response(customer):

    goal = customer["goal"]
    income = customer["income"]
    occupation = customer["occupation"]

    if goal == "Buy Home":

        product = "🏠 SBI Home Loan"

        pitch = f"""
### Customer Analysis

**Segment:** Young Professional

**Recommended Product:** SBI Home Loan

### Why?

✅ Stable income of ₹{income:,}

✅ Goal is Home Ownership

✅ Attractive EMI Options

### AI Sales Recommendation

Dear customer,

Based on your profile as a {occupation}, SBI Home Loan is the most suitable product.

You are likely to qualify for competitive interest rates and flexible repayment plans.

**Confidence Score: 96%**
"""

    elif goal == "Investment":

        product = "📈 SBI Mutual Fund"

        pitch = """
### Customer Analysis

**Segment:** Investor

**Recommended Product:** SBI Mutual Fund

Confidence Score: 94%
"""

    elif goal == "Travel":

        product = "✈ SBI Credit Card"

        pitch = """
### Customer Analysis

**Segment:** Frequent Traveller

**Recommended Product:** SBI Travel Credit Card

Confidence Score: 93%
"""

    elif goal == "Business":

        product = "🏢 SBI SME Loan"

        pitch = """
### Customer Analysis

**Segment:** Business Owner

**Recommended Product:** SBI SME Loan

Confidence Score: 95%
"""

    else:

        product = "💰 SBI Savings Account"

        pitch = """
### Customer Analysis

**Recommended Product:** SBI Savings Account

Confidence Score: 91%
"""

    return pitch