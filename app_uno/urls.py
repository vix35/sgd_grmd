from django.urls import path
from app_uno import views

app_name = 'app_uno'

urlpatterns =[
                path('register/', views.register,name='register'),
                path('user_login/', views.user_login, name='user_login'),
                path('upload_plan_diario/', views.upload_plan_diario, name = 'upload_plan_diario'),
                path('upload_velocidad_de_quiebre/', views.upload_velocidad_de_quiebre, name = 'upload_velocidad_de_quiebre')

]
