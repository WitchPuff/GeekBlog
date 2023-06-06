from django.shortcuts import redirect, render
from django.db import connection
from .models import *
def query(q):
    with connection.cursor() as cur:
        cur.execute(q)
        data = cur.fetchall()
    columns = [col[0] for col in cur.description]
    keys = dict(zip(columns, data[0])).keys()
    return data, keys

# Create your views here.
def home(request):
    q = "select * from article order by post_date desc limit 3"
    data, keys = query(q=q)
    recent = {}
    for index, i in enumerate(data):
        blog = {}
        for j, k in enumerate(keys):
            if k == 'body':
                continue
            elif k == 'summary' and i[j] == None:
                blog.update({k:i[j+1][:300]})
            else:  
                blog.update({k:i[j]})
        recent.update({index:blog})
    q = "SELECT article.*, (SELECT COUNT(*) FROM kudos WHERE kudos.id = article.id) AS kudos_count FROM article WHERE article.last_update >= DATE_SUB(NOW(), INTERVAL 3 MONTH) ORDER BY kudos_count DESC LIMIT 3"
    data, keys = query(q=q)
    trend = {}
    for index, i in enumerate(data):
        blog = {}
        for j, k in enumerate(keys):
            if k == 'body':
                continue
            elif k == 'summary' and i[j] == None:
                blog.update({k:i[j+1][:300]})
            else:  
                blog.update({k:i[j]})
        trend.update({index:blog})
    return render(request, 'index.html',{'recent':recent, 'trend':trend})

def login(req):
    msg = ''
    if req.method == "POST":
        id = req.POST.get("name",None)
        pwd = req.POST.get("pwd",None)
        if not len(Auth.objects.filter(username=id)):
            msg = "Username Not Exist. Please Register first."
        elif not len(Auth.objects.filter(username=id, passwd=pwd)):
            msg = "Password Error! Please try again."
        else:
            return redirect("http://127.0.0.1:8000/blog")
    return render(req, 'login.html',{'msg':msg})


def register(req):
    msg = ''
    if req.method == "POST":
        id = req.POST.get("name",None)
        pwd = req.POST.get("pwd",None)
        if len(Auth.objects.filter(username=id)):
            msg = "Username Already Exists. Please Try with Another Name or Login."
        elif len(id) > 15 or len(id) < 3:
            msg = "The Length of Your Username should be >= 3 and <= 15! Please Try with Another Name."
        elif len(pwd) > 15 or len(pwd) < 6:
            msg = "The Length of Your Password should be >= 6 and <= 15! Please try again."
        else:
            Auth.objects.create(username=id, passwd=pwd)
            msg = f"Username {id} successfully registered! You could login now!"
            return redirect("http://127.0.0.1:8000/login")
    return render(req, 'register.html',{'msg':msg})

def blog(req):
    recent = {}
    q = "select article.*, (select count(*) from kudos where article.id = kudos.id) as kudos_cnt, (select count(*) from comment where comment.id=article.id) as comment_cnt from article order by last_update desc limit 20"
    data, keys = query(q)
    for index, i in enumerate(data):
        blog = {}
        for j, k in enumerate(keys):
            if k == 'body':
                continue
            elif k == 'summary' and i[j] == None:
                blog.update({k:i[j+1][:300]})
            elif k == 'tags' and i[j] != None:
                blog.update({k:i[j].split(sep=',')})
                print(i[j])
                print(i[j].split(sep=','))
            else:  
                blog.update({k:i[j]})
        recent.update({index:blog})
    return render(req, 'blog.html', {'recent': recent, 'num_page':len(recent), 'page':1})