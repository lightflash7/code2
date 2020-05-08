import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


# key points
# self.button1.clicked.connect   and     disconnect
# clicked(按钮被点击)是该控件的一个信号，connect()即连接
# self.change_text即下方定义的函数(我们称之为槽函数)。
# 所以通用的公式可以是：widget.signal.connect(slot)
class Demo(QWidget):                                            # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.button1 = QPushButton('hello world', self)                # 2
        self.button1.clicked.connect(self.change_text)           # 3绑定click信号与槽函数

    def change_text(self):
        print('change text')
        self.button1.setText('goodbye world')                             # 4
        self.button1.clicked.disconnect(self.change_text)        # 5解绑槽函数(不必要)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()                                               # 6
    demo.show()                                                 # 7
    sys.exit(app.exec_())
