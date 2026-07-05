# SBI-smart-customer-acquisition
SBI Smart Customer Acquisition Agent is an AI-powered customer advisory system that assists SBI relationship managers and digital banking platforms in identifying customer needs and recommending the most suitable banking products.

SBI Smart Customer Acquisition Agent is an AI-powered banking assistant built using Google Agent Development Kit (ADK) and Gemini 2.5 Flash. It helps identify a customer's profile based on age, occupation, income, and financial goals, and recommends the most suitable SBI product such as a Home Loan, Savings Account, Credit Card, Mutual Fund, or SME Loan.

The application uses Google ADK Runner, LlmAgent, and Python tools to analyze customer information, generate personalized recommendations, and create a natural-language sales pitch. To optimize API usage, deterministic business logic is handled by Python tools while Gemini is invoked only once per customer request.

A built-in Demo Mode enables offline demonstrations without consuming API quota, making the solution suitable for hackathons and live presentations.

Key Features
🤖 Google ADK-powered AI Agent
🏦 Personalized SBI product recommendations
📊 Customer profiling and segmentation
💬 AI-generated sales pitch
⚡ Single Gemini API call per customer
🎭 Demo Mode for quota-free demonstrations
🌐 Streamlit-based interactive web application

Technology Stack: Google ADK 2.3, Gemini 2.5 Flash, Python, Streamlit, Google GenAI SDK.

This solution enables relationship managers to engage customers more effectively, improve lead conversion, and deliver personalized banking experiences using Agentic AI.

| Layer                          | Technology                             | Purpose                                                                               |
| ------------------------------ | -------------------------------------- | ------------------------------------------------------------------------------------- |
| **Frontend**                   | Streamlit                              | Interactive web application for customer data entry and displaying AI recommendations |
| **Programming Language**       | Python 3.10+                           | Core application development and business logic                                       |
| **Agent Framework**            | Google Agent Development Kit (ADK) 2.3 | Agent orchestration, Runner, Session Management, and tool integration                 |
| **Large Language Model (LLM)** | Google Gemini 2.5 Flash                | Generates personalized product recommendations and AI-powered sales pitch             |
| **AI Runtime**                 | Google ADK Runner                      | Executes the AI agent and manages the complete workflow                               |
| **Session Management**         | InMemorySessionService (Google ADK)    | Maintains conversation state during customer interactions                             |
| **AI Agent**                   | Google ADK LlmAgent                    | Central AI agent that coordinates tool execution and interacts with Gemini            |
| **Business Logic Tools**       | Python Tools                           | Customer profiling and banking product recommendation without additional LLM calls    |
| **Google AI SDK**              | google-genai                           | Secure communication with Gemini API                                                  |
| **Configuration Management**   | python-dotenv                          | Secure loading of API keys and environment variables                                  |
| **API Authentication**         | Google AI Studio API Key               | Authenticates requests to the Gemini API                                              |
| **Deployment**                 | Streamlit Local / Streamlit Cloud      | Application deployment for demonstrations and production prototypes                   |
| **Version Control**            | Git & GitHub                           | Source code management and collaboration                                              |

Google ADK Components Used
LlmAgent – Main AI agent for customer interaction.
Runner – Executes the agent workflow.
InMemorySessionService – Manages user sessions.
Python Tools – Performs deterministic customer profiling and product recommendation.
Gemini 2.5 Flash – Generates the final personalized response.

##AI WorkFlow
<img width="902" height="540" alt="image" src="https://github.com/user-attachments/assets/bf83fc61-36cb-4882-b847-22d4a2124f02" />


##Development Tools
Visual Studio Code
Python Virtual Environment (venv)
Git & GitHub
Google AI Studio
Streamlit
