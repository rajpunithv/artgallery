from django.contrib import admin
from .models import Login,Customer
from .models import Feedback

# Register your models here.
admin.site.register(Login)
admin.site.register(Customer)
admin.site.register(Feedback)
