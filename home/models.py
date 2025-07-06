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

PAYMENT_METHOD_CHOICES = [
    ('COD','COD'),
    ('UPI','UPI'),
    ('CARD','CARD'),
    ('NETBANKING', 'NETBANKING')
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
    session_id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
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
    

class Cart(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gen = generate_ids()

    cart_id = models.CharField(max_length=20, editable=False, primary_key=True)
    session = models.OneToOneField(TableSession, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.cart_id:
            self.cart_id = self.gen.gen_cart_id()
        super().save(*args, **kwargs)

    def total_amount(self):
        return sum(item.total_price() for item in self.items.all())
    
    def __str__(self):
        return f"Cart for Session {self.session.session_id}"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'item')

    def total_price(self):
        return self.item.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} X {self.item.name} in Cart {self.cart.cart_id}"
    

class Order(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gen = generate_ids()

    order_id = models.CharField(max_length=20, editable=False, primary_key=True)
    session = models.ForeignKey(TableSession, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='PENDING')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='UPI')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    special_request = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self.gen.gen_order_id()
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.order_id} - {self.status} associated with {self.cart.cart_id}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE, related_name="items")
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} X {self.item.name}"