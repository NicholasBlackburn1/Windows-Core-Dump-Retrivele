"""
this will handle emailin he user a coredump file from widows
"""

import imports 
import ColorLog
class messaging(object):

    global  smtp_server 
    global sender_email 
    global password
    global port 
    global receiver_email

    #sets vars for 
    def emailServerConfig(self,smtp_server,port,sender_email,password, receiver_email):
        ColorLog.PipeLine_init("SMTP SERVER CONFIG:"+" "+ str(smtp_server)+" "+ str(port) +" "+str(sender_email)+ " "+str(password)+ " "+str(receiver_email))
        self.smtp_server =smtp_server
        self. port = port
        self.sender_email = sender_email
        self.password = password
        self.receiver_email = receiver_email


   
    # Create a secure SSL context
    context = imports.ssl.create_default_context()

    def sendTestEmail(self):
            
        # Try to log in to server and send email
        try:
            ColorLog.Warning("Connecting to EmailServer....")
            server = imports.smtplib.SMTP(self.smtp_server,self.port)
            server.ehlo() # Can be omitted
            server.starttls(context=self.context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(self.sender_email, self.password)

            ColorLog.Warning("got connection to Email Server...")

            ColorLog.Warning("sending  email...")
            server.sendmail(self.sender_email, self.receiver_email, "hello world")

            ColorLog.PipeLine_Ok("sent nt email")
            
        except Exception as e:
            # Print any error messages to stdout
            ColorLog.Error(e)
        finally:
            server.quit() 