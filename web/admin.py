from django.contrib import admin
from web.models import Subscribe, Customer, Feature, VideoBlog, Testimonial, MarketingFeature, Product, Blog, Contact

# Register your models here.
admin.site.register(Subscribe)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","name","image"]

admin.site.register(Customer,CustomerAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id","title","description","testimonial_description","testimonial_author","author_designation"]

admin.site.register(Feature,FeatureAdmin)


class VideoBlogAdmin(admin.ModelAdmin):
    list_display = ["id","image","title","logo"]

admin.site.register(VideoBlog,VideoBlogAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id","description","name","designation","company_name","is_featured"]

admin.site.register(Testimonial,TestimonialAdmin)


class MarketingFeatureAdmin(admin.ModelAdmin):
    list_display = ["id","description","title","image"]

admin.site.register(MarketingFeature,MarketingFeatureAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","description","title","image"]

admin.site.register(Product,ProductAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id","title","image","content_type"]

admin.site.register(Blog,BlogAdmin)


admin.site.register(Contact)





