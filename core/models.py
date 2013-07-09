from django.db import models
from django.contrib.auth.models import User

from ktree.models import *


class Profile(models.Model):
	name = models.TextField()
	email = models.TextField()

class Account(models.Model):
	user = models.OneToOneField(User)
	profile = models.ForeignKey(Profile, related_name="accounts")

class Team(models.Model):
	creator = models.ForeignKey(Profile)
	name = models.TextField()
	image = models.TextField()
	public = models.BooleanField(default=True)

class Membership(models.Model):
	member = models.ForeignKey(Profile, related_name="teams")
	team = models.ForeignKey(Team, related_name="members")

class ProfileKnowledge(models.Model):
	profile = models.ForeignKey(Profile)
	knowledge = models.ForeignKey(Term)
	level = models.IntegerField()

class ProfileKnowledgeEndorsement(models.Model):
	prokno = models.ForeignKey(ProfileKnowledge)
	endorser = models.ForeignKey(Profile)