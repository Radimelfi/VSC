import smtplib    

#-------------SEND EMAIL-----------------#
""" 
SMTP INFORMATION
Gmail  smtp.gmail.com  host
Hotmail smtp.live.com
Yahoo   smtp.mail.yahoo.com
   """

e = "radimelfibautistaantigua@gmail.com"
k = "lkhb1598kjm"


conection = smtplib.SMTP("smtp.gmail.com") #It is different for each email
conection.starttls() #transport Layer security of email
conection.login(user=e , password=k)
conection.sendmail(from_addr=e, to_addrs="radimelfi.bautista01@hotmail.com", 
                   msg="Subject:Hello\n\nThis is the body of my email.")
conection.close()
