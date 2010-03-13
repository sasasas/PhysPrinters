from django.db import models


class Computer(models.Model):
	name = models.CharField(max_length=30, verbose_name='Computer Name')
	IPaddress = models.IPAddressField(max_length=15)
	default_user = models.CharField(max_length=30)
	printers = models.ManyToManyField('Printer', blank=True, null=True)

	def __unicode__(self):
		return self.name

class Printer(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name	

