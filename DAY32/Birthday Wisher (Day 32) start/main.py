import smtplib    

#-------------SEND EMAIL-----------------#
""" 
SMTP INFORMATION
Gmail  smtp.gmail.com  host
Hotmail smtp.live.com
Yahoo   smtp.mail.yahoo.com
   """

e = "radimelfi.bautista01@hotmail.com"
k= input(str("enter your password: "))


conection = smtplib.SMTP("smtp.live.com", 587) #It is different for each email
conection.starttls() #transport Layer security of email
conection.login(user=e , password=k)
print("login success")
conection.sendmail(from_addr=e, to_addrs="radimelfibautistaantigua@gmail.com", 
                   msg="Subject:Hello\n\nThis is the body of my email.")
conection.close()
