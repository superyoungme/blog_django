# -*- coding:utf-8 -*-
from django.shortcuts import render

def title(request):
    context = {}
    context['title'] = 'SYM的小黑屋'
    return render(request, 'index.html', context)