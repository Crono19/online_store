from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)

    def delete(self):
        self.deleted = True
        self.save()

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)

    def delete(self):
        self.deleted = True
        self.save()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    deleted = models.BooleanField(default=False)

    def delete(self):
        self.deleted = True
        self.save()

    def __str__(self):
        return self.name
    
STATUS_TYPE = [
("Pendiente de envío", "Pendiente de envío"),
("Enviado", "Enviado"),
("Entregado", "Entregado")
]

class Order(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_TYPE, default="Pendiente de envío")
    address = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)

    def delete(self):
        self.deleted = True
        self.save()

    def __str__(self):
        return self.customer