from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import F
from django.contrib.auth.decorators import login_required
from .models import Item, Operation, PostManage
from .forms import LoginForm, OperateForm, PostForm
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
    next_to = request.GET.get('next', False)
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request, user)
            if next_to:
                return redirect(next_to)
            return redirect(request.GET.get('from', reverse('show')))
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }
    return render(request, 'store/login.html', context)


@login_required
def do_operate(request):
    operations = Operation.objects.all()[:10]
    if request.method == 'POST':
        operate_form = OperateForm(request.POST)
        if operate_form.is_valid():
            operate_item = operate_form.cleaned_data['item']
            operate = operate_form.cleaned_data['operate']
            num = operate_form.cleaned_data['num']
            item = Item.objects.get(name=operate_item)
            item_qty = item.qty
            if operate == 'plus':
                item.qty += num
                item.save()
                operation = {
                    'item': operate_item,
                    'operate': operate,
                    'num': num,
                }
                Operation.objects.create(**operation)
            else:
                if num > item_qty:
                    messages.warning(request, '减少数量不能大于库存')
                else:
                    item.qty -= num
                    item.save()
                    operation = {
                        'item': operate_item,
                        'operate': operate,
                        'num': num,
                    }
                    Operation.objects.create(**operation)
    else:
        operate_form = OperateForm()

    context = {
        'operations': operations,
        'operate_form': operate_form,
    }

    return render(request, 'store/operate.html', context)


@login_required
def do_post(request):
    posts = PostManage.objects.all()
    if request.method == 'POST':
        post_form = PostForm(request.POST)

    else:
        post_form = PostForm()
    
    context = {
        'posts': posts,
        'post_form': post_form,
    }

    return render(request, 'store/postmanage.html', context)
