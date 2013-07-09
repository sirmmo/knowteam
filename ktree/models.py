from django.db import models

# Create your models here.
class Knowledge(models.Model):
	parent = models.ForeignKey('Knowledge', null=True, blank=True)
	name = models.TextField()

	wikipedia = models.URLField(null=True, blank=True)

	def get_ancestors(self):
		ancestors = [self]
		p = self.parent
		while p is not None:
			ancestors.append(p)
			p = p.parent
		ancestors.reverse()
		return ancestors

	def path(self, separator="."):
		return separator.join(self.get_ancestors())
