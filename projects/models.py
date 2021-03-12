from django.db import models
from Groups.models import Groups
# Create your models here.
class Projects(models.Model):
    id_projects = models.AutoField(db_column='id_Projects', primary_key=True)  # Field name made lowercase.
    name_projects = models.CharField(db_column='title_projects',max_length=45, blank=True, null=True)
    filled_projects = models.CharField(max_length=45, blank=True, null=True)
    descriotion_projects = models.CharField(max_length=45, blank=True, null=True)
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True)  # Field name made lowercase.
    file_project = models.FileField(upload_to='doucment',db_column='File_Project')  # Field name made lowercase.
    def __str__(self):
        return str(self.id_projects)
    class Meta:
        managed = False
        db_table = 'projects'
