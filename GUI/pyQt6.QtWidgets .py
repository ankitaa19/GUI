# hello.py

"""Simple Hello, World example with PyQt6."""

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# Create an instance of QApplication
app = QApplication([])

# Create your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

# Show your application's GUI
window.show()

# Run your application's event loop
app.exec().