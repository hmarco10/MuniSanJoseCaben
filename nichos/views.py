from django.shortcuts import render, redirect,HttpResponse, HttpResponseRedirect, reverse
from user.models import User
from nichos.models import Reservation, Predio, Propietario
from nichos.forms import OwnerForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy



def landing_page(request):
    template = 'nichos/landing_page.html'
    return render(request, template)

def index(request, user_pk):
    template = 'nichos/index.html'
    context = {
        'user': User.objects.get(pk=user_pk),
    }
    return render(request, template, context)


def about(request, user_pk):
    template = 'nichos/about.html'
    context = {
        'user': User.objects.get(pk=user_pk),
    }
    return render(request, template, context)


def contact(request, user_pk):
    template = 'nichos/contacts.html'
    context = {
        'user': User.objects.get(pk=user_pk),
    }
    return render(request, template, context)


def contact1(request):
    template = 'nichos/contact1.html'
    return render(request, template)


def crear_reservacion(request, user_pk):
    if request.method == 'POST':
        post_predio = Predio.objects.get(pk=request.POST['predio'])
        post_propietario = Propietario.objects.get(pk=request.POST['propietario'])
        nueva_reservacion = Reservation(
            titular=request.POST['titular'],
            espacios=request.POST['espacios'],
            niveles=request.POST['niveles'],
            ornato=request.POST['ornato'],
            cancelado=request.POST['cancelado'],
            inspeccion=request.POST['inspeccion'],
            fecha=request.POST['fecha'],
            predio = post_predio,
            propietario= post_propietario,
        )
        nueva_reservacion.save()
        return HttpResponseRedirect(reverse('nichos:index', kwargs={'user_pk': user_pk}))
    elif request.method == 'GET':
        template = 'nichos/about.html'
        context = {
            'user': User.objects.get(pk=user_pk),
            'predios': Predio.objects.all(),
            'propietarios': Propietario.objects.all(),
        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar')


def show_reservation(request, user_pk):
    template = 'nichos/show_reservations.html'
    context = {
        'reservations': Reservation.objects.all(),
        'user': User.objects.get(pk=user_pk),
    }
    return render(request, template, context)


def edit_reservation(request, user_pk, reservation_pk):
    if request.method == 'POST':
        post_propietario = Propietario.objects.get(pk=request.POST['propietario'])
        post_predio = Predio.objects.get(pk=request.POST['predio'])
        updated_reservation = Reservation.objects.get(pk=reservation_pk)
        updated_reservation.titular = request.POST['titular']
        updated_reservation.espacios = request.POST['espacios']
        updated_reservation.niveles = request.POST['niveles']
        updated_reservation.ornato = request.POST['ornato']
        updated_reservation.cancelado = request.POST['cancelado']
        updated_reservation.inspeccion = request.POST['inspeccion']
        updated_reservation.fecha = request.POST['fecha']
        updated_reservation.propietario = post_propietario
        updated_reservation.predio = post_predio
        updated_reservation.save()

        return HttpResponseRedirect(reverse('nichos:show-reservation', kwargs={'user_pk': user_pk}))

    elif request.method == 'GET':
            template = 'nichos/edit.html'
            prop_post = Reservation.objects.get(pk=reservation_pk)
            pred_post = Reservation.objects.get(pk=reservation_pk)
            context = {
                'reservation': Reservation.objects.get(pk=reservation_pk),
                'propietarios': Propietario.objects.all(),
                'predios': Predio.objects.all(),
                'prop_instance': prop_post,
                'pred_instance': pred_post,
                'user': User.objects.get(pk=user_pk),
            }
            return render(request, template, context)
    return HttpResponse('Error, method not allowed!')

def delete_reservation(request, reservation_id):
    deleted_reservation = Reservation.objects.get(id=reservation_id)
    deleted_reservation.delete()

    return HttpResponseRedirect(reverse('nichos:index',  kwargs={'user_pk': deleted_reservation.propietario.id}))

#CURD WHIT CLASS BASE VIEWS

class ownerList(ListView):
    model = Propietario
    template_name=('nichos/showowner.html')


class createOwner(CreateView):
    model = Propietario
    form_class = OwnerForm
    template_name =('nichos/propietario.html')
    success_url = reverse_lazy('nichos:create_owner')



def deleteOwner(request, owner_id):
    deleted_owner = Propietario.objects.get(id=owner_id)
    deleted_owner.delete()

    return HttpResponseRedirect(reverse('nichos:list_owner'))


#### IMPRIMIR RESERVACION
def categoria_print(self, pk=None):  
   import io  
   from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle  
   from reportlab.lib.styles import getSampleStyleSheet  
   from reportlab.lib import colors  
   from reportlab.lib.pagesizes import letter, landscape  
   from reportlab.platypus import Table
   from reportlab.pdfgen import canvas  
   from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
   from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
   
   
   response = HttpResponse(content_type='application/pdf')  
   buff = io.BytesIO()  
  
   
   doc = SimpleDocTemplate(buff, 
               pagesize=letter,  
               rightMargin=40,  
               leftMargin=40,  
               topMargin=120,  
               bottomMargin=18,
               alignment=TA_LEFT,

               )  
   
   categorias = []  
   styles = getSampleStyleSheet()
   
   styles.add(ParagraphStyle(name='normal', fontSize=20, leading =60, alignment=TA_CENTER))
   header3 = Paragraph("Coorporación Auxiliar San José Caben 2019 Comprobante De Reservación De Predio", styles['normal'])  
   categorias.append(header3)
   
 
   
   styles.add(ParagraphStyle(name='normal3', fontSize=15, leading = 40, alignment=TA_CENTER))
   header2 = Paragraph('F:__________________________', styles['normal3'])  
   categorias.append(header2)
   header4 = Paragraph('    Autorizado', styles['normal3'])  
   categorias.append(header4) 
   
   styles.add(ParagraphStyle(name='normal4', fontSize=15, leading = 40, alignment=TA_CENTER))
   header5 = Paragraph('F:__________________________', styles['normal4'])  
   categorias.append(header5)  
   header6 = Paragraph('    Recibido', styles['normal4'])  
   categorias.append(header6)
   
   headings = ('No.', 'Propietario', 'Nich.', 'Niv.','Ornato','Pago','inspecc.','Fecha','Encargado','Nomc.')  
   
   
   
   if not pk:  
     todascategorias = [(p.id, p.propietario, p.espacios, p.niveles,p.ornato,p.cancelado,p.inspeccion,p.fecha,p.titular,p.predio)  
               for p in Reservation.objects.all().order_by('pk')]  
   else:  
     todascategorias = [(p.id, p.titular, p.espacios, p.niveles,p.ornato,p.cancelado,p.inspeccion,p.fecha,p.propietario,p.predio)  
               for p in Reservation.objects.filter(id=pk)]   
    
           
   t = Table([headings] + todascategorias)  
   
   t.setStyle(TableStyle(  
     [  
       ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),  
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),  
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)  
     ]  
   ))  
   
   categorias.append(t)  
   doc.build(categorias)  
   response.write(buff.getvalue())  
   buff.close()  
   return response 



