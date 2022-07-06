from django.contrib import admin
from .models import Fir,Techtracker,Oem,Specification,Application,CustomerRaisedBy,Customerissue,Resolutiontype,Status,Diagnosis,Priority,Resolution, AdditionalInfo,Complaint
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group,User
from fir_model.models import AuthUser,IsUser


class FirAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('complaint_id','serial_no','register_date','specification','application_type','oem','dealer_name','location','customer_raised_by','resolution_type','tracker','status')
    list_filter = ['complaint_id','oem']

    class Media:
        js=("fir_model/newajax.js",)


class TechTracerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('sku','complaint_id','oem','application_type','serial_no','receipt_date','diagnosis','resolution','dealer_name','status')
    list_filter = ['complaint_id','serial_no','oem']

    def clean_name(self):
        return self.cleaned_data["name"].upper()

class ComplaintAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('created_by','assign_by','complaint_id','serial_no','oem','customer_issue')
    list_filter = ['complaint_id','serial_no','oem']
 

admin.site.register(AuthUser)
admin.site.register(IsUser)
admin.site.register(Fir,FirAdmin)
admin.site.register(Techtracker,TechTracerAdmin)
admin.site.register(Oem)
admin.site.register(Specification)
admin.site.register(Application)
admin.site.register(Customerissue)
admin.site.register(CustomerRaisedBy)
admin.site.register(AdditionalInfo)
admin.site.register(Resolution)
admin.site.register(Resolutiontype)
admin.site.register(Status)
admin.site.register(Diagnosis)
admin.site.register(Priority)
admin.site.register(Complaint,ComplaintAdmin)


admin.site.site_header = "Service Tracker"
