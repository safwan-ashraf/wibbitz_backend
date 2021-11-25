from django.db import models


CHOICE = (
    ("blog_post","Blog Post"),
    ("webinar","Webinar"),
    ("report","Report"),
)

COMPANY_SIZE = (
    ("1","1-10"),
    ("2","11-50"),
    ("3","51-200"),
    ("4","201-500"),
)

INDUSTRY = (
    ("1","Agriculture"),
    ("2","Banking & Finance"),
    ("3","Business Services & Software"),
)

JOB_ROLE = (
    ("1","C-Suite"),
    ("2","Banking & Finance"),
)

COUNTRY = (
    ("us","United States"),
    ("albania","Albania"),
)
# Create your models here.
class Subscribe(models.Model):
    email = models.EmailField()

    class Meta:
        db_table="web_subscribe"
        ordering=["-id"]

    def __str__(self):
        return self.email


class Customer(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to="customers/")

    class Meta:
        db_table="web_customer"
        ordering=["id"]

    def __str__(self):
        return self.name 


class Feature(models.Model):
    image = models.ImageField(upload_to="features/images/")
    icon = models.FileField(upload_to="features/icons/")
    icon_background = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    description = models.TextField()
    testimonial_description = models.TextField() 
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="features/logos/")

    class Meta:
        db_table="web_feature"
        ordering=["id"]

    def __str__(self):
        return self.title 


class VideoBlog(models.Model):
    image = models.ImageField(upload_to="video_blogs/")
    title = models.CharField(max_length=255)
    logo = models.FileField(upload_to="video_blogs/")

    class Meta:
        db_table="web_video_blog"
        ordering=["id"]

    def __str__(self):
        return self.title



class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonials/")
    logo = models.FileField(upload_to="testimonials/",blank=True,null=True) 
    description = models.TextField()
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=128)
    is_featured = models.BooleanField(default=False)

    class Meta:
        db_table="web_testimonial"
        ordering=["id"]
    
    def __str__(self):
        return self.name


class MarketingFeature(models.Model):
    image = models.FileField(upload_to="marketings/")
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table="web_marketing"
        ordering=["id"]
    
    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.FileField(upload_to="products/images/") 
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.FileField(upload_to="products/logos/")

    class Meta:
        db_table="web_products"
        ordering=["id"]

    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.FileField(upload_to="blogs/") 
    title = models.CharField(max_length=128)
    content_type = models.TextField(choices=CHOICE)

    class Meta:
        db_table="web_blogs"
        ordering=["id"]

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128) 
    company = models.CharField(max_length=128) 
    company_size =  models.CharField(max_length=128,choices=COMPANY_SIZE)
    industry =  models.CharField(max_length=128,choices=INDUSTRY)
    job_role =  models.CharField(max_length=128,choices=JOB_ROLE)
    country =  models.CharField(max_length=128,choices=COUNTRY)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table="web_contact"
        ordering=["id"]

    def __str__(self):
        return self.first_name









