from rest_framework import serializers
from Quiz.models import Quiz_Categories,Quiz,Questions_Answers,Quiz_User_Anaytics


class Category_serializers(serializers.ModelSerializer):

    class Meta:
        model = Quiz_Categories
        fields = '__all__'

class Quiz_Serializer(serializers.ModelSerializer):
    quiz_category=Category_serializers()
    class Meta:
        model=Quiz
        fields='__all__'

class custom_quiz_name_serializers(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=['quiz_name']

class Question_Answers_serializers(serializers.ModelSerializer):

    class Meta:
        model=Questions_Answers
        fields=['id','question_name','question_type','question_options','answer_score']

class Question_Answers_id_serializers(serializers.ModelSerializer):
    class Meta:
        model= Questions_Answers
        fields=['id']

