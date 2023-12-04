from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('name', 'author', 'isbn', 'year')
        read_only_fields = ('created_at',)
