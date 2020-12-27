from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from login.models import ActiveInvite
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required
def myprofile(request):
    profile = ActiveInvite.objects.filter(user=request.user)
    return render(request, 'myprofile/myprofile_page.html', { 'profile': profile})


@login_required
def userlogout(request):
    logout(request)
    return redirect('login')


def profileedit(request):
    activeinvite = ActiveInvite.objects.get(user=request.user)
    form = forms.MyProfile(initial={'first_name': activeinvite.first_name, 'middle_name': activeinvite.middle_name, 'last_name': activeinvite.last_name, 'nick_name': activeinvite.nick_name, 'mobile1': activeinvite.mobile1, 'mobile2': activeinvite.mobile2, 'whatsapp': activeinvite.whatsapp, 'email': activeinvite.email, 'father': activeinvite.father, 'mother': activeinvite.mother, 'address': activeinvite.address, 'temp_address': activeinvite.temp_address, 'parish': activeinvite.parish, 'dob': activeinvite.dob, 'blood': activeinvite.blood, 'occupation': activeinvite.occupation, 'company': activeinvite.company, 'occupation_place': activeinvite.occupation_place, 'spouse_name': activeinvite.spouse_name, 'spouse_father': activeinvite.spouse_father, 'spouse_mother': activeinvite.spouse_mother, 'wedding_date': activeinvite.wedding_date})
    form2 =forms.UpdatePass()
    now = datetime.datetime.now()
    now_full = now.strftime("%Y-%m-%d")
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        nick_name = request.POST.get('nick_name')
        mobile1 = request.POST.get('mobile1')
        mobile2 = request.POST.get('mobile2')
        whatsapp = request.POST.get('whatsapp')
        email = request.POST.get('email')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        address = request.POST.get('address')
        temp_address = request.POST.get('temp_address')
        parish = request.POST.get('parish')
        dob = request.POST.get('dob')
        blood = request.POST.get('blood')
        occupation = request.POST.get('occupation')
        company = request.POST.get('company')
        occupation_place = request.POST.get('occupation_pace')
        spouse_name = request.POST.get('spouse_name')
        spouse_father = request.POST.get('spouse_father')
        spouse_mother = request.POST.get('spouse_mother')
        wedding_date = request.POST.get('wedding_date')
        #children_number = request.POST.get('children_number')
        #child1 = request.POST.get('child1')
        #child2 = request.POST.get('child2')
        #child3 = request.POST.get('child3')
        #child4 = request.POST.get('child4')
        #counter = request.POST.get('counter')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username != None:
            user = User.objects.get(username__exact=request.user)
            user.username = username
            user.set_password(password)
            user.save()
            activeinvite = ActiveInvite(user=request.user)
            activeinvite.save()
            return redirect('login')
        else:
            activeinvite = ActiveInvite.objects.get(user=request.user)
            activeinvite.first_name = first_name
            activeinvite.middle_name = middle_name
            activeinvite.last_name = last_name
            activeinvite.nick_name = nick_name
            activeinvite.mobile1 = mobile1
            activeinvite.mobile2 = mobile2
            activeinvite.whatsapp = whatsapp
            activeinvite.email = email
            activeinvite.father = father
            activeinvite.mother = mother
            activeinvite.address = address
            activeinvite.temp_address = temp_address
            activeinvite.parish = parish
            activeinvite.dob = dob
            activeinvite.blood = blood
            activeinvite.occupation = occupation
            activeinvite.company = company
            activeinvite.occupation_place = occupation_place
            activeinvite.spouse_name = spouse_name
            activeinvite.spouse_father = spouse_father
            activeinvite.spouse_mother = spouse_mother
            activeinvite.wedding_date = wedding_date
            ActiveInvite.date_edited = now_full
            #activeinvite.children_number = children_number
            #activeinvite.child1 = child1
            #activeinvite.child2 = child2
            #activeinvite.child3 = child3
            #activeinvite.child4 = child4
            activeinvite.save()
            return redirect('myprofile')
    profile = ActiveInvite.objects.filter(user=request.user)

    return render(request,'myprofile/myprofile_edit.html', {'form': form, 'form2': form2, 'profile': profile})



