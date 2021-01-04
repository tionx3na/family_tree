from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import FamilyEvent

# Create your views here.

@login_required
def events(request):
    event = FamilyEvent.objects.all()
    return render(request, 'familyevents/event_page.html', {'event': event})

@login_required
def addevent(request):
    form = forms.Event()
    if request.method == 'POST':
        pro_pic = request.FILES.getlist('thumbnail')
        title = request.POST.get('title')
        date = request.POST.get('date')
        content = request.POST.get('content')
        mod_date = date.split("-")
        month = mod_date[1]
        year = mod_date[0]
        day = mod_date[2]
        author = request.user
        month_name = " "
        if(month == "01"):
            month_name = "January"

        elif (month == "02"):
            month_name = "February"

        elif (month == "03"):
            month_name = "March"

        elif (month == "04"):
            month_name = "April"

        elif (month == "05"):
            month_name = "May"

        elif (month == "06"):
            month_name = "June"

        elif (month == "07"):
            month_name = "July"

        elif (month == "08"):
            month_name = "August"

        elif (month == "09"):
            month_name = "September"

        elif (month == "10"):
            month_name = "October"

        elif (month == "11"):
            month_name = "November"

        elif (month == "12"):
            month_name = "December"

        familyevent = FamilyEvent()
        familyevent.author = author
        familyevent.title = title
        familyevent.date = date
        familyevent.day = day
        familyevent.month = month_name
        familyevent.year = year
        familyevent.content = content
        for pic in pro_pic:
            print(pro_pic)
            familyevent.pic = pic
            familyevent.save()

        return redirect('events')


    return render(request, 'familyevents/addevent_page.html', {'form': form})
