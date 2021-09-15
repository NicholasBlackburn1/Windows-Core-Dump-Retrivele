"""
this will handle emailin he user a coredump file from widows
"""

import imports 
import ColorLog
class messaging(object):

    global  smtp_server 
    global sender_email 
    global password


    def emailServerConfig(self,smtp_server,port,sender_email,password):
        ColorLog.Warning("SMTP SERVER CONFIG:"+" "+ str(smtp_server)+" "+ str(port) +" "+str(sender_email)+ " "+str("password"))
        self.smtp_server =smtp_server
        self. port = port
        self.sender_email = sender_email
        self.password = password


   
    # Create a secure SSL context
    context = imports.ssl.create_default_context()

    def sendTestEmail(self):
            
        # Try to log in to server and send email
        try:
            server = imports.smtplib.SMTP(self.smtp_server,self.port)
            self.server.ehlo() # Can be omitted
            self.server.starttls(context=self.context) # Secure the connection
            self.server.ehlo() # Can be omitted
            self.server.login(self.sender_email, self.password)
            # TODO: Send email here
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            self.server.quit() 