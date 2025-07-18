# ☕ SmartCafe Console Assistant

A simple console-based assistant built for SmartCafe that answers customer FAQs using a local knowledge base (`cafe_data.json`). The assistant is fully offline and does not use any external APIs, AI, or internet access.

---

## 🎯 Project Objective

To simulate a smart in-store or website chatbot assistant using **pure Python**, **Object-Oriented Programming**, and **regex pattern matching**, without any external AI models.

---

## 📦 Project Structure

| File                | Description                                                        |
|---------------------|--------------------------------------------------------------------|
| `main.py`           | Entry point that runs the assistant and handles the user loop      |
| `chatbot_agent.py`  | Contains the `ChatBotAgent` class – handles question parsing       |
| `research_agent.py` | Contains the `ResearchAgent` class – loads & queries JSON data     |
| `cafe_data.json`    | JSON knowledge base with menu items and working hours              |
| `README.md`         | Project documentation (this file)                                  |

---

## 🧠 How It Works

- Users type natural language-like questions into the console.
- `ChatBotAgent` uses regular expressions to detect the intent.
- The bot passes the intent to `ResearchAgent`, which looks up data in `cafe_data.json`.
- A friendly response is printed back to the user.

---

## 🔍 Detected Intents (via Regex)

| Intent Type            | Example Question                         | Response                          |
|------------------------|------------------------------------------|-----------------------------------|
| Menu Ingredients       | `What's in a Mocha?`                     | List of ingredients               |
| Calories/Nutrition     | `How many calories in Hot Chocolate?`
