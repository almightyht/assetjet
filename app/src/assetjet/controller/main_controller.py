import os
from PySide import QtGui, QtCore
from assetjet.view.vw_main import Ui_Main
from assetjet.cfg import db
from assetjet.log import log
from assetjet.util import util
import sqlalchemy.orm as orm

from assetjet.model import asset

class MainController(QtGui.QMainWindow):

    eventsInitialised = False
            
    def __init__(self, parent=None):
        super(MainController, self).__init__(parent)
            
    def show_(self):        
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        mainPath = os.path.join(util.getBaseDir(), 'httpdocs', 'main.html')
        mainUrl = QtCore.QUrl.fromLocalFile(mainPath)
        self.ui.webView.load(mainUrl)
        self.ui.webView.url = mainUrl
        self.show()
        self.setWindowState(QtCore.Qt.WindowMaximized)


        """
        tickers = self.GetAllSymbols()

        for i in range(0, len(tickers)):            
            #liTicker = self.lstSymbols.model.item(i, 0)
            liTicker = QtGui.QListWidgetItem(tickers[i].name)
            self.ui.lstSymbolList.addItem(liTicker)
        """

               