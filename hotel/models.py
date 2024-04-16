from django.db import models
from userauths.models import User
from shortuuid.django_fields import ShortUUIDField
import shortuuid
from django.utils.text import slugify
from django.utils.html import mark_safe

# Create your models here.
HOTEL_STATUS = {
    ('Draft','Draft'),
    ('Disable','Disable'),
    ('Rejected','Rejected'),
    ('In review','In review'),
    ('Live','Live')
}

ICON_TYPE = {
    ('Bootstrap icons','Bootstrap icons'),
    ('Fontawesome icons','Fontawesome icons'),
    ('Box icons','Box icons'),
    ('Remi icons','Remi icons'),
    ('Flat icons','Flat icons')
}
PAYMENT_STATUS = {
    ('paid','Paid'),
    ('pending','Pending'),
    ('processing','Processing'),
    ('cancelled','Cancelled'),
    ('initiated','Initiated'),
    ('failed','Failed'),
    ('refunding','Refunding'),
    ('refunded','refunded'),
    ('unpaid' , 'Unpaid'),
    ('expired','Expired')
}

class Hotel(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='hotel-images')
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    status = models.CharField(max_length=20, choices=HOTEL_STATUS , default="Live")

    tags = models.CharField(max_length=200,help_text="Separate tags with comma")
    views = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    hid = ShortUUIDField(unique=True,length=10, max_length=15, prefix="HTL", alphabet="0123456789")
    slug =models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


    def save(self, *args , **kwargs):
        if self.slug == "" or self.slug == None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.name) + '-' +str(uniqueid.lower())
        super(Hotel, self).save(*args,**kwargs)

    def thumbnail(self):
        return mark_safe("<img src='%s' width='50' height='50' style:'cover-fit:cover; border-raduis:6px' />" % (self.image.url))
    



class HotelGallery(models.Model):
    hotel =models.ForeignKey(Hotel,on_delete=models.CASCADE)
    image =models.FileField(upload_to="gallery-hotel")
    hgid = ShortUUIDField(unique=True,length=10, max_length=15, prefix="HGL", alphabet="0123456789")
    
    def __str__(self):
        return str(self.hotel.name)
    
    class Meta:
        verbose_name_plural = 'Hotel Gallery'


class HotelFeatures(models.Model):
    hotel =models.ForeignKey(Hotel,on_delete=models.CASCADE)
    icontype = models.CharField(max_length=100, blank=True, null=True,choices=ICON_TYPE)
    icon = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = 'Hotel Features'


class HotelFaq(models.Model):
    hotel =models.ForeignKey(Hotel,on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000 , blank=True, null=True)
    date =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.question)
    class Meta:
        verbose_name_plural = 'Hotel FAQs'



class RoomType(models.Model):
    hotel =models.ForeignKey(Hotel,on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    number_beds = models.PositiveIntegerField(default=0)
    room_capacity = models.PositiveIntegerField(default=0)
    rtid = ShortUUIDField(unique=True,length=10, max_length=15, prefix="RT", alphabet="0123456789")
    slug =models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.type}-{self.hotel.name}-{self.price}'
    
    class Meta:
        verbose_name_plural = 'Rooms Types'

    def rooms_count(self):
        Room.objects.filter(room_type=self).count()

    
    def save(self, *args , **kwargs):
        if self.slug == "" or self.slug == None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.name) + '-' +str(uniqueid.lower())
        super(RoomType, self).save(*args,**kwargs)


class Room(models.Model):
    hotel =models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType,on_delete=models.CASCADE)
    room_number = models.CharField(max_length=1000)
    is_available = models.BooleanField(default=True)
    rid = ShortUUIDField(unique=True, max_length=8, prefix="ROOM", alphabet="0123456789")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.room_type.type}-{self.hotel.name}-{self.price}'

    class Meta:
        verbose_name_plural = 'Rooms'
    
    def price(self):
        return f'{self.room_type.price}'
    
    def number_beds(self):
        return self.room_type.number_beds
    
class Booking(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , blank=True, null=True)
    status_payment =models.CharField(max_length=100 , choices=PAYMENT_STATUS)

    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)

    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType,on_delete=models.CASCADE)
    room = models.ManyToManyField(Room)
    before_discount = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(decimal_places=2 , max_digits=12)
    saved = models.DecimalField(decimal_places=2 , max_digits=12)


    check_in_date = models.DateField()
    check_out_date =models.DateField()

    total_days = models.PositiveIntegerField(default=0)
    num_adults = models.PositiveIntegerField(default=1)
    num_chlidren =models.PositiveIntegerField(default=1)

    checked_in =models.BooleanField(default=False)
    checked_out =models.BooleanField(default=False)

    is_active =models.BooleanField(default=False)

    checked_in_tracker =models.BooleanField(default=False)
    checked_out_tracker  =models.BooleanField(default=False)

    date =models.DateTimeField(auto_now_add=True)
    stripe_payment_intent = models.CharField(max_length=1000,blank=True, null=True)
    success_id = models.CharField(max_length=1000,blank=True, null=True)
    booking_id = ShortUUIDField(unique=True, max_length=8, prefix="BOOK", alphabet="0123456789")

    def __str__(self):
        return f'{self.booking_id}'
    
    def rooms(self):
        return self.room.all().count()
    


class ActivityLog(models.Model):
    booking = models.ForeignKey(Booking , on_delete=models.CASCADE)
    guess_out =models.DateTimeField()
    guess_in = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.booking}'
    
class StaffOnDuty(models.Model):
    booking = models.ForeignKey(Booking , on_delete=models.CASCADE)
    staff_id =models.CharField(max_length=50,blank=True, null=True)
    date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff_id}"
    
