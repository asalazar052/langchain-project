# sql_agent_runner.py

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase
from langchain.agents import AgentExecutor

def main():
    # Load environment
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("❌ OPENAI_API_KEY not set.")
        return

    # Setup LLM
    llm = ChatOpenAI(temperature=0, model="gpt-4", verbose=False)

    # Connect to the SQLite database
    db = SQLDatabase.from_uri("sqlite:///chinook.db")

    # Create the agent with the database
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=SQLDatabaseToolkit(db=db, llm=llm),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True  # for debugging, can turn off later
    )

    # Terminal loop
    print("🎶 SQL Agent Chat — Chinook Music DB (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break
        try:
            response = agent_executor.run(user_input)
            print(f"🤖: {response}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    main()
