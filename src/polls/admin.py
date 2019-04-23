from django.contrib import admin
from .models import Choice,Question

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

# ChoiceInLine을 Stack --> Tab 형태로.
class ChoiceInline(admin.TabularInline):
    model = Choice # 모델은 Choice이며,
    extra = 3 #  기본적으로, 3개의 choice 칸을 생성해놓겠다.

class questionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['question_text']} ),
        ('Date information', {'fields': ['pub_date'],
                              'classes':['collapse']} ) # 'class' : 'collapse' --> hideBoxFrame
    ]
    inlines = [ChoiceInline] # Question 모델에서 Choice 까지.
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']  # 화면 우측에 해당 컬럼을 기준으로 필터생성
    search_fields = ['question_text'] # 사이트 내 해당 컬럼 기준으로 검색창 생성




admin.site.register(Question, questionAdmin)
admin.site.register(Choice)
# Register your models here.
