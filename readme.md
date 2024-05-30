- 가상환경 실행
source venv/bin/activate

- 프로그램 실행
flask run --debug

- 5000포트 이미 사용하고 있는 경우

lsof -n -i TCP:5000

로 5000포트 사용중인 프로세스의 PID 확인
kill -9 <PID>