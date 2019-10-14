from django.urls import path
from nichos import views
from nichos.views import categoria_print,createOwner,ownerList, deleteOwner



app_name = 'nichos'
urlpatterns = [
    path('index/<int:user_pk>/', views.index, name='index'),
    path('about/<int:user_pk>/', views.about, name='about'),
    path('contacts/<int:user_pk>/', views.contact, name='contacts'),
    path('', views.landing_page, name='landing'),
    path('contact1/', views.contact1, name='contact1'),
    path('crear_reservacion/<int:user_pk>/', views.crear_reservacion, name='crear_reservacion'),
    
    path('show-reservations/<int:user_pk>/', views.show_reservation, name='show-reservation'),
    path('edit-reservation/<int:user_pk>/<int:reservation_pk>/',  views.edit_reservation, name='edit-reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete'),
    path('categorias/<int:pk>', categoria_print, name='categoria_print_one'),
    path('create_owner/', createOwner.as_view() , name='create_owner'),
    path('list_owner/', ownerList.as_view() , name='list_owner'),
    path('delete_owner/<int:owner_id>/', views.deleteOwner, name='delete_owner'),
]