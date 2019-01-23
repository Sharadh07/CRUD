from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()

            return render(request, 'createpost.html')

    else:
        return render(request, 'createpost.html')

def show(request):
	user = Post.objects.all()
	return render(request,"show.html",{'user':user})
	

def destroy(request):
	if request.method=='POST':
		post = Post()
		post.id = request.POST.get('id')
		post.delete()
		return HttpResponse('deleted')
	else:
		return render(request, 'deletepost.html')
		
def update(request):  
	if request.method=='POST':
		post = Post()
		post.id = request.POST.get('id')
		post.title = request.POST.get('title')
		post.content = request.POST.get('content')
		post.save()  
		return HttpResponse('updated') 
	else:
		return render(request, 'edit.html')