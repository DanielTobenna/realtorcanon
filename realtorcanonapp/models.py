from django.db import models

# Create your models here.

class Agent(models.Model):
	name= models.CharField(max_length=100, null=True, blank=True)
	email= models.EmailField( null=True, blank=True)
	phone= models.CharField(max_length=100, null=True, blank=True)
	bio= models.CharField(max_length=100, null=True, blank=True)
	photo= models.ImageField(upload_to='images/', null=True, blank=True)
	created= models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name

class PropertyCategory(models.Model):
	name= models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.name

class PropertyFeature(models.Model):
	name= models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.name

class Property(models.Model):
	agent= models.ForeignKey(Agent, on_delete=models.CASCADE)
	title= models.CharField(max_length=200, null=True, blank=True)
	description= models.TextField(max_length=200, null=True, blank=True)
	price= models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	location= models.CharField(max_length=100, null=True, blank=True)
	bedrooms= models.IntegerField()
	bathrooms= models.DecimalField(max_digits=4, decimal_places=1)
	sqft= models.IntegerField()
	image= models.ImageField(upload_to='images/')
	is_published= models.BooleanField(default=True)
	list_date= models.DateTimeField(auto_now_add=True)
	category= models.ForeignKey(PropertyCategory, on_delete=models.SET_NULL, null=True)
	features= models.ForeignKey(PropertyFeature, on_delete=models.SET_NULL, null=True)
	status= models.CharField(max_length=20, choices=[
		('active', 'Active'),
		('pending', 'Pending'),
		('sold', 'Sold'),
		('expired', 'Expired'),
		], default='active')

	def __str__(self):
		return self.title

class PropertyImage(models.Model):
	property= models.ForeignKey(Property, on_delete=models.CASCADE)
	image= models.ImageField(upload_to='images/')

	def __str__(self):
		return self.property.title + 'Image'