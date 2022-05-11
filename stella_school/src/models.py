from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail


class Contacts(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    query = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True, null=True, blank=True)
    is_send = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self, ):
        return str(self.name)

    class meta:
        db_table = "Contacts"



@receiver(post_save, sender=Contacts)
def send_email_notification(sender, instance, **kwargs):
    created = False
    if 'created' in kwargs:
        if kwargs['created']:
            if not instance.is_send:
                try:
                    subject = '{} is just contacted to the portal.'.format(instance.name)
                    content = '''<p>Greetings...<br>
                    A user named <strong>{}</strong> contact recently from email <strong>{}</strong> and Mobile number 
                    <strong>{}</strong>.
                    <br>
                    The message was : {}.
                    <br><br>
                    This is a auto generated email. Please don't reply to this mail.
                    <br>
                    <i>From Auto Mail Service, STELLA MARIS CONVENT SCHOOL. 
                    </p>
                    '''.format(instance.name, instance.email, instance.mobile, instance.query)

                    resp = send_mail(subject,
                                     content,
                                     settings.EMAIL_HOST_USER,
                                     [settings.ADMIN_RECEIVE_EMAIL],
                                     html_message=content)

                    if resp:
                        instance.is_send = True
                        instance.save()
                    created = True
                except Exception as e:
                    print(e)

    # If signal is from object creation, return
    if created:
        return