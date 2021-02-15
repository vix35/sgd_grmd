from django.shortcuts import render
from app_uno.forms import UserForm, UploadFileForm
from app_uno.models import Plan_diario, Velocidad_de_quiebre, DBF
from time import time
#from app_uno.helpers import FactoryPlanesDiarios#
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required

import csv
import io

#Funciones utiles

def is_pd_modified(row,old_data):
    for i in old_data:
        if (i.sector == row[0] and i.punto == row[1] and i.fecha == row[2] and i.TPD != row[3]):
            return True
        else:
            return False

def is_pd_new(row, old_data):
    for i in old_data:
        if (i.sector == row[0] and i.punto == row[1] and i.fecha == row[2]):
            return False

    return True




# Create your views here.

def index (request):
    return render(request, 'app_uno/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register (request):

    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'app_uno/registration.html', { 'user_form':user_form,
                                                            'registered':registered})

def user_login (request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Cuenta no activa')

        else:
            print('Alguien intento loguearse y fallo')
            print('username: {} and password {}'.format(username,password))
            return HttpResponse("los datos proporcionados para los campos requeridos son invalidos")
    else:
        return render(request, 'app_uno/login.html',{})

@login_required()
@permission_required('app_uno.add_Plan_diario', raise_exception=True)
def upload_plan_diario(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with io.TextIOWrapper(form.cleaned_data['file'].file) as f:
                reader = csv.reader(f)
                inicio = time()
                obj_upd = []
                obj_new = []
                old_data = []
                ultima_fecha = []
                for i, row in enumerate(reader):
                    print(row)
                    if ((i==0) or (row[0]=='')):
                        pass
                    else:
                        if i == 1 or ultima_fecha != row[2]:
                            ultima_fecha = row[2]
                            old_data = Plan_diario.objects.filter(fecha = ultima_fecha)
                        if is_pd_new(row, old_data) == (True or None):
                            print('new')
                            obj_new.append(Plan_diario(sector = row[0], punto = row[1], fecha = row[2], TPD = row[3]))
                        else:
                            if is_pd_modified(row, old_data):
                                print('modificado')
                                obj_upd.append(Plan_diario.objects.get(sector = row[0], punto = row[1], fecha = row[2]))
                                obj_upd[len(obj_upd)-1].TPD = row[3]
                            else:
                                continue
                Plan_diario.objects.bulk_create(obj_new)
                Plan_diario.objects.bulk_update(obj_upd, ['TPD'])
                duracion = time() - inicio
                print("Tiempo de ejecucion :"+str(duracion))
    else:
        form = UploadFileForm()
    return render(request, 'app_uno/upload_plan_diario.html', {'form': form})


@login_required()
@permission_required('app_uno.add_Velocidad_de_quiebre', raise_exception=True)
def upload_velocidad_de_quiebre(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with io.TextIOWrapper(form.cleaned_data['file'].file) as f:
                reader = csv.reader(f)
                inicio = time()
                for i, row in enumerate(reader):
                    if ((i==0) or (row[0]=='')):
                        pass
                    else:
                        obj, created = Velocidad_de_quiebre.objects.update_or_create (
                                                                            sector = row[0],
                                                                            punto = row[1],
                                                                            fecha = row[2],
                                                                            turno = row[3],
                                                                            defaults =  {
                                                                                        'condicion_geomecanica': row[4],
                                                                                        'velocidad_recomendada': row[5],
                                                                                        'observaciones_SGO': row[6],
                                                                                        'poligono_control_sismico_asociado': row[7],
                                                                                        'id_para_control_SGP_focos': row[8],
                                                                                        'porcentaje_ext_primario': row[9],
                                                                                        }
                                                                            )

    else:
        form = UploadFileForm()
    return render(request, 'app_uno/upload_velocidad_de_quiebre.html', {'form': form})
