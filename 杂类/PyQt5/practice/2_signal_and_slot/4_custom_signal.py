import sys
from PyQt5.QtCore import pyqtSignal                             # 1
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


# key points
# 导入pyqtSignal包
# 实例化一个my_signal
# my_signal.emit()即可发出自定义信号

# 另外，这个例子还监控了鼠标信号，
# mousePressEvent()方法是许多控件自带的，这里来自于QWidget。这里对这个函数重写了
# 该方法用来监测鼠标是否有按下。现在鼠标若被按下，则会发出自定义的信号。
class Demo(QWidget):
    my_signal = pyqtSignal()                                    # 2

    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel('Hello World', self)
        self.my_signal.connect(self.change_text)                # 3

    def change_text(self):
        if self.label.text() == 'Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')

    def mousePressEvent(self, QMouseEvent):                     # 4重写父类QWidget中的鼠标动作函数,它本来就是工作的
        self.my_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())