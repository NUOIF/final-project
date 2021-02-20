from django.db import models

# Create your models here.

class Groups(models.Model):
    id_groups = models.IntegerField(primary_key=True)
    name_groups = models.CharField(db_column='name_Groups', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idea_groups = models.CharField(db_column='idea_Groups', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idea_fescription = models.CharField(max_length=45, blank=True, null=True)
    idea_speciallty = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return str(self.id_groups)

    class Meta:
        managed = False
        db_table = '_groups'