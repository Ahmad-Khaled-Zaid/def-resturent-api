from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model


# Create your models here.

class Reservation(models.Model):
    table_number = models.IntegerField()
    reservation_by = models.CharField(max_length=256)
    reservation_for = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    people_number = models.IntegerField()
    additional_info = models.TextField(blank=True, max_length=256)
    reservation_date = models.DateTimeField('Reservation in : ')

    def __str__(self):
        return self.reservation_by
