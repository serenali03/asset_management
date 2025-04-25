from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, InventoryItem
from .models import User

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

#model form is built in class that allows to use inventoryitem model
class InventoryItemForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
	class Meta:
		model = InventoryItem

		#fields we want in the inventory item form
		fields = ['name', 'category', 'description', 'artist', 'dimension', 'image', 'purchase_date']