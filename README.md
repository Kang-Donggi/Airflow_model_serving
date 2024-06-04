#### Airflow의 핵심 개념

1. DAGs(directed acyclic graphs) : airflow에서 작업을 정의하는 방법, 작업의 흐름과 순서 정의
2. operator : airflow의 작업 유형을 나타내는 클래스, bashoperator, pythonoperator, sqloperator 등 다양한 operator 존재
3.  Scheduler : airflow의 핵심 구성 요수 중 하나, DAGs를 보며 현재 실행하야 하는지 스케줄 확인
DAGs의 실행을 관리하고 스케줄링
4. Executor : LocalExcutor, CeleryExcutor 등 다양한 executor가 존재

#### 기본 아키텍처

- DAG directory: DAG 파일들을 저장, DAG_FOLDER 라고도 부르며 이 폴더 내부에 폴더 구조를 어떻게 두어도 상관 없음, scheduler에 의해 .py 파일은 모두 탐색되고 DAG이 파싱
- Operator: batch scheduling을 위한  DAG을 생성 airflow에서는 스케줄링할 작업을 DAG라고 부름, 순환하지 않는 방향이 존재하는 그래프 의미
단순히 하나의 파일 실행이 아닌 여러 작업의 조합도 가능
task: DAG 내에서 실행할 작업 하나의 DAG에 여러 task 조합으로 구성


#### operator
airflow operator

bashoperator

pythonoperator

simplehttpoperator :

- 특정 호스트로 http 요청을 보내고 respon를 반환
- 파이썬 함수에서 request 모듈을 사용한 뒤 pythonoperator로 실행시켜도 무방

provider를 통해 외부 third party와 연동 가능

branchpythonoperator : 

- 특정 조건에 따라 실행을 제어하는 operator
- 특정 상황에 A 작업, 없으면 생략
- 학습 결과가 기존 모델보다 좋으면 저장, 업데이트 좋지 않으면 저장만

#### 기타 개념

variable : airflow console에서 변수(variable)을 저장해 airflow dag에서 사용

connection & hook : 연결하기 위한 설정(MySQL, GCP) 등

sensor : 외부 이벤트를 기다리며 특정 조건이 만족되면 실행

Xcoms : task 끼리 결과를 주고받고 싶은 경우

jinja template : 파이썬의 템플릿 문법. Fast api에서도 사용
