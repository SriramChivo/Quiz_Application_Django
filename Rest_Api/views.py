from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from Quiz.models import Quiz_Categories,Quiz,Questions_Answers,Quiz_User_Anaytics
from Rest_Api.serializers import (Category_serializers,Quiz_Serializer,
                                    custom_quiz_name_serializers,Question_Answers_id_serializers,
                                    Question_Answers_serializers)
from rest_framework.renderers import JSONRenderer
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.
User = get_user_model()


class quiz_home(View):
    

    def get(self,request):
        if(not request.user.is_authenticated):
            return HttpResponseRedirect(reverse("auth-implementation"))
        return render(request,"Rest_Api/quiz_home.html")

class list_all_quiz_categories(APIView,LoginRequiredMixin):

    renderer_classes = [JSONRenderer]

    def get(self,request):
        get_all_Quiz_Categories=Quiz_Categories.objects.all()
        serialized_response=Category_serializers(get_all_Quiz_Categories,many=True)
        return Response({"Categories":serialized_response.data})

class list_all_quiz(APIView,LoginRequiredMixin):

    def get(self,request):
        get_all_Quiz_Categories=Quiz.objects.all()
        serialized_response=Quiz_Serializer(get_all_Quiz_Categories,many=True)
        jsonified_response = JSONRenderer().render(serialized_response.data)
        return Response(jsonified_response)

class Create_quiz(APIView,LoginRequiredMixin):

    renderer_classes = [JSONRenderer]

    def post(self,request):

        payload_received=request.data
        get_quiz_name=payload_received["quiz_name"]
        get_quiz_category=payload_received["get_quiz_category"]
        get_quiz_difficulty=payload_received["get_quiz_difficulty"]

        print(get_quiz_name,get_quiz_category,get_quiz_difficulty)

        try:
            check_quiz_exist=Quiz.objects.get(quiz_name=get_quiz_name)
            return Response({"Is_Created":"already exist"})
        except:
            pass

        try:
            get_quiz_category=Quiz_Categories.objects.get(category=get_quiz_category)
            get_user=User.objects.get(id=request.user.pk)
            quiz_object_creation=Quiz.objects.create(quiz_name=get_quiz_name,quiz_category=get_quiz_category,quiz_difficulty=get_quiz_difficulty,created_by=get_user)
            return Response({"Is_Created":'true',"quiz_id":str(quiz_object_creation.quiz_name)})
        except Exception as e:
            print(e)
            return Response({"Is_Created":'False'})

class get_user_created_quiz(APIView,LoginRequiredMixin):

    renderer_classes=[JSONRenderer]

    def get(self,request):
        try:
            get_user=User.objects.get(username=request.user.username)
            get_all_user_created_quiz= get_user.get_all_quizes.all()
            print(get_all_user_created_quiz)
            get_all_user_created_quiz=custom_quiz_name_serializers(get_all_user_created_quiz,many=True)
            response_format={
                "All_Quizes":get_all_user_created_quiz.data
            }
            return Response(response_format)
        except Exception as e:
            print(e)
            return Response({
                "Message":"Error"
            })

class create_question(APIView,LoginRequiredMixin):

    renderer_classes=[JSONRenderer]

    def post(self,request):
        payload_received=request.data
        print(payload_received)
        get_question=payload_received["question"]
        get_question_type=payload_received["question_type"]
        score=payload_received["score"]
        answer=payload_received["answer"].lower()
        quiz_id=payload_received["quiz_name"]
        get_quiz_obj=Quiz.objects.get(quiz_name=quiz_id)
        try:
            get_options=payload_received["options"]
            # print(get_options)
            # get_options=json.dumps(get_options)
        except Exception as err:
            print(err)
            get_options=json.dumps({})
        
        print(get_question,get_question_type,score,answer)
        print(get_options)
        print(get_quiz_obj)
        
        try:
            question_added=Questions_Answers.objects.create(quiz_id=get_quiz_obj,question_name=get_question,question_type=get_question_type,question_options=get_options,answers=answer,answer_score=score)
            print(question_added)
            return Response({"Is_Created":'true'})
        except Exception as e:
            print(e)

class Take_Quiz(TemplateView,LoginRequiredMixin):

    template_name = "Rest_Api/quiz_main.html"

    def get_context_data(self,quiz_name,**kwargs):
        # print(quiz_name)
        context = super().get_context_data(**kwargs)
        context['Questions_url'] = reverse("get_questions",kwargs={"quiz_name":quiz_name})
        return context

class get_questions(APIView):

    renderer_classes=[JSONRenderer]
    
    def get(self,request,quiz_name):

        get_quiz_object= Quiz.objects.get(quiz_name=quiz_name)
        get_all_the_questions=get_quiz_object.get_all_questions.all()
        get_total_score=get_quiz_object.get_all_questions.values("answer_score")
        get_all_question_id=get_quiz_object.get_all_questions.values("id")
        quiz_id=[]
        for each in get_all_question_id:
            quiz_id.append(each['id'])
        tot_score=0
        for each in get_total_score:
            tot_score+=int(each['answer_score'])
        # print(get_total_score)
        print(quiz_id)
        # get_all_questions=Question_Answers_id_serializers(get_all_the_questions,many=True)
        return Response({
            "questions_ids":quiz_id,
            'total_score':str(tot_score)
        })

class get_question_answer(APIView,LoginRequiredMixin):

    renderer_classes=[JSONRenderer]

    def get(self,request,question_id,quiz_name):

        get_question=Questions_Answers.objects.get(id=question_id)
        get_serialized=Question_Answers_serializers(get_question)
        return Response(get_serialized.data)

class get_answer(APIView,LoginRequiredMixin):

    renderer_classes=[JSONRenderer]

    def get(self,request,question_id,quiz_name):
        get_question=Questions_Answers.objects.get(id=question_id)
        return Response({
            "Answer":get_question.answers
        })




















