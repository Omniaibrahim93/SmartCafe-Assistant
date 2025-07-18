from research_agent import ResearchAgent
from chatbot_agent import ChatBotAgent

def main():
    researcher = ResearchAgent("cafe_data.json")
    bot = ChatBotAgent(researcher)

    print("Welcome to SmartCafe ☕️! Ask me anything about the menu or opening hours.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input(">> ")
        if user_input.lower() in ("exit", "quit"):
            print("Goodbye! 🤍")
            break
        response = bot.parse_and_reply(user_input)
        print(response)

if __name__ == "__main__":
    main()
