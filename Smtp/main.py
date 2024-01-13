#!/usr/bin/python3

import smtplib

connection = smtplib.SMTP(host="smtp.gmail.com")

# Then we use the starttls method to secure our connection
connection.starttls()

# Afterwards, create an app password
# For gmail, go to mannage google accounts, Then security
# Turnon 2-step verification
#Then generat an app password 
connection.login(user="taskhub2023@gmail.com",
                 password="xmyp fkpl evos iltv")

connection.sendmail(from_addr="taskhub2023@gmail.com",
                    to_addrs="angelayu987@yahoo.com",
                    msg="Subject: This is the Subject\n\nHere is the body of the email")

# Close the connection once youre done sending
connection.close()

# You can also use the with context manager to handle a connection

with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="taskhub2023@gmail.com",
                     password="xmyp fkpl evos iltv")
    connection.sendmail(from_addr="taskhub2023@gmail.com",
                        to_addrs="angelayu987@yahoo.com",
                        msg="Subject: This is the Subject\n\nHere is the body of the email")
