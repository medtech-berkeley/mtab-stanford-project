from rest_framework import serializers
from .models import Question, QuestionUserData, Category, Answer, Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'name', 'location', 'description', 'image', 'completed_survey')

class SmallStudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = ('user',)

class CategorySerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='text', allow_null=True)
    class Meta:
        model = Category
        fields = ('name', 'start', 'end', 'sponsor', 'is_challenge', 'image', 'tags')

class AnswerSerializer(serializers.ModelSerializer):
    # TODO: Get rid of is_correct in serializer
    class Meta:
        model = Answer
        fields = ('id', 'text', 'is_correct')

class SecureAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('is_correct',)

class QuestionUserDataSerializer(serializers.ModelSerializer):
    student = SmallStudentSerializer()
    answer = SecureAnswerSerializer()
    class Meta:
        model = QuestionUserData
        fields = ('student', 'question', 'answer', 'time_started', 'time_completed')

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'category', 'text', 'answers', 'created', 'max_time')


class StudentStatsSerializer(serializers.Serializer):
    name = serializers.CharField()
    subjects = serializers.DictField()
    questions_answered = serializers.IntegerField()
    num_correct = serializers.IntegerField()
    num_incorrect = serializers.IntegerField()
