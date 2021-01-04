from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from login.models import ActiveInvite
from blog.models import Post

# Create your views here.

@login_required
def search(requests, param):
    arg = param
    mail = param
    first_name = ''
    middle_name = ''
    last_name = ''
    mobile = ''
    email = ''
    father = ''
    mother = ''
    address = ''
    occupation = ''
    wife = ''
    if requests.method == 'POST':
        s = requests.POST.get('search')
        arg = s
        mail = s
        arg = arg.split()
        for i in arg:
            arg = i.capitalize()
            print(arg)
            first_name = ActiveInvite.objects.filter(first_name__icontains=arg)
            middle_name = ActiveInvite.objects.filter(middle_name=arg)
            last_name = ActiveInvite.objects.filter(last_name=arg)
            mobile = ActiveInvite.objects.filter(mobile1=arg) | ActiveInvite.objects.filter(mobile2=arg)
            email = ActiveInvite.objects.filter(email=mail)
            father = ActiveInvite.objects.filter(father__icontains=arg)
            mother = ActiveInvite.objects.filter(mother__icontains=arg)
            address = ActiveInvite.objects.filter(address__icontains=arg)
            occupation = ActiveInvite.objects.filter(occupation__icontains=arg)
            wife = ActiveInvite.objects.filter(spouse_name__icontains=arg)
    arg = arg.split()
    for i in arg:
        arg = i.capitalize()
        print(arg)
        first_name = ActiveInvite.objects.filter(first_name__icontains=arg)
        middle_name = ActiveInvite.objects.filter(middle_name=arg)
        last_name = ActiveInvite.objects.filter(last_name=arg)
        mobile = ActiveInvite.objects.filter(mobile1=arg) | ActiveInvite.objects.filter(mobile2=arg)
        email = ActiveInvite.objects.filter(email=mail)
        father = ActiveInvite.objects.filter(father__icontains=arg)
        mother = ActiveInvite.objects.filter(mother__icontains=arg)
        address = ActiveInvite.objects.filter(address__icontains=arg)
        occupation = ActiveInvite.objects.filter(occupation__icontains=arg)
        wife = ActiveInvite.objects.filter(spouse_name__icontains=arg)
    context = {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name,'arg': arg, 'mobile': mobile, 'email': email, 'father': father, 'mother': mother, 'address': address, 'occupation': occupation, 'wife': wife }
    return render(requests, 'search/search_page.html', context)


@login_required
def userpage(requests, param):
    user = ActiveInvite.objects.filter(id=param)

    return render(requests, 'search/search_userpage.html', {'user': user})
