"""
Main file for the module this is where code will execute
"""
import imports 



## this is the main function this will run the module when u rn py CoredumpRetrievals

def Main():
    #imports.logging.basicConfig(filename= str(imports.datetime.now().strftime('CoreDumpCollector%Y-%m-%d_%H-%M-%s.log')),level=imports.logging.DEBUG)
   
    print("starting up Core Dump Collector...")



    if(imports.platform.system()== 'Windows'):  
        print('Running on windows... Now going to do windows stuff With windows paths')
        
        print("Config file:"+str(imports.pathlib.Path.cwd())+"\Config.ini")
        
        config = imports.configparser.ConfigParser()
        config.read(str(imports.pathlib.Path.cwd())+"\Config.ini"))



    
    if(imports.platform.system()== 'Linux'):  
    
        print('Running on Linux... Now going to do windows stuff With Linux paths')
        
        print("Config file:"+str(imports.pathlib.Path.cwd())+"/Config.ini")

        # this will read the config.ini
        config = imports.configparser.ConfigParser())
        config.read((str(imports.pathlib.Path.cwd())+"\Config.ini")

















if __name__== '__main__':
    Main()
