from django.db import models
from django.conf import settings
# Create your models here.
class Mast(models.Model):
	client = models.ForeignKey(to=settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.CASCADE)
	q1 = models.BooleanField(null=False, blank=False)
	q2 = models.BooleanField(null=False, blank=False)
	q3 = models.BooleanField(null=False, blank=False)
	q4 = models.BooleanField(null=False, blank=False)
	q5 = models.BooleanField(null=False, blank=False)
	q6 = models.BooleanField(null=False, blank=False)
	q7 = models.BooleanField(null=False, blank=False)
	q8 = models.BooleanField(null=False, blank=False)
	q9 = models.BooleanField(null=False, blank=False)
	q10 = models.BooleanField(null=False, blank=False)
	q11 = models.BooleanField(null=False, blank=False)
	q12 = models.BooleanField(null=False, blank=False)
	q12 = models.BooleanField(null=False, blank=False)
	q13 = models.BooleanField(null=False, blank=False)
	q14 = models.BooleanField(null=False, blank=False)
	q15 = models.BooleanField(null=False, blank=False)
	q16 = models.BooleanField(null=False, blank=False)
	q17 = models.BooleanField(null=False, blank=False)
	q18 = models.BooleanField(null=False, blank=False)
	q19 = models.BooleanField(null=False, blank=False)
	q20 = models.BooleanField(null=False, blank=False)
	q21 = models.BooleanField(null=False, blank=False)
	q21Yes = models.IntegerField(null=True, blank=True)
	q22 = models.BooleanField(null=False, blank=False)
	q22Yes = models.IntegerField(null=True, blank=True)
	mastScore = models.IntegerField(null=False, blank=False )

class Profile(models.Model):
	client = models.ForeignKey(to=settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.CASCADE)
	streetAddress = models.CharField(null=False, blank=False, max_length=100)
	streetAddress2 = models.CharField(null=True, blank=True, max_length=30)
	city = models.CharField(null=False, blank=False, max_length=100)
	zipCode = models.CharField(null=False,blank=False, max_length=5)
	state = models.CharField(null=False, blank=False, max_length=2)
	primePhone = models.CharField(null=False,blank=False, max_length=10) 
	workPhone = models.CharField(null=True,blank=True, max_length=10)
	dob = models.DateField(null=False, blank=True)
	idType = models.CharField(blank=False, null=False, max_length=14)
	ethnicity = models.CharField(blank=False, null=False, max_length=20)
	gender = models.CharField(null=False, blank=False, max_length=6)
	martial = models.CharField(null=False, blank=False, max_length=9)
	emp = models.CharField(null=False, blank=False, max_length=18)
	emergencyContact = models.CharField(null=False, blank=False, max_length=50)
	emergencyRelationship = models.CharField(null=False, blank=False, max_length=20)
	emergencyPhone = models.CharField(null=False, blank=False, max_length=10,)
	emergencyEmail = models.EmailField(blank=False, null=False, max_length=150)
	income = models.CharField(max_length=10, blank=True, null=True)
	idNumber = models.CharField(blank=False, null=False, max_length=50)
	collegeGrad = models.CharField(blank=True, null=True, max_length=3)
	hsGrad = models.CharField(blank=True, null=True, max_length=3)
	interpreter = models.CharField(blank=True, null=True, max_length=3)
	edLevel = models.CharField(blank=True, null=True, max_length=150)
	familySize = models.CharField(blank=True, null=True, max_length=3)
	occupation = models.CharField(blank=True, null=True, max_length=100)
	collegeGrad = models.CharField(blank=True, null=True, max_length=3)

class PsychSoc(models.Model):
	client = models.ForeignKey(to=settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.CASCADE)
	ls1 = models.BooleanField(null=False, blank=False)
	ls2 = models.BooleanField(null=False, blank=False)
	ls3 = models.BooleanField(null=False, blank=False)
	ls4 = models.BooleanField(null=False, blank=False)
	ls5 = models.BooleanField(null=False, blank=False)
	ls6 = models.BooleanField(null=False, blank=False)
	ss1 = models.BooleanField(null=False, blank=False)
	ss2 = models.BooleanField(null=False, blank=False)
	ss3 = models.BooleanField(null=False, blank=False)
	ss4 = models.BooleanField(null=False, blank=False)
	ss5 = models.BooleanField(null=False, blank=False)
	fs1 = models.BooleanField(null=False, blank=False)
	fs2 = models.BooleanField(null=False, blank=False)
	fs3 = models.BooleanField(null=False, blank=False)
	fs4 = models.BooleanField(null=False, blank=False)
	fs5 = models.BooleanField(null=False, blank=False)
	hs1 = models.BooleanField(null=False, blank=False)
	hs2 = models.BooleanField(null=False, blank=False)
	hs3 = models.BooleanField(null=False, blank=False)
	hs4 = models.BooleanField(null=False, blank=False)
	hs5 = models.BooleanField(null=False, blank=False)
	ms1 = models.BooleanField(null=False, blank=False)
	ms2 = models.BooleanField(null=False, blank=False)
	ms2Yes =  models.CharField(max_length=3, blank=True, null=True)
	ms3 = models.BooleanField(null=False, blank=False)
	ms3Yes =  models.CharField(max_length=3, blank=True, null=True)
	ms4 = models.BooleanField(null=False, blank=False)
	ms4Yes =  models.CharField(max_length=3, blank=True, null=True)
	ms5 = models.BooleanField(null=False, blank=False)
	ms5Yes =  models.CharField(max_length=3, blank=True, null=True)
	em1 = models.BooleanField(null=False, blank=False)
	em2 = models.BooleanField(null=False, blank=False)
	em3 = models.BooleanField(null=False, blank=False)
	em4 = models.BooleanField(null=False, blank=False)
	em5 = models.BooleanField(null=False, blank=False)
	em6 = models.BooleanField(null=False, blank=False)
	em7 = models.BooleanField(null=False, blank=False)
	em7Yes = models.TextField(max_length=150, null=True, blank=True)
	fd1 = models.BooleanField(null=False, blank=False)
	fd2 = models.BooleanField(null=False, blank=False)
	fd3 = models.BooleanField(null=False, blank=False)
	fd4 = models.BooleanField(null=False, blank=False)
	fd5 = models.BooleanField(null=False, blank=False)
	fd6 = models.BooleanField(null=False, blank=False)
	fd7 = models.BooleanField(null=False, blank=False)
	fd8 = models.BooleanField(null=False, blank=False)
	fd9 = models.BooleanField(null=False, blank=False)
	su1 = models.BooleanField(null=False, blank=False)
	alcFirst = models.CharField(max_length=2, blank=True, null=True)
	alcLast = models.CharField(max_length=2, blank=True, null=True)
	alcFreq = models.CharField(max_length=22, blank=True, null=True)
	alcAmount = models.CharField(max_length=30, blank=True, null=True)
	su2 = models.BooleanField(null=False, blank=False)
	ampFirst = models.CharField(max_length=2, blank=True, null=True)
	ampLast = models.CharField(max_length=2, blank=True, null=True)
	ampFreq = models.CharField(max_length=22, blank=True, null=True)
	ampAmount = models.CharField(max_length=30, blank=True, null=True)
	su3 = models.BooleanField(null=False, blank=False)
	barbFirst = models.CharField(max_length=2, blank=True, null=True)
	barbLast = models.CharField(max_length=2, blank=True, null=True)
	barbFreq = models.CharField(max_length=22, blank=True, null=True)
	barbAmount = models.CharField(max_length=30, blank=True, null=True)
	su4 = models.BooleanField(null=False, blank=False)
	cafFirst = models.CharField(max_length=2, blank=True, null=True)
	cafLast = models.CharField(max_length=2, blank=True, null=True)
	cafFreq = models.CharField(max_length=22, blank=True, null=True)
	cafAmount = models.CharField(max_length=30, blank=True, null=True)
	su5 = models.BooleanField(null=False, blank=False)
	cocFirst = models.CharField(max_length=2, blank=True, null=True)
	cocLast = models.CharField(max_length=2, blank=True, null=True)
	cocFreq = models.CharField(max_length=22, blank=True, null=True)
	cocAmount = models.CharField(max_length=30, blank=True, null=True)
	su6 = models.BooleanField(null=False, blank=False)
	crcFirst = models.CharField(max_length=2, blank=True, null=True)
	crcLast = models.CharField(max_length=2, blank=True, null=True)
	crcFreq = models.CharField(max_length=22, blank=True, null=True)
	crcAmount = models.CharField(max_length=30, blank=True, null=True)
	su7 = models.BooleanField(null=False, blank=False)
	lsdFirst = models.CharField(max_length=2, blank=True, null=True)
	lsdLast = models.CharField(max_length=2, blank=True, null=True)
	lsdFreq = models.CharField(max_length=22, blank=True, null=True)
	lsdAmount = models.CharField(max_length=30, blank=True, null=True)
	su8 = models.BooleanField(null=False, blank=False)
	inhFirst = models.CharField(max_length=2, blank=True, null=True)
	inhLast = models.CharField(max_length=2, blank=True, null=True)
	inhFreq = models.CharField(max_length=22, blank=True, null=True)
	inhAmount = models.CharField(max_length=30, blank=True, null=True)
	su9 = models.BooleanField(null=False, blank=False)
	thcFirst = models.CharField(max_length=2, blank=True, null=True)
	thcLast = models.CharField(max_length=2, blank=True, null=True)
	thcFreq = models.CharField(max_length=22, blank=True, null=True)
	thcAmount = models.CharField(max_length=30, blank=True, null=True)
	su10 = models.BooleanField(null=False, blank=False)
	nicFirst = models.CharField(max_length=2, blank=True, null=True)
	nicLast = models.CharField(max_length=2, blank=True, null=True)
	nicFreq = models.CharField(max_length=22, blank=True, null=True)
	nicAmount = models.CharField(max_length=30, blank=True, null=True)
	su11 = models.BooleanField(null=False, blank=False)
	pcpFirst = models.CharField(max_length=2, blank=True, null=True)
	pcpLast = models.CharField(max_length=2, blank=True, null=True)
	pcpFreq = models.CharField(max_length=22, blank=True, null=True)
	pcpAmount = models.CharField(max_length=30, blank=True, null=True)
	su12 = models.BooleanField(null=False, blank=False, default=False)
	preFirst = models.CharField(max_length=2, blank=True, null=True)
	preLast = models.CharField(max_length=2, blank=True, null=True)
	preFreq = models.CharField(max_length=22, blank=True, null=True)
	preAmount = models.CharField(max_length=30, blank=True, null=True)