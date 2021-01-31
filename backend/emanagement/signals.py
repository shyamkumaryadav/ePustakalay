import data_list
from django.dispatch import receiver
from django.db.models import signals
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.core.mail import EmailMultiAlternatives
from emanagement.models import Book, Issue

def create_genre(sender, *args, **kwargs):
    is_create = False
    for i in data_list.BOOK_GENRE:
        _, create = sender.models['genre'].objects.get_or_create(name=i[0])
        if create:
            print('Y', end="")
            is_create = True
    if is_create:        
        print(f"\n------------------Done---------------------")

@receiver(signals.pre_save, sender=Book)
def p_update_book_today_stock(sender, instance, **kwargs):
    instance.today_stock = instance.stock - instance.issue_set.all().count()
    instance.in_stock = False if instance.today_stock < 1 else True
    


@receiver(signals.post_save, sender=Issue)
def issue_update_book_today_stock(sender, instance, created, **kwargs):
    instance.book.today_stock = instance.book.stock - instance.book.issue_set.count()
    instance.book.in_stock = False if instance.book.today_stock < 1 else True
    instance.book.save(update_fields=['today_stock', 'in_stock'])


@receiver(signals.post_delete, sender=Issue)
def issue_delete_update_book_today_stock(sender, instance, **kwargs):
    instance.book.today_stock = instance.book.stock - instance.book.issue_set.count()
    instance.book.save(update_fields=['today_stock'])

@receiver(user_logged_in)
def user_logged_in_send_mail(sender, request, user, *args, **kwargs):
    print("*"*18)
    print(user)
    print("*"*18)
    print(request)
    print("*"*18)
    print(sender)
    print("*"*18)

def send_mail(self, subject_template_name, email_template_name,
                context, from_email, to_email, html_email_template_name=None):
    """
    Send a django.core.mail.EmailMultiAlternatives to `to_email`.
    """
    subject = loader.render_to_string(subject_template_name, context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
    body = loader.render_to_string(email_template_name, context)

    email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
    if html_email_template_name is not None:
        html_email = loader.render_to_string(html_email_template_name, context)
        email_message.attach_alternative(html_email, 'text/html')

    email_message.send()