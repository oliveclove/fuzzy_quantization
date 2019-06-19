import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from menu import Ui_MainWindow
import sentiAnalysis as sa
import word_fetch as wf

#需要继承Ui_MainWindow
class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QWidget.__init__(self)
        
        #用setupUi完成初始化窗口的操作
        self.setupUi(self)
        self.pushButton.clicked.connect(self.avc)
        self.pushButton_2.clicked.connect(self.aac)
        self.pushButton_3.clicked.connect(self.score)

    def avc(self):
        text=self.textEdit.toPlainText()
        word_f = wf.word_classify(text)
        r=word_f.adv_v_classify()
        if r == []:
            self.textBrowser.append('不存在副词-动词的组合')
        else:
            avc_str = str(r)
            self.textBrowser.append(avc_str)

    def aac(self):
        text=self.textEdit.toPlainText()
        word_f = wf.word_classify(text)
        r = word_f.adv_adj_classify()
        if r == []:
            self.textBrowser_2.append('不存在副词-形容词的组合')
        else:
            aac_str = str(r)
            self.textBrowser_2.append(aac_str)

    def score(self):
        text=self.textEdit.toPlainText()
        sA = sa.senti_AVAC()
        r=str(sA.sent_sc(text))
        self.textBrowser_3.append(r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
