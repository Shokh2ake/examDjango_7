from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, CharField

# from apps.tasks import task_send_email


class User(AbstractUser):
    image = ImageField(upload_to='users/images/', default='users/default.jpg')
    job = CharField(max_length=255)
    address = CharField(max_length=255)

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     # if self.date_joined is None:
    #     all_emails: list = User.objects.values_list('email', flat=True)
    #     task_send_email().delay('NETFLIX', 'Welcome to our website!', list(all_emails))
    #     super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.username

    def full_name(self):
        return self.first_name + ' ' + self.last_name
