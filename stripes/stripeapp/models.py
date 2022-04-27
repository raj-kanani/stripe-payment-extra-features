from django.db import models


class Product(models.Model):

    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.name), filename])

    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
    file = models.FileField(upload_to=nameFile, blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
