from django.db import models

class LoanBook(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9,decimal_places=2)
    item = models.CharField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name