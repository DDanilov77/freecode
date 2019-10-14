#main page - first program
#random.randint - Return a random integer N such that a <= N <= b

import sys, random
#from gi.repository import Gtk
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication,QDialog, QPushButton

xx=[5, 110, 215, 320, 425]
yy=[25, 110, 215, 320, 425]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        Menu1 = menubar.addMenu('&File')
        Menu2 = menubar.addMenu('&Save')
        Menu3 = menubar.addMenu('&Load')
        Menu3 = menubar.addMenu('&Exit')

        self.redraw()
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Testirovshikov na mylo 5x5')
        self.setFixedWidth(530)  # а так работает
        self.setFixedHeight(550)
        self.backgroundRole()
        self.center()
        self.show()

    def redraw(self):
        #row1
        btn1 = QPushButton(str(m[0][0]), self)
        btn1.move(xx[0], yy[0])
        btn1.setFixedWidth(100)
        btn1.setFixedHeight(100)
        btn1.clicked.connect(self.buttonClicked1)

        btn2 = QPushButton(str(m[0][1]), self)
        btn2.move(xx[1], yy[0])
        btn2.setFixedWidth(100)
        btn2.setFixedHeight(100)
        btn2.clicked.connect(self.buttonClicked2)

        btn3 = QPushButton(str(m[0][2]), self)
        btn3.move(xx[2], yy[0])
        btn3.setFixedWidth(100)
        btn3.setFixedHeight(100)
        btn3.clicked.connect(self.buttonClicked3)

        btn4 = QPushButton(str(m[0][3]), self)
        btn4.move(xx[3], yy[0])
        btn4.setFixedWidth(100)
        btn4.setFixedHeight(100)
        btn4.clicked.connect(self.buttonClicked4)

        btn5 = QPushButton(str(m[0][4]), self)
        btn5.move(xx[4], yy[0])
        btn5.setFixedWidth(100)
        btn5.setFixedHeight(100)
        btn5.clicked.connect(self.buttonClicked5)
        #row2
        btn6 = QPushButton(str(m[1][0]), self)
        btn6.move(xx[0], yy[1])
        btn6.setFixedWidth(100)
        btn6.setFixedHeight(100)
        btn6.clicked.connect(self.buttonClicked6)

        btn7 = QPushButton(str(m[1][1]), self)
        btn7.move(xx[1], yy[1])
        btn7.setFixedWidth(100)
        btn7.setFixedHeight(100)
        btn7.clicked.connect(self.buttonClicked7)

        btn8 = QPushButton(str(m[1][2]), self)
        btn8.move(xx[2], yy[1])
        btn8.setFixedWidth(100)
        btn8.setFixedHeight(100)
        btn8.clicked.connect(self.buttonClicked8)

        btn9 = QPushButton(str(m[1][3]), self)
        btn9.move(xx[3], yy[1])
        btn9.setFixedWidth(100)
        btn9.setFixedHeight(100)
        btn9.clicked.connect(self.buttonClicked9)

        btn10 = QPushButton(str(m[1][4]), self)
        btn10.move(xx[4], yy[1])
        btn10.setFixedWidth(100)
        btn10.setFixedHeight(100)
        btn10.clicked.connect(self.buttonClicked10)
        #row3
        btn11 = QPushButton(str(m[2][0]), self)
        btn11.move(xx[0], yy[2])
        btn11.setFixedWidth(100)
        btn11.setFixedHeight(100)
        btn11.clicked.connect(self.buttonClicked11)

        btn12 = QPushButton(str(m[2][1]), self)
        btn12.move(xx[1], yy[2])
        btn12.setFixedWidth(100)
        btn12.setFixedHeight(100)
        btn12.clicked.connect(self.buttonClicked12)

        btn13 = QPushButton(str(m[2][2]), self)
        btn13.move(xx[2], yy[2])
        btn13.setFixedWidth(100)
        btn13.setFixedHeight(100)
        btn13.clicked.connect(self.buttonClicked13)

        btn14 = QPushButton(str(m[2][3]), self)
        btn14.move(xx[3], yy[2])
        btn14.setFixedWidth(100)
        btn14.setFixedHeight(100)
        btn14.clicked.connect(self.buttonClicked14)

        btn15 = QPushButton(str(m[2][4]), self)
        btn15.move(xx[4], yy[2])
        btn15.setFixedWidth(100)
        btn15.setFixedHeight(100)
        btn15.clicked.connect(self.buttonClicked15)
        #row4
        btn16 = QPushButton(str(m[3][0]), self)
        btn16.move(xx[0], yy[3])
        btn16.setFixedWidth(100)
        btn16.setFixedHeight(100)
        btn16.clicked.connect(self.buttonClicked16)

        btn17 = QPushButton(str(m[3][1]), self)
        btn17.move(xx[1], yy[3])
        btn17.setFixedWidth(100)
        btn17.setFixedHeight(100)
        btn17.clicked.connect(self.buttonClicked17)

        btn18 = QPushButton(str(m[3][2]), self)
        btn18.move(xx[2], yy[3])
        btn18.setFixedWidth(100)
        btn18.setFixedHeight(100)
        btn18.clicked.connect(self.buttonClicked18)

        btn19 = QPushButton(str(m[3][3]), self)
        btn19.move(xx[3], yy[3])
        btn19.setFixedWidth(100)
        btn19.setFixedHeight(100)
        btn19.clicked.connect(self.buttonClicked19)

        btn20 = QPushButton(str(m[3][4]), self)
        btn20.move(xx[4], yy[3])
        btn20.setFixedWidth(100)
        btn20.setFixedHeight(100)
        btn20.clicked.connect(self.buttonClicked20)
        #row5
        btn21 = QPushButton(str(m[4][0]), self)
        btn21.move(xx[0], yy[4])
        btn21.setFixedWidth(100)
        btn21.setFixedHeight(100)
        btn21.clicked.connect(self.buttonClicked21)

        btn22 = QPushButton(str(m[4][1]), self)
        btn22.move(xx[1], yy[4])
        btn22.setFixedWidth(100)
        btn22.setFixedHeight(100)
        btn22.clicked.connect(self.buttonClicked22)

        btn23 = QPushButton(str(m[4][2]), self)
        btn23.move(xx[2], yy[4])
        btn23.setFixedWidth(100)
        btn23.setFixedHeight(100)
        btn23.clicked.connect(self.buttonClicked23)

        btn24 = QPushButton(str(m[4][3]), self)
        btn24.move(xx[3], yy[4])
        btn24.setFixedWidth(100)
        btn24.setFixedHeight(100)
        btn24.clicked.connect(self.buttonClicked24)

        btn25 = QPushButton(str(m[4][4]), self)
        btn25.move(xx[4], yy[4])
        btn25.setFixedWidth(100)
        btn25.setFixedHeight(100)
        btn25.clicked.connect(self.buttonClicked25)
        btn1.show(); btn2.show(); btn3.show(); btn4.show(); btn5.show(); btn6.show(); btn7.show(); btn8.show(); btn9.show(); btn10.show(); btn11.show(); btn12.show(); btn13.show(); btn14.show(); btn15.show(); btn16.show(); btn17.show(); btn18.show(); btn19.show(); btn20.show(); btn21.show(); btn22.show(); btn23.show(); btn24.show(); btn25.show()
        self.checklist()
        #print("Buttons was redrawed")

    def buttonClicked1(self):	#good
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

    def buttonClicked2(self):	#good
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

    def buttonClicked3(self):	#good
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

    def buttonClicked4(self):	#good
        sender = self.sender()
        if m[0][4]=='':
            m[0][4]=m[0][3]
            m[0][3]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
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

    def buttonClicked5(self):	#good
        sender = self.sender()
        if m[1][4]=='':
            m[1][4]=m[0][4]
            m[0][4]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[0][3]=='':
            m[0][3]=m[0][4]
            m[0][4]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked6(self):	#good
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

    def buttonClicked7(self):	#good
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

    def buttonClicked8(self):	#good
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

    def buttonClicked9(self):	#good
        sender = self.sender()
        if m[0][3]=='':
            m[0][3]=m[1][3]
            m[1][3]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][4]=='':
            m[1][4]=m[1][3]
            m[1][3]=''
            #print('to right',m)
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

    def buttonClicked10(self):	#good
        sender = self.sender()
        if m[0][4]=='':
            m[0][4]=m[1][4]
            m[1][4]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][4]=='':
            m[2][4]=m[1][4]
            m[1][4]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[1][3]=='':
            m[1][3]=m[1][4]
            m[1][4]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked11(self):	#good
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

    def buttonClicked12(self):	#good
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

    def buttonClicked13(self):	#good
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

    def buttonClicked14(self):	#good
        sender = self.sender()
        if m[1][3]=='':
            m[1][3]=m[2][3]
            m[2][3]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][4]=='':
            m[2][4]=m[2][3]
            m[2][3]=''
            #print('to right',m)
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

    def buttonClicked15(self):	#good
        sender = self.sender()
        if m[1][4]=='':
            m[1][4]=m[2][4]
            m[2][4]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][4]=='':
            m[3][4]=m[2][4]
            m[2][4]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[2][3]=='':
            m[2][3]=m[2][4]
            m[2][4]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked16(self):	#good
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
        if m[4][0]=='':
            m[4][0]=m[3][0]
            m[3][0]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked17(self):	#good
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
        if m[4][1]=='':
            m[4][1]=m[3][1]
            m[3][1]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][0]=='':
            m[3][0]=m[3][1]
            m[3][1]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked18(self):	#good
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
        if m[4][2]=='':
            m[4][2]=m[3][2]
            m[3][2]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][1]=='':
            m[3][1]=m[3][2]
            m[3][2]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked19(self):	#good
        sender = self.sender()
        if m[2][3]=='':
            m[2][3]=m[3][3]
            m[3][3]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][4]=='':
            m[3][4]=m[3][3]
            m[3][3]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][3]=='':
            m[4][3]=m[3][3]
            m[3][3]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][2]=='':
            m[3][2]=m[3][3]
            m[3][3]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked20(self):	#good
        sender = self.sender()
        if m[2][4]=='':
            m[2][4]=m[3][4]
            m[3][4]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][4]=='':
            m[4][4]=m[3][4]
            m[3][4]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[3][3]=='':
            m[3][3]=m[3][4]
            m[3][4]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked21(self):	#good
        sender = self.sender()
        if m[3][0]=='':
            m[3][0]=m[4][0]
            m[4][0]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][1]=='':
            m[4][1]=m[4][0]
            m[4][0]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked22(self):	#good
        sender = self.sender()
        if m[3][1]=='':
            m[3][1]=m[4][1]
            m[3][1]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][2]=='':
            m[4][2]=m[4][1]
            m[4][1]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][0]=='':
            m[4][0]=m[4][1]
            m[4][1]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked23(self):	#good
        sender = self.sender()
        if m[3][2]=='':
            m[3][2]=m[4][2]
            m[4][2]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][3]=='':
            m[4][3]=m[4][2]
            m[4][2]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][1]=='':
            m[4][1]=m[4][2]
            m[4][2]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked24(self):	#good
        sender = self.sender()
        if m[3][3]=='':
            m[3][3]=m[4][3]
            m[3][3]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][4]=='':
            m[4][4]=m[4][3]
            m[4][3]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][2]=='':
            m[4][2]=m[4][3]
            m[4][3]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClicked25(self):	#good
        sender = self.sender()
        if m[3][4]=='':
            m[3][4]=m[4][4]
            m[4][4]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[4][3]=='':
            m[4][3]=m[4][4]
            m[4][4]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def buttonClickedXY(self):
        sender = self.sender()
        if m[x-1][y]=='':
            m[x-1][y]=m[x][y]
            m[x][y]=''
            #print('to up',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[x][y+1]=='':
            m[x][y+1]=m[x][y]
            m[x][y]=''
            #print('to right',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[x+1][y]=='':
            m[x+1][y]=m[x][y]
            m[x][y]=''
            #print('to down',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        if m[x][y-1]=='':
            m[x][y-1]=m[x][y]
            m[x][y]=''
            #print('to left',m)
            self.statusBar().showMessage(sender.text() + ' was replaced')
        self.redraw()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_F:
            #self.close()
            self.statusBar().showMessage('Key <F> was pressed')
        if e.key() == Qt.Key_S:
            #self.close()
            self.statusBar().showMessage('Key <S> was pressed')
        if e.key() == Qt.Key_L:
            #self.close()
            self.statusBar().showMessage('Key <L> was pressed')
        if e.key() == Qt.Key_E:
            #self.close()
            self.statusBar().showMessage('Key <E> was pressed')

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
            (screen.height()-size.height())/2)

    def checklist(self):
#        if (m[0][0]==1) and (m[0][1]==2) and (m[0][2]==3) and (m[0][3]==4) and\
#            (m[1][0]==5) and (m[1][1]==6) and (m[1][7]==7) and (m[1][3]==8)and\
#            (m[2][0]==9) and (m[2][1]==10) and (m[2][11]==11) and (m[2][3]==12)and\
#            (m[3][0]==13) and (m[3][1]==14) and (m[3][15]==15) and (m[3][3]==16):
        if m[0][0]==1:
            btn = QPushButton("Game over", self)
            btn.move(1, 1)
            btn.setFixedWidth(529)
            btn.setFixedHeight(549)
            btn.clicked.connect(self.buttonClicked)
            btn.show()

    def buttonClicked(self):
        self.close()


#definition of
m = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
z=0

for i in range(0, 5):
    for y in range(0, 5):
        x = 1
        while (x == 1 and z!=25):
            r1 = random.randint(0, 24)
            if r1 in list1:
                list1[r1] = None
                            #-1
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
