from django.db import models

# Create your models here.
class CarDb(models.Model):
    maker = models.CharField(max_length=30, null=True)
    genmodel = models.CharField(max_length=30, null=True)
    adv_year = models.IntegerField(null=True)
    adv_month = models.IntegerField(null=True)
    colour = models.CharField(max_length=30, null=True)
    reg_year = models.IntegerField(null=True)
    bodytype = models.CharField(max_length=30, null=True)
    mileage = models.IntegerField(null=True)
    engine_size = models.FloatField(null=True)
    gearbox = models.CharField(max_length=30, null=True)
    fuel_type = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)
    seat_num = models.IntegerField(null=True)
    door_num = models.IntegerField(null=True)

    class Meta:
        db_table = "ad_table"