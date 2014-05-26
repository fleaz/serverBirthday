#! /usr/bin/env python3

import subprocess
import re
import smtplib
from email.mime.text import MIMEText


def send_mail(email, years):
    msg = MIMEText("Your Server is %d years old" % years)
    msg['Subject'] = "It's your servers birthday today"
    msg['From'] = "ServerBirthday"
    msg['To'] = email

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

def main():
    args = ("uptime")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    output = output.decode("utf-8").strip()
    pattern = re.compile("\d{2}:\d{2}:\d{2}\sup\s(\d+)\sdays.*")
    match = pattern.match(output)
    days = int(match.group(1))

    if (days % 365 == 0):
        years = int(days / 365)
        send_mail("youare@awesome.com", years)

if __name__ == "__main__":
    main()
