from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from Home.models import *
from accounts.models import *
from accounts.views import *

from accounts.models import cart

RGD = razorpay_gateway_detail.objects.all()[0]
# client = razorpay.Client(auth=("rzp_test_vlK7qms1BtJdXt", "GmrIdfs0XYoLWtXsY2E7D5pk"))
client = razorpay.Client(auth=(RGD.razorpay_id, RGD.razorpay_SECRET))


# Create your views here.
def fetching_link(price, reference_id, user_name, user_contact, user_email):
    p = client.payment_link.create({
        "amount": price,
        "currency": "INR",
        "accept_partial": False,
        "first_min_partial_amount": 100,
        "reference_id": reference_id,
        "callback_url": RGD.call_back_url,
        "description": "Payment for policy no #23456",
        "customer": {
            "name": user_name,
            "contact": user_contact,
            "email": user_email
        },
        "notify": {
            "sms": False,
            "email": False
        },
        "reminder_enable": True,
        "options": {
            "checkout": {
                "theme": {
                    "hide_topbar": True
                }
            }
        }
    })
    return redirect(p['short_url'])

def create_payment_link(request, hording_id):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_contact = request.POST['contact']
        user_email = request.POST['email']
        try:
            hoarding = Hoarding.objects.filter(id=hording_id)

            obj = Create_payment_link.objects.create(Amount=int(hoarding.all().values()[0]['price']),

                                                     user_name=user_name,
                                                     user_contact=user_contact,
                                                     user_email=user_email
                                                     )
            obj.Hoarding_id.set(hoarding)
            obj.save()

            fetching_link(int(hoarding.all().values()[0]['price']),
                          str(obj.id),
                          user_name, user_contact, user_email)

        except Exception as e:
            print(e)
            return HttpResponse('Some thing went wrong!!!!!')
    return render(request, 'html/details.html')


def verify_payment(request):
    if request.method == 'GET':
        payment_id = request.GET['razorpay_payment_id']
        payment_linkID = request.GET['razorpay_payment_link_id']
        payment_link_reference_id = request.GET['razorpay_payment_link_reference_id']
        payment_link_status = request.GET['razorpay_payment_link_status']
        signature = request.GET['razorpay_signature']
        obj = Create_payment_link.objects.filter(id=payment_link_reference_id)
        if obj:
            if get_verify(payment_link_id=payment_linkID,
                          payment_link_reference_id=payment_link_reference_id,
                          payment_link_status=payment_link_status,
                          razorpay_payment_id=payment_id,
                          razorpay_signature=signature):
                obj.update(payment_link_id=payment_linkID,
                           payment_link_status=payment_link_status,
                           razorpay_payment_id=payment_id,
                           razorpay_signature=signature

                           )

                return render(request, 'html/Bookings_completed.html', obj.values()[0])
            else:
                return HttpResponse('Something went Wrong!!!!!')
        return HttpResponse('not Found')
    return HttpResponse('error')


def get_verify(payment_link_id, payment_link_reference_id,
               payment_link_status, razorpay_payment_id, razorpay_signature):
    o = False
    try:

        o = client.utility.verify_payment_link_signature({
            'payment_link_id': payment_link_id,
            'payment_link_reference_id': payment_link_reference_id,
            'payment_link_status': payment_link_status,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        })
    except razorpay.errors.SignatureVerificationError as e:
        print(e)

    print(o)
    return o


def book_cart(request):
    if request.user.is_authenticated:
        car = cart.objects.filter(user=request.user)[0]
        obj = Time.objects.filter(cart=car)
        Total_price = 0
        hoarding_list=[]
        for i in obj:
            Total_price += int(i.hoarding.price) * int(i.quantity)
            print(int(i.hoarding.price) ,int(i.quantity))
            hoarding_list.append(i.hoarding)
        print(Total_price)
        cpl = Create_payment_link.objects.create(Amount=int(Total_price),

                                                 user_name=car.user.username,
                                                 user_contact='24234',
                                                 user_email=car.user.email)

        cpl.Hoarding_id.set(hoarding_list)
        cpl.save()
        return fetching_link(Total_price, str(cpl.id), car.user.username, '8938095294', car.user.email)
    else:
        return redirect(login)