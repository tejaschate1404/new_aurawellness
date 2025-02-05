from django.contrib import admin
from .models.counseling import *
from .models.physicalCounseling import *
from .models.distanceHealing import *
# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryPhysical)
admin.site.register(Gmail)
admin.site.register(GmailPhysical)
admin.site.register(Image)
admin.site.register(ImagePhysical)
admin.site.register(Counselling)
admin.site.register(CounsellingPhysical)
admin.site.register(Notes)
admin.site.register(NotesPhysical)
admin.site.register(Phone)
admin.site.register(PhonePhysical)


# Register additional models similar to counseling and physical counseling
admin.site.register(CategoryDistance)
admin.site.register(GmailDistance)
admin.site.register(ImageDistance)
admin.site.register(DistanceHealing)
admin.site.register(NotesDistance)
admin.site.register(PhoneDistance)





