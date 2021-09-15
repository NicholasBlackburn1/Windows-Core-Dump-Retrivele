"""
Main file for the module this is where code will execute
"""
from CoreDumpRetreval import ColorLog
from messaging import messaging
import imports 



## this is the main function this will run the module when u rn py CoredumpRetrievals

def Main():
    #imports.logging.basicConfig(filename= str(imports.datetime.now().strftime('CoreDumpCollector%Y-%m-%d_%H-%M-%s.log')),level=imports.logging.DEBUG)
   
    ColorLog.Warning("starting up Core Dump Collector...")



    # Runs on Windows platform
    if(imports.platform.system()== 'Windows'):  
        ColorLog.PipeLine_Ok('Running on windows... Now going to do windows stuff With windows paths')
        
        ColorLog.PipeLine_Data("Config file:"+str(imports.pathlib.Path.cwd())+"\Config.ini")
        
        config = imports.configparser.ConfigParser()
        config.read(str(imports.pathlib.Path.cwd())+"\Config.ini")
        
        email = config['EMAIL']



    # Runs on linux platform
    if(imports.platform.system()== 'Linux'):  
    
        ColorLog.PipeLine_Ok('Running on Linux... Now going to do windows stuff With Linux paths')
        
        ColorLog.PipeLine_Data("Config file:"+" "+str(imports.pathlib.Path.cwd())+"/Config.ini")

        # this will read the config.ini
        config = imports.configparser.ConfigParser()
        config.read((str(imports.pathlib.Path.cwd())+"/"+"Config.ini"))
       
        email= config['EMAIL']

        # sets email up to be sent
        messaging.emailServerConfig(messaging,email['ip'],email['port'],email['sender'],email['password'])
        messaging.sendTestEmail(messaging)
     
















if __name__== '__main__':
    Main()
