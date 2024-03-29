# ReadME



### 1. 목표

- 거래소가 제공하는 API를 둘러보고, 파이썬으로 트레이딩 가능한 모듈을 만든다.
- 암호화폐 가격 데이터를 저장, 가공, 분석한다.
- 나만의 트레이딩 로직을 구현해 자동으로 동작하는 시스템을 만든다.
- Git을 통한 소스코드 버전 관리 및 협업
- 서비스 배포





### 2. 개발환경

- Python Web Framework
  - Django 2.1.8
  - Python 3.6.7


- 사용 라이브러리

  ```shell
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  
  exec "$SHELL"
  
  pyenv install 3.6.7
  pyenv global 3.6.7
  
  pip install --upgrade pip
  
  pip install django==2.1.8
  
  pip install django-bootstrap4
  
  pip install pybithumb
  ```



### 3. 서비스 아키텍쳐

- 데이터베이스 모델링

  - Coin
    - name
    - check_price
    - complete_price
    - max_price
    - today_result
    - result_date


- 핵심 기능

  - 거래소 데이터 파싱
  - 자동 거래(알고리즘에 의거함)



### 4. 참고 문헌

- [**누구나 할 수 있다. 비트코인 자동매매**](https://wikidocs.net/21887)


- [**학습 계획서 및 학습 정리**](https://drive.google.com/file/d/1FFHVmQEkoFWH0tfB-ovqep12Nrh-L3vm/view?usp=sharing)