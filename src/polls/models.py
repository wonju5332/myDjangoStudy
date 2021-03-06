import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# 각 모델은 django.db.model.Model이라는 클래스의 서브 클래스로 표현된다.
# 각 인스턴스의 이름은 데이터베이스 필드의 이름과 동일하게!

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data Published')
    def __str__(self):
        return "Question : " + self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    '''
    각각의 choice가 하나의 Question과 연관된다는 것을 정의하기 위해, foreignkey로 정의..
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

