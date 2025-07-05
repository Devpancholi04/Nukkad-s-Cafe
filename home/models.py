from django.db import models

from uuid import uuid4
from base.generate import generate_ids

# Create your models here.
ORDER_STATUS = [
    ('PENDING', 'Pending'),
    ('PREPARING','Preparing'),
    ('READY','Ready'),
    ('SERVED','Served'),
    ('CANCELLED','Cancelled'),
    ('COMPLETED','Completed'),
]

PAYMENT_STATUS = [
    ('PENDING','Pending'),
    ('PAID','Paid'),
    ('FAILED','Failed'),
]

class Table(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gen = generate_ids()

    table_id = models.CharField(max_length=20, editable=False, primary_key=True)
    is_occupied = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='NukkadCafe/qr_codes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.table_id:
            self.table_id = self.gen.gen_table_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Table {self.table_id}"
    

class TableSession(models.Model):
    session_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Session {self.session_id} for Table {self.table.table_id}"
    

class Category(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gen = generate_ids()

    category_id = models.CharField(max_length=20, editable=False, primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.category_id:
            self.category_id = self.gen.gen_category_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category_id} for {self.name}"


class MenuItem(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gen = generate_ids()

    menu_item_id = models.CharField(max_length=20, editable=False, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    images = models.ImageField(upload_to="images/menu/item/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.menu_item_id:
            self.menu_item_id = self.gen.gen_menu_item_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.menu_item_id} for {self.name}"
    

class Testimonials(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="images/home/user/", blank=True, null=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} rated {self.rating} | title: {self.title}"
    