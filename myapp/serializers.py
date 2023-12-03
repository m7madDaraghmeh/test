from rest_framework import serializers, status
from .models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data.get('title')


        if Book.objects.filter(title=title).exists():
            validator =  serializers.ValidationError({"details": "This record already exists with the same title"})
            validator.status_code = status.HTTP_409_CONFLICT
            raise validator

        return data
      
        
