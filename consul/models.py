from django.db import models
from django.conf import settings

# Create your models here.
class Counselor(models.Model):
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.CASCADE)
	sunStart = models.TimeField(null=False, blank=False)
	sunEnd = models.TimeField(null=False, blank=False)
	monStart = models.TimeField(null=False, blank=False)
	monEnd = models.TimeField(null=False, blank=False)
	tueStart = models.TimeField(null=False, blank=False)
	tueEnd = models.TimeField(null=False, blank=False)
	wedStart = models.TimeField(null=False, blank=False)
	wedEnd = models.TimeField(null=False, blank=False)
	thurStart = models.TimeField(null=False, blank=False)
	thurEnd = models.TimeField(null=False, blank=False)
	friStart = models.TimeField(null=False, blank=False)
	friEnd = models.TimeField(null=False, blank=False)
	satStart = models.TimeField(null=False, blank=False)
	satEnd = models.TimeField(null=False, blank=False)

class Course(models.Model):
	counselor1 = models.ForeignKey(to=Counselor,null=False, blank=False, on_delete=models.CASCADE)
	counselor2 = models.ForeignKey(to=Counselor,null=True, blank=True, related_name='counselor2',on_delete=models.CASCADE)
	counselor3 = models.ForeignKey(to=Counselor,null=True, blank=True, related_name='counselor3',on_delete=models.CASCADE)
	startTime = models.TimeField(null=False, blank=False)
	endTime = models.TimeField(null=False, blank=False)
	sun = models.BooleanField(null=False,blank=False)
	mon = models.BooleanField(null=False,blank=False)
	tue = models.BooleanField(null=False,blank=False)
	wed = models.BooleanField(null=False,blank=False)
	thur = models.BooleanField(null=False,blank=False)
	fri = models.BooleanField(null=False,blank=False)
	sat = models.BooleanField(null=False,blank=False)
	numPpl = models.IntegerField(null=False,blank=False )

