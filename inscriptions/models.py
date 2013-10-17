#!/usr/bin/python
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin

import csv
from django.http import HttpResponse

def export_as_csv_action(description=u"Exporter en CSV les valeurs sélectionnées", fields=None, exclude=None, header=True):
	"""
	This function returns an export csv action
	'fields' and 'exclude' work like in django ModelForm
	'header' is whether or not to output the column names as the first row
	"""
	def export_as_csv(modeladmin, request, queryset):
		"""
		Generic csv export admin action.
		based on http://djangosnippets.org/snippets/1697/
		"""
		opts = modeladmin.model._meta
		field_names = set([field.name for field in opts.fields])
		if fields:
			fieldset = set(fields)
			field_names = field_names & fieldset
		elif exclude:
			excludeset = set(exclude)
			field_names = field_names - excludeset

		response = HttpResponse(mimetype='text/csv')
		response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')

		writer = csv.writer(response)
		if header:
			writer.writerow(list(field_names))
		for obj in queryset:
			writer.writerow([unicode(getattr(obj, field)).encode("utf-8","replace") for field in field_names])
		return response

	export_as_csv.short_description = description
	return export_as_csv

class InscritAdmin(admin.ModelAdmin):
	list_display = ['nom','prenom','stage','adherent']
	actions = [export_as_csv_action()]

class Inscrit(models.Model):
	nom = models.CharField(max_length=40, verbose_name="Nom")
	prenom = models.CharField(max_length=40, verbose_name=u"Prénom")
	adresse = models.TextField(verbose_name="Adresse")
	email = models.EmailField(verbose_name="Adresse email")
	telephone = models.CharField(max_length=10, verbose_name="Numéro de téléphone")
	stage = models.IntegerField(choices = ((2,'Aisne'),(60,'Oise'),(80,'Somme')), verbose_name="Département où vous souhaitez participer")
	pratique_naturaliste = models.TextField(verbose_name="Pratiquez-vous une activité naturaliste ?", blank=True)
	contributeur_clicnat = models.BooleanField(verbose_name=" Êtes vous déjà un contributeur de données dans Clicnat ?")
	pref_oiseaux = models.BooleanField(verbose_name="Intéressé par les oiseaux")
	pref_mam_terr = models.BooleanField(verbose_name="Intéressé par les mammifères terrestres")
	pref_mam_marin = models.BooleanField(verbose_name="Intéressé par les mammifères marins")
	pref_chauves_souris = models.BooleanField(verbose_name="Intéressé par les chauves-souris")
	pref_insectes = models.BooleanField(verbose_name="Interessé par les insectes")
	motivations = models.TextField(verbose_name="Qu'est-ce qui motive votre inscription ?")
	implication = models.TextField(verbose_name="Suite à ce stage, quelle serait  votre implication dans nos activités naturalistes ?")
	moyen_comm = models.TextField(blank=True, verbose_name="Comment avez-vous découvert les stages ?")
	covoiturage = models.BooleanField(default=True, verbose_name="Vous participez a un système de covoiturage (échanges de numéros téléphone entre participants au stage)")
	commentaire = models.TextField(blank=True, verbose_name="Avez-vous une question ou une remarque ?")
	adherent = models.BooleanField(verbose_name="Êtes-vous adhérent de Picardie-Nature ?")

class InscritPerfAdmin(admin.ModelAdmin):
	list_display = ['nom','prenom','email','telephone','adherent']
	actions = [export_as_csv_action()]

class InscritPerf(models.Model):
	nom = models.CharField(max_length=40, verbose_name="Nom")
	prenom = models.CharField(max_length=40, verbose_name=u"Prénom")
	adresse = models.TextField(verbose_name="Adresse")
	email = models.EmailField(verbose_name="Adresse email")
	telephone = models.CharField(max_length=10, verbose_name="Numéro de téléphone")
	adherent = models.BooleanField(verbose_name="Êtes-vous adhérent de Picardie-Nature ?")
	pratique_naturaliste = models.BooleanField(verbose_name="Pratique naturaliste")
	motivation = models.TextField(blank=True, verbose_name="Motivations pour l'évènement ?")
	moyen_de_com = models.CharField(max_length=40, verbose_name="Par quel moyen de communication avez vous découvert ces stages")
	covoiturage = models.BooleanField(verbose_name="Souhaitez-vous participer a un système de covoiturage (échanges de numéros téléphone entre participants au stage) ?")
	commentaire = models.TextField(blank=True, verbose_name="Avez-vous une question ou une remarque ?")
	stage_chant_des_oiseaux = models.BooleanField(verbose_name="Stage de perfectionnement chant des oiseaux")
	stage_chauves_souris = models.BooleanField(verbose_name="Stage de formation : comprendre et apprendre le monde silencieux des chauves-souris")
	stage_papillons = models.BooleanField(verbose_name="Stage de perfectionnement d'étude des papillons")
	stage_etude_vexin = models.BooleanField(verbose_name="Week-end d'inventaires naturalistes pluridisciplinaires dans le Vexin")
	stage_odonates = models.BooleanField(verbose_name="Apprendre à étudier les libellules")
	journee_etude_marne = models.BooleanField(verbose_name="Journée étude coteaux vallée de la Marne")
	stage_clicnat_aisne = models.BooleanField(verbose_name="Observez et agissez pour la nature avec Clicnat")
	journee_etude_papillons = models.BooleanField(verbose_name="Journée d'études du réseau papillons")
	stage_plantes_animaux = models.BooleanField(verbose_name="Stage thématique : plantes-hôtes, insectes et jardin sauvage")
	stage_orthopteres = models.BooleanField(verbose_name="Journée d'étude et stage de perfectionnement Orthoptères")
	journee_araignees = models.BooleanField(verbose_name="A la recherche des araignées")
	journee_coccinelle = models.BooleanField(verbose_name="A la recherche des coccinelles de nos landes !")
	stage_clicnat_oise = models.BooleanField(verbose_name="Observez et agissez pour la nature avec Clicnat")
	stage_continuite_eco = models.BooleanField(verbose_name="Quand nos routes croisent leurs chemins")
	

