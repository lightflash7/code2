import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


# 额外知识：调整QWidget大小： .resize(300,400)
# 额外知识2:设置窗口名称setWindowTitle('name')
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)                                   # 1
        self.setWindowTitle('demo')                             # 2
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_window_size)    # 3
        self.button.clicked.connect(self.change_window_title)   # 4

    def change_text(self):
        print('change text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):                               # 5
        print('change window size')
        self.resize(500, 500)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):                              # 6
        print('change window title')
        self.setWindowTitle('window title changed')
        self.button.clicked.disconnect(self.change_window_title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())