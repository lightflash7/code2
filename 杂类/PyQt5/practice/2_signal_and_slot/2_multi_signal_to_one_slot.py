import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


# 多信号连接同一个槽函数
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.pressed.connect(self.change_text)     # 1
        self.button.released.connect(self.change_text)    # 2

    def change_text(self):
        if self.button.text() == 'Start':                 # 3
            self.button.setText('Stop')
        else:
            self.button.setText('Start')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())