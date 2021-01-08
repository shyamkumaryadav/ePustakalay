import data_list
from django.dispatch import receiver
from django.db.models import signals
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