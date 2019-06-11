from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]


class Company(models.Model):
    help = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name="companies", on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.owner, self.help)


class InCompanies(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Company, through='Membership')

    def __str__(self):
        return "{},  {}".format(self.name, self.members)


class Membership(models.Model):
    incompanies = models.ForeignKey(InCompanies, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{} === {}".format(self.incompanies, self.company)


