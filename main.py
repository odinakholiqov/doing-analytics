import sys
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout,
    QLineEdit, QPushButton, QLabel
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class LinearPlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure(figsize=(5, 4))
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)

        self.m = 2
        self.b = 1
        self.plot_line()

    def plot_line(self, x_point=None):
        self.ax.clear()

        x = np.linspace(-10, 10, 100)
        y = self.m * x + self.b
        self.ax.plot(x, y, label=f"y = {self.m}x + {self.b}")

        if x_point is not None:
            y_point = self.m * x_point + self.b
            self.ax.plot(x_point, y_point, 'ro')
            self.ax.annotate(f"({x_point}, {y_point:.2f})", (x_point, y_point),
                             textcoords="offset points", xytext=(10, 10), ha='center')

        self.ax.set_title("Linear Line Plot")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.grid(True)
        self.ax.legend()
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linear Line Plotter")
        self.setGeometry(100, 100, 700, 500)

        widget = QWidget()
        layout = QVBoxLayout()

        # Plot canvas
        self.canvas = LinearPlotCanvas(self)
        layout.addWidget(self.canvas)

        # Input section
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter x value")
        self.button = QPushButton("Plot Point")
        self.button.clicked.connect(self.update_plot)

        input_layout.addWidget(QLabel("x:"))
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.button)

        layout.addLayout(input_layout)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def update_plot(self):
        try:
            x_val = float(self.input_field.text())
            self.canvas.plot_line(x_point=x_val)
        except ValueError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
