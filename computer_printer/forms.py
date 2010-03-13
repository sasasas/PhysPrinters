from django import forms
from webproject2.computer_printer.models import Printer


 
class InstallRequestForm(forms.Form):
	computer_name = forms.CharField(max_length=30)
	# printer_list = Printer.objects.all()
	#printer_name = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=printer_list, label='Printer(s) you would like installed for your computer:')
	printer_name = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Printer.objects.all(), label='Printer(s) you would like installed for your computer:')
	email = forms.EmailField(label='Your e-mail address:')
