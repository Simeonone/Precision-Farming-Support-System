from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# customer
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    #digital is a boolean value because we want to know if the item is digital, we don't need to ship it
    #if it's false means it's a physical product, meaning we have to ship it
    image = models.ImageField(null=True, blank=True, upload_to='storeimages')

    def __str__(self):
        return self.name
#code below - if you upload an item without an image, you'll get an error.
#the code below solves this issue
    @property
#above- its a property decorator that lets us access as an attribute rather than a method
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank= True)
    #above - customer can have many orders
    #set null- if a customer is deleted, we dont want to delete the order, we just want to set the customer value
    #to null
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    #above - if complete is false, that is an open cart and we can continue adding items to that cart
    #if its true, its a closed cart, we need to create items and add them to a different order
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    #returns the grand total for purchase

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    #returns the number of items in a cart

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    #order is our cart and orderitem is an item within our cart, cart can have multiple order items,
    #hence need for the multiple relationships
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    #returns the total for each item, ie. item * quantity
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True)
    #Reason for above - if an order gets deleted, I'd still want to have the shipping address for a customer
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
