from .models import LoanBook
from rest_framework import serializers

class LoanSerailizer(serializers.ModelSerializer):
    class Meta:
        model = LoanBook
        fields = "__all__"

        