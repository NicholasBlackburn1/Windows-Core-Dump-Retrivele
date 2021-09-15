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

    def sendTestEmail(self,whatOS,osversion):
            
        message = imports.MIMEMultipart("alternative")
        message["Subject"] = "Oh No a "+ str(whatOS)+" "+ "Computer as crashed"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        # plain-text Message
        text = """\
        Hi,
        How are you?
        A pc Crashed!
        here is some info Below!"""

        OperatingSystem = "\
            <h3> OS:"+str(whatOS)+"</h3>"

        version="\
            <h4>VERSION:"+" "+str(osversion)+"</h>"


        # Turn these into plain/html MIMEText objects
        part1 = imports.MIMEText(text, "plain")
        part2 = imports.MIMEText(OperatingSystem, "html")
        part3 = imports.MIMEText(version, "html")


        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)
        message.attach(part3)

            
        # Try to log in to server and send email
        try:
            ColorLog.Warning("Connecting to EmailServer....")
            server = imports.smtplib.SMTP(self.smtp_server,self.port)
            server.ehlo() # Can be omitted
            server.starttls(context=self.context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(self.sender_email, self.password)

            ColorLog.PipeLine_Ok("got connection to Email Server...")
            
            ColorLog.Warning("sending  email...")
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            ColorLog.PipeLine_Ok("sent  email...")
            
        except Exception as e:
            # Print any error messages to stdout
            ColorLog.Error(e)
        finally:
            server.quit() 