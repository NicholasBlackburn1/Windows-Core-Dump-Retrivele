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

    def sendTestEmail(self,whatOS,arch,osversion,hostname):
            
        message = imports.MIMEMultipart("alternative")
        message["Subject"] = "Oh No a "+ str(whatOS)+" "+ "Computer as crashed at "+str(imports.datetime.now())
        message["From"] = self.sender_email
        message["To"] = self.receiver_email



        
        version="\
            <h3>VERSION:"+" "+str(osversion)+"</h3>"

        OperatingSystem = "\
            <h3> OS:"+" "+str(whatOS)+" "+str(arch)+"</h3>" + version

        HostName= "\
            <h3> Hostname:"+" "+str(hostname)+"</h3>" +OperatingSystem

        Intro = "\
        <h4> "+"Hi,\
        How are you ? \
        Probally Not good....\
        A pc Crashed!\
        here is some info Below!</h4>"+ HostName


        

    
        # Turn these into plain/html MIMEText objects
     
        part2 = imports.MIMEText(Intro, "html")


        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part2)
      
            
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