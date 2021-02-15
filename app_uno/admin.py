from django .contrib import admin
from app_uno .models import  Velocidad_de_quiebre, DBF, Plan_diario
# Register your models here.

admin.site.register(Velocidad_de_quiebre)
admin.site.register(DBF)
admin.site.register(Plan_diario)
