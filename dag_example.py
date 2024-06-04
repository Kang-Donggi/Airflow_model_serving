from datetime import timedelta

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# catchup : 과거에 지나간 일자의 DAG을 실행할지 옵션

def print_world():
    print("World")

# with 구문으로 DAG 정의
with DAG(
    dag_id="Hello_world", # DAG의 식별자용 id
    description="My First DAG", # DAG에 대한 설명
    start_date=days_ago(2),  # 정의 기준 2일 전부터 시작
    schedule_interval="0 6 * * *", # cron 표현식. 매일 오전 6시 0분에 실행하겠다 (UTC). 한국은 UTC+9. 한국 시간으로는 6+9=15
    tags=["my_dags"] # DAG에 대한 검색을 위한 tag
) as dag:
    # 테스크 정의
    # bash 커맨드로 echo hello 를 실행함
    t1 = BashOperator( # bash 커맨드 실행
        task_id="print_hello",
        bash_command="echo Hello",
        owner="k", # 작업의 오너 보통 담당자 이름 사용
        retries=3, # 태스크 실패시 3번 재시도
        retry_delay=timedelta(minutes=5), # 재시도하는 시간 간격은 5분
    )

    # 테스크 정의
    # python 함수인 print_world를 실행
    t2 = PythonOperator( # python 함수 실행
        task_id="print_world",
        python_callable=print_world,
        depends_on_past=True, # 특정 task가 이전 DAG 실행 결과에 의존할지 결정
                                 # 하루 단위 작업들이 의존성이 있다면 True 주고 순차적 실행
                                  # True : 이전 DAG이 성공적으로 완료되어야 이후 DAG 실행
                                  # False : 이전 DAG 상관없이 스케줄이 되면 DAG 실행
        owner='k',
        retries=3,
        retry_delay=timedelta(minutes=5),
    )

    # 테스크 실행 순서 t1 실행 후 t2 실행
    t1 >> t2

    # A task 이후 B,C 동시 실행
    # A>>B
    # A>>c or A>>[B,C ]
