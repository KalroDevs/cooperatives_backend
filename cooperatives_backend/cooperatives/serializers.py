# cooperatives/serializers.py
from rest_framework import serializers
from .models import *

class CooperativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperative
        fields = [
            'organization_name',
            'secretariate_county',
            'secretariate_sub_county',
            'secretariate_ward',
            'gps_latitude',
            'gps_longitude',
            'gps_altitude',
            'gps_precision',
            'organization_type',
            'registration_status',
            'registration_number',
            'registration_date',
            'registered_office_address',            
            'is_automated',
            'common_bond',
            'previous_year_membership',
            'institutional_membership',
            'male_membership',
            'female_membership',
            'male_youth_membership',
            'female_youth_membership',
            'indigenous_membership',
            'cig_federated_count',
            'cig_membership_count',
            'vmg_federated_count',
            'vmg_membership_count',
        ]


# cooperatives/serializers.py


class BookKeeperRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookKeeperRegister
        fields = '__all__'

class SACCOGrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmountsDisbursedToOrganisations
        fields = '__all__'

class MemberRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRegister
        fields = '__all__'

class SACCOShareCapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberSavings
        fields = '__all__'

class SACCOLoanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanType
        fields = '__all__'

class LoansIssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoansIssued
        fields = '__all__'

class LoansPaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoansPaid
        fields = '__all__'
