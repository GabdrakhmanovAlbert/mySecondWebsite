# Здесь прописываем свои поля для тега html <form>

from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'css_input'}))
    # required=False - отключить обязательность ввода
    # widget=forms.TextInput(attrs={'class': 'css_input'} - приставить class="css_input" к <input>
    phone = forms.DecimalField(min_value=10000000, max_value=999999999999999)