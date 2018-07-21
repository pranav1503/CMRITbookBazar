from django.db import models
from django.urls import reverse
from django.utils import timezone
class Items(models.Model):
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='books')
    semester = models.CharField(max_length=5)
    branch = models.CharField(max_length=5)
    cost = models.IntegerField();
    seller = models.ForeignKey('auth.User', related_name='sellers',on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('mainApp:home')


class AddCart(models.Model):
    book = models.OneToOneField(Items,related_name='addCart',on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User',related_name='buyer',on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.book.book_name

    def get_absolute_url(self):
        return reverse('mainApp:cart')

class OrderInfo(models.Model):
    book = models.ForeignKey(Items,related_name='order',on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User',related_name='buyers',on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.book.book_name
