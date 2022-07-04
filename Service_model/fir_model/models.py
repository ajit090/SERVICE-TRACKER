from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.utils import timezone
import datetime

class IsUser(models.Model):
    user = models.CharField(max_length = 20, unique = True)

    class  Meta:  
        verbose_name_plural  =  "ISUSER"  

    def __str__(self):
        return self.user
    
class AuthUser(AbstractUser):
   user = models.ForeignKey(IsUser, on_delete=models.SET_NULL, null=True)

   def __str__(self):
       return str(self.user)
   

class Specification(models.Model):
    specification = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "SPECIFICATION"  

    def __str__(self):
        return self.specification


class Application(models.Model):
    application = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "APPLICATION"  

    def __str__(self):
        return self.application
    
    
class Oem(models.Model):
    oem = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "OEM"  

    def __str__(self):
        return self.oem


class Customerissue(models.Model):
    name = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "CUSTOMER ISSUE"

    def __str__(self):
        return self.name

class Customer(models.Model):
    customer = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "CUSTOMER"

    def __str__(self):
        return self.customer

class AdditionalInfo(models.Model):
    customer_issue = models.ForeignKey(Customerissue, on_delete=models.CASCADE, related_name='additionalinfos')
    name = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "ADDITIONAL INFO"

    def __str__(self):
        return self.name
    
class Resolutiontype(models.Model):
    resolution_type = models.CharField(max_length=250)

    class  Meta:  
        verbose_name_plural  =  "RESOLUTION TYPE"

    def __str__(self):
        return self.resolution_type

class Status(models.Model):
    status = models.CharField(max_length=100)

    class  Meta:  
        verbose_name_plural  =  "STATUS"

    def __str__(self):
        return self.status
    

class Diagnosis(models.Model):
    diagnosis = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "DIAGNOSIS"

    def __str__(self):
        return self.diagnosis

class Priority(models.Model):
    priority = models.CharField(max_length=100)

    class  Meta:  
        verbose_name_plural  =  "PRIORITY"

    def __str__(self):
        return self.priority

class Resolution(models.Model):
    resolution = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "RESOLUTION"

    def __str__(self):
        return self.resolution
    



class Fir(models.Model):
    comments= models.CharField(max_length=100,blank=True)
    complaint_id = models.IntegerField()
    serial_no = models.CharField(max_length=50)
    register_date =  models.DateTimeField()
    specification = models.ForeignKey(Specification, on_delete=models.SET_NULL, null=True)
    application_type =  models.ForeignKey(Application, on_delete=models.SET_NULL, null=True)
    oem = models.ForeignKey(Oem, on_delete=models.SET_NULL, null=True)
    dealer_name = models.CharField(max_length=100)
    state = models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100,blank=True)
    contact_no = models.CharField(max_length=50,blank = True)
    customer_raised_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    customer_issue = models.ForeignKey(Customerissue, on_delete=models.SET_NULL, null=True,related_name='cissues')
    additional_info =models.ForeignKey(AdditionalInfo, on_delete=models.SET_NULL, null=True,related_name='add')
    resolution_type =  models.ForeignKey(Resolutiontype, on_delete=models.SET_NULL, null=True)
    observations = models.CharField(max_length=250,blank=True)
    tracker = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    pickup_date = models.DateTimeField(null=True,blank=True)
    receipt_date = models.DateTimeField(null=True,blank=True)
    closure_date =  models.DateTimeField(null=True,blank=True)
    remark = models.CharField(max_length=150)


    class  Meta:  
        verbose_name_plural  =  "FIR"

    def __str__(self):
        return self.serial_no


class Techtracker(models.Model):
    sku =  models.ForeignKey(Specification, on_delete=models.SET_NULL, null=True)
    complaint_id = models.IntegerField()
    oem = models.ForeignKey(Oem, on_delete=models.SET_NULL, null=True)
    application_type =  models.ForeignKey(Application, on_delete=models.SET_NULL, null=True)
    dealer_name = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    receipt_date = models.DateTimeField()
    diagnosis =  models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True)
    resolution =  models.ForeignKey(Resolution, on_delete=models.SET_NULL, null=True)
    additional_comments = models.CharField(max_length=150,blank=True)
    capacity_after_testing = models.CharField(max_length=100,blank=True)
    closure_date = models.DateTimeField(null=True,blank=True)
    priority =  models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    final_remarks = models.CharField(max_length=100,blank=True)
    remarks_dispatched = models.CharField(max_length=150,blank=True)

    class  Meta:  
        verbose_name_plural  =  "TECH TRACKER"


    def __str__(self):
        return self.serial_no

class Complaint(models.Model):
    created_by =  models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True,related_name='Created_by',blank=True)
    assign_by = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True,related_name='Assigned_by',blank=True)
    comments= models.CharField(max_length=100,blank=True)
    complaint_id = models.IntegerField()
    serial_no = models.CharField(max_length=50,blank=True)
    soft_pack_serial_no = models.CharField(max_length=50,blank=True)
    register_date =  models.DateTimeField()
    specification = models.ForeignKey(Specification, on_delete=models.SET_NULL, null=True)
    application_type =  models.ForeignKey(Application, on_delete=models.SET_NULL, null=True)
    oem = models.ForeignKey(Oem, on_delete=models.SET_NULL, null=True)
    dealer_name = models.CharField(max_length=100)
    state = models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100,blank=True)
    contact_no = models.CharField(max_length=50,blank = True)
    customer_raised_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)
    customer_issue = models.ForeignKey(Customerissue, on_delete=models.SET_NULL, null=True,related_name='cissues1',blank=True)
    additional_info =models.ForeignKey(AdditionalInfo, on_delete=models.SET_NULL, null=True,related_name='add2',blank=True)
    resolution_type =  models.ForeignKey(Resolutiontype, on_delete=models.SET_NULL, null=True,blank=True)
    observations = models.CharField(max_length=250,blank=True)
    tracker = models.CharField(max_length=100,blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    pickup_date = models.DateTimeField(null=True,blank=True)
    receipt_date = models.DateTimeField(null=True,blank=True)
    closure_date =  models.DateTimeField(null=True,blank=True)
    remark = models.CharField(max_length=150)
    diagnosis =  models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True)
    resolution =  models.ForeignKey(Resolution, on_delete=models.SET_NULL, null=True)
    additional_comments = models.CharField(max_length=150,blank=True)
    capacity_after_testing = models.CharField(max_length=100,blank=True)
    final_remarks = models.CharField(max_length=100,blank=True)
    remarks_dispatched = models.CharField(max_length=150,blank=True)


    class Meta:
        verbose_name_plural  =  "COMPLAINT"

    def __str__(self):
        return self.serial_no
    