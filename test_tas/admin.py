from django.contrib import admin
from .models import Appuser, Applicantprofile, Applicantskilllevel, Offer

class ApplicantprofileInline(admin.StackedInline):
    model = Applicantprofile

class ApplicantskilllevelInline(admin.TabularInline):
    model = Applicantskilllevel

# Register your models here.
@admin.register(Appuser)
class AppuserAdmin(admin.ModelAdmin):
    inlines = [ApplicantprofileInline, ApplicantskilllevelInline, ]

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('courseofferingid', 'appuserid', 'offerstatus')
    list_filter = ('courseofferingid__termcode', )
