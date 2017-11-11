# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
	search = request.GET.get('q')

	profile = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5Nzg2MTgwMl5BMl5BanBnXkFtZTcwNTA0NjcxMw@@._V1_UY317_CR0,0,214,317_AL_.jpg"
	context = {
		'search' : search,
		'profile': profile
	}
	return render(request, 'index.html', context)

def BlogSearchListView(request):
	search = self.request.GET.get('q')
	context = {
		'search' : search
	}
	return render(request, 'test_result.html', context)
