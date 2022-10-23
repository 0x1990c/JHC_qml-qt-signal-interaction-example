import os
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QVBoxLayout


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        self.__lbl = QLabel()
        self.__lbl.setAlignment(Qt.AlignCenter)

        lay = QVBoxLayout()

        file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "slider.qml")

        sliderQmlWidget = QQuickWidget()
        sliderQmlWidget.setSource(QUrl.fromLocalFile(file))
        sliderQmlWidget.setMaximumHeight(sliderQmlWidget.height())
        sliderQmlWidget.setResizeMode(QQuickWidget.SizeRootObjectToView)

        objForEventHandle = sliderQmlWidget.rootObject()
        objForEventHandle.moved.connect(self.__moved)

        lay.addWidget(sliderQmlWidget)
        lay.addWidget(self.__lbl)
        lay.setContentsMargins(0, 0, 0, 0)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

    def __moved(self, i):
        self.__lbl.setText(f'Value {i}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    default_style = "Material"

    settings = QtCore.QSettings()
    style = settings.value("style")
    if not style:
        style = default_style
        settings.setValue("style", style)

    os.environ["QT_QUICK_CONTROLS_STYLE"] = style
    w = Window()
    w.showMaximized()
    sys.exit(app.exec_())