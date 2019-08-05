from django.core.mail import send_mail, EmailMessage

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
#from sparkpost import SparkPost
#from django.conf import settings
#sp = SparkPost(settings.SPARKPOST_API_KEY)  # this will use the api key specified in settings.py

message = EmailMessage(
    to = ["Arnav <arnav@meshedu.org>"]
)


message.esp_extra = {
    'transactional': True,  # treat as transactional for unsubscribe and suppression
    'description': "Marketing test-run for new templates",
    'template': 'my-first-email',
    'use_sandbox': True

}




if __name__ == "__main__":

    message.send()

