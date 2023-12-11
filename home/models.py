from django.db import models

# Create your models here.
class CarDb(models.Model):
    maker = models.CharField(max_length=30, null=True)
    genmodel = models.CharField(max_length=30, null=True)
    genmodel_id = models.CharField(max_length=30, null=True)
    adv_id = models.CharField(max_length=30, null=True)
    adv_year = models.CharField(max_length=30, null=True)
    adv_month = models.CharField(max_length=30, null=True)
    colour = models.CharField(max_length=30, null=True)
    reg_year = models.CharField(max_length=30, null=True)
    bodytype = models.CharField(max_length=30, null=True)
    mileage = models.CharField(max_length=30, null=True)
    engine_size = models.CharField(max_length=30, null=True)
    gearbox = models.CharField(max_length=30, null=True)
    fuel_type = models.CharField(max_length=30, null=True)
    price = models.CharField(max_length=30, null=True)
    seat_num = models.CharField(max_length=30, null=True)
    door_num = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = "ad_table"