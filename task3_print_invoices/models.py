from django.db import models


class Order(models.Model):
    person_name = models.CharField(max_length=44, null=False, blank=False)
    product = models.CharField(max_length=130)  # default - cannot be blank
    company = models.CharField(max_length=44)
    ship_date = models.DateTimeField()
    ordered_warranty = models.BooleanField(default=False)
