from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from user.models import User

# Create your views here.


def login_user(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
        except User.DoesNotExist:
            return HttpResponse('User does not exist!!!')

        return HttpResponseRedirect(reverse('nichos:index', kwargs={'user_pk': user.pk}))
    elif request.method == 'GET':
        template = 'user/login.html'
        return render(request, template)
    return HttpResponse('Error, Method not allowed!')


def register_user(request):
    if request.method == 'POST':
        new_customer = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            address=request.POST['address'],
            password=request.POST['password'],
        )
        new_customer.save()
        return HttpResponseRedirect(reverse('user:login'))
    elif request.method == 'GET':
        template = 'user/register.html'
        return render(request, template)
    return HttpResponse('Error: No se puede Guardar!')
