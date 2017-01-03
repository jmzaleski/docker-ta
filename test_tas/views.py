from rest_framework import viewsets
from test_tas.serializers import AppSerializer, OfferSerializer
from .models import Applicantprofile, Offer

class AppViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Applicantprofile.objects.all()
    serializer_class = AppSerializer

class OfferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
