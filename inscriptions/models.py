#!/usr/bin/python
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin

class InscritAdmin(admin.ModelAdmin):
	list_display = ['nom','prenom','stage','adherent']

class Inscrit(models.Model):
	nom = models.CharField(max_length=40, verbose_name="Nom")
	prenom = models.CharField(max_length=40, verbose_name=u"Prénom")
	adresse = models.TextField(verbose_name="Adresse")
	email = models.EmailField(verbose_name="Adresse email")
	telephone = models.CharField(max_length=10, verbose_name="Numéro de téléphone")
	stage = models.IntegerField(choices = ((2,'Aisne'),(60,'Oise'),(80,'Somme')), verbose_name="Département où vous souhaitez participer")
	pratique_naturaliste = models.TextField(verbose_name="Pratiquez-vous une activitée naturaliste ?", blank=True)
	pref_oiseaux = models.BooleanField(verbose_name="Intéressé par les oiseaux")
	pref_mam_terr = models.BooleanField(verbose_name="Intéressé par les mammifères terrestres")
	pref_mam_marin = models.BooleanField(verbose_name="Intéressé par les mammifères marins")
	pref_chauves_souris = models.BooleanField(verbose_name="Intéressé par les chauves-souris")
	pref_insectes = models.BooleanField(verbose_name="Interessé par les insectes")
	motivations = models.TextField(verbose_name="Qu'est-ce qui motive votre inscription ?")
	moyen_comm = models.TextField(blank=True, verbose_name="Comment avez-vous découvert les stages ?")
	covoiturage = models.BooleanField(verbose_name="Souhaitez-vous participer a un système de covoiturage (échanges de numéros téléphone entre participants au stage) ?")
	commentaire = models.TextField(blank=True, verbose_name="Avez-vous une question ou une remarque ?")
	adherent = models.BooleanField(verbose_name="Êtes-vous adhérent de Picardie-Nature ?")
