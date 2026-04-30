from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import datetime
# Create your models here.
class ShippingAddress(models.Model):
    shipping_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True) #One user can have multiple addresses, But each address belongs to only one user.
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_address1 = models.CharField(max_length=255)
    shipping_address2 = models.CharField(max_length=255,blank=True,null=True)
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255,blank=True, null=True)
    shipping_pincode = models.CharField(max_length=255,blank=True,null=True)
    shipping_country = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Shipping Address"
    def __str__(self):
        return f'Shipping Adress - {str(self.id)}'
# Create a user shipping address by default when user signs up
def create_shipping(sender,instance,created,**kwargs):
    if created:
        user_shipping = ShippingAddress(shipping_user=instance)
        user_shipping.save()
# Automate this 
post_save.connect(create_shipping,sender=User)
    
    
# Create Order Model
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    shipping_address = models.TextField(max_length=10000)
    amount_paid = models.DecimalField(max_digits=7,decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    date_shipped = models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return f'Order - {str(self.id)}'
    
# Auto add shipping date
@receiver(pre_save, sender=Order)
def set_shipped_date_on_update(sender, instance, **kwargs):
    if instance.pk:
        now = datetime.datetime.now()
        obj = sender.objects.get(pk=instance.pk)
        if instance.shipped and not obj.shipped:
            instance.date_shipped = now
    # here instance is current object so when we hit shipped button and save @receiver called and it holds db pre save data and instance current 
    # data so if condition got true and obj old data also got true in if statement.
    

# Create order items model
class OrderItem(models.Model):
    # Foreign Keys
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return f'Order item - {str(self.id)}' 