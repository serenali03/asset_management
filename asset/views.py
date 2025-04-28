from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login

#import this so you can't access the dashboard unless you're logged in
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, InventoryItemForm
from .models import InventoryItem, Category

# API imports
from rest_framework import generics
from .serializers import ItemSerializer


from rest_framework import viewsets
from .models import InventoryItem
from .serializers import ItemSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = ItemSerializer


#generic home page class, using django template

#inherit from TemplateView class
class Index(TemplateView):
    template_name = 'asset/index.html'

class Dashboard(LoginRequiredMixin, View):
	def get(self, request):
		#before returning to template, get the items for the logged in user and order them by the user id
		items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')

		#query set of items saved in dictionary
		return render(request, 'asset/dashboard.html', {'items':items})
	
class SignUpView(View):
	def get(self, request):
		form = UserRegisterForm()
		return render(request, 'asset/signup.html', {'form': form})

	def post(self, request):
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			form.save()
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1']
			)

			login(request, user)
			return redirect('index')

		return render(request, 'asset/signup.html', {'form': form})
            
class AddItem(LoginRequiredMixin, CreateView):
	model = InventoryItem
	form_class = InventoryItemForm
	template_name = 'asset/item_form.html'
	success_url = reverse_lazy('dashboard') #redirects us back to dashboard page

	#get categories data so user can select a category for their new item
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context
	
	#overwrite form valid function
	def form_valid(self, form):
		
		#we want to set the user as the logged in user by default when they create a new item
		form.instance.user = self.request.user
		return super().form_valid(form)
	
class EditItem(LoginRequiredMixin, UpdateView):
	model = InventoryItem
	form_class = InventoryItemForm
	template_name = 'asset/item_form.html'
	success_url = reverse_lazy('dashboard')

class DeleteItem(LoginRequiredMixin, DeleteView):
	model = InventoryItem
	template_name = 'asset/delete_item.html'
	success_url = reverse_lazy('dashboard')

	#rename default name to item to be consistent with 'dashboard.html'
	context_object_name = 'item'

# API views for the InventoryItem model
class AssetListCreateAPIView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = ItemSerializer