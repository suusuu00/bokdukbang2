from django.db import models
from accounts.models import User

# Create your models here.
class Rooms(models.Model):
    rooms_id = models.AutoField(primary_key=True)
    ruser = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    area = models.IntegerField()
    deposit = models.IntegerField(blank=True, null=True)
    monthly_rent = models.IntegerField(blank=True, null=True)
    maintenance_cost = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=20)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    structure = models.CharField(max_length=3)
    women_only = models.IntegerField()
    location = models.CharField(max_length=5, blank=True, null=True)
    sold = models.IntegerField()
    category = models.CharField(max_length=5)
    title = models.CharField(max_length=30)
    comment = models.TextField()
    interest = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'rooms'