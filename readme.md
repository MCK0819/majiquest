# Majiquest

현실 퀘스트 요청/완료 게시판 페이지

## 기술 스택

python3.9 , postgresql, django, django-restframework,

### Prerequisites / 선행 조건
커맨드를 입력하면 필요한 라이브러리들이 설치됩니다.
```
pip install -r requirements.txt
```
## Running the tests / 테스트의 실행
```
coverage run manage.py test
```
### 테스트는 이런 식으로 동작합니다

```
coverage report # console 창에서 테스트 현황을 보여줍니다.
coverage html # html으로 테스트 커버리지 현황을 볼수있습니다.

```

## Deployment / 배포

```
name: Django CI

on:
  push:
    branches: [ "master", "dev" ]
  pull_request:
    branches: [ "master" ]

jobs:
  build:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:latest
        env:
          POSTGRES_DB: majiquest
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        ports:
          - 5433:5432
        options: --health-cmd pg_isready --health-interval 10s --health-timeout 5s --health-retries 5

    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.9]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      env:
        SECRET_KEY: ${{ secrets.SECRET_KEY }}
        DB_NAME: ${{ secrets.DB_NAME }}
        DB_HOST: ${{ secrets.DB_HOST }}
        DB_USER: ${{ secrets.DB_USER }}
        DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
      run: |
        python manage.py test
```

## License / 라이센스
This project is licensed under the MIT License - see the [LICENSE.md](https://gist.github.com/PurpleBooth/LICENSE.md) file for details / 이 프로젝트는 MIT 라이센스로 라이센스가 부여되어 있습니다. 자세한 내용은 LICENSE.md 파일을 참고하세요.
