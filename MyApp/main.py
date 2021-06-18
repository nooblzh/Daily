#  __
# |  |  __ __  ____
# |  | |  |  \/  _ \
# |  |_|  |  (  <_> )
# |____/____/ \____/
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets, QtGui, QtCore
from MyApp import Ui_MainWindow
from PIL import Image
import sys
import os


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.root = None
        self.toolButton.clicked.connect(self.showPath)
        self.pushButton.clicked.connect(self.changeName)
        self.pushButton_7.clicked.connect(self.clearOutput)
        self.pushButton_2.clicked.connect(self.RGBtoGray)
        self.pushButton_4.clicked.connect(self.OtherToPng)
        self.pushButton_3.clicked.connect(self.adjustScale)
        print(self.root)

    def clearOutput(self):
        self.textBrowser.clear()

    def showPath(self):
        target_path = QtWidgets.QFileDialog.getExistingDirectory(self, '浏览', '/Users/law')
        self.root = target_path
        self.textBrowser.append(self.root)

    def changeName(self):
        if os.path.exists(self.root) is True and self.root is not None:
            file = os.listdir(self.root)
            if '.DS_Store' in file:
                file.remove('.DS_Store')
            file.sort()
            self.textBrowser.append('--------开始改名--------')
            n = 0
            for i in file:
                oldname = file[n]
                newname = str(n) + '.png'
                self.textBrowser.append('正在改名:{}'.format(i))
                os.rename(self.root+'/'+oldname, self.root+'/'+newname)
                n = n + 1
            self.textBrowser.append('--------改名结束--------')
        else:
            error = QMessageBox.information(self, 'Error', '请先选择文件所在的位置！！！', QMessageBox.Yes)

    def RGBtoGray(self):
        if os.path.exists(self.root) is True and self.root is not None:
            parent_path = os.path.dirname(self.root)
            save_path = os.path.join(parent_path, 'gray')
            if os.path.exists(save_path) is False:
                os.mkdir(save_path)
            # print(os.path.exists(save_path))
            file = os.listdir(self.root)
            if '.DS_Store' in file:
                file.remove('.DS_Store')
            self.textBrowser.append('--------开始转换--------')
            for imageName in file:
                self.textBrowser.append('正在转换{}'.format(imageName))
                im = Image.open(os.path.join(self.root, imageName)).convert('L')
                im.save(os.path.join(save_path, imageName))

            self.textBrowser.append('--------转换完成--------')
        else:
            error = QMessageBox.information(self, 'Error', '请先选择文件所在的位置！！！', QMessageBox.Yes)

    def adjustScale(self):
        if os.path.exists(self.root) is True and self.root is not None:
            print(self.root)
        else:
            error = QMessageBox.information(self, 'Error', '请先选择文件所在的位置！！！', QMessageBox.Yes)

    def OtherToPng(self):
        if os.path.exists(self.root) is True and self.root is not None:
            parent_path = os.path.dirname(self.root)
            save_path = os.path.join(parent_path, 'png')
            if os.path.exists(save_path) is False:
                os.mkdir(save_path)
            self.textBrowser.append('--------开始转换--------')
            file = os.listdir(self.root)
            if '.DS_Store' in file:
                file.remove('.DS_Store')
            for imageName in file:
                self.textBrowser.append('正在转换{}'.format(imageName))
                image = Image.open(os.path.join(self.root, imageName))
                image.save(os.path.join(save_path, imageName[:-4] + '.png'))

            self.textBrowser.append('--------转换完成--------')
        else:
            error = QMessageBox.information(self, 'Error', '请先选择文件所在的位置！！！', QMessageBox.Yes)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
