from datetime import datetime

class PiggyBank:
    def __init__(self):
        self.goal = 0.0
        self.saved = 0.0
        self.history = []  # historia (czas, kwota)

    def set_goal(self, amount):
        self.goal = float(amount)

    def add_money(self, amount):
        self.saved += float(amount)
        self.history.append((datetime.now(), self.saved))

    def remove_money(self, amount):
        self.saved -= float(amount)
        if self.saved < 0:
            self.saved = 0.0
        self.history.append((datetime.now(), self.saved))

    def get_status(self):
        remaining = self.goal - self.saved
        if self.goal == 0:
            return "Nie ustawiono celu."
        elif remaining <= 0:
            return f"🎉 Cel osiągnięty! Masz {self.saved:.2f} zł."
        else:
            return f"💰 Masz {self.saved:.2f} zł. Brakuje {remaining:.2f} zł do celu {self.goal:.2f} zł."

    def get_history(self):
        return self.history
