from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # Add a new field to the serializer that will not be saved in the database. Calculate field
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    # get_<field_name> is the standard for creating methods that return calculated field values.
    def get_rate(self, obj):
        # It uses the related_name of the ForeignKey field in the Review model.
        # ["stars__avg"] is used to get the average of the stars field in the Review model.
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return round(rate, 1)

        return None

        # reviews = obj.reviews.all()
        # if reviews:
        #     return round(sum(review.stars for review in reviews) / len(reviews), 1)

    # The method name should be validate_<field_name>
    def validate_release_date(self, value):
        # The year is an attribute of value, which is an object of type datetime.date.
        if value.year < 1900:
            raise serializers.ValidationError("Release date must be after 1900")
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("Resume must be 200 characters or less")
        return value
