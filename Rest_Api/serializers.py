from rest_framework import serializers
from Quiz.models import Quiz_Categories,Quiz,Questions_Answers,Quiz_User_Anaytics


class Category_serializers(serializers.ModelSerializer):

    class Meta:
        model = Quiz_Categories
        fields = '__all__'

class Quiz_Serializer(serializers.ModelSerializer):
    quiz_category=Category_serializers()
    total_count=serializers.SerializerMethodField()
    class Meta:
        model=Quiz
        fields=["id","quiz_name","quiz_category","quiz_difficulty","created_by","total_count"]
    def get_total_count(self,obj):
        return obj.get_all_questions.all().count()

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

