import sys
import os
import ui_Login
import PyQt5
from pathlib import Path, PureWindowsPath
from images import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ui_Register(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setLayout(self.ui_Layout())
        self.setFixedSize(self.sizeHint())
        self.setWindowFlag(Qt.FramelessWindowHint)

    def ui_Layout(self):
        #Inv
        inv1 = QLabel()

        #Labels
        label1 = QLabel('Username: ')
        label2 = QLabel('First Name: ')
        label3 = QLabel('Last Name: ')
        label4 = QLabel('Password: ')
        label5 = QLabel('Re-type Password: ')

        #Image
        imageLabel = QLabel()
        pixmap = QPixmap(os.path.join(sys.path[0], 'images\weather-icon.png'))
        pixmap = pixmap.scaledToWidth(150)
        imageLabel.setPixmap(pixmap)
        imageLabel.setFixedHeight(150)
        imageLabel.setAlignment(Qt.AlignCenter)

        #LineEdits
        self.usrbox = QLineEdit()
        self.fnbox = QLineEdit()
        self.lnbox = QLineEdit()
        self.passbox = QLineEdit()
        self.repassbox = QLineEdit()
        self.passbox.setEchoMode(QLineEdit.Password)
        self.repassbox.setEchoMode(QLineEdit.Password)

        #Buttons
        registerbutton = QPushButton('Register')
        cancelbutton = QPushButton('Cancel')

        #Button Action
        cancelbutton.clicked.connect(self.on_cancel_clicked)
        registerbutton.clicked.connect(self.on_register_clicked)

        #Layout
        input_layout = QGridLayout()
        final_layout = QVBoxLayout()
        cancel_layout = QHBoxLayout()

        input_layout.addWidget(label1, 0,0)
        input_layout.addWidget(self.usrbox, 0,1)
        input_layout.addWidget(label2, 1,0)
        input_layout.addWidget(self.fnbox, 1,1)
        input_layout.addWidget(label3, 2,0)
        input_layout.addWidget(self.lnbox, 2,1)
        input_layout.addWidget(label4, 3,0)
        input_layout.addWidget(self.passbox, 3,1)
        input_layout.addWidget(label5, 4,0)
        input_layout.addWidget(self.repassbox, 4,1)

        cancel_layout.addWidget(inv1)
        cancel_layout.addWidget(cancelbutton)

        final_layout.addWidget(imageLabel)
        final_layout.addSpacing(50)
        final_layout.addLayout(input_layout)
        final_layout.addWidget(registerbutton)
        final_layout.addSpacing(100)
        final_layout.addLayout(cancel_layout)

        return final_layout

    @pyqtSlot()
    def on_register_clicked(self):
        msg = QMessageBox()
        msg.setWindowTitle('Warning!')
        pixmap = QPixmap(32,32)
        pixmap.fill(Qt.transparent)
        msg.setWindowIcon(QIcon(pixmap))
        
        if self.usrbox.text() != '' and self.fnbox.text() != '' and self.lnbox.text() != '' and self.passbox.text() != '' and self.repassbox.text() != '': 
            if self.passbox.text() == self.repassbox.text():
                print('ok')
            else:
                msg.setText('Password did not match.')
                msg.exec_()
        else:
            msg.setText('Pls Complete Information.')
            msg.exec_()
        return


    @pyqtSlot()
    def on_cancel_clicked(self):
        self.window = ui_Login.ui_Login()
        self.hide()
        self.window.exec_()


if __name__ == '__main__':
    app = QApplication([])
    
    window = ui_Register()
    cond = window.show()

    sys.exit(app.exec_())