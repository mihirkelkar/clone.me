from django.db import models

class User(models.Model):
	name = models.CharField(max_length=80)
	slogan = models.CharField(max_length = 200)
	twt = models.CharField(max_length = 50)
	lk = models.CharField(max_length = 50)
	fb = models.CharField(max_length = 50)
	p1 = models.CharField(max_length = 50)
	tech1 = models.CharField(max_length = 50)
	pd1 = models.CharField(max_length = 300)
	p2 = models.CharField(max_length = 50)
	tech2 = models.CharField(max_length = 50)
	pd2 = models.CharField(max_length = 300)
	p3 = models.CharField(max_length = 50)
	tech3 = models.CharField(max_length = 50)
	pd3 = models.CharField(max_length = 300)
	p4 = models.CharField(max_length = 50)
	tech4 = models.CharField(max_length = 50)
	pd4 = models.CharField(max_length = 300)
	ed1 = models.CharField(max_length = 50)
	loc1 = models.CharField(max_length = 50)
	dur1 = models.CharField(max_length = 50)
	edd1 = models.CharField(max_length = 400)
	ed2 = models.CharField(max_length = 50)
	loc2 = models.CharField(max_length = 50)
	dur2 = models.CharField(max_length = 50)
	edd2 = models.CharField(max_length = 400)
	ed3 = models.CharField(max_length = 50)
	loc3 = models.CharField(max_length = 50)
	dur3 = models.CharField(max_length = 50)
	edd3 = models.CharField(max_length = 400)
	hometown = models.CharField(max_length = 50)
	current = models.CharField(max_length = 50)
	ctf = models.CharField(max_length = 500)
	love = models.CharField(max_length = 500)