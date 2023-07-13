from django.db import models

class MyModel(models.Model):
    TUR_CHOICES = (
        ('uy', 'Uy'),
        ('dom', 'Dom'),
        ('kvartira', 'Kvartira'),
        ('bezniz', 'Bezniz uchun'),
    )

    tur = models.CharField(max_length=20, choices=TUR_CHOICES)
    joy = models.CharField(max_length=100)
    kv_soni = models.IntegerField()
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    describe = models.TextField()
    rasm1 = models.ImageField(upload_to='rasm')
    rasm2 = models.ImageField(upload_to='rasm')
    rasm3 = models.ImageField(upload_to='rasm')
    rasm4 = models.ImageField(upload_to='rasm')
    rasm5 = models.ImageField(upload_to='rasm')
    rasm6 = models.ImageField(upload_to='rasm')

    def __str__(self):
        return self.joy
