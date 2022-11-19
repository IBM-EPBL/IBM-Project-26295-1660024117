import smtplib
import sendgrid as sg
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

SUBJECT = "Expense Tracker"


def sendmail(TEXT, email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('petamailsender@gmail.com', 'petamail@123')
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail('petamailsender@gmail.com', email, message)
    s.quit()


def sendgridmail(user, TEXT):
    sg = sendgrid.SendGridAPIClient('SG.AycyTCTj73r1TxQ.3H0kajWkEYpo0RVfdgsgxSVKbqvtjyZ_nhPbKi3zeZnc')
    from_email = Email('petamailsender@gmail.com')
    to_email = To(user)
    content = Content("text/plain", TEXT)
    mail = Mail(from_email, to_email, SUBJECT, content)

    mail_json = mail.get()
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)