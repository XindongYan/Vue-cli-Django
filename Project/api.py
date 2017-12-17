from Project.models import Book

# 序列化器，把数据包装成类似字典的格式
from rest_framework import serializers

# 这两个模块把序列化后的数据包装成 api
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 创建一个 Book 的序列化器
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # 序列化的对象
        fields = '__all__'  # 序列化的属性


@api_view(['GET'])  # 装饰器，使得 book 函数具有 api_view 的相关方法
def book(request):
    book_list = Book.objects.all() # Book 的全部数据
    serializer = BookSerializer(book_list, many=True) # 序列化 Book 的数据
    return Response(serializer.data)