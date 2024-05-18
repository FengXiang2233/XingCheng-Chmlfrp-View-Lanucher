import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton


class Lanucher_tunnel(QWidget):

    def __init__(self):
        super().__init__()
        self.show()


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 650)
        self.setWindowTitle('XingCheng-Chmlfrp-View-Lanucher')
        self.view = QWebEngineView()
        self.view.load(QUrl('https://panel.chmlfrp.cn/'))
        self.setCentralWidget(self.view)
        self.pb = QPushButton("启动隧道", self)
        self.pb.clicked[bool].connect(self.lanucher)
        self.pb.setGeometry(860, 590,140,60)
        self.show()

    def lanucher(self):
        self.LanucherWin=Lanucher_tunnel()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    k = App()
    sys.exit(app.exec_())
