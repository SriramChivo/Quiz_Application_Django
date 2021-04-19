from django.contrib import admin
from .models import Questions_Answers,Quiz,Quiz_User_Anaytics,Quiz_Categories

admin.site.register(Questions_Answers)
admin.site.register(Quiz)
admin.site.register(Quiz_User_Anaytics)
admin.site.register(Quiz_Categories)