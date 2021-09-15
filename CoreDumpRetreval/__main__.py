"""
Main file for the module this is where code will execute
"""
import ColorLog
from messaging import messaging
import imports 


# allows me to send emails withtout cultterign up main function
def sendmail(email):
    
        # sets email up to be sent
        messaging.emailServerConfig(messaging,email['ip'],email['port'],email['sender'],email['password'],email['recv'])
        messaging.sendTestEmail(messaging,imports.platform.system(),imports.platform.version())

## this is the main function this will run the module when u rn py CoredumpRetrievals

def Main():
    #imports.logging.basicConfig(filename= str(imports.datetime.now().strftime('CoreDumpCollector%Y-%m-%d_%H-%M-%s.log')),level=imports.logging.DEBUG)
   
    ColorLog.Warning("starting up Core Dump Collector...")



    # Runs on Windows platform
    if(imports.platform.system()== 'Windows'):  
        ColorLog.PipeLine_Ok('Running on windows... Now going to do windows stuff With windows paths')
        
        ColorLog.PipeLine_Data("Config file:"+str(imports.pathlib.Path.cwd())+"\Config.ini")
        
        # this will read the config.ini
        config = imports.configparser.ConfigParser()
        config.read(str(imports.pathlib.Path.cwd())+"\Config.ini")
        
        email = config['EMAIL']


        # sets email up to be sent
        sendmail(email)

    # Runs on linux platform
    if(imports.platform.system()== 'Linux'):  
    
        ColorLog.PipeLine_Ok('Running on Linux... Now going to do windows stuff With Linux paths')
        
        ColorLog.PipeLine_Data("Config file:"+" "+str(imports.pathlib.Path.cwd())+"/Config.ini")

        # this will read the config.ini
        config = imports.configparser.ConfigParser()
        config.read((str(imports.pathlib.Path.cwd())+"/"+"Config.ini"))
       
        email= config['EMAIL']

        # sets email up to be sent
        sendmail(email)














if __name__== '__main__':
    Main()
