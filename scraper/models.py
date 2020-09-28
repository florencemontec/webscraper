from django.db import models

class Lotto(models.Model):
	result = models.TextField()
	date_entered = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.result
	
	def get_absolute_url(self):
		return reverse('home')
	
	def save(self, *args, **kwargs):
		for field_name in ['result']:
			val = getattr(self, field_name, False)
			if val:
				setattr(self, field_name, val.upper())
		super(Lotto, self).save(*args, **kwargs)
		
		
class Lazada(models.Model):
	image_url = models.TextField()
	description = models.TextField()
	price = models.TextField()
	
	def __str__(self):
		return self.description
	
	def get_absolute_url(self):
		return reverse('home')
	
	
