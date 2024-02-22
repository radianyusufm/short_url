from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from user_agents import parse
from django.db.models import Count


from .models import User, Urlshort, Analytics
from .util import generate_slug


@login_required(login_url="/login")
def index(request):
    links = Urlshort.objects.filter(user=request.user).order_by('-waktu')

    context = { "all_links": links}
    return render(request, "capstone/index.html", context)



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "capstone/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "capstone/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "capstone/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "capstone/register.html")



@login_required(login_url="/login")
def create_short_url(request):
    if request.method == "POST":
    
        url_asli = request.POST.get("url_asli")
        password = request.POST.get("password")
        url_singkat = generate_slug()
    
        while True:
            check_url = Urlshort.objects.filter(url_singkat=url_singkat).exists()
            if check_url: 
                url_singkat = generate_slug()
            else:
                break
            
        result = f'http://127.0.0.1:8000/s/{url_singkat}'
        print(result)

        url_short = Urlshort(
            user = request.user,
            url_asli = url_asli,
            url_singkat = url_singkat,
            password = password,
            waktu = datetime.now(),
            jumlah_klik = 0
        )
        url_short.save()

        return HttpResponseRedirect(reverse("index"))
    
    else:
        return render(request, 'capstone/create_url.html')




def get_url_short(request, url):
    get_url_asli = Urlshort.objects.filter(url_singkat=url).values('id' ,'url_asli', 'password', 'url_singkat', 'jumlah_klik')
    
    if get_url_asli.exists():

        url_asli = None
        password = None
        
        for url in get_url_asli:
            url_id = url['id']
            url_asli = url['url_asli']
            url_singkat = url['url_singkat']
            password = url['password']
            
        data = Urlshort.objects.get(url_singkat=url_singkat)
        data.jumlah_klik = url["jumlah_klik"] + 1
        data.save()

        ua_string = request.META.get("HTTP_USER_AGENT")
        user_agent = parse(ua_string)

        if user_agent.is_mobile:
            device_user = 'Mobile'
        elif user_agent.is_tablet:
            device_user = 'Tablet'
        elif user_agent.is_pc:
            device_user = 'Pc'
        else:
            device_user = 'Other'

        urlshort = Urlshort.objects.get(id=url_id)
        analytics = Analytics(
            urlshort = urlshort,
            os_link = user_agent.os.family,
            browser_link = user_agent.browser.family,
            device_link = device_user
        )
        analytics.save()

        if len(str(password)) > 0:
            return render(request, 'capstone/password.html', {'slug': url_singkat})
        else:
            return redirect(url_asli)
    
    else:
        return render(request, 'capstone/404.html')




def password(request):
    if request.method == "POST":
        password = request.POST["password"]
        slug = request.POST["slug"]
        
        print(password)
        password_db = Urlshort.objects.filter(url_singkat=slug).values('url_asli','url_singkat', 'password', 'jumlah_klik')

        for pas in password_db:
            if pas["password"] == password:
                return redirect(pas["url_asli"])
            
        return render(request, "capstone/password.html", {
                "message": "Invalid password.", "slug": slug
            })


def detail(request, id):
    detail_url = Urlshort.objects.filter(id=id).values('url_asli', 'url_singkat', 'waktu', 'password', 'jumlah_klik')
    
    urlshort = Urlshort.objects.get(id=id)
    os_counts = Analytics.objects.filter(urlshort=urlshort).values('os_link').annotate(count=Count('os_link')).order_by('-count')
    browser_counts = Analytics.objects.filter(urlshort=urlshort).values('browser_link').annotate(count=Count('browser_link')).order_by('-count')
    device_counts = Analytics.objects.filter(urlshort=urlshort).values('device_link').annotate(count=Count('device_link')).order_by('-count')

    for url in detail_url:
        url_asli = url['url_asli']
        url_singkat = url['url_singkat']
        waktu = url['waktu']
        is_password = len(url['password']) > 0
        jumlah_klik = url['jumlah_klik']

    context = {
        'id': id,
        'url_asli' : url_asli,
        'url_singkat' : url_singkat,
        'waktu' : waktu,
        'is_password': is_password,
        'jumlah_klik' : jumlah_klik,
        'os_counts': os_counts,
        'browser_counts': browser_counts,
        'device_counts': device_counts
    }
    
    return render(request, 'capstone/detail.html', context)


def delete_url(request, id):
    
    urlshort = Urlshort.objects.get(id=id)
    urlshort.delete()

    print(urlshort)
    return HttpResponseRedirect(reverse("index"))