from django.contrib import admin
from .models import Dojo, Member, DojoLeader, Registration, Grading, GradingResult

# Register your models here.

admin.site.register(Dojo)
admin.site.register(Member)
admin.site.register(DojoLeader)
admin.site.register(Registration)
admin.site.register(Grading)
admin.site.register(GradingResult)
