from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField( max_length=100,)
    descripcion = models.CharField( max_length=4000,)
    imagen = models.ImageField(upload_to="media", null = True)
    def save(self):
        super(Servicio,self).save()
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nit = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    id_servicio = models.ForeignKey(
        Servicio,
        on_delete =models.CASCADE
    )
    def save(self):
        super(Cliente,self).save()
    def __str__(self):
        return self.nombre

class Peticion(models.Model):
    nombre = models.CharField( max_length = 100)
    correo = models.CharField( max_length = 100)
    telefono = models.CharField( max_length = 15)
    descripcion = models.CharField( max_length = 400)
    fecha = models.DateField()
    estado_revision = models.IntegerField()
    id_Servicio = models.ForeignKey(
        Servicio,
        on_delete= models.CASCADE,
        null = True
    )
    def save(self):
        super(Peticion,self).save()
    def __str__(self):
        return self.nombre

class contenido_nosotros(models.Model):
    desc_vision = models.CharField(max_length=4000)
    desc_mision = models.CharField(max_length=4000)
    desc_val_ser = models.CharField(max_length=4000)
    desc_derechos = models.CharField(max_length=4000)
    desc_escogenos = models.CharField(max_length=4000)
    desc_te_ayudamos = models.CharField(max_length=4000)
    desc_nuestros_clientes = models.CharField(max_length=4000)
    def save(self):
        super(contenido_nosotros,self).save()

class contenido_servicio(models.Model): 
    ases_impuestos_tributaria = models.CharField(max_length=4000)
    ases_administrativa_financiera =models.CharField(max_length=4000)
    revisoria_fiscal=models.CharField(max_length=4000)
    ases_contable=models.CharField(max_length=4000)
    def save(self):
        super(contenido_servicio,self).save()
    

























