from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import UpdateView
from .models import UserInfoModel
from .forms import UserForm,PhoneForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserInfoModel

def Register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        phone_form = PhoneForm(data=request.POST)

        if user_form.is_valid() and phone_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            phone = phone_form.save(commit=False)
            phone.user = user
            phone.save()
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        user_form = UserForm()
        phone_form = PhoneForm()
    return render(request,'accounts/register.html',{'user':user_form,'phone':phone_form,'registered':registered})

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainApp:home'))


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,"\t",password)
        user =  authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('mainApp:home'))
            else:
                return render(request,'accounts/login.html',{'message':'Sorry, your account is not active.'})
        else:

            return render(request,'accounts/login.html',{'message':'Entered username or password incorrect.'})
    return render(request,'accounts/login.html')


@login_required
def Profile(request):
    return render(request,'accounts/profile.html')


class UpdateProfile(UpdateView):
    model = UserInfoModel
    template_name = 'accounts/profile_edit.html'
    fields = ['describe', 'bday']

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('hot'))
