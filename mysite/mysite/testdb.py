from django.http import HttpResponse
 
from blog.models import Movie
 
# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    list=Movie.obj
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")