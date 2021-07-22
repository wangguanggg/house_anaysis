from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Qiugou
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
@login_required()
def show(request):
    return render(request, 'qiugou/show.html')

def showbypage(request):
    houses = Qiugou.objects.all()
    lis = [
        {"id": house.id, "name": house.name, "card": house.card, "phone": house.phone, "num": house.num, "money": house.money} for house in houses]
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
        beike = Qiugou.objects.get(pk=id)
        beike.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)

@login_required()
def add(request):
    if request.method == 'POST':
        house = Qiugou()
        house.name = request.POST.get("name")
        house.card = request.POST.get("card")
        house.phone = request.POST.get("phone")
        house.num = request.POST.get("num")
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
        house = Qiugou.objects.get(pk=id)
        house.name = request.POST.get("name")
        house.card = request.POST.get("card")
        house.phone = request.POST.get("phone")
        house.num = request.POST.get("num")
        house.money = request.POST.get("money")

        house.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)