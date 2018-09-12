from django.db import models
from django.conf import settings
from django.utils import timezone

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
	counselors = models.ManyToManyField(Counselor, through='CounselorCourse')
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
	name = models.CharField(max_length=100, blank=False, null=False)

class CounselorCourse(models.Model):
	counselor = models.ForeignKey(to=Counselor,null=False, blank=False, on_delete=models.CASCADE)
	course = models.ForeignKey(to=Course,null=False, blank=False, on_delete=models.CASCADE)
	priority = models.IntegerField(null=False, blank=False)

class Contact(models.Model):
	name = models.CharField(max_length=30, null=False, blank=False)
	email = models.EmailField(max_length=25, null=False, blank=False)
	phone = models.CharField(max_length=11, null=False, blank=False)
	message = models.CharField(max_length=500, null=False, blank=True)
	title = models.CharField(max_length=20, null=False, blank=False)
	q1 = models.CharField(max_length=5, null=False, blank=False)
	dui = models.CharField(max_length=20, null=False, blank=True)
	famCounseling = models.CharField(max_length=20, null=False, blank=True)
	domViolence = models.CharField(max_length=20, null=False, blank=True)
	empAssistance = models.CharField(max_length=20, null=False, blank=True)
	partnership = models.CharField(max_length=25, null=False, blank=True)
	teenHelp = models.CharField(max_length=20, null=False, blank=True)
	athCounseling = models.CharField(max_length=20, null=False, blank=True)
	submitted = models.DateTimeField(default=timezone.now)

class ScheduleClass(models.Model):
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.CASCADE)
	course_sched = models.ForeignKey(to=Course,null=True, blank=True, on_delete=models.CASCADE)
	date = models.DateField(null=False, blank=False)


