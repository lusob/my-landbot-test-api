import json
import time
from urllib.request import urlopen
from threading import Thread
from flask_mail import Message


def _send_deferred_email(app, mail, user_name, user_email, seconds=60):
    with app.app_context():
        time.sleep(seconds)  # Wait seconds and send email then
        msg = Message(
            sender="sender@example.com",
            recipients=[user_email],
            subject=f"Welcome {user_name}",
            body=f"Welcome {user_name}, this email has been sent by the API called by the lanbotio bot",
        )
        mail.send(msg)



def send_deferred_email(app, mail, user_name, user_email):
    # Using multithreading to send the email deferred in a simple way, for a more
    # scalable approach is better to user a middleware or a tasks queue as celery
    thread = Thread(
        target=_send_deferred_email,
        kwargs={"app": app, "mail": mail, "user_name": user_name, "user_email": user_email},
    )
    thread.start()
