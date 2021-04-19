from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from Quiz.views import login_auth_implementation
from Rest_Api.views import (list_all_quiz_categories,Create_quiz,get_user_created_quiz,
                            create_question,list_all_quiz,get_questions,Take_Quiz,get_question_answer
                            ,get_answer,quiz_home)
from django.urls import include, path
# from views import Auth_Implementation

# http://127.0.0.1:8000/quiz-api/home/
urlpatterns = [
    path('home/',quiz_home.as_view(),name="quiz-home"),
    path('get_categories/',list_all_quiz_categories.as_view(),name="get-category"),
    path('register_quiz/',Create_quiz.as_view(),name="Quiz-register"),
    path('list_quiz/',list_all_quiz.as_view(),name="list_quiz"),
    path('get_user_quiz/',get_user_created_quiz.as_view(),name="user_created_quiz"),
    path('register_question/',create_question.as_view(),name="register_question"),
    path('api/<str:quiz_name>/',get_questions.as_view(),name="get_questions"),
    path('api/<str:quiz_name>/<int:question_id>/',get_question_answer.as_view(),name="get_question_answer"),
    path('api/<str:quiz_name>/answer/<int:question_id>/',get_answer.as_view(),name="get_answer"),
    path('home/<str:quiz_name>/',Take_Quiz.as_view(),name="take_quiz"),
    path('quiz-creator/', TemplateView.as_view(template_name="Rest_Api/quiz_creator.html"),name="quiz-creator")
]
urlpatterns += [path('api-auth/', include('rest_framework.urls')),]

