from django.shortcuts import render, redirect
from mysql.connector import connect
from django.http import HttpResponse

car = connect(user='root', password='',
              host='127.0.0.1',
              database='student')
cu = car.cursor()


def insert(request):
    data = {'done': ''}
    if request.GET.get('submit'):
        name = request.GET['name']
        course = request.GET['course']
        e = f'insert into profile(name,coase) value("{name}","{course}")'
        cu.execute(e)
        car.commit()
        data['done'] = 'done'

    e = f'select * from profile'
    cu.execute(e)
    a = []
    for i in cu:
        ds = {'id': i[0], 'name': i[1], 'course': i[2]}
        a.append(ds)
    data['data'] = a
    print(data)

    return render(request, 'html/form.html', data)


def user_info(request):

    if request.method == 'GET' :
        username = request.GET['username']
        password = request.GET['password']
        e = f'select * from account where username="{username}" and password="{password}"'
        cu.execute(e)
        o = False
        data = {}
        for i in cu:
            print(i)
            data['username'] = i[0]
            data['password'] = i[1]
            data['email'] = i[2]
            data['phone'] = i[3]
            data['address'] = i[4   ]
            o = True
        if o:
            return render(request, 'html/en/user_info.html', data)
        else:
            return HttpResponse('username or password is not match!!!')
    return redirect(login)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        e = f'select * from account where username="{username}" and password="{password}"'
        cu.execute(e)
        o = False
        for i in cu:
            o = True
        if o:
            return redirect(f'/e/account?username={username}&password={password}')
        else:
            return HttpResponse('username or password is not match!!!')
    return render(request, 'html/en/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        if password != re_password:
            return HttpResponse('password Not match')
        e = f'insert into account values("{username}","{password}","{email}","{phone}","{address}");'
        cu.execute(e)
        car.commit()
        return redirect(login)
    return render(request, 'html/en/register.html')
