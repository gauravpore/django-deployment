from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio, Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # skills
    categories = Category.objects.all()

    #portfolio
    portfolios = Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }
    if request.method=='POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return render(request, 'contact.html', context)

    return render(request,'index.html',context)