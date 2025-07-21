# runner.py

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def main():
    # Load environment variables from .env
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("❌ OPENAI_API_KEY not found in environment.")
        return

    # Initialize the LLM
    llm = ChatOpenAI(temperature=0, model="gpt-4o")

    # Create a memory-enabled conversation chain
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

    print("💬 LangChain Terminal Chat (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        response = conversation.predict(input=user_input)
        print(f"🤖: {response}\n")

if __name__ == "__main__":
    main()
