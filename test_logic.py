import unittest
from datetime import datetime
from logic import PiggyBank

class TestPiggyBank(unittest.TestCase):

    def setUp(self):
        self.bank = PiggyBank()

    def test_initial_status(self):
        self.assertEqual(self.bank.get_status(), "Nie ustawiono celu.")
        self.assertEqual(self.bank.saved, 0)
        self.assertEqual(len(self.bank.get_history()), 0)

    def test_set_goal(self):
        self.bank.set_goal(100)
        self.assertEqual(self.bank.goal, 100)

    def test_add_money(self):
        self.bank.set_goal(100)
        self.bank.add_money(50)
        self.assertEqual(self.bank.saved, 50)
        self.assertIn("Masz 50.00 zł", self.bank.get_status())
        self.assertEqual(len(self.bank.get_history()), 1)

    def test_remove_money(self):
        self.bank.set_goal(100)
        self.bank.add_money(70)
        self.bank.remove_money(20)
        self.assertEqual(self.bank.saved, 50)
        self.assertEqual(len(self.bank.get_history()), 2)

    def test_remove_more_than_saved(self):
        self.bank.add_money(30)
        self.bank.remove_money(50)  # should not go below 0
        self.assertEqual(self.bank.saved, 0.0)

    def test_goal_achieved(self):
        self.bank.set_goal(100)
        self.bank.add_money(100)
        self.assertIn("🎉 Cel osiągnięty!", self.bank.get_status())

    def test_history_timestamps(self):
        self.bank.add_money(10)
        self.bank.remove_money(5)
        history = self.bank.get_history()
        for t, _ in history:
            self.assertIsInstance(t, datetime)

if __name__ == "__main__":
    unittest.main()
