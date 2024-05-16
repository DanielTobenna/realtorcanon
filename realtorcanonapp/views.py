from django.shortcuts import render, redirect

from django.core.mail import BadHeaderError, send_mail

from django.http import HttpResponse

from django.contrib import messages

from .forms import *

from .models import *

# Create your views here.

def home(request):
	return render(request, 'realtorcanonapp/home.html')

def about(request):
	return render(request, 'realtorcanonapp/about.html')

def contact(request):
	if request.method == 'GET':
		form= ContactForm()
	else:
		form = ContactForm(request.POST or None)
		if form.is_valid():
			name= form.cleaned_data['name']
			email= form.cleaned_data['email']
			message= form.cleaned_data['message']
			print(name)
		try:
			send_mail("RealtorCanon website test", "User with name {} and email {} has sent a message saying: {}".format(name, email, message),email, ['daniel@bigtchub.com'])
			print('Message Sent')
		except:
			print('Message not sent')
			messages.error(request, 'Message Not sent, Try again later.')
		messages.success(request, 'Your message has been sent successfully')
	context={'form':form}
	return render(request, 'realtorcanonapp/contact.html', context)

def suscribe(request):
	return render(request, 'realtorcanonapp/suscribe.html')

def property(request):
	properties= Property.objects.all()
	context={'properties':properties, }
	return render(request, 'realtorcanonapp/property.html', context)

def propertyInfo(request, pk):
	property_info = Property.objects.get(id=pk)
	property_id = property_info.id
	property_details= Property.objects.filter(id=property_id)
	for i in property_details:
		property_images= i.propertyimage_set.all()
	list_date= property_info.list_date
	title= property_info.title
	description= property_info.description
	price= property_info.price
	location= property_info.location
	bedrooms= property_info.bedrooms
	bathrooms= property_info.bathrooms
	sqft= property_info.sqft
	is_published= property_info.is_published
	category= property_info.category
	features= property_info.features
	status= property_info.status
	agent_id= property_info.agent.id
	print(agent_id)
	context={'property_info': property_info, 'property_details': property_details, 'property_images': property_images, 
	'title':title, 'list_date':list_date, 'description':description, 'price':price, 'location':location, 'bedrooms': bedrooms,
	'bathrooms':bathrooms, 'sqft':sqft, 'is_published':is_published, 'category':category, 'features':features, 'status':status, 
	'agent_id':agent_id  }
	return render(request, 'realtorcanonapp/propertyInfo.html', context)


def propertyAgent(request, pk):
	agent_info = Agent.objects.get(id=pk)
	agent_name= agent_info.name
	agent_pic= agent_info.photo
	agent_date= agent_info.created
	context={'agent_name':agent_name, 'agent_pic':agent_pic, 'agent_date':agent_date}
	return render(request, 'realtorcanonapp/propertyAgent.html', context)
