# The Backend Onboarding Challenge

**The Backend Onboarding Challenge**는 Django와 Docker를 활용하여 인증 기능을 구현하고, AWS EC2에 배포하는 백엔드 프로젝트입니다.
이 프로젝트를 통해 JWT 인증, Django 기반의 백엔드 개발, 테스트 코드 작성, AWS 배포 등을 실습할 수 있습니다.

---
## 👀 주요 기능

- JWT 기반 사용자 인증 (회원가입, 로그인, 토큰 발급)
- Swagger UI를 통한 API 문서화
- PostgreSQL을 사용한 데이터 저장
- Docker를 활용한 컨테이너 기반 실행 및 배포

---
## 👀 사전 학습

**👩🏻‍💻Pytest를 이용한 테스트 코드 작성법 이해**

- **Pytest**는 간결한 문법으로 테스트를 작성할 수 있는 Python 프레임워크
- `pytest-django` 플러그인을 통해 Django 프로젝트의 모델과 뷰를 테스트
- **Fixture**를 사용해 반복적인 테스트 준비 작업을 자동화하고 재사용 가능
- Pytest는 테스트 실패 시 상세한 오류 메시지를 제공하여 문제를 빠르게 파악
- **Assertion**을 통해 코드의 예상 결과와 실제 결과를 비교하여 자동으로 검증

**👩🏻‍💻Django를 이용한 인증과 권한 이해**

- Django는 사용자 인증을 위해 기본적으로 `User` 모델을 제공하며, 이를 확장하여 다양한 인증 시스템을 구축
- **JWT**를 사용한 인증 방식은 세션을 사용하지 않고, **Access Token**과 **Refresh Token**을 이용하여 사용자 인증을 처리
- Django에서 JWT 인증을 구현하려면 `djangorestframework-simplejwt`와 같은 라이브러리를 사용하여 토큰 발급과 검증을 관리
- Django의 **Permission** 시스템은 사용자 권한을 설정하여, 특정 뷰에 대한 접근을 제어할 수 있도록 도와줌
- **Middleware**는 요청과 응답을 처리하면서 인증 정보를 확인하거나 로그를 기록하는 등의 기능을 제공

**👩🏻‍💻 JWT 기본 이해**

- JWT는 JSON 형식의 데이터를 서명하여 인증하는 방식으로, 3부분(헤더, 페이로드, 서명)으로 구성
- **Access Token**은 제한된 시간 동안 유효하며, **Refresh Token**은 만료된 Access Token을 갱신하는 데 사용
- JWT는 **무상태(stateless)** 인증 방식으로, 서버가 세션 정보를 저장하지 않기 때문에 뛰어난 확장성과 성능
- 보안을 위해 HTTPS를 사용해 토큰을 안전하게 전송
- 이 방식은 API 인증과 정보 교환에서 널리 사용

---

## 🤖 진행 순서

### 1.  Django 폴더 생성부터, 로그인,로그아웃 api 등 필요한 파일 생성

### 1-1. 토큰 발행과 유효성 확인

- Access / Refresh Token 발행과 검증에 관한 테스트 시나리오 작성하기 (tests.py)

### 1-2. 유닛 테스트 작성

- Pytest를 이용한 JWT Unit 테스트 코드 작성해보기 (test_auth.py)
  

### 2. 백엔드 배포하고 개선하기

**2-1 . Docker에 띄우기**
![image](https://github.com/user-attachments/assets/aa10056f-ac88-4afa-9a49-f57b4f05bbbb)

**2-2 . AWS EC2에 배포하여 서비스 운영 환경 구축**
![image](https://github.com/user-attachments/assets/ad033738-a14c-41ae-9832-2d2ba4022335)


**2-2. API 접근과 검증**

- Swagger UI를 통해 API를 시각적으로 확인하고 테스트 가능하도록 설정
![image](https://github.com/user-attachments/assets/ae9a1ab1-4772-445c-a759-caf0736a75b5)



### 3. AI-assisted programming

- AI에게 코드 리뷰 받아보기
![image](https://github.com/user-attachments/assets/5db9479c-febd-4d5e-9507-729281f39b5f)

- **Refactoring**

- 피드백 받아서 코드 개선하기

- 중간중간에 pr 사용
  ![image](https://github.com/user-attachments/assets/572d9e69-9233-4213-a072-b2136c2cb923)


### 4. AWS EC2 재배포하기로 마무리
![image](https://github.com/user-attachments/assets/7794e0e5-1c9e-4b03-b910-215fc9e1d72c)

---
## 🛠 기술 스택

### Backend
- Python, Django REST Framework (DRF)
- PostgreSQL
- JWT (JSON Web Token) 인증

### Cloud/Infrastructure & Collaboration
- Docker, Docker Compose
- AWS EC2
- Gunicorn, Nginx

---
## 🛠 설치 및 실행 방법

### 로컬 환경 실행 방법

```sh
# 가상 환경 설정 및 활성화 (Windows - PowerShell 기준)
python -m venv onboardingtest
onboardingtest\Scripts\Activate.ps1

# 필수 패키지 설치
python -m pip install --upgrade pip
pip install -r requirements.txt

# 데이터베이스 마이그레이션
python manage.py migrate

# 서버 실행
python manage.py runserver
```

### Docker로 실행하는 방법

```sh
# Docker 빌드 및 실행
docker-compose up --build -d
```

### AWS 배포 방법

1. EC2 인스턴스 생성 (Ubuntu 20.04 권장)
2. SSH 접속 후 필수 패키지 설치
   ```sh
   sudo apt update && sudo apt install -y docker.io docker-compose
   ```
3. 프로젝트 코드 가져오기 (GitHub에서 clone)
   ```sh
   git clone <repository-url>
   cd The_Backend_Onboarding_Challenge
   ```
4. Docker 실행
   ```sh
   docker-compose up --build -d
   ```

---
## API 문서 (Swagger UI)

Swagger UI를 통해 API를 쉽게 테스트할 수 있습니다.

### Swagger 접속 방법

서버 실행 후 아래 URL에서 API 문서를 확인할 수 있습니다.

```
http://localhost:8000/swagger/
```

## 프로젝트 구조

```
The_Backend_Onboarding_Challenge/
├── README.md               # 프로젝트 설명 파일
├── docker-compose.yml       # Docker 컨테이너 설정 파일
├── Dockerfile               # Docker 이미지 빌드 파일
├── init.sql                 # 초기 데이터베이스 설정 파일
├── manage.py                # Django 관리 명령어 파일
├── users/                   # 사용자 관련 코드 디렉토리
│   ├── __init__.py          # 패키지 초기화 파일
│   ├── admin.py             # Django admin 설정 파일
│   ├── apps.py              # Django 애플리케이션 설정 파일
│   ├── models.py            # 데이터베이스 모델 정의 파일
│   ├── serializers.py       # 데이터 직렬화 파일
│   ├── tests/test_auth.py   # 인증 관련 테스트 파일
│   ├── tests.py             # 일반 테스트 파일
│   ├── views.py             # 요청 처리 로직 파일
│   ├── urls.py              # URL 경로 설정 파일
│   └── migrations/          # 데이터베이스 마이그레이션 파일
│       ├── __init__.py      # 마이그레이션 초기화 파일
│       └── 0001_initial.py  # 첫 번째 마이그레이션 파일
├── requirements.txt         # 필요한 파이썬 패키지 목록
└── ...                      # 기타 파일들


```

## 테스트 방법

```sh
# pytest 설치
pip install pytest pytest-django

# 테스트 실행
pytest
```

---
## Troubleshooting

### 1. `ModuleNotFoundError: No module named 'drf-yasg'` 오류 발생

**원인:** 가상 환경이 올바르게 활성화되지 않았거나 패키지가 설치되지 않음\
**해결 방법:**

```sh
pip install -r requirements.txt
```

### 2. Docker 실행 시 `ValueError: Dependency on app with no migrations: users` 오류 발생

**원인:** 마이그레이션 파일이 없거나 초기화되지 않음\
**해결 방법:**

```sh
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### 3. `JWT Token Issue: Token Expiry`
- **문제:** JWT 액세스 토큰이 만료되어 API 호출 시 "Unauthorized" 응답이 발생.
- **원인:** 액세스 토큰의 유효 기간이 짧게 설정되었거나 Refresh Token을 이용해 새로운 액세스 토큰을 발급받는 로직이 구현되지 않음.
- **해결 방법:**  
  - JWT의 만료 시간 설정을 확인하고 적절히 조정.  
  - Refresh Token을 사용하여 새로운 액세스 토큰을 발급하는 기능을 추가.

### 4. `Docker 이미지 빌드 오류`
- **문제:** Docker 이미지 빌드 중 `Permission Denied` 오류 발생.
- **원인:** Dockerfile에서 권한이 필요한 명령어(예: 파일 복사, 패키지 설치)가 실행되기 전에 권한이 부족한 경우.
- **해결 방법:**  
  - `USER` 명령어를 사용하여 적절한 권한을 가진 사용자로 전환하거나,  
  - Docker 이미지 내에서 적절한 권한을 설정.

### 5. `EC2 서버에서 Swagger UI 접근 불가`
- **문제:** EC2에서 실행 중인 서버의 Swagger UI에 접근할 수 없음.
- **원인:** EC2 인스턴스의 보안 그룹 설정에서 포트 8000이 열려 있지 않거나, Nginx 리버스 프록시 설정이 잘못됨.
- **해결 방법:**  
  - EC2의 보안 그룹에서 8000 포트를 열고,  
  - Nginx 설정에서 Swagger UI를 올바르게 라우팅하도록 수정.

### 6. `Database Connection Error after Docker Deployment`
- **문제:** Docker로 배포한 후 데이터베이스 연결 오류가 발생.
- **원인:** Docker Compose에서 데이터베이스 연결 설정이 잘못되었거나, 데이터베이스 서비스가 정상적으로 시작되지 않음.
- **해결 방법:**  
  - `docker-compose.yml` 파일에서 데이터베이스 연결 설정을 확인하고,  
  - `docker-compose logs` 명령어로 에러 로그를 확인하여 문제를 해결.

### 7. `Pytest: Database not initialized`
- **문제:** pytest를 실행할 때 데이터베이스가 초기화되지 않아 테스트가 실패.
- **원인:** 테스트 데이터베이스가 설정되지 않았거나, 마이그레이션이 제대로 적용되지 않음.
- **해결 방법:**  
  - `pytest-django`의 `DATABASES` 설정을 확인하고, 테스트 전에 마이그레이션을 적용.

## 기여 방법

- Pull Request를 통해 기능 추가 및 버그 및 충돌 수정 
- 기존 공부한 것들을 최대한 활용 및 ai 리뷰의 도움



