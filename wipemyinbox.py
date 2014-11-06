#!/usr/bin/python3 

import imaplib
import getpass
mail_address = str(input('Email: '))
passwd = getpass.getpass()
connection = imaplib.IMAP4_SSL('imap.mail.yahoo.com')
if '@yahoo.com' in mail_address:
    connection.login(mail_address, passwd)
else:
    connection.login(mail_address+'@yahoo.com', passwd)
connection.select()
trash, emails = connection.search(None, 'all')
for i in emails[0].split():
    connection.store(i, '+FLAGS', '\\Deleted')
connection.expunge()
