from django.contrib import admin

from users.models import User,Seller

# Register your models here.
admin.site.register(User)
admin.site.register(Seller)