from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Order
from .serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request):
    # """получите список книг из БД
    # отсериализуйте и верните ответ"""
    all_books = Book.objects.all()
    serializer = BookSerializer(all_books, many=True)
    return Response(serializer.data)


class CreateBookView(APIView):
    def post(self, request):
        #получите данные из запроса
        data = request.data# to deserialize data
        serializer = BookSerializer(data=data)  #передайте данные из запроса в сериализатор
        if serializer.is_valid(raise_exception=True): #если данные валидны
            serializer.save() # to create a new book
            return Response('Книга успешно создана')  # возвращаем ответ об этом


class BookDetailsView(RetrieveAPIView):
    # реализуйте логику получения деталей одного объявления
    queryset = Book.objects.all()
    lookup_field = 'pk'
    serializer_class = BookSerializer

class BookUpdateView(UpdateAPIView):
    # реализуйте логику обновления объявления
    queryset = Book.objects.all()
    lookup_field = 'pk'
    serializer_class = BookSerializer

class BookDeleteView(DestroyAPIView):
    # реализуйте логику удаления объявления
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderViewSet(viewsets.ModelViewSet):
    # реализуйте CRUD для заказов
    queryset = Order.objects.all()
    serializer_class = OrderSerializer





