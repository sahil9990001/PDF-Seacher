from django.shortcuts import render,HttpResponse
from .models import Post
from .forms import DocumentForm
import PyPDF2
import re

def home(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form = DocumentForm()
    return render(request, 'home.html', {
        'form': form
    })

def search(request):
    query=request.GET['query']
    if len(query)>100:
        allposts=[]
    else:
        allposts=Post.objects.filter(PDF__icontains=query)
    params={'allposts':allposts, 'query':query}
    # print(params)
    return render(request,'search.html',params)
