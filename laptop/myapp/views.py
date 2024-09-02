from django.shortcuts import render,redirect
from myapp.models import Men
from django.contrib import messages 

def index(request):
	hi = Men.objects.all()
	context = {'hi':hi}
	return render(request, 'index.html', context)

def create(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		amount = request.POST.get("amount")
		hello = Men(name=name,amount=amount)
		hello.save()
		messages.info(request,"Create Successfully")
		return redirect("/")
	return render(request,'index.html')

def updatedata(request,id):
	men = Men.objects.get(id=id)
	if request.method=='POST':
		name = request.POST["name"]
		amount = request.POST["amount"]

		men.name=name
		men.amount=amount
		men.save()
		messages.warning(request,"Update Successfully")
		return redirect("/")
	return render(request, 'update.html',{'men':men})

def delete(request,id):
	men = Men.objects.get(id=id)
	men.delete()
	messages.error(request, "Delete Successfully")
	return redirect('/')


