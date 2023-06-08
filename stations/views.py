import csv
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

def bus_stations(request):
    with open(settings.BASE_DIR / 'data-398-2018-08-30.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        bus_stations_list = list(reader)

    paginator = Paginator(bus_stations_list, 10)  # Показывать 10 станций на странице
    page = request.GET.get('page')
    try:
        bus_stations = paginator.page(page)
    except PageNotAnInteger:
        bus_stations = paginator.page(1)
    except EmptyPage:
        bus_stations = paginator.page(paginator.num_pages)

    context = {
        'bus_stations': bus_stations,
    }
    return render(request, 'stations/index.html', context)