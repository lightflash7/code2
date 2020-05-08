import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout


# key points
# QGridLayout的addWidget()方法遵循如下语法形式：addWidget(widget, row, column, rowSpan, columnSpan)
# widget就是要添加的控件；row为第几行，0代表第一行；column为第几列，0代表第一列；rowSpan表示要让这个控件去占用几行(默认一行)；columnSpan表示要让这个控件去占用几列(默认一列)。
class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.grid_layout = QGridLayout()                                # 1
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)         # 2
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        # 前四行由于有默认值也可以写成如下：
        # self.grid_layout.addWidget(self.user_label, 0, 0)
        # self.grid_layout.addWidget(self.user_line, 0, 1)
        # self.grid_layout.addWidget(self.pwd_label, 1, 0)
        # self.grid_layout.addWidget(self.pwd_line, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)                       # 3
        self.v_layout.addLayout(self.h_layout)                          # 4

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())