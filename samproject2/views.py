from django.shortcuts import render, redirect
from .models import People


# function for index page

def indexpage(request):
    data = People.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


# Function to delete data
def deleteData(request, id):
    d = People.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


# Function to update our records
def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        city = request.POST.get('city')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit_data = People.objects.get(id=id)
        edit_data.name = name
        edit_data.email = email
        edit_data.age = age
        edit_data.phone = phone
        edit_data.country = country
        edit_data.city = city
        edit_data.gender = gender
        edit_data.save()

        return redirect("/")

    dta = People.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        country = request.POST.get('country')
        city = request.POST.get('city')
        gender = request.POST.get('gender')

        query = People.objects.create(name=name, email=email, country=country, city=city, phone=phone, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")
