from rest_framework import serializers

from main.models import Book, Order


class BookSerializer(serializers.ModelSerializer): #Для сериализации книг, укажите в нём все поля
    # реализуйте сериализацию объектов модели Book
    class Meta:
        model = Book
        fields = '__all__'

        #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['orders_count'] = ...
    #     return representation


class OrderSerializer(serializers.ModelSerializer): # Для сериализации заказов, укажите в нём все поля
    # добавьте поля модели Order
    class Meta:
        model = Order
        fields = '__all__'

    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['books'] = ...
    #     return representation
