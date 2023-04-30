from django.db import models

class Carta(models.Model):
    front = models.ImageField(upload_to= 'imagem', blank=False)
    elemento = models.CharField(max_length= 100,  blank=False, default='')
    ataque = models.PositiveIntegerField(blank=False, default=0)
    defesa = models.PositiveIntegerField(blank=False, default=0)
