import sys
import random

# PySide dependency
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

# Matplotlib dependencies
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure


class App(QWidget):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        # Set properties of the window
        self.resize(600, 490)
        self.title = 'The Window Title'
        self.setWindowTitle(self.title)

        # Create the matplotlib canvas
        canvas = PlotCanvas(self)

        # Add the plot canvas to the horizontal box layout
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.setLayout(layout)

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, dpi=100):
        super(PlotCanvas, self).__init__(Figure()) 

        self.setParent(parent)

        # Create the figure and figure canvas
        fig = Figure(dpi=dpi)
        self.figure = fig
        self.canvas = FigureCanvas(self.figure)
        self.axes = fig.add_subplot()

        # Create data for the graph
        data = [random.random() for i in range(25)]

        # Line style
        self.axes.plot(data, linestyle='dashed')

        # Graph title text
        self.axes.set_title('The Graph Title')

        # Axes labels text
        self.axes.set_ylabel('Y Label')
        self.axes.set_xlabel('X Label')

        # X-axis color change
        self.axes.xaxis.label.set_color('blue')

        # Set the x-axis ticks and labels
        self.axes.xaxis.set_tick_params(colors='red')

        # Set y-axis label line color
        self.axes.spines['left'].set_color('orange')
        
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Additional styling for the widget which houses
    # the chart
    app.setStyleSheet("""
      QWidget {
        background-color: "green";
        padding: 20px;
      }
    """)

    widget = App()
    widget.show()
    sys.exit(app.exec())
