import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from page0 import Ui_mainWindow
from page1 import Ui_firstPage
from page2 import Ui_secondPage

UI_folder = "../UI_images/qt/"


class mainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)

        self.first = firstPage()
        self.pageController.addWidget(self.first)
        self.second = secondPage()
        self.pageController.addWidget(self.second)

        self.first.pushButton_report.clicked.connect(self.go_to_second)
        self.second.pushButton.clicked.connect(self.go_to_first)

    def go_to_first(self):
        self.pageController.setCurrentIndex(0)

    def go_to_second(self):
        self.pageController.setCurrentIndex(1)


class firstPage(QtWidgets.QWidget, Ui_firstPage):
    def __init__(self, parent=None):
        super(firstPage, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_start.clicked.connect(self. clear_canvas)
        self.pushButton_calibrate.clicked.connect(self.show_plant)

    def clear_canvas(self):
        self.graphicsScene_video.clear()

    def show_plant(self):
        self.graphicsScene_video.addPixmap(QtGui.QPixmap(UI_folder + "IMG_4029.JPG"))


class secondPage(QtWidgets.QWidget, Ui_secondPage):
    def __init__(self, parent=None):
        super(secondPage, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.show_plant)

    def show_plant(self):
        self.graphicsScene.addPixmap(QtGui.QPixmap(UI_folder + "/IMG_7330.JPG"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    currentWin = mainWindow()
    currentWin.show()
    sys.exit(app.exec_())
