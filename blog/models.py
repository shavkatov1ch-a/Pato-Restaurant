from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='home')

    def __str__(self):
        return self.title


class Pato(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='pato')

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title

