from django.contrib import admin
from .models import SaleForm
from .models import RentForm
from .models import Contact


# Register your models here.
admin.site.register(SaleForm)
admin.site.register(RentForm)
admin.site.register(Contact)
