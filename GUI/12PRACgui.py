# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
# hello.py
# ...

# 2. Create an instance of QApplication
app = QApplication([])
# hello.py
# ...

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("shikha app")
window.setGeometry(200, 200, 280, 280)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)
# hello.py
# ...

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())