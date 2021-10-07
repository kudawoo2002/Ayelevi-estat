from django.shortcuts import render
from .models import Location, House, Contract, Seller
# Create your views here.

def index(request):
    locations = Location.objects.all()
    houses = House.objects.filter(is_available=True).order_by('-create_date')[:3]
    contracts = Contract.objects.all()
    context = {
        'locations': locations,
        'houses': houses,
        'contracts': contracts,
    }
    return render(request, 'houses/index.html', context)


def property(request):
    locations = Location.objects.all()
    houses = House.objects.filter(is_available=True).order_by('-create_date')
    contracts = Contract.objects.all()
    context = {
        'locations': locations,
        'houses': houses,
        'contracts': contracts,
    }
    return render(request, 'houses/propertie.html', context)

def house_detail(request, house_slug):
    locations = Location.objects.all()
    house = House.objects.get(slug=house_slug)
    houses = House.objects.filter(is_available=True).order_by('-create_date')[:4]
    house_sale = House.objects.filter(contract__contract_type='For Sale')[:2]
    print(house_sale)
    context = {
        'house': house,
        'houses':houses,
        'house_sale':house_sale,
        'locations': locations,
    }
    return render(request, 'houses/house_detail.html', context)

def house_by_location(request, location_slug):
    locations = Location.objects.all()
    location = Location.objects.get(slug=location_slug)
    houses = House.objects.filter(location__location_name=location)
    # for item in locations:
    #     print(item)
    context = {
        'houses':houses,
        'location': location,
        'locations': locations,
    }
    return render(request, 'houses/house_by_location.html', context)
