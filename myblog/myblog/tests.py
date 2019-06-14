# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.test import TestCase
from blogapp.models import Article

# Create your tests here.
def addArticle(request):
    test1 = Article(title = '第一篇文章')
    test1.save()
    return HttpResponse("<p>数据添加成功</p>")