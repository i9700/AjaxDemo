from django.shortcuts import render, HttpResponse
from .models import User
from django.http import JsonResponse


# Create your views here.

def reg(request):
    return render(request, "reg.html")


def username_auth(request):
    print(request.POST)
    res = {"exist": False, "msg": ""}
    # 获取客户端数据：用户名
    username = request.POST.get("username")
    data = User.objects.filter(name=username)
    # 校验用户是否存在
    if data:
        res["exist"] = True
        res["msg"] = "该用户已存在"
    return JsonResponse(res)


def add(request):
    c1 = request.POST.get("c1")
    c2 = request.POST.get("c2")
    c3 = int(c1) + int(c2)
    res = JsonResponse(c3, safe=False)
    res["Access-Control-Allow-Origin"] = "*"
    return res
