import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap
from random import randint
from PyQt5.QtCore import Qt
from random import choice, choices
from alg import createbuild, trans, trans1

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Style.ui", self)
        self.setWindowTitle("DBG")
        self.setWindowIcon(QIcon('logo.png'))
        self.pushButton.clicked.connect(self.run)
        self.status = False

    def run(self):
        if self.lineEdit.text() and createbuild(self.lineEdit.text()) != None:
            her, p1, n1, p2, n2, p3, n3, p4, n4 = createbuild(self.lineEdit.text())
            print(her, p1, n1, p2, n2, p3, n3, p4, n4)
            self.name1.setText(p1)
            self.name2.setText(p2)
            self.name3.setText(p3)
            self.name4.setText(p4)
            self.hero.setPixmap(QPixmap(trans1(her)))
            self.icons1 = [self.icon1, self.icon2, self.icon3, self.icon4, self.icon5]
            self.icons2 = [self.icon6]
            self.icons3 = [self.icon7, self.icon8, self.icon9]
            self.icons4 = [self.icon10, self.icon11, self.icon12, self.icon13, self.icon14]


            self.c = 0
            self.icon1.clear()
            self.icon2.clear()
            self.icon3.clear()
            self.icon4.clear()
            self.icon5.clear()
            for i in n1:
                self.pixmap = QPixmap(trans(i))
                print(trans(i))
                self.icons1[self.c].setPixmap(self.pixmap)
                self.c += 1


            self.icon6.setPixmap(QPixmap(trans(n2[0])))
            print(trans(n2[0]))

            self.c = 0
            self.icon7.clear()
            self.icon8.clear()
            self.icon9.clear()
            for i in n3:
                self.pixmap = QPixmap(trans(i))
                print(trans(i))
                self.icons3[self.c].setPixmap(self.pixmap)
                self.c += 1


            self.c = 0
            self.icon10.clear()
            self.icon11.clear()
            self.icon12.clear()
            self.icon13.clear()
            self.icon14.clear()
            for i in n4:
                self.pixmap = QPixmap(trans(i))
                print(trans(i))
                self.icons4[self.c].setPixmap(self.pixmap)
                self.c += 1
            self.status = False


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.run()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
