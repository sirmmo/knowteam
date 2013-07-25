from django.db import models

# Create your models here.
class Term(models.Model):
	name = models.TextField()

	wikipedia = models.URLField(null=True, blank=True)

	primary = models.BooleanField(default=False)

	accepted = models.BooleanField(default=False)

	def connections(self):
		p1 = list(Term.objects.starts.all().values())
		p2 = list(Term.objects.ends.all().values())
		return p1.extend(p2)

	def  __str__(self):
		return self.name

class LinkType(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name

class Link(models.Model):
	a = models.ForeignKey(Term, related_name="starts")
	b = models.ForeignKey(Term, related_name="ends")
	name = models.ForeignKey(LinkType)
	bidirectional = models.BooleanField(default=False)

	def __str__(self):
		return "%s %s-%s-> %s" % (self.a, "<" if self.bidirectional else "-", self.name, self.b)



