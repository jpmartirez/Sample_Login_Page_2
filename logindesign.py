
from PyQt6 import QtCore, QtGui, QtWidgets
import resources

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(925, 602)
        
        flags = QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint
        Login.setWindowFlags(flags)
        Login.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.label = QtWidgets.QLabel(parent=Login)
        self.label.setGeometry(QtCore.QRect(180, 60, 611, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/cp.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(parent=Login)
        self.frame.setGeometry(QtCore.QRect(340, 80, 291, 461))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 50%;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(parent=Login)
        self.label_2.setGeometry(QtCore.QRect(330, 130, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(parent=Login)
        self.username.setGeometry(QtCore.QRect(380, 220, 211, 31))
        self.username.setStyleSheet("border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: #efefef;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(parent=Login)
        self.password.setGeometry(QtCore.QRect(380, 290, 211, 31))
        self.password.setStyleSheet("border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: #efefef;")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.loginbtn = QtWidgets.QPushButton(parent=Login)
        self.loginbtn.setGeometry(QtCore.QRect(380, 370, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.loginbtn.setFont(font)
        self.loginbtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.loginbtn.setStyleSheet("QPushButton {\n"
"    border-radius: 20%;\n"
"    color: white;\n"
"    background-color: black;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border: 2px solid black;\n"
"    color: black;\n"
"    background-color: white;\n"
"\n"
"\n"
"}")
        self.loginbtn.setObjectName("loginbtn")
        self.label_3 = QtWidgets.QLabel(parent=Login)
        self.label_3.setGeometry(QtCore.QRect(390, 415, 101, 31))
        self.label_3.setObjectName("label_3")
        self.create_account = QtWidgets.QPushButton(parent=Login)
        self.create_account.setGeometry(QtCore.QRect(490, 420, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.create_account.setFont(font)
        self.create_account.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.create_account.setStyleSheet("border:none;\n"
"")
        self.create_account.setObjectName("create_account")
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.username.raise_()
        self.password.raise_()
        self.loginbtn.raise_()
        self.label_3.raise_()
        self.create_account.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.label_2.setText(_translate("Login", "L O G I N  "))
        self.username.setPlaceholderText(_translate("Login", "Username"))
        self.password.setPlaceholderText(_translate("Login", "Password"))
        self.loginbtn.setText(_translate("Login", "L O G I N"))
        self.label_3.setText(_translate("Login", "Not registred yet?"))
        self.create_account.setText(_translate("Login", "Create an account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
