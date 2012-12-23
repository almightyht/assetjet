from PySide import QtGui
from src.view.vw_main import Ui_Main
from src.cfg import db
import sqlalchemy.orm as orm

from src.model import symbol

class MainController(QtGui.QMainWindow):

    eventsInitialised = False
            
    def __init__(self, parent=None):
        super(MainController, self).__init__(parent)
            
    def Show(self):
        # Go borderless so it looks the same no matter what platform? TBD
        
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        tickers = self.GetAllSymbols()

        for i in range(0, len(tickers)):            
            #liTicker = self.lstSymbols.model.item(i, 0)
            liTicker = QtGui.QListWidgetItem(tickers[i].symbol)
            self.ui.lstSymbolList.addItem(liTicker)
            super(QtGui.QMainWindow, self).show()

    def GetAllSymbols(self):
        Session = orm.sessionmaker(bind=db.GetEngine())        
        session = Session()
        return session.query(symbol.Symbol).all()

"""
    def InitialiseEvents(self):
        self.connect(self.ui.lstSymbolList, SIGNAL("doubleClicked()", self.AddSymbol)
        
    def AddSymbol(self):
        pass
"""        
               