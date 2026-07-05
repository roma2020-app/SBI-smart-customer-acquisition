import asyncio
import streamlit as st
from google.genai import types

from demo import get_demo_response

from runner import (
    runner,
    create_session,
    USER_ID,
)

st.set_page_config(
    page_title="SBI Smart Customer Acquisition Agent",
    page_icon="🏦",
    layout="wide",
)

st.title("🏦 SBI Smart Customer Acquisition Agent")
st.write("Powered by Google ADK + Gemini 2.5 Flash")

# Remove this line after testing if you want
st.write("API Key Loaded:", "GOOGLE_API_KEY" in st.secrets)

# ------------------------
# Demo Mode Toggle
# ------------------------

demo_mode = st.toggle(
    "🎭 Demo Mode (No Gemini API)",
    value=True,
)

# ------------------------
# Customer Inputs
# ------------------------

age = st.number_input("Age", 18, 100, 29)

occupation = st.selectbox(
    "Occupation",
    [
        "Student",
        "Software Engineer",
        "Business",
        "Doctor",
        "Teacher",
        "Government Employee",
    ],
)

income = st.number_input(
    "Monthly Income",
    min_value=0,
    max_value=1000000,
    value=90000,
)

goal = st.selectbox(
    "Goal",
    [
        "Buy Home",
        "Save Money",
        "Travel",
        "Investment",
        "Business",
    ],
)

# ------------------------
# Google ADK Function
# ------------------------

async def get_response():

    session_id = await create_session()

    message = types.Content(
        role="user",
        parts=[
            types.Part(
                text=f"""
Customer Details

Age : {age}
Occupation : {occupation}
Income : {income}
Goal : {goal}
"""
            )
        ],
    )

    final_response = ""

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session_id,
        new_message=message,
    ):

        if event.content and event.content.parts:

            for part in event.content.parts:

                if getattr(part, "text", None):

                    final_response = part.text

    return final_response


# ------------------------
# Button
# ------------------------

if st.button("🚀 Get Recommendation"):

    customer = {
        "age": age,
        "occupation": occupation,
        "income": income,
        "goal": goal,
    }

    # ------------------------
    # Demo Mode
    # ------------------------

    if demo_mode:

        st.success("🎭 Demo Mode Enabled")

        response = get_demo_response(customer)

        st.markdown(response)

    # ------------------------
    # Real Google ADK
    # ------------------------

    else:

        st.info("🤖 Using Google ADK + Gemini")

        try:

            with st.spinner("Analyzing Customer..."):

                response = asyncio.run(get_response())

            st.success("✅ Recommendation Generated")

            st.markdown(response)

        except Exception:

            st.warning("⚠️ Live AI is currently unavailable.")

            st.info("Showing Demo Recommendation instead.")

            response = get_demo_response(customer)

            st.markdown(response)
