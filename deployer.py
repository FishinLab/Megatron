import os
import sys
import smtplib

def deploy_report(mail_server = "local mail server", user_from = "mail address", users_to = ["users", "list"], mail_subject = "UI Testing Report-SERVER-IE"):
    mail_content = ""
    server = smtplib.SMTP(mail_server)
    server.login("user name", "user password")
    server.sendmail(user_from, users_to, mail_content)
    server.quit()

if "__main__" == __name__:
    deploy_report()
