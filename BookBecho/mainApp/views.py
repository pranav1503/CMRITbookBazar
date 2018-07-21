from django.conf import settings
from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from django.utils import timezone
from django.core.mail import send_mail
from .forms import SellForm, CartAdd
from .models import Items,AddCart,OrderInfo
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
import smtplib

def sendEmail(receiver,subject,msg):
    try:
        use = 'CMRITbookBazar@gmail.com'
        pswd = '1cr17ec141'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(use,pswd)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(use,receiver,message)
        server.quit()
        print("success")
    except:
        print("Failed")




class Home(ListView):
    model = Items
    template_name = 'mainApp/home.html'
    context_object_name = 'lists'

    def get_queryset(self):
        print(Items.objects.filter(semester__iexact='I').order_by('-published_date'))
        print("Reached")
        return Items.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class SellBook(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('accounts:login')
    model = Items
    form_class = SellForm
    template_name = 'mainApp/SellBook.html'
    def get_initial(self):
        initial = super(SellBook,self).get_initial()
        initial['seller'] = self.request.user
        return initial
class EditSellBook(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('accounts:login')
    model = Items
    form_class = SellForm
    template_name = 'mainApp/SellBook.html'

class DeleteSellBook(DeleteView):
    model = Items
    template_name = 'mainApp/DeleteSellBook.html'
    context_object_name = 'bookdel'
    success_url = reverse_lazy('mainApp:home')

class Cart(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('accounts:login')
    model = AddCart
    template_name = 'mainApp/cart.html'
    context_object_name = 'lists'
    def get_context_data(self,**kwargs):
        context = super(Cart, self).get_context_data(**kwargs)
        AllCosts = AddCart.objects.filter(user=self.request.user)
        temp =0
        for i in AllCosts:
             temp = temp + i.book.cost

        context['total'] = temp
        return context

    def get_queryset(self):
        return AddCart.objects.filter(user=self.request.user).order_by('-published_date')

class AddToCart(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('accounts:login')
    model = AddCart
    form_class = CartAdd
    template_name = 'mainApp/add_to_cart.html'
    def get_initial(self):
        initial = super(AddToCart,self).get_initial()
        initial['user'] = self.request.user
        initial['book'] = self.kwargs['pk']
        return initial

class RemoveFromCart(DeleteView):
    model = AddCart
    template_name = 'mainApp/remove_from_cart.html'
    context_object_name = 'Item'
    success_url = reverse_lazy('mainApp:cart')

def removeFromCart(request):
    #query = AddCart.objects.order_by(id=request.id)
    print(kwargs['id'])
    return HttpResponseRedirect(reverse('mainApp:cart'))

def emptyCart(request):
    query = AddCart.objects.filter(user=request.user)
    query.delete()
    return HttpResponseRedirect(reverse('mainApp:cart'))

def checkOut(request):
    return render(request,'mainApp/Confirm_Checkout.html')

# def Orders(request):
#     query = AddCart.objects.filter(user=request.user)
#     for i in query:
#         OrderInfo.objects.create(book=i.book,user=i.user)
#     query.delete()
#     return render(request,'mainApp/orders.html')

class ConfirmOrders(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('mainApp:login')
    model = OrderInfo
    template_name = 'mainApp/orders.html'
    context_object_name = 'order_lists'
    def get_queryset(self):
        query = AddCart.objects.filter(user=self.request.user)
        for i in query:
            OrderInfo.objects.create(book=i.book,user=i.user)
            receiver = self.request.user.email
            message = "Order details of "+i.book.book_name+". \nSeller Name: "+i.book.seller.first_name+" \nSeller Email: "+ i.book.seller.email+" \nSeller Mobile: " + "+91"+str(i.book.seller.phone.phone_number)
            sendEmail(self.request.user.email,"CMRITbookBazar:Your Orders",message)

        query.delete()
        arrangement = OrderInfo.objects.filter(user=self.request.user).order_by('-published_date')
        return arrangement


class Orders(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('mainApp:login')
    model = OrderInfo
    template_name = 'mainApp/orders.html'
    context_object_name = 'order_lists'
    def get_queryset(self):
        arrangement = OrderInfo.objects.filter(user=self.request.user).order_by('-published_date')
        return arrangement


class FinishedReceiving(DeleteView):
    model = OrderInfo
    template_name = 'mainApp/finished_order.html'
    context_object_name = 'Item'
    success_url = reverse_lazy('mainApp:orders')


class Search(ListView):
    model = Items
    template_name = 'mainApp/home.html'
    context_object_name = 'lists'

    def get_queryset(self):
        query = self.request.GET.get('q')
        branch = ""
        semester = ""
        results = ""
        try:
            branch = self.request.GET['b']
        except Exception as e:
            branch = ""
        try:
            semester = self.request.GET['s']
        except Exception as e:
            semester = ""
        print(branch," ",semester)
        if branch != "" and semester != "":
            results = Items.objects.filter((Q(book_name__icontains=query)|Q(book_author__icontains=query)) & Q(branch__icontains=branch) & Q(semester__icontains=semester))
        elif branch != "":
            results = Items.objects.filter((Q(book_name__icontains=query)|Q(book_author__icontains=query)) & Q(branch__icontains=branch))
        elif semester != "":
            results = Items.objects.filter((Q(book_name__icontains=query) | Q(book_author__icontains=query))& Q(semester__icontains=semester))


        return results
