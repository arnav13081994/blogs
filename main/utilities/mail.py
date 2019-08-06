from django.core.mail import EmailMessage
from django.template.loader import render_to_string



to_list = ["arnav13@gmail.com"]
subject = "Thanks for signing up!"
template_name = 'email/email.html'
context = {
    'username': "fry",
    'password': "password_yo",
    'full_name': "Philip J Fry"
}



msg_html = render_to_string(template_name, context)

msg = EmailMessage(subject=subject, body= msg_html, to=to_list)

msg.content_subtype = "html"  # Main content is now text/html

msg.send()
