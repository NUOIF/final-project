from Department.models import Department
from django.db import models
from projects.models import Projects
from Department.models import Department
from Groups.models import Groups
from Examiners.models import Examiners
from Evaluation.models import Evaluation

class CommitteesCharis(models.Model):
    id_committees_charis = models.IntegerField(primary_key=True) # Return the primary to True
    name_committees_charis = models.CharField(max_length=45, blank=True, null=True)
    passwords = models.CharField(max_length=45, blank=True, null=True)
    id_department_fk = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department_fk', blank=True, null=True)
    def __str__(self):
        return self.name_committees_charis

    class Meta:
        managed = False
        db_table = 'committees_charis'

