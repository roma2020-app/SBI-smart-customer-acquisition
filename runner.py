import uuid

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from agent import root_agent

APP_NAME = "sbi_customer_agent"
USER_ID = "demo_user"

session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)


async def create_session():
    session_id = str(uuid.uuid4())

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_id,
    )

    return session_id