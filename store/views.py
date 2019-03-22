from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Item, Operation, PostManage, Box
from .forms import LoginForm, OperateForm, PostForm
# Create your views here.


def show(request):
    items = Item.objects.all()
    postmanage_sends = PostManage.objects.filter(post_type='send')
    postmanage_receives = PostManage.objects.filter(post_type='receive')
    context = {
        'items': items,
        'postmanage_sends': postmanage_sends,
        'postmanage_receives': postmanage_receives,
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
            note = operate_form.cleaned_data['note']
            item = Item.objects.get(name=operate_item)
            item_qty = item.qty
            if operate == 'plus':
                item.qty += num
                item.save()
                operation = {
                    'item': operate_item,
                    'operate': operate,
                    'num': num,
                    'note': note,
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
                        'note': note,
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

    video = {
        '视频服务器外壳': 1,
        '大华电源适配器': 1,
        '内置型4G天线': 1,
        '4G模块': 1,
        'RF射频SMA-KKY母对母转接头': 2,
        '劲霸18650锂电池': 2,
        '视频服务器主板固定板': 1,
        '视频服务器摄像头固定板': 1,
        '电池盒': 1,
        '主板(有探针)': 1,
        'CR1220锂电池': 1,
        '树莓派': 1,
        '树莓派摄像头': 2,
        '2.4G小辣椒wifi天线': 2,
        '射频线SMA公针-SMA公针15cm': 2,
        '自攻螺丝M2.6*6': 4,
        '六角铜柱(双通M3*10)': 6,
        '六角铜柱(单头螺栓M3*18+4)': 6,
        '六角螺母M2': 8,
        '平头螺丝M2*10': 8,
        '尼龙双通六角柱M2*6': 8,
        '12VDC转2pin电源线': 1
    }

    wifi = {
        '4G模块': 1,
        '劲霸18650锂电池': 2,
        '电池盒': 1,
        '主板(有探针)': 1,
        'CR1220锂电池': 1,
        '树莓派': 1,
        '射频线SMA公针-SMA公针40cm': 1,
        'RF射频SMA-KKY母对母转接头': 1,
        '2.4G小辣椒wifi天线': 1
    }

    posts = PostManage.objects.all()
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_num = post_form.cleaned_data['post_num']
            post_type = post_form.cleaned_data['post_type']
            server_type = post_form.cleaned_data['server_type']
            server_num = post_form.cleaned_data['server_num']
            note_text = post_form.cleaned_data['note_text']
            post_date = post_form.cleaned_data['post_date']
            post_manage = PostManage()
            post_manage.post_num = post_num
            post_manage.post_type = post_type
            post_manage.server_type = server_type
            post_manage.server_num = server_num
            post_manage.note_text = note_text
            post_manage.post_date = post_date
            post_manage.save()
            if post_type == 'send':
                if server_type == 'video':
                    for key in video.keys():
                        reduce_item(key, video[key], server_num)
                else:
                    for key in wifi.keys():
                        reduce_item(key, wifi[key], server_num)
            else:
                if server_type == 'video':
                    for key in video.keys():
                        add_item(key, video[key], server_num)
                else:
                    for key in wifi.keys():
                        add_item(key, wifi[key], server_num)

    else:
        post_form = PostForm()
    
    context = {
        'posts': posts,
        'post_form': post_form,
    }

    return render(request, 'store/postmanage.html', context)


# 查询配件，减去配件数量
def reduce_item(name, num, server_num):
    item = Item.objects.get(name=name)
    item.qty -= num * server_num
    item.save(update_fields=['qty'])


# 查询配件，增加配件数量
def add_item(name, num, server_num):
    item = Item.objects.get(name=name)
    item.qty += num * server_num
    item.save(update_fields=['qty'])


def card_record(request):
    boxes = Box.objects.all()
    context = {
        'boxes': boxes,
    }
    return render(request, 'store/card.html', context)
