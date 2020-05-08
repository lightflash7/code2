import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout, QFormLayout


# key points
# 表单布局QFormLayout 以及该对象的addRow(left, right)方法
# 表单布局可以将控件以两列的形式进行排布，左列控件为文本标签，右列为输入型的控件，如QLineEdit。用这个布局管理器我们可以更加快速方便地构写有表单的界面。
# 下面即用表单布局对第三个代码的改写
class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.f_layout = QFormLayout()                           # 1
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.f_layout.addRow(self.user_label, self.user_line)   # 2
        self.f_layout.addRow(self.pwd_label, self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)
        self.all_v_layout.addLayout(self.f_layout)              # 3
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())