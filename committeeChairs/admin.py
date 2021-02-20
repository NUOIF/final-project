from django.contrib import admin
from .models import CommitteesCharis,Groups,Projects,Evaluation,Doctors,Students,Department,Examiners


admin.site.register(Groups)
admin.site.register(Projects)
admin.site.register(Evaluation)
admin.site.register(Doctors)
admin.site.register(Students)
admin.site.register(Department)
admin.site.register(CommitteesCharis)
admin.site.register(Examiners)


# Register your models here.
