from django.db import models

# Create your models here.
class Client(models.Model):
    nom=models.CharField(max_length=200,null=True)
    email = models.EmailField(default="nom.prenom@gmail.com ")
    telephone=models.CharField(max_length=200,null=True)
    adresse = models.TextField(default="Adresse par défaut")  # Spécifiez une valeur par défaut
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self) :
        return self.nom
    
