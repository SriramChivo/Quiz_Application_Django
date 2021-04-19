from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# class Quiz_Category(models.Model):
#     Quiz_Category_name=
# difficulty_CHOICES = [
#     ('ea', 'Easy'),
#     ('me', 'Medium'),
#     ('diff', 'Expert'),
# ]
# question_type_CHOICES=[
#     ("multichoice","Multi Choice Question"),
#     ("multiselect","Multi Select Question"),
#     ("Bool","Boolean Question"),
#     ("text","accept Text Question")
# ]

class Quiz_Categories(models.Model):
    category=models.CharField(max_length=30,blank=False)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural="Quiz_Category"

class Quiz(models.Model):

    quiz_name=models.CharField(max_length=30,unique=True,blank=False)
    quiz_category=models.ForeignKey(Quiz_Categories,on_delete=models.CASCADE)
    quiz_difficulty=models.CharField(max_length=30,blank=False)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="get_all_quizes")

    def __str__(self):
        return self.quiz_name
        
    class Meta:
        verbose_name_plural = "Quiz_info"

class Questions_Answers(models.Model):

    quiz_id=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="get_all_questions")
    question_name=models.CharField(max_length=250,blank=False)
    question_type=models.CharField(max_length=30,blank=False)
    question_options=models.JSONField()
    answers=models.CharField(max_length=250,blank=False)
    answer_score=models.CharField(max_length=5,default="10")

    def __str__(self):
        return self.question_name
    
    class Meta:
        verbose_name_plural = "Question_Answers"

class Quiz_User_Anaytics(models.Model):

    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.CharField(max_length=5,blank=True)

    def __str__(self):
        return f'{self.user}_{self.score}'
    
    class Meta:
        verbose_name_plural = "Quiz_User_Anaytics"