import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


# key points
# 1、实例化一个QPushButton并将clicked信号与自定义的show_messagebox槽函数连接起来，这样点击按钮后，信号发出，槽函数就会启动
# 2、基本用法如下：QMessageBox.information(QWidget, 'Title', 'Content', buttons)
#    常见的按钮种类有以下几种：    QMessageBox.Ok  QMessageBox.Yes  QMessageBox.No  QMessageBox.Close   QMessageBox.Cancel  QMessage.Open  QMessage.Save
# 3、如果你没有显示指定信息框的按钮，那信息框会自己默认加上合适的按钮上去

# 另外，除了information类型的message框，还有QMessageBox.question 问答框
#                                       QMessageBox.warning 警告框
#                                      ​QMessageBox.critical 错误框
#                                       QMessageBox.about 关于框
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('information', self)
        self.button.clicked.connect(self.show_messagebox)      # 1

    def show_messagebox(self):
        QMessageBox.information(self, 'MyTitle', 'MyContent',
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())