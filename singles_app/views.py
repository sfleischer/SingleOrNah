# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .api import api
from django.shortcuts import render
from random import randint

# Create your views here.

def index(request):
    search = request.GET.get('q')
    keys = ["phacks1", "phacks2", "phacks3", "phacks4", "wae3wae3", "singleornaw1154"]
    values = ["penn123", "penn123", "penn123", "penn123", "phacks", "phacks"]
    
    if search:
        if search[0] == '@':
            search = search[1:]
        r = randint(0, len(keys)-1)
        values = api.api_entry(search, keys[r], values[r])

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
                'pic1' : values['top_three'][0][1]["profile_pic_url"],
                'pic2' : values['top_three'][1][1]["profile_pic_url"],
                'pic3' : values['top_three'][2][1]["profile_pic_url"]
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
