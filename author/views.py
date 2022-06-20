from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm
from django.contrib import messages

# Create your views here.
def index(request):  
    authors = Author.objects.all() 
    params = {
        'authors': authors,
    }
    return render(request, 'author/index.html', params)

def create(request):
    if (request.method == 'POST'):
        name = request.POST['name']
        author = Author(name=name)
        author.save()
        messages.success(request,"Author created successfully")
        return redirect('index')
    else:
        params = {
            'form': AuthorForm(),
        }
        return render(request, 'author/create.html',params)

def detail(request, author_id):
    author = Author.objects.get(id=author_id)
    params = {
        'author': author,
    }
    return render(request, 'author/detail.html', params)

def edit(request, author_id):
    author = Author.objects.get(id = author_id)
    if(request.method == 'POST'):
        author.name = request.POST['name']
        author.save()
        messages.success(request,"Author updated successfully")
        return redirect('detail', author_id)
    else:
        form = AuthorForm(initial={
            'name':author.name,
        })
        params = {
            'author': author,
            'form': form
            }
        return render(request, 'author/edit.html', params)

def delete(request, author_id):
    author = Author.objects.get(id=author_id)
    if(request.method == 'POST'):
        author.delete()
        return redirect('index')
    else:
        params = {
            'author': author,
        }
        return render(request, 'author/delete.html', params)
 

    
    