import json

class ResearchAgent:
    def __init__(self, file_path: str):
        self.data = self._load_data(file_path)

    def _load_data(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[ResearchAgent] خطأ في التحميل: {e}")
            return {}

    def get_ingredients(self, item):
        return self.data.get("menu", {}).get(item, {}).get("ingredients")

    def get_calories(self, item):
        return self.data.get("menu", {}).get(item, {}).get("calories")

    def get_hours(self, day):
        return self.data.get("hours", {}).get(day)

    def list_drinks(self):
        return list(self.data.get("menu", {}).keys())
