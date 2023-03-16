import smtplib    

#-------------SEND EMAIL----------------#
""" 
SMTP INFORMATION
Gmail  smtp.gmail.com  host
Hotmail smtp.live.com
Yahoo   smtp.mail.yahoo.com
   """

e = "radimelfibautistaantigua@gmail.com"
k= input(str("enter your password: "))


conection = smtplib.SMTP("smtp.gmail.com", 587) #It is different for each email
conection.starttls() #transport Layer security of email
conection.login(user=e , password=k)
print("login success")
conection.sendmail(from_addr=e, to_addrs="radimelfi.bautista01@hotmail.com", 
                   msg="Subject:Hello\n\nThis is the body of my email.")
conection.close()
#--------------------------------------------------------------------------------#

sender ="radimelfibautistaantigua@gmail.com" 
recive= "radimelfi.bautista01@hotmail.com"
p = input(str("please enter your password: "))


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls
    smtp.ehlo()
    smtp.login(sender, p)
    subject = 'grab dinner this weekend?'
    body = 'How about dinner at 7pm this sunday'
    msg= f'Subject:{subject}\n\n{body}'
    smtp.sendmail(sender,recive,msg)
    smtp.close()





#"tkkveyqqnbdlzzoq"