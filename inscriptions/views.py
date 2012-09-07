#!/usr/bin/python
# -*- encoding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader,RequestContext
from forms import InscritForm
from django.core.mail import send_mail

def index(request):
	if request.method == 'POST':
		form = InscritForm(request.POST)
		if form.is_valid():
			form.save()
			message = """Bonjour,

Nous avons enregistré votre pré-inscription.

Vous allez bientôt recevoir un courrier vous présentant le stage et qui vous indiquera aussi comment confirmer votre inscription.

À bientôt,
L'équipe de Picardie Nature.
"""
			send_mail("Confirmation d'inscription au stage naturaliste", message, "support@picardie-nature.org", [form.cleaned_data['email']], fail_silently=False)
			return HttpResponseRedirect('/merci')
	else:
		form = InscritForm()
	
	t = loader.get_template('index.html')
	c = RequestContext(request, {'form':form})
	return HttpResponse(t.render(c))

