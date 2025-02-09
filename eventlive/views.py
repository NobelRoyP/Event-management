from django.shortcuts import render,redirect,HttpResponse
from .models import Transaction, cart, regester,organizer,event,fb,eventsupdates
from django.shortcuts import get_object_or_404
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request,'index.html')
def userhome(request):
      if 'email' in request.session:
        email=request.session['email']
        return render(request,'userhome.html')
      else:
          return redirect('login')
def contact(request):
    return render(request,'contact.html')
def aboutus(request):
    return render(request,'about-us.html')
def speaker(request):
    return render(request,'speaker.html')
def schedule(request):
    return render(request,'schedule.html')
def oindex(request):
    if 'email' in request.session:
        email=request.session['email']
        user=organizer.objects.get(email=email)
        return render(request,'oindex.html',{'user':user})
    else:
        return redirect('organizerlogin')
    

   


def user_register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone_number=request.POST.get('phone_number')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        image=request.FILES.get('image')
        try:
            usrd= regester.objects.get(email=email)
            
            alert_message="<script>alert('EMAIL ALREADY EXIST⚠️'); window.location.href='/user_regester/';</script>"
            return HttpResponse(alert_message)
        except Exception as e:
            print(e)
            obj=regester(name=name,email=email,password=password,phone_number=phone_number,age=age,gender=gender,address=address,image=image)
            obj.save()
            return redirect('login')

    
    else:
        return render(request,'user_regester.html')


def user_list(request):
    users = regester.objects.all()
    return render(request, 'user_list.html', {'users': users})

def organizer_list(request):
    organizers = organizer.objects.all()
    return render(request, 'organizer_list.html', {'organizers': organizers})

def monitor(request):
    complaint = fb.objects.all()
    return render(request, 'monitor.html', {'complaint': complaint})
def login(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=regester.objects.get (email=username,password=password)
            semail=user.email
            request.session['email']=semail
            return redirect('userhome')
        except:
            alert_message="<script>alert('INCORRECT EMAIL⚠️'); window.location.href='/login';</script>"
            return HttpResponse(alert_message)
    return render(request,'login.html')

def deleteuser(request,id):
    u=regester.objects.get(id=id)
    u.delete()
    return redirect('user_list')

def deleteorganizer(request,id):
    u=organizer.objects.get(id=id)
    u.delete()
    return redirect('organizer_list')

def adminlogin(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        password=request.POST.get('password')
        u='admin'
        p='123456'
        if uname==u:
            
            if password==p:
                return redirect('admin_dashboard')
            alert_message="<script>alert('INCORRECT EMAIL⚠️'); window.location.href='/adminlogin';</script>"
            return HttpResponse(alert_message)
    return render(request,'adminlogin.html')

def admin_dashboard(request):

    return render(request,'admin_dashboard.html')
    
def profile(request):
    if'email' in request.session:
        mail=request.session['email']
        user=regester.objects.get(email=mail)
        print(user)
        return render(request,'profile.html',{'user':user})
    return redirect('login')
    
def edit(request,eid):
    edit=regester.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        edit.name=name
        edit.address=address
        edit.age=age
        edit.gender=gender
        edit.phone_number=phone_number
        edit.password=password           
        edit.email=email
        edit.image=image
        edit.save()
        return redirect('profile')
    return render(request,'edit.html',{'edit':edit})


def register_organizer(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone_number=request.POST.get('phone_number')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        image=request.FILES.get('image')
        try:
            usrd  = organizer.objects.get(email=email)
            # type: ignore
            alert = "<script>alert('user exists');window.location.href = '/index/';</script>"
            return HttpResponse(alert)
        except Exception as e:
            print("fuuu",e)
            try:
                obj=organizer(name=name,email=email,password=password,phone_number=phone_number,age=age,gender=gender,address=address,image=image)
                obj.save()
                return redirect('organizerlogin')
            except Exception as e:
                print(e)
                alert = "<script>alert('user exists');window.location.href = '/index/';</script>"
                return HttpResponse(alert)


    else:
        return render(request,'regester_organizer.html')
    


    
def organizerlogin(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=organizer.objects.get (email=username,password=password)
            semail=user.email
            request.session['email']=semail
            return redirect('oindex')
        except:
            alert_message="<script>alert('INCORRECT EMAIL⚠️'); window.location.href='/organizerlogin';</script>"
            return HttpResponse(alert_message)
    return render(request,'organizerlogin.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import eventsupdates

def edit_event(request, event_id):
    # Fetch the event by its ID
    event = get_object_or_404(eventsupdates, id=event_id)
    
    if request.method == 'POST':
        # Update model fields manually from POST data
        event.category = request.POST.get('category', event.category)
        event.eventname = request.POST.get('eventname', event.eventname)
        event.details = request.POST.get('details', event.details)
        event.eventdate = request.POST.get('eventdate', event.eventdate)
        event.amount = request.POST.get('amount', event.amount)
        event.registerenddate = request.POST.get('registerenddate', event.registerenddate)
        event.resultdate = request.POST.get('resultdate', event.resultdate)
        event.status = request.POST.get('status', event.status)
        event.staff_user_id = request.POST.get('staff_user', event.staff_user_id)
        event.msg = request.POST.get('msg', event.msg)

        # Handle file uploads
        if 'image' in request.FILES:
            event.image = request.FILES['image']

        # Save the updated event
        event.save()

        return redirect('event_detail', event_id=event.id)  # Redirect to the event detail page or list

    else:
        # Display the current event details when the form is first loaded
        return render(request, 'edit_event.html', {'event': event})

def oeventlist(request):
    if 'email' in request.session:
        email = request.session.get('email')
        events = eventsupdates.objects.filter(user__email=email)
        return render(request,'oeventlist.html',{'events':events})
    return render(request,'organizerlogin.html')

def listevent(request):
    events = eventsupdates.objects.all()
    return render(request,'listevent.html',{'user':events})
def eventlist(request):
    events = eventsupdates.objects.all()
    return render(request,'eventlist.html',{'user':events})
    
def editevent(request,eid):
    try:
        ev=event.objects.get(id=eid)
    except:
        print("eventnotfound")
    if request.method=="POST" :
      eventid=request.POST.get('eventid')
      eventname=request.POST.get('eventname')
      description=request.POST.get('description')
      amount=request.POST.get('amount')
      sampleimage=request.FILES.get('sampleimage')
      organizerid=request.POST.get('organizerid')
      if eventid != ev.eventid and event.objects.filter(id=eventid).exists():
        alert="<script> alert('Email already exists'); window.location.href='/listevent/'; </script>"
        return HttpResponse(alert)
        # return redirect('listevent')
      else:
        ev.eventid=eventid
        ev.eventname=eventname
        ev.description=description
        ev.amount=amount
        ev.organizerid=organizerid
        if sampleimage:
            ev.sampleimage=sampleimage
        ev.save()
        return redirect('listevent')
    else:
        return render(request,'editevent.html',{'usr': ev})
    
def deleteevent(request,eid):
    try:
        ev=event.objects.get(id=eid)
        ev.delete()
        alert="<script> alert('delete sussefull'); window.location.href='/listevent/'; </script>"
        return HttpResponse(alert)
    except:
        alert="<script> alert('unexpect error'); window.location.href='/listevent/'; </script>"
        return HttpResponse(alert)
def rat(request):
        if request.method=="POST":
                name=request.POST.get('name')
                feedback=request.POST.get('feedback')
                rating=request.POST.get('rating')
                obj=fb(name=name,feedback=feedback,rating=rating)
                obj.save()
                alert="<script>alert('thank you!!!');window.location.href='/userhome';</script>"
                return HttpResponse(alert)
        return render(request,'rat.html')
def fbdel(request,id):
    if 'email' in request.session:
        email=request.session['email']
        try:
            user=fb.objects.get(id=id)
            print(user)
            user.delete()
            return redirect('monitor')
        except Exception as e:
            print(e)
            Alert="<script> alert('no user found'); window.location.href='/adminlogin/'; </script>"
            return HttpResponse(Alert)
    else:
        return redirect('monitor')




         

def addevents(request):
    if 'email' in request.session:
        email = request.session.get('email')
        print(email)

        try:
            # Fetch the registered user based on email
            userd = organizer.objects.get(email=email)  
        except Exception as e:
            print(e)
            return redirect('organizerlogin')  # Redirect to login if no session exists
        
        if request.method == 'POST' and userd:
            category = request.POST.get('category')
            eventname = request.POST.get('eventname')
            image = request.FILES.get('image')
            details = request.POST.get('details')
            eventdate = request.POST.get('eventdate')
            amount = request.POST.get('amount')
            registerenddate = request.POST.get('registerenddate')
            resultdate = request.POST.get('resultdate')

            # Save the event with the associated user
            try:
                data = eventsupdates(
                    user=userd,  # Associate the event with the logged-in user
                    category=category,
                    eventname=eventname,
                    image=image,
                    details=details,
                    eventdate=eventdate,
                    amount=amount,
                    registerenddate=registerenddate,
                    resultdate=resultdate
                )
                data.save()
                return redirect('oeventlist')
            except Exception as e:
                print(e)

        return render(request, 'organizereventcreate.html')

    return redirect('organizerlogin')
def approved_events(request,event_id):
    event = get_object_or_404(eventsupdates, id=event_id)
    event.status="APPROVED"
    
   
     # Track who approved the event
    event.save()
    return redirect('pendingevent')

from django.shortcuts import render, get_object_or_404, redirect
from .models import eventsupdates

def reject_events(request, event_id):
    event = get_object_or_404(eventsupdates, id=event_id)
    
    event.status = "REJECTED"
    event.save()
    
    # Redirect to the event list page after rejection to reflect the changes
    return redirect('pendingevent')

    

def pendingevent(request):
    # current_date = timezone.now().date()
    events = eventsupdates.objects.all()
    return render(request,'pendingevent.html',{'events':events})
def listing(request):
    events = eventsupdates.objects.all()
    return render(request,'listing.html',{'events':events})

# gallery/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image

def add_gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')  # Redirect to list page after saving
    else:
        form = ImageForm()
    return render(request, 'add_gallery.html', {'form': form})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

def gallery_list(request):
    # Get all images from the database
    images = Image.objects.all()
    return render(request, 'gallery_list.html', {'images': images})

def edit_gallery(request, id):
    image = Image.objects.get(id=id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')  # Redirect to list page after saving
    else:
        form = ImageForm(instance=image)
    return render(request, 'edit_gallery.html', {'form': form})

def delete_gallery(request, id):
    image = get_object_or_404(Image, id=id)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery_list')  # Redirect to list page after deleting
    return render(request, 'confirm_delete.html', {'image': image})

def service(request):
    organizers = organizer.objects.all()
    
    return render(request,'service.html',{'organizers':organizers})

def stagedecoration(request):
    return render(request,'stagedecoration.html')
def cateringservice(request):
    return render(request,'cateringservice.html')
def livejuice(request):
    return render(request,'livejuice.html')
def royalhosting(request):
    return render(request,'royalhosting.html')
def clothsetting(request):
    return render(request,'clothsetting.html')
    



from django.shortcuts import render, get_object_or_404, redirect
from .models import eventsupdates

def edit_event(request, event_id):
    # Fetch the event by its ID
    event = get_object_or_404(eventsupdates, id=event_id)
    
    if request.method == 'POST':
        # Update model fields manually from POST data
        event.category = request.POST.get('category', event.category)
        event.eventname = request.POST.get('eventname', event.eventname)
        event.details = request.POST.get('details', event.details)
        
     

        # Handle file uploads
        if 'image' in request.FILES:
            event.image = request.FILES['image']

        # Save the updated event
        event.save()

        return redirect('oeventlist')  # Redirect to the event detail page or list

    else:
        # Display the current event details when the form is first loaded
        return render(request, 'edit_event.html', {'event': event})
    
def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('photo')
    return render(request,'upload.html')  


from django.shortcuts import redirect


from django.shortcuts import render, redirect

def user_logout(request):
    # Manually flush the session
    request.session.flush()

    # Redirect to the login page
    return redirect('login')




          






def delete_product(request,pid):
    email = request.session.get('email')
    if not email:
        return redirect('organizelogin')
    
    prf= eventsupdates.objects.get(id=pid)

    prf.delete()
    return redirect('oeventlist')
          

from django.contrib.auth import logout
import razorpay # type: ignore
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.conf import settings
# from razorpay.errors import BadRequestError
from django.views.decorators.csrf import csrf_exempt

# from razorpay.errors import BadRequestError
from django.views.decorators.csrf import csrf_exempt




def initiate_payment(request,cid):
    email = request.session['email']
    if email:
        crt=cart.objects.get(id=cid)
        am=crt.total_price
        amount = int(am)*100 
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment_order = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        order_id = payment_order['id']
        juser = regester.objects.get(email=email)
        buyer_data = {
            'buyer': {
                'id': juser.id,
                'name': juser.name,
                'email': juser.email,
                'phone': juser.phone_number,
                # Add other fields as needed
            }
        }
        response_data = {'order_id': order_id, 'amount': amount}
        response_data.update(buyer_data)
        return JsonResponse(response_data, encoder=DjangoJSONEncoder)
    else:
        return redirect('log')
    

from decimal import Decimal   
@csrf_exempt
def confirm_payment(request, order_id, payment_id,crti_id):
    print('Confirm payment')
    try:
        print('Payment ID:', payment_id)
        print('order_id:', order_id)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment = client.payment.fetch(payment_id)
        print('Payment:', payment['order_id'])
        print('payment', payment)
        if payment['order_id'] == order_id and payment['status'] == 'captured':
            pemail = payment.get('email')
            amount = payment.get('amount')
            amount_in_rupees = Decimal(amount) / Decimal(100)  

            if pemail:
                usr = regester.objects.get(email=pemail)
                crts=cart.objects.get(id=crti_id)
             
                prd=crts.products
                trns=Transaction(user=usr,products=prd,amount=amount_in_rupees,quantity=crts.quantity,order_id=order_id)
                trns.save()
                crts.delete()
                return redirect('userhome')

            else:
               return JsonResponse({'status': 'failure', 'error': 'User email not found'})
        else:
            print(payment['status'])
            return JsonResponse({'status': 'failure', 'error': 'Payment status not captured'})
    except Exception as e:
        print('Error:', str(e))
        return redirect('userhome')






def addcart(request,pid):
    if 'email' in request.session:
        email=request.session.get('email')
        us=regester.objects.get(email=email)
        products=eventsupdates.objects.get(id=pid)

        if request.method == "POST":
            quantity = request.POST.get('quantity')
            quantity=int(quantity)
            total_price = products.amount*quantity
            cart_item,created=cart.objects.get_or_create(user=us,products=products,defaults={'quantity':quantity,'total_price':total_price} )
            if not created:
                cart_item.quantity = quantity
                cart_item.total_price=products.amount*quantity
                cart_item.save()

                return redirect('cartlist')
            return redirect('cartlist')
        
        else:
            return render(request,'cart.html',{'prd':products})
    else:
        return redirect('login')

def cart_list(request):
    # Fetch the user's cart items
    if 'email' in request.session:
        email = request.session['email']
        user = regester.objects.get(email=email)
        cart_items = cart.objects.filter(user=user)

        return render(request, 'cartlist.html', {'cart_items': cart_items})
    else:
        return redirect('login')
    

def  mybooking(request):
    if 'email' in request.session:
        email=request.session.get('email')
        bike=Transaction.objects.filter(user__email=email)
        return render(request,'mybooking.html',{'bike':bike})
    return render(request,'index.html')