import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout


# 这个例子告诉我们垂直（水平）布局管理器还可以处理水平（垂直）管理器自身
# 将两个QLabel用垂直布局方式摆放，将两个QLineEdit也用垂直布局方式摆放，最后用一个水平布局管理来摆放着两个垂直布局管理器。
class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.label_v_layout = QVBoxLayout()                      # 1
        self.line_v_layout = QVBoxLayout()                       # 2
        self.button_h_layout = QHBoxLayout()                     # 3
        self.label_line_h_layout = QHBoxLayout()                 # 4
        self.all_v_layout = QVBoxLayout()                        # 5

        self.label_v_layout.addWidget(self.user_label)           # 6
        self.label_v_layout.addWidget(self.pwd_label)
        self.line_v_layout.addWidget(self.user_line)
        self.line_v_layout.addWidget(self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)
        self.label_line_h_layout.addLayout(self.label_v_layout)  # 7
        self.label_line_h_layout.addLayout(self.line_v_layout)
        self.all_v_layout.addLayout(self.label_line_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)


# 其实这个思路好点：
        # 三个水平，最后垂直起来
        # self.user_h_layout = QHBoxLayout()
        # self.pwd_h_layout = QHBoxLayout()
        # self.button_h_layout = QHBoxLayout()
        # self.all_v_layout = QVBoxLayout()
        #
        # self.user_h_layout.addWidget(self.user_label)
        # self.user_h_layout.addWidget(self.user_line)
        # self.pwd_h_layout.addWidget(self.pwd_label)
        # self.pwd_h_layout.addWidget(self.pwd_line)
        # self.button_h_layout.addWidget(self.login_button)
        # self.button_h_layout.addWidget(self.signin_button)
        # self.all_v_layout.addLayout(self.user_h_layout)
        # self.all_v_layout.addLayout(self.pwd_h_layout)
        # self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())