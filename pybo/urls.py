from django.urls import path, include
from .views import HelloAPI, questionsAPI, questionsById, QuestionsAPI, QuestionsByAPI
urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/questions/', questionsAPI),
    path('fbv/questions/<int:id>/', questionsById),
    path('cbv/questions/', QuestionsAPI.as_view()),
    path('cbv/questions/<int:id>/', QuestionsByAPI.as_view()),

]