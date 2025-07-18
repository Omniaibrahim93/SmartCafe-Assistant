import re
from research_agent import ResearchAgent

class ChatBotAgent:
    def __init__(self, researcher: ResearchAgent):
        self.researcher = researcher
        self.patterns = {
            "ingredients": re.compile(r"(?i).*what'?s in a ([\w\s]+)\??"),
            "calories":    re.compile(r"(?i).*how many calories in ([\w\s]+)\??"),
            "hours":       re.compile(r"(?i).*when are you open on ([\w\s]+)\??"),
            "list":        re.compile(r"(?i).*what drinks do you have\??")
        }

    def parse_and_reply(self, question: str) -> str:
        q = question.strip()
        
        if self.patterns["list"].match(q):
            drinks = self.researcher.list_drinks()
            return "Available drinks: " + ", ".join(drinks)

        m_ing = self.patterns["ingredients"].match(q)
        if m_ing:
            item = m_ing.group(1).title()
            ing = self.researcher.get_ingredients(item)
            return f"Ingredients of {item}: {', '.join(ing)}" if ing else f"{item} is not available."

        m_cal = self.patterns["calories"].match(q)
        if m_cal:
            item = m_cal.group(1).title()
            cal = self.researcher.get_calories(item)
            return f"Calories in {item}: {cal} kcal" if cal else f"{item} is not available."

        m_hrs = self.patterns["hours"].match(q)
        if m_hrs:
            day = m_hrs.group(1).title()
            hrs = self.researcher.get_hours(day)
            return f"Opening hours on {day}: {hrs}" if hrs else f"No data available for {day}."

        return "Sorry, I didn't understand your question. Could you please rephrase it? 😊"
