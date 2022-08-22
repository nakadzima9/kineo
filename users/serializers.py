from rest_framework import serializers
from booking.models import Ticket
from .models import User, ClubCard, Feedback


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
        ]
        extra_kwargs = {"password": {"write_only", True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "username"]


class ClubCardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    balance = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ClubCard
        fields = ["id", "user", "balance", "discount_value"]

    def get_balance(self, obj):
        orders = Ticket.objects.filter(user=obj.owner)
        balance = 0
        for i in orders:
            balance += i.price
            if balance > 10000:
                obj.discount_value = 3
            if balance > 15000:
                obj.discount_value = 5
            if balance > 20000:
                obj.discount_value = 7
        return balance


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Feedback
        fields = ["id", "user", "description"]
