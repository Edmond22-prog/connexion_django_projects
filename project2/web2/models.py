from django.db import models


TONTINES_LIST = [
    ("52 USDT", "Tontine 52 USDT"),
    ("302 USDT", "Tontine 302 USDT"),
    ("502 USDT", "Tontine 502 USDT"),
    ("1002 USDT", "Tontine 1002 USDT"),
    ("2002 USDT", "Tontine 2002 USDT")
]

class Registration(models.Model):
    tontine = models.CharField(max_length=255, choices=TONTINES_LIST, null=False)
    email = models.EmailField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)


    def __str__(self):
        return self.email
