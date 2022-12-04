from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Users_Message/')

    def __str__(self):
        return str(self.name)


class BeforeAfter(models.Model):
    image_before = models.ImageField(
        upload_to='Before_images/')
    image_after = models.ImageField(upload_to='After_images/')


class ClientsAboutUs(models.Model):
    image = models.ImageField(upload_to="Clients_About_Us/")

    class Meta:
        db_table = "Client About Us"


class SmiAboutUs(models.Model):
    image = models.ImageField(upload_to="Smi_about_us/")


class Portfolio(models.Model):
    image = models.ImageField(upload_to="Portfolio/")
