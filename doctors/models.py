from django.db import models
from Department.models import Department
from Groups.models import Groups
from Examiners.models import Examiners
# Create your models here.

class Doctors(models.Model):
    id_doctors = models.IntegerField(db_column='id_Doctors', primary_key=True)  # Field name made lowercase.
    name_doctors = models.CharField(db_column='name_Doctors', max_length=45, blank=True, null=True)  # Field name made lowercase.
    passwords = models.CharField(max_length=45, blank=True, null=True)
    id_department_fk = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department_fk', blank=True, null=True)
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True)  # Field name made lowercase.
    id_examiners_fk = models.ForeignKey(Examiners, models.DO_NOTHING, db_column='id_Examiners_fk', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.name_doctors
    class Meta:
        managed = False
        db_table = 'doctors'


