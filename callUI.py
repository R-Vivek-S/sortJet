from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication,QFileDialog
import sys
import SORT

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('SORT.ui', self)
        self.show()
        self.Path.clicked.connect(self.browsefiles)
        self.path.clicked.connect(self.sortB)

    def browsefiles(self):
        self.Fpath= QFileDialog.getExistingDirectory(self,'open file') 
        self.lineEdit.setText(Fpath)
    def sortB():
        SORT.sort(self.Fpath)   

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
app.exec_()