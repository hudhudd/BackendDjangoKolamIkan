from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Datakol(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ph = models.DecimalField(max_digits=4,decimal_places=2)
    temp = models.DecimalField(max_digits=4, decimal_places=2)
    alat = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #   get_latest_by = 'upload_date'
    def __str__(self):
        return str(self.owner)