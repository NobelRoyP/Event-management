from django.urls import path
from eventlive import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('speaker/',views.speaker,name='speaker'),
    path('schedule/',views.schedule,name='schedule'),
    path('user_regester/',views.user_register,name='user_regester'),
    path('user_list/',views.user_list,name='user_list'),
    path('login/',views.login,name='login'),
    path('deleteuser/<int:id>/',views.deleteuser,name='deleteuser'),
    path('deleteorganizer/<int:id>/',views.deleteorganizer,name='deleteorganizer'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('profile/',views.profile,name='profile'),
    path('userhome/',views.userhome,name='userhome'),
    path('edit/<int:eid>',views.edit,name='edit'),
    path('regester_organizer/',views.register_organizer,name='register_organizer'),
    path('organizerlogin/',views.organizerlogin,name='organizerlogin'),
    path('oindex/',views.oindex,name='oindex'),
    # path('addevent/',views.addevent,name='addevent'),
    path('listevent/',views.listevent,name='listevent'),
    path('editevent/<int:eid>',views.editevent,name='editevent'),
    path('deleteevent/<int:eid>',views.deleteevent,name='deleteevent'),
    path('rat/', views.rat, name='rat'),
    path('monitor/', views.monitor, name='monitor'),
    path('fbdel/<int:id>/', views.fbdel, name='fbdel'),
    path('pendingevent/', views.pendingevent, name='pendingevent'),
    path('organizereventcreate/', views.addevents, name='organizereventcreate'),
    path('approve_event/<int:event_id>/',views.approved_events, name='approve_event'),
    path('reject_event/<int:event_id>/',views.reject_events, name='reject_event'),
    path('listing/',views.listing, name='listing'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery_list/', views.gallery_list, name='gallery_list'),  # Gallery List page
    path('add_gallery/', views.add_gallery, name='add_gallery'),
    path('<int:id>/edit/', views.edit_gallery, name='edit'),
    path('<int:id>/delete/', views.delete_gallery, name='delete'),
    path('service/', views.service, name='service'),
    path('cateringservice/', views.cateringservice, name='cateringservice'),
    path('stagedecoration/', views.stagedecoration, name='stagedecoration'),
    path('livejuice/', views.livejuice, name='livejuice'),
    path('royalhosting/', views.royalhosting, name='royalhosting'),
    path('clothsetting/', views.clothsetting, name='clothsetting'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('oeventlist/', views.oeventlist, name='oeventlist'),
    path('upload/', views.upload, name='upload'),
    path('logout/', views.user_logout, name='logout'),
    path('delete_product/<pid>/',views.delete_product,name='delete_product'),
    path('initiate-payment/<cid>/', views.initiate_payment, name='initiate-payment'),
    path('confirm-payment/<order_id>/<payment_id>/<crti_id>/', views.confirm_payment, name='confirm-payment'),
    path('addcart/<int:pid>/',views.addcart,name='addcart'),
    path('cartlist/',views.cart_list,name='cartlist'),
    path('mybooking/',views.mybooking,name='mybooking'),
    path('about-us/',views.aboutus,name='about-us'),
    path('organizer_list/',views.organizer_list,name='organizer_list'),


    
    
    
    
    

]