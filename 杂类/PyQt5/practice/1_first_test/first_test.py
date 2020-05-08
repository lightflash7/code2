import sys
from PyQt5.QtWidgets import QApplication, QLabel


# keypoint
# QLabel显示文字
# QLabel文字的两种设置办法：1、定义时候设置 2、setText方法
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # label = QLabel(‘HelloWorld’)  # 2
    label = QLabel() #QLabel展示图片或者文字
    label.setText('Hello World')
    label.show()
    sys.exit(app.exec_())# app.exec()执行界面程序