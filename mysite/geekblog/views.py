from django.shortcuts import redirect, render
from django.db import connection
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article
from django.db.models import Count
def query(q):
    with connection.cursor() as cur:
        cur.execute(q)
        data = cur.fetchall()
    columns = [col[0] for col in cur.description]
    keys = dict(zip(columns, data[0])).keys()
    return data, keys

def structuralize(data, keys):
    recent = {}
    for index, i in enumerate(data):
        blog = {}
        for j, k in enumerate(keys):
            if k == 'body':
                continue
            elif k == 'summary' and i[j] == None:
                blog.update({k:i[j+1][:300]})
            elif k == 'tags' and i[j] != None:
                blog.update({k:i[j].split(sep=',')})
            else:  
                blog.update({k:i[j]})
        recent.update({index:blog})
    return recent

# Create your views here.
def home(request):
    q = "select * from article order by post_date desc limit 3"
    data, keys = query(q=q)
    recent = structuralize(data, keys)
    q = "SELECT article.*, (SELECT COUNT(*) FROM kudos WHERE kudos.id = article.id) AS kudos_count FROM article WHERE article.last_update >= DATE_SUB(NOW(), INTERVAL 3 MONTH) ORDER BY kudos_count DESC LIMIT 3"
    data, keys = query(q=q)
    trend = structuralize(data, keys)
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
            req.session["logined"] = 1
            req.session["username"] = id
            return redirect('blog')
            # return redirect(f"http://127.0.0.1:8000/blog/latest?username={id}")
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

def blog(request):
    page = int(request.GET.get('page',1))
    order = (request.GET.get('order','latest'))
    if order == 'trending':
        q = "select article.*, (select count(*) from kudos where article.id = kudos.id) as kudos_cnt, (select count(*) from comment where comment.id=article.id) as comment_cnt from article order by last_update"
    else:
        order = 'latest'
        q = "select article.*, (select count(*) from kudos where article.id = kudos.id) as kudos_cnt, (select count(*) from comment where comment.id=article.id) as comment_cnt from article order by kudos_cnt, comment_cnt, last_update"
    num_page = len(Article.objects.filter()) // 20
    if page == None or page < 1 or not isinstance(page, int):
        page = 1
    elif page > num_page:
        page = num_page
    data, keys = query(q)
    paginator = Paginator(data, 20)
    cur = paginator.page(page).object_list
    recent = structuralize(cur, keys)
    logined = 1 if "logined" in request.session.keys() else 0
    username = "Login" if not logined else request.session["username"]
    context = {'recent': recent,'pages': range(max(1, page-9), min(page+9, num_page)), 
               'num_page':num_page,
               'page': page, 'order': order,
               'logined': logined, 
               'username': username}
    return render(request, 'blog.html', context)

def flush(req):
    req.session.flush()
    return redirect('blog')
    