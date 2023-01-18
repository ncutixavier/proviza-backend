from django.shortcuts import render
from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer

# Create your views here.
class QuestionsList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionUpdate(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDelete(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
