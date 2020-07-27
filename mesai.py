from PyQt5 import QtWidgets
import sys

from saatkayit import Ui_hesap
from anasayfa import Ui_anasayfa
from PyQt5.QtGui import *

class uygulama(QtWidgets.QMainWindow):
    def __init__(self):
        super(uygulama, self).__init__()    
        self.ui = Ui_anasayfa()        
        self.ui.setupUi(self)
            
                
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = uygulama()
    win.setWindowTitle("Mustafa Teker")
    jpg = QIcon("mt.jpg")
    win.setWindowIcon(jpg)
    win.show()
    sys.exit(app.exec ())       
app()


