from rest_framework import serializers
from test_tas.models import Applicantprofile, Offer

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applicantprofile
        fields = ('studentnumber', 'familyname', 'givennames', )

class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = ('courseofferingid', 'appuserid', 'offerstatus', 'offerhours', 'offerappointments' )


