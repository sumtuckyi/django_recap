from django.shortcuts import render, redirect
# 사용자 인증을 위한 데이터를 입력받고자 하는 경우 django가 기본적으로 제공하는 Form을 사용
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout


# Create your views here.
def index(request):
    # html파일이 위치한 app이름을 경로로 사용(앱마다 동일한 이름의 HTML파일이 존재할 수도 있기 때문에)
    return render(request, 'accounts/index.html')

# 요청이 GET인 경우라면 로그인 페이지를 렌더링 / 요청이 POST인 경우라면 실제 로그인 로직을 구현
# 세션 아이디를 생성하고 데이터베이스에 저장한뒤 클라이언트에 전달 
def login(request):
    print(request.POST)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")
        print(form.errors)
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, "accounts/login.html", context)

# 데이터 베이스의 세션 아이디를 삭제 
def logout(request):
    auth_logout(request)
    return redirect("accounts:index")