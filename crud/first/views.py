from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request,'first/one.html')
    
    
def two(request):
    return render(request,'first/two.html')


   
def main(request):
    return render(request,'first/main.html')
   
def myprofile(request):
    return render(request,'first/myprofile.html')


def edit(request):
    return render(request,'first/edit.html')
