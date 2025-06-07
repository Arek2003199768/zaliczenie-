from PyQt6.QtWidgets import QApplication
import sys
from piggy_ui import PiggyBankUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PiggyBankUI()
    window.show()
    sys.exit(app.exec())
