# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .api import api
from django.shortcuts import render
from random import randint

import numpy as np
import math

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

        if values is None or math.isnan(values['p']):
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
                'pic3' : values['top_three'][2][1]["profile_pic_url"],
                'val1' : round(np.mean(values['top_three'][0][1]["comment_sentiment"]) * 100, 2),
                'val2' : round(np.mean(values['top_three'][1][1]["comment_sentiment"]) * 100, 2),
                'val3' : round(np.mean(values['top_three'][2][1]["comment_sentiment"]) * 100, 2),
                'percent' : int(values['p'] * 100),
                'profile_pic_url' : values['target_pro_pic']
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
