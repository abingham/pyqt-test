import pkg_resources
import sys
import time

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QVBoxLayout

import numpy as np

from matplotlib.backends.qt_compat import is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class StaticPlot(FigureCanvas):
    def __init__(self):
        super().__init__(Figure(figsize=(5, 3)))
        t = np.linspace(0, 10, 501)
        ax = self.figure.add_subplot(111)
        ax.plot(t, np.tan(t), ".")


class DynamicPlot(FigureCanvas):
    def __init__(self):
        super().__init__(Figure(figsize=(5, 3)))
        self.ax = self.figure.add_subplot(111)
        self._timer = self.new_timer(
            100, [(self._update_canvas, (), {})])
        self._timer.start()

    def _update_canvas(self):
        self.ax.clear()
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self.ax.plot(t, np.sin(t + time.time()))
        self.ax.figure.canvas.draw()


def main():
    app = QApplication(sys.argv)
    mainwindow = uic.loadUi(
        pkg_resources.resource_filename(
            'plot_test', 'ui/mainwindow.ui'))
    layout = mainwindow.findChild(
        QVBoxLayout,
        'layout')

    static = StaticPlot()
    layout.addWidget(static)
    mainwindow.addToolBar(NavigationToolbar(static, mainwindow))

    dynamic = DynamicPlot()
    layout.addWidget(dynamic)
    mainwindow.addToolBar(NavigationToolbar(dynamic, mainwindow))

    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
