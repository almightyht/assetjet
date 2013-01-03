
import ConfigParser, os
from assetjet.util import util

class Cfg(ConfigParser.ConfigParser):
    DbFileName = ""
    UpdateUrl = ""
    def __init__(self, cfgFile=None):
        ConfigParser.ConfigParser.__init__(self)
        if cfgFile is None:
            return
        defaultDbFileName = str(cfgFile.get('Database', 'filePath'))    
        self.DbFileName = defaultDbFileName 
        self.UpdateUrl = str(cfgFile.get('Updates', 'url'))    
        

config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join(util.getBaseDir(), 'app.cfg')))
root = Cfg(config)