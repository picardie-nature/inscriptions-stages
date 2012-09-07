from django.forms import ModelForm
from models import Inscrit

class InscritForm(ModelForm):
	class Meta:
		model = Inscrit
