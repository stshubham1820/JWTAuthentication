from django.contrib import admin
from .models import *
# Register your models here.
class studpersonal(admin.ModelAdmin):
    list_display = ('Name','Age','Dob','Father_Name'
    ,'Mother_Name','Mobile_Number','Email','Blood_Group','Class','Sec')
    def __str__(self) -> str:
        return self.Name
admin.site.register(Studpersonal,studpersonal)
