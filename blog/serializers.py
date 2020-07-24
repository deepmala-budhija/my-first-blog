from rest_framework import serializers

from .models import LineListing

class LineListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LineListing
        fields = ('village','house_number','household_number','survey_date','person_name_collecting_data',)