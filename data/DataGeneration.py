databases = ('auth','profile','constant','article','comment','kudos')
with open('data/relations.sql','a') as f:
    for db in databases:
        f.write(f'delete from {db};\n')

names = []
with open('data/name_list.txt','r') as f:
    for i in f.readlines():
        names.append(i.replace('\n',''))
categories = []
with open('data/category_list.txt','r') as f:
    for i in f.readlines():
        i = i.replace('\n','')
        if len(i)>1 and i not in categories:
            categories.append(i)
            with open('data/relations.sql','a') as f:
                f.write(f'insert into constant values ("{categories[-1]}");\n')
    print('Categories generated!')
tags = []
with open('data/tag_list.txt','r') as f:
    for i in f.readlines():
        i = i.replace('\n','')
        if len(i)>1 and i not in tags:
            tags.append(i)
import random
import time

a1=(2021,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(2024,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）
a3=(2025,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）

start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳
newend=time.mktime(a3)      #生成结束时间戳

def random_time(a,b):
    t=random.randint(a,b)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    date=time.strftime("%Y-%m-%d %H:%M:%S",date_touple)  #将时间元组转成格式化字符串
    return t, date

import string
def random_account(length):
    characters = string.ascii_letters + string.digits
    # 生成指定长度的随机字符串
    username = ''.join(random.choice(characters) for _ in range(length))
    passwd = ''.join(random.choice(characters) for _ in range(length))
    return username, passwd
accounts = []
def generate_account(k):
    for i in range(k):
        with open('data/relations.sql','a') as f:
            accounts.append(random_account(6))
            f.write(f'insert into auth values {accounts[-1]};\n')
            f.write(f'insert into profile (username) values ("{accounts[-1][0]}");\n')
    print('Accounts generated!')

def generate_article(k):
    for i in range(k):
        username = random.choice(accounts)[0]
        title = "Lorem ipsum"
        category = random.choice(categories)
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pulvinar nunc id risus lacinia ultrices. Sed euismod massa ac lacus iaculis, nec auctor justo tincidunt. Fusce placerat mauris et ullamcorper consectetur. Aliquam fringilla maximus semper. Nullam vulputate massa non libero volutpat, vel dictum ex tempus. Suspendisse vitae justo nec est molestie iaculis sed et purus. Nam fringilla odio sit amet felis efficitur, eu sollicitudin dui luctus. Sed mollis nibh in risus scelerisque, id rutrum risus semper."
        post_date = last_update = random_time(start, end)[1]
        tag = ",".join(random.choices(tags,k=random.randint(0,4)))
        article = (username, title, category, tag, body, post_date, last_update)
        with open('data/relations.sql','a') as f:
            f.write(f'insert into article (username, title, category, tags, body, post_date, last_update) VALUES {article};\n')
    print('Articles generated!')
    
def generate_kudos_comment(k):
    for i in range(k):
        username = random.choice(accounts)[0]
        id = random.randint(1, k)
        content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pulvinar nunc id risus lacinia ultrices."
        with open('data/relations.sql','a') as f:
            f.write(f'insert into comment VALUES {(id, username, content,random_time(end, newend)[1])};\n')
            f.write(f'insert into kudos VALUES {(id, username)};\n')
    print('Kudos and comments generated!')


def generate():
    generate_account(500)
    generate_article(1000)
    generate_kudos_comment(800)

generate()

            