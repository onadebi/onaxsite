from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import models;
from rest_framework import serializers;


class ContactOptions(models.Model):
    """ContactOptions model for the Contact app"""
    id = models.AutoField(primary_key=True)
    option_name = models.CharField(max_length=100, null=False)
    option_value = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'ContactOptions';

    def __str__(self) -> str:
        return f"[{self.id}]-{self.option_name} - {self.option_value}";

    def get_option(self, option_name: str) -> str:
        return self.option_value if self.option_name == option_name else None


@receiver(post_migrate)
def populate_contact_options(sender, **kwargs):
    if sender.name == 'onaxmain':
        if not ContactOptions.objects.exists():
            ContactOptions.objects.create(option_name='Enquiry', option_value='enquiry')
            ContactOptions.objects.create(option_name='Let\'s collaborate', option_value='lets-collaborate')
            ContactOptions.objects.create(option_name='Contract for us', option_value='contract-for-us')

class ContactMessages(models.Model):
    """ContactMessages model for the Contact Us module"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=True)
    contact_option = models.ForeignKey(ContactOptions, on_delete=models.RESTRICT, null=False)
    message = models.TextField(max_length=500,null=False)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);

    class Meta:
        db_table = 'ContactMessage';

    def __str__(self) -> str:
        return f"[{self.id}]-{self.name} - {self.email} - {self.phone} - {self.is_read} - {self.created_at}";

    def mark_read(self):
        self.is_read = True
        self.save()
        return self.is_read

    def mark_unread(self):
        self.is_read = False
        self.save()
        return self.is_read
        

class ContactOptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactOptions
        fields = ['id', 'option_name']