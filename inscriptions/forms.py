from django.forms import ModelForm
from models import Inscrit,InscritPerf

class InscritForm(ModelForm):
	class Meta:
		model = Inscrit

class InscritPerfForm(ModelForm):
	class Meta:
		model = InscritPerf
