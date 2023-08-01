from django.shortcuts import render, redirect
from .models import People


# function for index page

def indexpage(request):
    data = People.objects.all()
    context = {"data": data}
    return render(request, "home.html", context)


# Function to delete data
def deleteData(request, id):
    d = People.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "home.html")


# Function to update our records
def updateData(request, id):
    if request.method == "POST":
        model = request.POST.get('model')
        location = request.POST.get('location')
        year = request.POST.get('year')
        cartype = request.POST.get('cartype')
        price = request.POST.get('price')

        edit_data = People.objects.get(id=id)
        edit_data.model = model
        edit_data.location = location
        edit_data.year = year
        edit_data.cartype = cartype
        edit_data.price = price

        edit_data.save()

        return redirect("/")

    dta = People.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)


def insertData(request):
    if request.method == "POST":
        model = request.POST.get('model')
        location = request.POST.get('location')
        year = request.POST.get('year')
        cartype = request.POST.get('cartype')
        price = request.POST.get('price')

        query = People.objects.create(model=model, location=location, year=year, cartype=cartype, price=price)
        query.save()
        return redirect("/")
    return render(request, "home.html")
