import sys
import numpy as np
import sympy as sp
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wolfram Father")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter a function in x, e.g.: x**2 - 3*x")

        self.button = QPushButton("Plot it!")

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.button.clicked.connect(self.plot)

    def plot(self):
        expression = self.input.text()
        x = np.linspace(-10, 10, 400)

        y = sp.symbols("y")
        expression
        try:
            y = eval(expression, {"x": x, "np": np, "__builtins__": {}})
            dfdx = np.gradient(y, x)
        except Exception as e:
            print("Invalid function:", e)
            return    


        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, color="blue")
        ax.plot(x, dfdx, color="red")
        ax.grid(True)
        ax.legend()
        ax.set_title(f"y = {expression}")
        self.canvas.draw()


app = QApplication(sys.argv)
window = PlotWindow()
window.show()
sys.exit(app.exec())
