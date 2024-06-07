from django.db import models


# Create your models here.
class BrazoRobotico(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fechaAgregado = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'brazo robotico'
        verbose_name_plural = 'brazos roboticos'

    def __str__(self):
        return f'{self.nombre} - {self.modelo}'
