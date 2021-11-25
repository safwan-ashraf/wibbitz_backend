import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse

from web.models import Subscribe, Customer, Feature, VideoBlog, Testimonial,\
     MarketingFeature, Product, Blog
from web.forms import ContactForm

# Create your views here.
def index(request):
    customers = Customer.objects.all()
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
        "form": form
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


def contact(Request):
    email = request.POST.get("email")
    # the value we are passing inside get is the the value inside the name of input tags in our html
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    company = request.POST.get("company")
    company_size = request.POST.get("company_size")
    industry = request.POST.get("industry")
    job_role = request.POST.get("job_role")
    country = request.POST.get("country")
    user_agreement = request.POST.get("user_agreement")


    if not Contact.objects.filter(email=email).exists():
        Contact.objects.create(
            email = email,
            # left side value depends on the value in the models.py for this model(here, Contact)
            # right side value depwnds on value in the current function, i.e def contact(Request)
            first_name = first_name,
            last_name = last_name,
            company = company,
            company_size = company_size,
            industry = industry,
            job_role = job_role,
            country = country,
            user_agreement = user_agreement
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



    
