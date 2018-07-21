from django import forms
from .models import Items,AddCart
SEM_CHOICES = [
    ('I/II','I/II'),('III','III'),('IV','IV'),('V','V'),('VI','VI'),('VII','VII'),('VIII','VIII'),
]

BRANCH_CHOICES = [
    ('chem','Chemistry Cycle'),('phy','Physics Cycle'),('EC','EC'),('CS','CS'),('ME','ME'),('IS','IS'),('TC','TC'),('CIV','CIV'),('EEE','EEE'),
]

class SellForm(forms.ModelForm):
    cost = forms.IntegerField(label='Cost ₹')
    class Meta:
        model = Items
        fields = ('book_name','book_author','book_image','semester','branch','cost','seller')
        widgets = {
            'book_name' : forms.TextInput(attrs={'class':'form-control'}),
            'book_author' : forms.TextInput(attrs={'class':'form-control'}),
            'semester' : forms.Select(choices=SEM_CHOICES),
            'branch' : forms.Select(choices=BRANCH_CHOICES),
            'seller' : forms.HiddenInput(),
        }

class CartAdd(forms.ModelForm):
    class Meta:
        model = AddCart
        fields = ('book','user')
        widgets = {
            'book' : forms.HiddenInput(),
            'user' : forms.HiddenInput(),
        }
