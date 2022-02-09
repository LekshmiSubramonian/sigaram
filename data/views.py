from os import name
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import SaleForm
from .form import Sale
from .models import RentForm
from .form import Rent
from .models import Contact
from .form import Contacts
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mass_mail


# Create your views here.

def home(request):
    return render(request, "home.html")


def advertise(request):
    prdt = SaleForm.objects.all()
    prd = RentForm.objects.all()
    return render(request, "advertise.html", {'prdts': prdt, 'prds': prd})


def about(request):
    return render(request, "about.html")


'''
def contact(request):
    return render(request, "contact.html")
    '''


def saleform(request):
    if request.method == "POST":
        form = Sale(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'thankyou.html')

    else:
        form = Sale()

    return render(request, "saleform.html")


def rentform(request):
    if request.method == "POST":
        form = Rent(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')

    else:
        form = Rent()

    return render(request, "rentform.html")


def search(request):
    query = request.GET['query']

    if(query == "sale" or query == "Sale"):
        prdt = SaleForm.objects.all()
        return render(request, "sale.html", {'prdts': prdt})
    elif(query == "rent" or query == "Rent"):
        prd = RentForm.objects.all()
        return render(request, "rent.html", {'prds': prd})
    # res=SaleForm.objects.all()
    elif len(query) > 78:
        res = SaleForm.objects.none()
        ren = RentForm.objects.none()
    else:
        restype = SaleForm.objects.filter(types__icontains=query)
        resthaluk = SaleForm.objects.filter(thaluk__icontains=query)
        ownmail = SaleForm.objects.filter(email__icontains=query)
        ownphn = SaleForm.objects.filter(phone__icontains=query)
        ownimage = SaleForm.objects.filter(image__icontains=query)
        #resamtr1 = SaleForm.objects.filter(amt__range=[5000, 10000000])

        rentype = RentForm.objects.filter(types__icontains=query)
        renthaluk = RentForm.objects.filter(thaluk__icontains=query)
        ownmailren = RentForm.objects.filter(email__icontains=query)
        ownphnren = RentForm.objects.filter(phone__icontains=query)
        ownimageren = RentForm.objects.filter(image__icontains=query)

        res = restype.union(resthaluk, ownmail, ownimage, ownphn)
        ren = rentype.union(renthaluk, ownmailren, ownphnren, ownimageren)

        prores = {'prdts': res, 'prds': ren, 'query': query}

        return render(request, "search.html", prores)


def contact(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = 'Sigaram Associates'
        content = 'Thank you,'+username.capitalize() + \
            '! Your Query has been recorded. We will get back to you soon!'
        email_to = settings.EMAIL_HOST_USER
        send_mail(subject, content, email_to, [email], fail_silently=False)
        form = Contacts(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thankyou.html", {'email': email_to})
        return redirect('/')

    else:
        form = Contacts()

    return render(request, "contact.html")


def order(request):
    if request.method == "POST":
        query = request.POST.get('ord')
        res = SaleForm.objects.filter(image__icontains=query)
        prores = {'prdts': res, 'query': query}
        return render(request, "order.html", prores)


def orderrent(request):
    if request.method == "POST":
        query = request.POST.get('ordren')
        ren = RentForm.objects.filter(image__icontains=query)
        prore = {'prds': ren, 'query': query}
        return render(request, "orderrent.html", prore)
        # return render(request, 'thankyou.html')


def thankyou(request):
    if request.method == "POST":
        ownname = request.POST.get('ownname')
        ownphn = request.POST.get('ownphone')
        ownmail = request.POST.get('ownmail')
        ownimage = request.POST.get('ownimage')
        cusname = request.POST.get('cusname')
        cusphn = request.POST.get('cusphn')
        cusmail = request.POST.get('cusmail')
        cxt = {
            'ownername': ownname,
            'ownerphone': ownphn,
            'ownermail': ownmail,
            'property': ownimage,
            'cusname': cusname,
            'cusphn': cusphn,
            'cusmail': cusmail
        }
        message = get_template('myorder.html').render(cxt)
        deal = ('Sigram Associates', 'Your property has been wishlisted by Mr/Mrs '+cusname.capitalize() +
                '! Sigaram Associates is working on for progress. We will get back to you soon.', 'sigaramassociates00@gmail.com', [ownmail])
        cus = ('Sigram Associates', "Thankyou! You have wishlisted Mr/Mrs "+ownname.capitalize() +
               "'s property. Sigram Associates is working on for progress. We will get back to you soon.", 'sigaramassociates@gmail.com', [cusmail])
        myself = EmailMessage(
            'Subject',
            message,
            'sigaramassociates00@gmail.com',
            ['sigaramassociates00@gmail.com'],
        )
        myself.content_subtype = "html"  # Main content is now text/html
        send_mass_mail((deal, cus), fail_silently=False)
        myself.send()
    return render(request, "thankyou.html")
