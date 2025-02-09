from django.db import models

# Create your models here.
class regester(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True,unique=True)
    phone_number=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=10)
    age=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='reg/', null=True,blank=True)
    

class organizer(models.Model):
        name=models.CharField(max_length=50,null=True,blank=True)
        email=models.EmailField(max_length=50,unique=True)
        phone_number=models.IntegerField(null=True,blank=True)
        password=models.CharField(max_length=100,null=True,blank=True)
        gender=models.CharField(max_length=10,null=True,blank=True)
        age=models.IntegerField(null=True,blank=True)
        address=models.CharField(max_length=100,null=True,blank=True)
        image=models.ImageField(upload_to='oreg/', null=True,blank=True)


class event(models.Model):
      eventid=models.IntegerField(null=True,blank=True)
      eventname=models.CharField(max_length=50,null=True,blank=True)
      description=models.CharField(max_length=500,null=True,blank=True)
      amount=models.IntegerField(null=True,blank=True)
      sampleimage=models.ImageField(upload_to='img/',null=True,blank=True)
      organizerid=models.IntegerField(null=True,blank=True)


class booking(models.Model):
      eventid=models.IntegerField(null=True,blank=True)
      customernumber=models.IntegerField(null=True,blank=True)
      date=models.IntegerField(null=True,blank=True)
      place=models.CharField(max_length=50,null=True,blank=True)
      description=models.CharField(max_length=500,null=True,blank=True)
      payment=models.IntegerField(null=True,blank=True)
      address=models.CharField(max_length=50,null=True,blank=True)



class fb(models.Model):
    name=models.CharField(null=True,blank=True,max_length=10)
    feedback=models.CharField(null=True,blank=True,max_length=1000)
    rating_choices=(
        ('1STAR','1star'),
        ('2STAR','2star'),      
        ('3STAR','3star'),
        ('4STAR','4star'),
        ('5STAR','5star'),
        
    )
    rating=models.CharField(choices=rating_choices,max_length=10)




class eventsupdates(models.Model):
    user=models.ForeignKey(organizer,null=True, blank=True,on_delete=models.CASCADE)
    category=models.CharField(max_length=60,null=True, blank=True)
    eventname=models.CharField(max_length=60,null=True, blank=True)
    image=models.ImageField(upload_to='eventsimg/', null=True,blank=True)
    details=models.CharField(max_length=300,null=True,blank=True)
    eventdate=models.DateField(null=True,blank=True)
    amount=models.DecimalField(null=True, blank=True,decimal_places=2, max_digits=6)
    registerenddate=models.DateField(null=True, blank=True)
    resultdate=models.DateField(null=True,blank=True)
    status_choices=(
        ('approved','APPROVED'),
        ('pending','PENDING'),
        ('rejected','REJECTED')
    )
    status=models.CharField(max_length=12,choices=status_choices,default='pending')
    staff_user=models.ForeignKey(regester,null=True, blank=True,on_delete=models.SET_NULL)
    msg=models.CharField(max_length=45,default='None')
    stock = models.IntegerField(default=100)
    def __str__(self):
        return f"{self.eventname} - {self.category}"
    

    # gallery/models.py

from django.db import models
from django.utils.translation import gettext_lazy as _

class Image(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='gallery_images/')
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title if self.title else "Untitled Image"

    def save(self, *args, **kwargs):
        from PIL import Image as PILImage
        from io import BytesIO
        from django.core.files.uploadedfile import InMemoryUploadedFile

        img = PILImage.open(self.image)

        # Resize image to a fixed size (600x400)
        img = img.resize((600, 400))
        img_io = BytesIO()
        img.save(img_io, 'JPEG', quality=85)
        img_io.seek(0)

        self.image = InMemoryUploadedFile(
            img_io, None, self.image.name, 'image/jpeg', img_io.getbuffer().nbytes, None
        )
        
        super().save(*args, **kwargs)





class cart(models.Model):
    user=models.ForeignKey(regester,on_delete=models.CASCADE)
    products=models.ForeignKey(eventsupdates,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    total_price=models.IntegerField()
    

# Create your models here.

class Transaction(models.Model):
    user=models.ForeignKey(regester,on_delete=models.CASCADE)
    products = models.ForeignKey(eventsupdates,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)
    order_id= models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)