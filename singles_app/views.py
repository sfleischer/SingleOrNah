# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .api import api
from django.shortcuts import render

# Create your views here.
def index(request):
    search = request.GET.get('q')
    
    if search:
        if search[0] == '@':
            search = search[1:]
        values = api.api_entry(search, "phacks3", "penn123")

        context = None

        if values is None:
            context = {
                'error' : "yes",
                'search' : None
            }
        else :
            context = {
                'error' : None,
                'search' : search,
                'top1' : values['top_three'][0][0],
                'top2' : values['top_three'][1][0],
                'top3' : values['top_three'][2][0],
            }
    else:
        context = None
    return render(request, 'index.html', context)

def BlogSearchListView(request):
    search = self.request.GET.get('q')
    context = {
        'search' : search
    }
    return render(request, 'test_result.html', context)
