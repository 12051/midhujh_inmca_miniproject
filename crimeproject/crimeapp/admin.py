from django.contrib import admin
from .models import CustomUser,CrimeReport,AnonyReport,SpecLoc,Aadhaar,DocReport,EvidenceCrimeReport, PublicReport

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CrimeReport)
admin.site.register(PublicReport)
admin.site.register(AnonyReport)
admin.site.register(DocReport)
admin.site.register(SpecLoc)
admin.site.register(Aadhaar)
admin.site.register(EvidenceCrimeReport)