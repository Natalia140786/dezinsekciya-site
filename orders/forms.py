from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'message', 'service', 'area', 'preferred_time']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
            'preferred_time': forms.TextInput(attrs={'placeholder': 'например, завтра после 14:00'}),
        }