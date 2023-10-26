from django.db import models
from django.utils import timezone


# Create your models here.
class departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.TextField()

    def __str__(self):
        return self.dept_name
class doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_dept = models.ForeignKey(departments,on_delete=models.CASCADE)
    doc_img = models.ImageField(upload_to='pictures/')
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.doc_name

class appointments(models.Model):
    p_name = models.CharField(max_length=1000)
    p_email = models.EmailField(max_length=100)
    p_phone = models.IntegerField()
    p_doc = models.ForeignKey(doctors,on_delete=models.CASCADE)
    p_date = models.DateField(default=timezone.now)
    p_msg = models.TextField()
    def get_doctor_name(self):
        return self.p_doc.doc_name
