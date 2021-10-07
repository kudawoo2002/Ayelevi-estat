from django.contrib import admin
from .models import Seller, Location, Contract, House
# Register your models here.




class HouseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('house_name',)}


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('location_name',)}

class ContractAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('contract_type',)}


admin.site.register(House, HouseAdmin)
admin.site.register(Seller)
admin.site.register(Location, LocationAdmin)
admin.site.register(Contract, ContractAdmin)
