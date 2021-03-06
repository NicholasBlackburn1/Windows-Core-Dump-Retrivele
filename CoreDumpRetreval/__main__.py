"""
Main file for the module this is where code will execute
"""
from sys import version
import ColorLog
from messaging import messaging
import imports 


# allows me to send emails withtout cultterign up main function
def sendmail(email,filename):
    
        # sets email up to be sent
        messaging.emailServerConfig(messaging,email['ip'],email['port'],email['sender'],email['password'],email['recv'])
        messaging.sendTestEmail(messaging,whatOS=imports.platform.system(),osversion=imports.platform.version(),hostname=imports.platform.node(),processor=imports.platform.processor(),filename=filename)

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
        dmp=False
        if(dmp == True):
            # sets email up to be sent
            sendmail(email,str("C:\Windows\memory.dmp"))
        else:
            messaging.emailServerConfig(messaging,email['ip'],email['port'],email['sender'],email['password'],email['recv'])
            messaging.sendUpdateLog(messaging,whatOS=imports.platform.system(),osversion=imports.platform.version(),hostname=imports.platform.node(),processor=imports.platform.processor(),filename=str(imports.pathlib.Path.home())+"\Desktop\WindowsUpdate.txt")


    # Runs on linux platform
    if(imports.platform.system()== 'Linux'):  
    
        ColorLog.PipeLine_Ok('Running on Linux... Now going to do windows stuff With Linux paths')
        
        ColorLog.PipeLine_Data("Config file:"+" "+str(imports.pathlib.Path.cwd())+"/Config.ini")

        # this will read the config.ini
        config = imports.configparser.ConfigParser()
        config.read((str(imports.pathlib.Path.cwd())+"/"+"Config.ini"))
       
        email= config['EMAIL']

        print(imports.pathlib.Path.home())
        # sets email up to be sent

        sendmail(email,(str(imports.pathlib.Path.cwd())+"/"+"testfile.txt"))














if __name__== '__main__':
    Main()
