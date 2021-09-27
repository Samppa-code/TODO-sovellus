from  django.db import  models


class Tehtava(models.Model):
    tehtava = models.CharField(max_length=200)
    

    def __str__(self):
        return f"Tehtava: {self.tehtava}"
