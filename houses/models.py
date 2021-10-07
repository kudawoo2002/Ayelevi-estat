from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    create_date = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.location_name


class Contract(models.Model):
    contract_type = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    create_date = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return f'Contract type: {self.contract_type}'


class Seller(models.Model):
    seller_name = models.CharField(max_length=100)
    seller_type = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return f'Seller name: {self.seller_name}'


class House(models.Model):
    house_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    year_built = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    bed = models.IntegerField()
    bath = models.IntegerField()
    room = models.IntegerField()
    garage = models.IntegerField()
    lot_size = models.CharField(max_length=100)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    main_pic = models.ImageField(upload_to="house/pictures")
    pic_2 = models.ImageField(upload_to="house/pictures", blank=True)
    pic_3 = models.ImageField(upload_to="house/pictures", blank=True)
    pic_4 = models.ImageField(upload_to="house/pictures", blank=True)
    pic_5 = models.ImageField(upload_to="house/pictures", blank=True)
    address = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add =True)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"House name: {self.house_name}"
