PRODUCTS = {

    "Buy Home": "SBI Home Loan",

    "Save Money": "SBI Savings Account",

    "Travel": "SBI Credit Card",

    "Investment": "SBI Mutual Fund",

    "Business": "SBI SME Loan",

}


def recommend_product(profile):

    product = PRODUCTS.get(
        profile["goal"],
        "SBI Savings Account"
    )

    return {
        "product": product,
        "reason": f"Recommended because customer wants to {profile['goal']}"
    }