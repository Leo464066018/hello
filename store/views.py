from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from .models import Item
from .forms import LoginForm, OperateForm
# Create your views here.


def show(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'store/list.html', context)


def search(request):
    name = request.POST['search_input']
    items = Item.objects.filter(name__icontains=name)
    context = {
        'items': items,
        'name': name,
    }
    return render(request, 'store/search.html', context)


def do_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request, user)
            return redirect(request.GET.get('from', reverse('show')))
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }
    return render(request, 'store/login.html', context)


def do_operate(request):
    if request.method == 'POST':
        pass
    else:
        operate_form = OperateForm()

    context = {
        'operate_form': operate_form,
    }
    return render(request, 'store/operate.html', context)
