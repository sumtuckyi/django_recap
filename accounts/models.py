from django.db import models
# Django가 사용하는 default User 모델 기반으로 개발을 할 것이라면
# 기존 클래스를 상속하면 된다.
from django.contrib.auth.models import AbstractUser 
# Create your models here.
# 필드 수정 등 추가적인 작업을 위해 상속을 받아 필요에 따라 정의(커스텀-나만의 User class)
class User(AbstractUser):
    pass