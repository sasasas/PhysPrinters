from django.core.mail import mail_admins
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from webproject2.computer_printer.models import Computer, Printer
from webproject2.computer_printer.forms import InstallRequestForm


def home(request):
	#return HttpResponse("Home test.")
	return render_to_response('computer_printerapp/homepage.html')

def printers(request):
	#return HttpResponse("Printers test.")	
	#try:		
	#IPvalue = request.META['REMOTE_ADDR']
	#except KeyError:
		#form2 = CPinstallFormPART2()		
		#return render_to_response('computer_printerapp/available_printers.no_ip.html', {'printerform2': form2, 'printer_list': Printer.objects.all()})
	if request.method == 'POST':	
		IPvalue = request.META['REMOTE_ADDR']		
		currentcomputer = Computer.objects.get(IPaddress=IPvalue)	
		printerform = InstallRequestForm(request.POST)
		if printerform.is_valid():
			cd = printerform.cleaned_data
			mail_admins(
				cd['computer_name'],
				cd.get('printer_name', 'email'),
				fail_silently=False
			)
			return HttpResponseRedirect('/confirmation/')
	else:
		IPvalue = request.META['REMOTE_ADDR']		
		currentcomputer = Computer.objects.get(IPaddress=IPvalue)		
		printerform = InstallRequestForm()
			#initial={'computer_name': currentcomputer}
		#)
		return render_to_response('computer_printerapp/available_printers.html', {'currentcomputer': currentcomputer, 'printerform': printerform})
	
def submitrequest(request):			
	#return HttpResponse("printers/searchcomputer/submitrequest test.")		
	if request.method == 'POST':			
		printerform = InstallRequestForm(request.POST)
		if printerform.is_valid():
			cd = printerform.cleaned_data
			mail_admins(
				cd['computer_name'],
				cd.get('printer_name', 'email'),
				fail_silently=False
			)
			return HttpResponseRedirect('/confirmation/')
	else:
		return HttpResponse("Error!!")

def searchcomputer(request):
	#return HttpResponse("printers/searchcomputer test.")
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		currentcomputer = Computer.objects.filter(name=q)
		printerform = InstallRequestForm()
		return render_to_response('computer_printerapp/computersearchresult.html', {'currentcomputer': currentcomputer, 'printerform': printerform})
	else:
		return render_to_response('computer_printerapp/computersearch.html')


def confirmation(request):
	#return HttpResponse("Confirmation test.")
	return render_to_response('computer_printerapp/confirmpage.html')


