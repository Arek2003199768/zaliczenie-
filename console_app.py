from logic import PiggyBank
import matplotlib.pyplot as plt

def print_menu():
    print("\n=== SKARBONKA ===")
    print("1. Ustaw cel")
    print("2. Dodaj pieniądze")
    print("3. Wyjmij pieniądze")
    print("4. Pokaż status")
    print("5. Pokaż wykres historii")
    print("6. Wyjście")

def main():
    bank = PiggyBank()

    while True:
        print_menu()
        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            amount = input("Podaj cel oszczędnościowy: ").strip()
            try:
                value = float(amount)
                if value <= 0:
                    raise ValueError
                bank.set_goal(value)
                print("✅ Cel ustawiony.")
            except ValueError:
                print("❌ Podaj poprawną kwotę większą niż 0.")

        elif choice == "2":
            amount = input("Podaj kwotę do dodania: ").strip()
            try:
                value = float(amount)
                if value <= 0:
                    raise ValueError
                bank.add_money(value)
                print("✅ Dodano pieniądze.")
            except ValueError:
                print("❌ Podaj poprawną kwotę większą niż 0.")

        elif choice == "3":
            amount = input("Podaj kwotę do wyjęcia: ").strip()
            try:
                value = float(amount)
                if value <= 0:
                    raise ValueError
                bank.remove_money(value)
                print("✅ Wyjęto pieniądze.")
            except ValueError:
                print("❌ Podaj poprawną kwotę większą niż 0.")

        elif choice == "4":
            print(bank.get_status())

        elif choice == "5":
            history = bank.get_history()
            if not history:
                print("Brak danych do wyświetlenia wykresu.")
                continue

            times, amounts = zip(*history)
            plt.figure(figsize=(8, 4))
            plt.plot(times, amounts, marker='o', linestyle='-', color='green')
            plt.title("Historia stanu skarbonki")
            plt.xlabel("Czas")
            plt.ylabel("Kwota w zł")
            plt.grid(True)
            plt.gcf().autofmt_xdate()
            plt.tight_layout()
            plt.show()

        elif choice == "6":
            print("👋 Do zobaczenia!")
            break

        else:
            print("❌ Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()

