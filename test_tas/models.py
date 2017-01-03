# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Applicantprofile(models.Model):
    appuserid = models.ForeignKey('Appuser', models.DO_NOTHING, db_column='appuserid', primary_key=True)
    studentnumber = models.CharField(max_length=10, blank=True, null=True)
    familyname = models.CharField(max_length=50)
    givennames = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20)
    emailaddress = models.CharField(max_length=50)
    personnelnumber = models.CharField(max_length=20, blank=True, null=True)
    workstatus = models.CharField(max_length=2)
    workstatusexplain = models.CharField(max_length=50, blank=True, null=True)
    studentstatus = models.CharField(max_length=5)
    studentstatusexplain = models.CharField(max_length=50, blank=True, null=True)
    studentdepartment = models.CharField(max_length=5)
    studentdepartmentexplain = models.CharField(max_length=50, blank=True, null=True)
    creditscompleted = models.IntegerField()
    csc_experience = models.TextField(blank=True, null=True)
    csc_coursescompleted = models.TextField(blank=True, null=True)
    csc_coursesinprogress = models.TextField(blank=True, null=True)
    otherinfo = models.TextField(blank=True, null=True)
    sectionswanted = models.IntegerField()
    sectionsowed = models.IntegerField()
    reading = models.IntegerField()
    writing = models.IntegerField()
    conversation = models.IntegerField()
    deptsectionsowed = models.FloatField()
    depthoursowed = models.FloatField()
    mathematics_experience = models.TextField(blank=True, null=True)
    studentstatusyear = models.IntegerField(blank=True, null=True)
    sahoursowed = models.FloatField(blank=True, null=True)
    grant_academichistory = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'applicantprofile'


class Applicantskilllevel(models.Model):
    appuserid = models.ForeignKey('Appuser', models.DO_NOTHING, db_column='appuserid', blank=True, null=True)
    skillid = models.ForeignKey('Skill', models.DO_NOTHING, db_column='skillid', blank=True, null=True)
    skilllevel = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'applicantskilllevel'


class Application(models.Model):
    courseofferingid = models.ForeignKey('Courseoffering', models.DO_NOTHING, db_column='courseofferingid')
    appuserid = models.ForeignKey('Appuser', models.DO_NOTHING, db_column='appuserid')
    preference = models.IntegerField(blank=True, null=True)
    previousappointments = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application'
        unique_together = (('courseofferingid', 'appuserid'),)


class Appuser(models.Model):
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    role = models.ForeignKey('Role', models.DO_NOTHING, db_column='role', blank=True, null=True)
    aut_code = models.ForeignKey('AppuserType', models.DO_NOTHING, db_column='aut_code')
    aut_termcode = models.ForeignKey('Term', models.DO_NOTHING, db_column='aut_termcode', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.email)

    class Meta:
        managed = False
        db_table = 'appuser'


class AppuserType(models.Model):
    aut_code = models.CharField(primary_key=True, max_length=6)

    def __str__(self):
        return '{}'.format(self.aut_code)

    class Meta:
        managed = False
        db_table = 'appuser_type'


class Campus(models.Model):
    campus = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'campus'


class Courseoffering(models.Model):
    courseofferingid = models.AutoField(primary_key=True)
    campus = models.ForeignKey(Campus, models.DO_NOTHING, db_column='campus', blank=True, null=True)
    department = models.ForeignKey('Department', models.DO_NOTHING, db_column='department', blank=True, null=True)
    termcode = models.ForeignKey('Term', models.DO_NOTHING, db_column='termcode', blank=True, null=True)
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    enrollment = models.IntegerField(blank=True, null=True)
    minpositions = models.IntegerField(blank=True, null=True)
    maxpositions = models.IntegerField(blank=True, null=True)
    appointmenthours = models.IntegerField(blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    duties = models.TextField(blank=True, null=True)
    course_level = models.CharField(max_length=1)

    def __str__(self):
        return '{} {} {}'.format(self.termcode, self.code, self.title)


    class Meta:
        managed = False
        db_table = 'courseoffering'
        unique_together = (('campus', 'department', 'termcode', 'code'),)


class Coursetime(models.Model):
    coursetimeid = models.AutoField(primary_key=True)
    courseofferingid = models.ForeignKey(Courseoffering, models.DO_NOTHING, db_column='courseofferingid', blank=True, null=True)
    section = models.CharField(max_length=10, blank=True, null=True)
    instructor = models.CharField(max_length=100, blank=True, null=True)
    day = models.ForeignKey('Dayinfo', models.DO_NOTHING, db_column='day', blank=True, null=True)
    starttime = models.CharField(max_length=7, blank=True, null=True)
    endtime = models.CharField(max_length=7, blank=True, null=True)
    room = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coursetime'
        unique_together = (('courseofferingid', 'section', 'day', 'starttime', 'endtime', 'room'),)


class Dayinfo(models.Model):
    code = models.CharField(primary_key=True, max_length=2)
    dayorder = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dayinfo'


class Department(models.Model):
    department = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return '{}'.format(self.department)

    class Meta:
        managed = False
        db_table = 'department'


class Offer(models.Model):
    courseofferingid = models.ForeignKey(Courseoffering, models.DO_NOTHING, db_column='courseofferingid')
    appuserid = models.ForeignKey(Appuser, models.DO_NOTHING, db_column='appuserid', primary_key=True)
    offerstatus = models.IntegerField(blank=True, null=True)
    offerhours = models.FloatField(blank=True, null=True)
    offerappointments = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer'
        unique_together = (('courseofferingid', 'appuserid'),)


class Role(models.Model):
    rolename = models.CharField(primary_key=True, max_length=10)

    def __str__(self):
        return '{}'.format(self.rolename)

    class Meta:
        managed = False
        db_table = 'role'


class Skill(models.Model):
    skillid = models.AutoField(primary_key=True)
    skillname = models.CharField(max_length=30, blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department', blank=True, null=True)

    def __str__(self):
        return '{} at {}'.format(self.skillname, self.department)

    class Meta:
        managed = False
        db_table = 'skill'


class Term(models.Model):
    termcode = models.IntegerField(primary_key=True)
    iscurrentterm = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.termcode)

    class Meta:
        managed = False
        db_table = 'term'


class Unavailabletimes(models.Model):
    appuserid = models.ForeignKey(Appuser, models.DO_NOTHING, db_column='appuserid')
    day = models.ForeignKey(Dayinfo, models.DO_NOTHING, db_column='day')
    hour = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unavailabletimes'
        unique_together = (('appuserid', 'day', 'hour'),)
