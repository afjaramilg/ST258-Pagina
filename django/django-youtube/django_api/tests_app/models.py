from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.db.models.fields import BooleanField, CharField, DateTimeField, FloatField, PositiveIntegerField, TextField

# Create your models here.


class test_model(models.Model):

    name = CharField(max_length=255, unique=True, null=True)
    description = TextField()
    phone_number = PositiveIntegerField()
    is_alive = BooleanField()
    amount = FloatField()
    extra_name = CharField(max_length=250, editable=False, default="null")
    created_at = DateTimeField( default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())

    def __str__(self):
        return self.extra_name

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = "Test model"

    def save(self, *args, **kargs):
        self.extra_name = f"{self.name} - {self.phone_number}"
        super().save(*args, **kargs)


class ModelX(models.Model):
    test_content = ForeignKey(test_model, on_delete=CASCADE, null=True, related_name="content")
    mail = FloatField()
    created_at = DateTimeField( default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.test_content.name} - {self.mail}"
