from rest_framework import serializers
from .models import User, ClubCard, Feedback


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'is_admin', ]
        extra_kwargs = {
            'password': {'write_only', True}
        }


class ClubCard(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = ClubCard
        fields = ['owner', 'balance', 'discount_value']


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Feedback
        fields = ['user', 'description']
