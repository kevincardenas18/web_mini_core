from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["name"]

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    product = models.CharField(max_length=200, verbose_name="Producto")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    creation_date = models.DateField(auto_now_add=False, verbose_name="Fecha de creación")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ["-creation_date"]