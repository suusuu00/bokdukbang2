from django.db import models
from accounts.models import User
from rooms_posts.models import Rooms

# Create your models here.
class MyInterest(models.Model):
    interest_id = models.AutoField(primary_key=True)
    muser = models.ForeignKey(User, on_delete=models.CASCADE)
    studio = models.ForeignKey(Rooms, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'my_interest'