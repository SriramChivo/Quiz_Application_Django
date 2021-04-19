from django.test import TestCase
from Rest_Api.models import Quiz_Categories,Quiz,Questions_Answers
from Rest_Api.serializers import Category_serializers
from Rest_Api.results import cat_results,quiz_results,question

# Create your tests here.

class get_answer(TestCase):

    data={
        "ques_id"="1"
    }

    def update(self):

        get_data=self.data

        collection_obj=Questions_Answers.objects.get(id=get_data["ques_id"]])
        get_ans=collection_obj.answers
        self.assertEqual(get_ans, "a")

class get_question(TestCase):

    data={
        "ques_id"="1"
    }

    def update(self):

        get_data=self.data

        collection_obj=Questions_Answers.objects.get(id=get_data["ques_id"]])
        get_int=collection_obj.pk
        self.assertEqual(get_int, 1)
    

class getcategories(TestCase):

    def get_categories(self):
        result=Quiz_Categories.objects.all()
        get_serialized_data=Category_serializers(result,many=True)
        result_expected = JSONRenderer().render(get_serialized_data.data)
        self.assertQuerysetEqual(cat_results == result)

class get_all_quizes(TestCase):

    def test(self):
        result=Quiz.objects.all()
        self.assertQuerysetEqual(quiz_results== result)

class create_quiz(TestCase):
    
    data={
        "quiz_name":"test_quiz",
        "quiz_category":0,
        "quiz_difficulty":"Easy",
        "created_by":0
    }

    def test(self):
        get_data=self.data

        get_cat=Quiz_Categories.objects.get(id=get_data["quiz_category"])

        get_user=Quiz_Categories.objects.get(created_by=get_data["created_by"])

        collection_obj=Quiz.objects.create(quiz_name=get_data["quiz_name"],quiz_category=get_cat,quiz_difficulty=get_data["quiz_difficulty"],created_by=get_user)

        self.assertIsInstance(collection_obj, object)

def create_question(TestCase):

    data={
        "question"="Is python used for web development?",
        "question_type"="True/False",
        "question_options"={
            "0":"True",
            "1"="False"
        }
        "answers":"a",
        "answer_score":"10"
    }

    def test(self):
        get_data=self.data

        que_create=Questions_Answers.objects.create(question=get_data["question"],question_type=get_data["question_type"],options=get_data["question_options"],answers=get_data["answers"],answer_score=get_data["answer_score"])

        return assertIsInstance(que_create,object)







    
