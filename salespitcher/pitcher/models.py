from django.db import models

# Create your models here.

class Player(models.Model):
	username = models.CharField(max_length=32)

class Subject(models.Model):
	prompt_text = models.CharField(max_length = 64)
	pub_date = models.DateTimeField('date published')
	num_answers = models.IntegerField(default=0)

	def __str__(self):
		return ( "Subject >'{0}' #{1} @{2};".format(self.prompt_text, self.num_answers, self.pub_date) )

class Tagline(models.Model):
	text = models.CharField(max_length=256)
	submit_date = models.DateTimeField('date submitted')
	subject = models.ForeignKey('Subject',on_delete=models.CASCADE,)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return ("Tagline >'{0}' >'{1}' #{2} @{3};".format(self.text, self.subject, self.votes, self.submit_date))

	class Meta:
		ordering = ('subject',)