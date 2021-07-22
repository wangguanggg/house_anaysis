from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Qiuzu
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
@login_required()
def show(request):
    return render(request, 'qiuzu/show.html')

@login_required()
def showbypage(request):
    houses = Qiuzu.objects.all()
    lis = [
        {"id": house.id, "name": house.name, "card": house.card, "phone": house.phone, "num": house.num, "money": house.money, "time": house.time} for house in houses]
    page_index = request.GET.get('page')
    page_limit = request.GET.get('limit')
    paginator = Paginator(lis, page_limit)
    data = paginator.page(int(page_index))
    house_info = [x for x in data]
    houses = {"code": 0, "msg": "", "count": houses.count(), "data": house_info}
    return JsonResponse(houses)

@login_required()
def delete(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        beike = Qiuzu.objects.get(pk=id)
        beike.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)

@login_required()
def add(request):
    if request.method == 'POST':
        house = Qiuzu()
        house.name = request.POST.get("name")
        house.card = request.POST.get("card")
        house.phone = request.POST.get("phone")
        house.num = request.POST.get("num")
        house.time = request.POST.get("time")
        house.money = request.POST.get("money")
        house.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)

@login_required()
def modify(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        house = Qiuzu.objects.get(pk=id)
        house.name = request.POST.get("name")
        house.card = request.POST.get("card")
        house.phone = request.POST.get("phone")
        house.num = request.POST.get("num")
        house.time = request.POST.get("time")
        house.money = request.POST.get("money")

        house.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)