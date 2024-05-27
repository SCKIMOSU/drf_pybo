from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

@api_view(['GET'])
def HelloAPI(request):
    return Response("hello pybo")

# FBV
@api_view(['GET', 'POST'])
def questionsAPI(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def questionsById(request, id):
    question = get_object_or_404(Question, pk=id)
    serializer = QuestionSerializer(question)
    return Response(serializer.data, status=status.HTTP_200_OK)

# CBV
class QuestionsAPI(APIView): # viewsets.ModelViewSet
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BooksAPI(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionsByAPI(APIView):
    def get(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HelloAPI(APIView):
    def get(self, request):
        return Response("hello pybo")



