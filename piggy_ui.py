from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from logic import PiggyBank
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class PiggyBankUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skarbonka")
        self.setGeometry(100, 100, 400, 300)

        self.bank = PiggyBank()

        self.layout = QVBoxLayout()

        # Status i cel
        self.status_label = QLabel("Nie ustawiono celu.")
        self.layout.addWidget(self.status_label)

        # Ustawienie celu
        self.goal_input = QLineEdit()
        self.goal_input.setPlaceholderText("Ustaw cel oszczędnościowy...")
        self.layout.addWidget(self.goal_input)

        self.goal_button = QPushButton("Ustaw cel")
        self.goal_button.clicked.connect(self.set_goal)
        self.layout.addWidget(self.goal_button)

        # Dodawanie pieniędzy
        self.add_input = QLineEdit()
        self.add_input.setPlaceholderText("Kwota do dodania...")
        self.layout.addWidget(self.add_input)

        self.add_button = QPushButton("Dodaj pieniądze")
        self.add_button.clicked.connect(self.add_money)
        self.layout.addWidget(self.add_button)

        # Wyjmowanie pieniędzy
        self.remove_input = QLineEdit()
        self.remove_input.setPlaceholderText("Kwota do wyjęcia...")
        self.layout.addWidget(self.remove_input)

        self.remove_button = QPushButton("Wyjmij pieniądze")
        self.remove_button.clicked.connect(self.remove_money)
        self.layout.addWidget(self.remove_button)

        # Przycisk do wykresu
        self.plot_button = QPushButton("Pokaż wykres historii")
        self.plot_button.clicked.connect(self.show_plot)
        self.layout.addWidget(self.plot_button)

        self.setLayout(self.layout)

    def set_goal(self):
        amount = self.goal_input.text().strip()
        try:
            value = float(amount)
            if value <= 0:
                raise ValueError
            self.bank.set_goal(value)
            self.goal_input.clear()
            self.update_status()
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Podaj poprawną kwotę większą niż 0!")

    def add_money(self):
        amount = self.add_input.text().strip()
        try:
            value = float(amount)
            if value <= 0:
                raise ValueError
            self.bank.add_money(value)
            self.add_input.clear()
            self.update_status()
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Podaj poprawną kwotę większą niż 0!")

    def remove_money(self):
        amount = self.remove_input.text().strip()
        try:
            value = float(amount)
            if value <= 0:
                raise ValueError
            self.bank.remove_money(value)
            self.remove_input.clear()
            self.update_status()
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Podaj poprawną kwotę większą niż 0!")

    def update_status(self):
        self.status_label.setText(self.bank.get_status())

    def show_plot(self):
        history = self.bank.get_history()
        if not history:
            QMessageBox.information(self, "Brak danych", "Brak danych do wyświetlenia wykresu.")
            return

        times, amounts = zip(*history)

        plt.figure(figsize=(8,4))
        plt.plot(times, amounts, marker='o', linestyle='-', color='blue')
        plt.title("Historia stanu skarbonki")
        plt.xlabel("Czas")
        plt.ylabel("Kwota w zł")
        plt.grid(True)

        # Lepsze formatowanie osi czasu
        plt.gcf().autofmt_xdate()
        plt.tight_layout()
        plt.show()
