from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import mainUser
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = mainUser
    # exclude = ('first_name', 'last_name','email')
    list_display = ('__str__', 'level', 'is_active','jpublish')
    list_filter = ('is_staff', 'is_active','date_joined')
    search_fields = ('salary', 'level')
    ordering = ('date_joined',)
    fieldsets = (
        ('main inforamation', {'classes': ('wide',),
            'fields': ('level', 'password',)}),
        ('initial information',{'fields': ( 'first_name' ,'last_name' ,'email', ) } ),
        ('technical information',{'fields': ( 'salary','date_joined' ) } ),
    )
    add_fieldsets = (
        ('initial information', {
            'classes': ('wide',),
            'fields': ('level','password','username','is_staff','first_name' ,'last_name' ,'email',)}
         ),
        ('another info', {'fields': (
        'age',)}),
        ('inffffff', {'fields': ('salary',)}),
    )
admin.site.register(mainUser,UserAdmin)