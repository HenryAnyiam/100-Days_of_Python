#!/usr/bin/python3
"""Handle sending notifications"""

from smtplib import SMTP
from typing import List


class NotificationManager:
    """sends mail notificaton"""

    def __init__(self, sender: str, receiver: List[str],
                 password: str,
                 host: str = "smtp.gmail.com") -> None:
        """Initialize NotificationManager"""
        self.sender = sender
        self.receiver = receiver
        self.connection = SMTP(host=host)
        self.connection.starttls()
        self.connection.login(user=self.sender,
                              password=password)

    def send_mail(self, message: str) -> None:
        """send a mail"""
        for i in self.receiver:
            self.connection.sendmail(from_addr=self.sender,
                                    to_addrs=i,
                                    msg=message)
