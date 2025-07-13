from rest_framework import serializers
from .models import Category,Books,Author
from rest_framework.exceptions import ValidationError

class BooksSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


    def validate(self,data):
        title = data.get('title',None)
        price = data.get('price',None)

        if not title.isalpha():
            context = {
                'status':False,
                'massage':'Hariplerden qollanilmadi'
            }
            raise ValidationError(context)
        if Books.objects.filter(title=title).exists():
            context = {
                'status':False,
                'massage':'Onday kitap uje bar'
            }
class CategorySerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'