import os
from dotenv import load_dotenv

try:
    import streamlit as st
    if "GOOGLE_API_KEY" in st.secrets:
        os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
    else:
        load_dotenv()
except Exception:
    load_dotenv()
from google.adk.agents import LlmAgent

from tools.profile_tool import analyze_profile
from tools.recommendation_tool import recommend_product

root_agent = LlmAgent(
    name="sbi_customer_advisor",

    model="gemini-2.5-flash",

    description="SBI Customer Acquisition Agent",

    instruction="""
You are an SBI Customer Acquisition Advisor.

Always follow these steps:

1. Call analyze_profile.
2. Call recommend_product.
3. Explain why the product is suitable.
4. Generate a professional sales pitch.
5. Keep response below 120 words.
6. Recommend only ONE product.
""",

    tools=[
        analyze_profile,
        recommend_product,
    ],
)
