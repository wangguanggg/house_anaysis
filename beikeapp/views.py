from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
from .models import sellhouse, resthouse

@login_required()
def showsell_view(request):
    return render(request, 'beikeapp/showsell.html')

@login_required()
def showsell_bypage(request):
    houses = sellhouse.objects.all()
    lis = [{"id": house.id, "title": house.title, "address": house.address, "unit_type": house.unit_type, "created_time": house.created_time
            , "room_type": house.room_type, "area": house.area, "toward": house.toward, "total_price": house.total_price
            , "unit_price": house.unit_price, "follows": house.follows} for house in houses]
    page_index = request.GET.get('page')
    page_limit = request.GET.get('limit')
    paginator = Paginator(lis, page_limit)
    data = paginator.page(page_index)
    house_info = [x for x in data]
    houses = {"code": 0, "msg": "", "count": houses.count(), "data": house_info}
    return JsonResponse(houses)

@login_required()
def dropsell(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        beike = sellhouse.objects.get(pk=id)
        beike.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)

@login_required()
def modifysell(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        beike = sellhouse.objects.get(pk=id)
        beike.title = request.POST.get("title")
        beike.address = request.POST.get("address")
        beike.unit_type = request.POST.get("unit_type")
        beike.created_time = request.POST.get("created_time")
        beike.room_type = request.POST.get("room_type")
        beike.area = request.POST.get("area")
        beike.toward = request.POST.get("toward")
        beike.total_price = request.POST.get("total_price")
        beike.unit_price = request.POST.get("unit_price")
        beike.follows = request.POST.get("follows")
        beike.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)

@login_required()
def findsellbymsg(request):
    msg = request.GET.get("msg")
    houses = sellhouse.objects.filter(Q(title__contains=msg) | Q(address__contains=msg) |
                                  Q(unit_type__contains=msg) | Q(room_type__contains=msg)|
                                  Q(area__contains=msg) | Q(toward__contains=msg) |
                                  Q(total_price__contains=msg) | Q(unit_price__contains=msg))
    lis = [{"id": house.id, "title": house.title, "address": house.address, "unit_type": house.unit_type,
            "created_time": house.created_time
               , "room_type": house.room_type, "area": house.area, "toward": house.toward,
            "total_price": house.total_price
               , "unit_price": house.unit_price} for house in houses]
    page_index = request.GET.get('page')
    page_limit = request.GET.get('limit')
    paginator = Paginator(lis, page_limit)
    data = paginator.page(page_index)
    house_info = [x for x in data]
    houses = {'code': 0, "msg": "", "count": houses.count(), "data": house_info}
    return  JsonResponse(houses)

@login_required()
def showrest_view(request):
    return render(request, "beikeapp/showrest.html")


@login_required
def showrest_bypage(request):
    houses = resthouse.objects.all()
    lis = [
        {"id": house.id, "title": house.title, "room_type": house.room_type, "area": house.area, "toward": house.toward,
         "month_price": house.month_price} for house in houses]
    page_index = request.GET.get('page')
    page_limit = request.GET.get('limit')
    paginator = Paginator(lis, page_limit)
    data = paginator.page(int(page_index))
    house_info = [x for x in data]
    houses = {"code": 0, "msg": "", "count": houses.count(), "data": house_info}
    return JsonResponse(houses)

@login_required()
def droprest(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        house = resthouse.objects.get(pk=id)
        house.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)

@login_required()
def modifyrest(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        house = resthouse.objects.get(pk=id)
        house.title = request.POST.get("title")
        house.room_type = request.POST.get("room_type")
        house.toward = request.POST.get("toward")
        house.area = request.POST.get("area")
        house.month_price = request.POST.get("month_price")
        house.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)

@login_required()
def findrestbymsg(request):
    msg = request.GET.get("msg")
    houses = resthouse.objects.filter(Q(title__contains=msg)|Q(room_type__contains=msg)| Q(toward__contains=msg) |
                                  Q(month_price__contains=msg) | Q(area__contains=msg))
    lis = [{"id": house.id, "title": house.title,
               "room_type": house.room_type, "area": house.area, "toward": house.toward,
            "month_price": house.month_price} for house in houses]
    page_index = request.GET.get('page')
    page_limit = request.GET.get('limit')
    paginator = Paginator(lis, page_limit)
    data = paginator.page(page_index)
    house_info = [x for x in data]
    houses = {'code': 0, "msg": "", "count": houses.count(), "data": house_info}
    return  JsonResponse(houses)

@login_required()
def echart(request):
    return render(request, "beikeapp/charts.html")

@login_required()
def gethistdata(request):
    data = {
        "y": [sellhouse.objects.filter(total_price__lt=300).count(),
              sellhouse.objects.filter(total_price__range=[300, 400]).count(),
              sellhouse.objects.filter(total_price__range=[400, 600]).count(),
              sellhouse.objects.filter(total_price__range=[600,800]).count(),
              sellhouse.objects.filter(total_price__range=[800, 1000]).count(),
              sellhouse.objects.filter(total_price__gte=1000).count()
              ]
    }
    return JsonResponse(data)

@login_required()
def getpiedata(request):
    data = {
        "data": [
            {"value": sellhouse.objects.filter(follows__lte=10).count(), "name": '小于10人'},
            {"value": sellhouse.objects.filter(follows__range=[11, 20]).count(), "name": '10-20人'},
            {"value": sellhouse.objects.filter(follows__range=[21, 40]).count(), "name": '21-40人'},
            {"value": sellhouse.objects.filter(follows__range=[41, 60]).count(), "name": '41-60人'},
            {"value": sellhouse.objects.filter(follows__gte=61).count(), "name": '大于60人'},
        ]
    }
    return JsonResponse(data)

@login_required
def getlinedata(request):
    data = {
        "data": [
            sellhouse.objects.filter(toward__contains="东").count(),
            sellhouse.objects.filter(toward__contains="南").count(),
            sellhouse.objects.filter(toward__contains="西").count(),
            sellhouse.objects.filter(toward__contains="北").count(),
            sellhouse.objects.filter(toward__contains="东南").count(),
            sellhouse.objects.filter(toward__contains="东北").count(),
            sellhouse.objects.filter(toward__contains="西南").count(),
            sellhouse.objects.filter(toward__contains="西北").count(),
        ]
    }
    return JsonResponse(data)

@login_required()
def getscatterdata(request):
    houses = sellhouse.objects.all().values_list("area", "total_price")
    data = {
        "data": [list(i) for i in houses],
    }
    data['data'] = data['data'][0:100]
    return JsonResponse(data)
