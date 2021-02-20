from django.db import models

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

class Projects(models.Model):
    id_projects = models.IntegerField(db_column='id_Projects', primary_key=True)  # Field name made lowercase.
    name_projects = models.CharField(max_length=45, blank=True, null=True)
    filled_projects = models.CharField(max_length=45, blank=True, null=True)
    descriotion_projects = models.CharField(max_length=45, blank=True, null=True)
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id_projects)
    class Meta:
        managed = False
        db_table = 'projects'


class Department(models.Model):
    id_department = models.IntegerField(primary_key=True)
    name_department = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.name_department

    class Meta:
        managed = False
        db_table = 'department'


class CommitteesCharis(models.Model):
    id_committees_charis = models.IntegerField(primary_key=True)
    name_committees_charis = models.CharField(max_length=45, blank=True, null=True)
    passwords = models.CharField(max_length=45, blank=True, null=True)
    id_department_fk = models.ForeignKey('Department', models.DO_NOTHING, db_column='id_department_fk', blank=True, null=True)
    def __str__(self):
        return self.name_committees_charis

    class Meta:
        managed = False
        db_table = 'committees_charis'



class Examiners(models.Model):
    id_examiners = models.IntegerField(db_column='id_Examiners', primary_key=True)  # Field name made lowercase.
    name_examiners = models.CharField(db_column='name_Examiners', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id_examiners)
    class Meta:
        managed = False
        db_table = 'examiners'



class Doctors(models.Model):
    id_doctors = models.IntegerField(db_column='id_Doctors', primary_key=True)  # Field name made lowercase.
    name_doctors = models.CharField(db_column='name_Doctors', max_length=45, blank=True, null=True)  # Field name made lowercase.
    passwords = models.CharField(max_length=45, blank=True, null=True)
    id_department_fk = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department_fk', blank=True, null=True)
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True)  # Field name made lowercase.
    id_examiners_fk = models.ForeignKey('Examiners', models.DO_NOTHING, db_column='id_Examiners_fk', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.name_doctors
    class Meta:
        managed = False
        db_table = 'doctors'


class Evaluation(models.Model):
    id_evaluation = models.IntegerField(db_column='id_Evaluation', primary_key=True)  # Field name made lowercase.
    gread_evaluation = models.CharField(max_length=45, blank=True, null=True)
    id_examiners_fk = models.ForeignKey('Examiners', models.DO_NOTHING, db_column='id_Examiners_fk', blank=True, null=True)  # Field name made lowercase.
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id_evaluation)
    class Meta:
        managed = False
        db_table = 'evaluation'


class Students(models.Model):
    id_students = models.IntegerField( db_column='id_Students', primary_key=True)  # Field name made lowercase.
    name_students = models.CharField(db_column='name_Students', max_length=45, blank=True, null=True)  # Field name made lowercase.
    passwords = models.CharField(max_length=45, blank=True, null=True)
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True)  # Field name made lowercase.
    id_department_fk = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department_fk', blank=True, null=True)
    def __str__(self):
        return str(self.id_students)

    class Meta:
        managed = False
        db_table = 'students'