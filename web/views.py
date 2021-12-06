import json

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponse

from web.models import Subscribe, Customer, Feature, VideoBlog, Testimonial,\
     MarketingFeature, Product, Blog
from web.forms import ContactForm

# Create your views here.
def index(request):
    customers = Customer.objects.all()
    latest_customers = Customer.objects.all()[:4]
    features = Feature.objects.all()
    video_blogs = VideoBlog.objects.all()[:3]
    testimonials = Testimonial.objects.filter(is_featured=True)[:2]
    marketings = MarketingFeature.objects.all()
    products = Product.objects.all()
    blog_post_blogs = Blog.objects.filter(content_type="blog_post")
    webinar_blogs = Blog.objects.filter(content_type="webinar")
    report_blogs = Blog.objects.filter(content_type="report")

    form = ContactForm()

    context = {
        "customers" : customers,
        "features" : features,
        "video_blogs" : video_blogs,
        "testimonials" : testimonials,
        "marketings" : marketings,
        "products" : products,
        "blog_post_blogs" : blog_post_blogs,
        "webinar_blogs" : webinar_blogs,
        "report_blogs" : report_blogs,
        "form": form,
        "latest_customers" : latest_customers,
    }
    return render(request,"index.html",context=context)



def subscribe(request):
    email = request.POST.get("email")

    if not Subscribe.objects.filter(email=email).exists():
        Subscribe.objects.create(
            email = email
        )

        response_data = {
            "status" : "success",
            "title" : "Successfully registered",
            "message" : "You subscribed to our newsletter successfully."
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "Already subscribed"
        }
    
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()

        response_data = {
            "status" : "success",
            "title" : "Successfully registered",
            "message" : "You subscribed to our newsletter successfully."
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "Already subscribed"
        }
    
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")



def product(request,pk):
    product = get_object_or_404(Product.objects.filter(pk=pk))
    customers = Customer.objects.filter(product=product)
    context = {
        "product" : product,
        "customers" : customers
    }
    return render(request,"product.html",context=context)



    
