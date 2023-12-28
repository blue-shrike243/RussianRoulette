from view import *
from PyQt5.QtWidgets import *
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.label_Result.setHidden(True)
        self.label_Bottom.setHidden(True)
        self.pushButton_Again.setHidden(True)

        self.randresult = random.randint(1,6)
        self.numspins = 0
        self.randspin = 0

        self.label_Icon.setStyleSheet("image: url(:/RR/revolver.gif);")

        self.pushButton_Spin.clicked.connect(lambda: self.spin())
        self.pushButton_Again.clicked.connect(lambda: self.again())

    def spin(self):
        self.randspin = random.randint(1,6)
        self.numspins += 1

        if self.randspin == self.randresult:
            self.label_Icon.setStyleSheet("image: url(:/RR/bang.jpg);")

            self.label_Result.setHidden(False)
            self.label_Result.setText('You Die!')
            self.label_Bottom.setHidden(False)
            if self.numspins == 2:
                self.label_Bottom.setText(f'You survived {self.numspins - 1} spin without dying.')
            else:
                self.label_Bottom.setText(f'You survived {self.numspins - 1} spins without dying.')
            self.numspins = 0
        else:
            self.label_Icon.setStyleSheet("image: url(:/RR/whew.jpg);")

            self.label_Result.setHidden(False)
            self.label_Result.setText('You Live!')
            self.label_Bottom.setHidden(False)
            self.label_Bottom.setText(f'Would you like to spin again?')

        self.pushButton_Spin.setHidden(True)
        self.pushButton_Again.setHidden(False)

    def again(self):
        self.label_Icon.setStyleSheet("image: url(:/RR/revolver.gif);")

        self.label_Result.setHidden(True)
        self.label_Bottom.setHidden(True)
        self.pushButton_Again.setHidden(True)

        self.pushButton_Spin.setHidden(False)
