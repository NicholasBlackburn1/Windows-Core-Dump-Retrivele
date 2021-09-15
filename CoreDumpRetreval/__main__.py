"""
Main file for the module this is where code will execute
"""
import imports 








## this is the main function this will run the module when u rn py CoredumpRetrievals
def Main():
    imports.logging.basicConfig(filename= str(imports.datetime.now().strftime('CoreDumpCollector%Y-%m-%d_%H-%M-%s.log')),level=imports.logging.DEBUG)

    print("starting up Core Dump Collector...")
    imports.logging.info("Starting Up the CoreDumpCollector")


    

















if __name__== '__main__':
    Main()
