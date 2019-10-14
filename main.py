#main page - first program
#random.randint - Return a random integer N such that a <= N <= b

import sys, random
#from gi.repository import Gtk
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication,QDialog, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def redraw(self):
        btn1 = QPushButton(str(m[0][0]), self)
        btn1.move(5, 5)
        btn1.setFixedWidth(100)
        btn1.setFixedHeight(100)
        btn1.clicked.connect(self.buttonClicked1)

        btn2 = QPushButton(str(m[0][1]), self)
        btn2.move(110, 5)
        btn2.setFixedWidth(100)
        btn2.setFixedHeight(100)
        btn2.clicked.connect(self.buttonClicked2)

        btn3 = QPushButton(str(m[0][2]), self)
        btn3.move(215, 5)
        btn3.setFixedWidth(100)
        btn3.setFixedHeight(100)
        btn3.clicked.connect(self.buttonClicked3)

        btn4 = QPushButton(str(m[0][3]), self)
        btn4.move(320, 5)
        btn4.setFixedWidth(100)
        btn4.setFixedHeight(100)
        btn4.clicked.connect(self.buttonClicked4)

        btn5 = QPushButton(str(m[1][0]), self)
        btn5.move(5, 110)
        btn5.setFixedWidth(100)
        btn5.setFixedHeight(100)
        btn5.clicked.connect(self.buttonClicked5)

        btn6 = QPushButton(str(m[1][1]), self)
        btn6.move(110, 110)
        btn6.setFixedWidth(100)
        btn6.setFixedHeight(100)
        btn6.clicked.connect(self.buttonClicked6)

        btn7 = QPushButton(str(m[1][2]), self)
        btn7.move(215, 110)
        btn7.setFixedWidth(100)
        btn7.setFixedHeight(100)
        btn7.clicked.connect(self.buttonClicked7)

        btn8 = QPushButton(str(m[1][3]), self)
        btn8.move(320, 110)
        btn8.setFixedWidth(100)
        btn8.setFixedHeight(100)
        btn8.clicked.connect(self.buttonClicked8)

        btn9 = QPushButton(str(m[2][0]), self)
        btn9.move(5, 215)
        btn9.setFixedWidth(100)
        btn9.setFixedHeight(100)
        btn9.clicked.connect(self.buttonClicked9)

        btn10 = QPushButton(str(m[2][1]), self)
        btn10.move(110, 215)
        btn10.setFixedWidth(100)
        btn10.setFixedHeight(100)
        btn10.clicked.connect(self.buttonClicked10)

        btn11 = QPushButton(str(m[2][2]), self)
        btn11.move(215, 215)
        btn11.setFixedWidth(100)
        btn11.setFixedHeight(100)
        btn11.clicked.connect(self.buttonClicked11)

        btn12 = QPushButton(str(m[2][3]), self)
        btn12.move(320, 215)
        btn12.setFixedWidth(100)
        btn12.setFixedHeight(100)
        btn12.clicked.connect(self.buttonClicked12)

        btn13 = QPushButton(str(m[3][0]), self)
        btn13.move(5, 320)
        btn13.setFixedWidth(100)
        btn13.setFixedHeight(100)
        btn13.clicked.connect(self.buttonClicked13)

        btn14 = QPushButton(str(m[3][1]), self)
        btn14.move(110, 320)
        btn14.setFixedWidth(100)
        btn14.setFixedHeight(100)
        btn14.clicked.connect(self.buttonClicked14)

        btn15 = QPushButton(str(m[3][2]), self)
        btn15.move(215, 320)
        btn15.setFixedWidth(100)
        btn15.setFixedHeight(100)
        btn15.clicked.connect(self.buttonClicked15)

        btn16 = QPushButton(str(m[3][3]), self)
        btn16.move(320, 320)
        btn16.setFixedWidth(100)
        btn16.setFixedHeight(100)
        btn16.clicked.connect(self.buttonClicked16)

        btn1.show(); btn2.show(); btn3.show(); btn4.show()
        btn5.show(); btn6.show(); btn7.show(); btn8.show()
        btn9.show(); btn10.show(); btn11.show(); btn12.show()
        btn13.show(); btn14.show(); btn15.show(); btn16.show()
        self.checklist()
        #print("Buttons was redrawed")

    def initUI(self):

        self.redraw()
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Testirovshikov na mylo')
        self.setFixedWidth(425)  # а так работает
        self.setFixedHeight(440)
        self.backgroundRole()
        self.center()
        self.show()

    def buttonClicked1(self):
        sender = self.sender()
        if m[0][1]=='':
            m[0][1]=m[0][0]
            m[0][0]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][0]=='':
            m[1][0]=m[0][0]
            m[0][0]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked2(self):
        sender = self.sender()
        if m[0][2]=='':
            m[0][2]=m[0][1]
            m[0][1]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][1]=='':
            m[1][1]=m[0][1]
            m[0][1]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[0][0]=='':
            m[0][0]=m[0][1]
            m[0][1]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked3(self):
        sender = self.sender()
        if m[0][3]=='':
            m[0][3]=m[0][2]
            m[0][2]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][2]=='':
            m[1][2]=m[0][2]
            m[0][2]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[0][1]=='':
            m[0][1]=m[0][2]
            m[0][2]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked4(self):
        sender = self.sender()
        if m[1][3]=='':
            m[1][3]=m[0][3]
            m[0][3]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[0][2]=='':
            m[0][2]=m[0][3]
            m[0][3]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked5(self):
        sender = self.sender()
        if m[0][0]=='':
            m[0][0]=m[1][0]
            m[1][0]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][1]=='':
            m[1][1]=m[1][0]
            m[1][0]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][0]=='':
            m[2][0]=m[1][0]
            m[1][0]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked6(self):
        sender = self.sender()
        if m[0][1]=='':
            m[0][1]=m[1][1]
            m[1][1]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][2]=='':
            m[1][2]=m[1][1]
            m[1][1]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][1]=='':
            m[2][1]=m[1][1]
            m[1][1]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][0]=='':
            m[1][0]=m[1][1]
            m[1][1]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked7(self):
        sender = self.sender()
        if m[0][2]=='':
            m[0][2]=m[1][2]
            m[1][2]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][3]=='':
            m[1][3]=m[1][2]
            m[1][2]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][2]=='':
            m[2][2]=m[1][2]
            m[1][2]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][1]=='':
            m[1][1]=m[1][2]
            m[1][2]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked8(self):
        sender = self.sender()
        if m[0][3]=='':
            m[0][3]=m[1][3]
            m[1][3]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][3]=='':
            m[2][3]=m[1][3]
            m[1][3]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][2]=='':
            m[1][2]=m[1][3]
            m[1][3]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked9(self):
        sender = self.sender()
        if m[1][0]=='':
            m[1][0]=m[2][0]
            m[2][0]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][1]=='':
            m[2][1]=m[2][0]
            m[2][0]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][0]=='':
            m[3][0]=m[2][0]
            m[2][0]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked10(self):
        sender = self.sender()
        if m[1][1]=='':
            m[1][1]=m[2][1]
            m[2][1]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][2]=='':
            m[2][2]=m[2][1]
            m[2][1]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][1]=='':
            m[3][1]=m[2][1]
            m[2][1]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][0]=='':
            m[2][0]=m[2][1]
            m[2][1]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked11(self):
        sender = self.sender()
        if m[1][2]=='':
            m[1][2]=m[2][2]
            m[2][2]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][3]=='':
            m[2][3]=m[2][2]
            m[2][2]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][2]=='':
            m[3][2]=m[2][2]
            m[2][2]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][1]=='':
            m[2][1]=m[2][2]
            m[2][2]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked12(self):
        sender = self.sender()
        if m[1][3]=='':
            m[1][3]=m[2][3]
            m[2][3]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][3]=='':
            m[3][3]=m[2][3]
            m[2][3]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][2]=='':
            m[2][2]=m[2][3]
            m[2][3]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked13(self):
        sender = self.sender()
        if m[2][0]=='':
            m[2][0]=m[3][0]
            m[3][0]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][1]=='':
            m[3][1]=m[3][0]
            m[3][0]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked14(self):
        sender = self.sender()
        if m[2][1]=='':
            m[2][1]=m[3][1]
            m[3][1]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][2]=='':
            m[3][2]=m[3][1]
            m[3][1]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][0]=='':
            m[3][0]=m[3][1]
            m[3][1]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked15(self):
        sender = self.sender()
        if m[2][2]=='':
            m[2][2]=m[3][2]
            m[3][2]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][3]=='':
            m[3][3]=m[3][2]
            m[3][2]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][1]=='':
            m[3][1]=m[3][2]
            m[3][2]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked16(self):
        sender = self.sender()
        if m[2][3]=='':
            m[2][3]=m[3][3]
            m[3][3]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][2]=='':
            m[3][2]=m[3][3]
            m[3][3]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
            (screen.height()-size.height())/2)


    def checklist(self):
        if (m[0][0]==1) and (m[0][1]==2) and (m[0][2]==3) and (m[0][3]==4) and\
            (m[1][0]==5) and (m[1][1]==6) and (m[1][7]==7) and (m[1][3]==8)and\
            (m[2][0]==9) and (m[2][1]==10) and (m[2][11]==11) and (m[2][3]==12)and\
            (m[3][0]==13) and (m[3][1]==14) and (m[3][15]==15) and (m[3][3]==16):
        #self.essageBox(0, 'hello', 'title')
            self.close()


#definition of
m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
z=0

for i in range(0, 4):
    for y in range(0, 4):
        x = 1
        while (x == 1 and z!=16):
            r1 = random.randint(0, 15)
            if r1 in list1:
                list1[r1] = -1
                x = 0
                #print("R1 = ", r1, m[0], m[1], m[2], m[3], " - = - ", list1)
                m[i][y] = r1
                if (r1 == 0): m[i][y]=''
            #NumberExist()
        z=z+1
        #print("Z = ",z," - ",m[i][y], " R1 = ", r1, m[0], m[1], m[2], m[3], " - = - ", list1)

#print(m[0])
#print(m[1])
#print(m[2])
#print(m[3])

if __name__ == '__main__':
    app = QApplication([])
    fifteen = MainWindow()
    sys.exit(app.exec_())
