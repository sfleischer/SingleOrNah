# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .api import api
from django.shortcuts import render

# Create your views here.
def index(request):
    search = request.GET.get('q')

    #profile = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5Nzg2MTgwMl5BMl5BanBnXkFtZTcwNTA0NjcxMw@@._V1_UY317_CR0,0,214,317_AL_.jpg"
    values = api.api_entry(search, "phacks1", "penn123")

    context = {
        'search' : search,
        'top1' : values['top_three'][0][0],
        'top2' : values['top_three'][1][0],
        'top3' : values['top_three'][2][0],
    }
    return render(request, 'index.html', context)

def BlogSearchListView(request):
    search = self.request.GET.get('q')
    context = {
        'search' : search
    }
    return render(request, 'test_result.html', context)
