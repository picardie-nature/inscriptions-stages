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
			message_equipe = u"""Nouvel inscrit au stage naturaliste %(stage)02d :
Nom, prénom : %(nom)s %(prenom)s
Adresse : 
%(adresse)s

Email : %(email)s 
Téléphone : %(telephone)s

Pratique naturaliste :
%(pratique_naturaliste)s

Préférences :
Oiseaux : %(pref_oiseaux)d Mam. Terr. : %(pref_mam_terr)d Mam. Marin : %(pref_mam_marin)d
Chauves souris : %(pref_chauves_souris)d Insectes : %(pref_insectes)d

Motivations :
%(motivations)s

Moyen de communication : 
%(moyen_comm)s

Adhérent : %(adherent)d 
Covoiturage : %(covoiturage)d

Commentaire :
%(commentaire)s
""" % form.cleaned_data

			send_mail("Confirmation pré-inscription au stage naturaliste", message, "support@picardie-nature.org", [form.cleaned_data['email']], fail_silently=False)
			send_mail(u"Pré-inscription stage naturaliste de %(prenom)s %(nom)s"%form.cleaned_data, message_equipe, "support@picardie-nature.org", ["observatoire@picardie-nature.org"], fail_silently=True)
			return HttpResponseRedirect('/merci')
	else:
		form = InscritForm()
	
	t = loader.get_template('index.html')
	c = RequestContext(request, {'form':form})
	return HttpResponse(t.render(c))

def merci(request):
	c = RequestContext(request, {})
	t = loader.get_template('merci.html')
	return HttpResponse(t.render(c))
