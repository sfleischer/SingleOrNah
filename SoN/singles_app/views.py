# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
	search = request.GET.get('q')

	context = {
		'search' : search
	}
	return render(request, 'index.html', context)

def BlogSearchListView(request):
	search = self.request.GET.get('q')
	context = {
		'search' : search
	}
	return render(request, 'test_result.html', context)
