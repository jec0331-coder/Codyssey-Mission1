# 과제1.내 컴퓨터에 개발자용 '작업실' 꾸미기
## 미션 목표
로컬 개발 환경 세팅, 재현 가능한 실행 환경 공유, 협업 기반 소스코드 관리 같은 상황에서 활용할 수 있도록 터미널, Docker, Git 이 세 가지를 세팅해 보고 다루는 법을 학습하여
코드가 "내 컴퓨터에서만" 돌아가는 문제를 줄이고, 팀원 누구나 같은 방식으로 실행, 배포, 디버깅할 수 있는 환경 구성을 목표로 합니다.


## 실행 환경
- macOS 13.7.8
- macOS 기본 터미널
- vscode 버전: 1.104.2
- OrbStack Version 1.9.5
- Docker version 
- git version 2.39.2


## 폴더 구조



## 터미널 조작
- 1.현재 위치 확인
```bash
pwd
```
```bash
/Users/jeong-uicheol/Desktop/VS_Code_Python
```
  - 스크린샷
<img width="481" height="48" alt="과제1 현재위치 확인" src="https://github.com/user-attachments/assets/5cee72c9-bdcc-4463-9a7b-6f6008b5dd64" />


- 2.목록 확인(숨김 파일 포함)
```bash
ls -la
```
```bash
total 192
drwxr-xr-x  11 jeong-uicheol  staff    352  8 12 13:15 .
drwx------+ 70 jeong-uicheol  staff   2240  8 13 19:40 ..
-rw-r--r--@  1 jeong-uicheol  staff   6148  8 10 17:49 .DS_Store
drwxr-xr-x  15 jeong-uicheol  staff    480  8 12 11:17 .git
-rw-r--r--   1 jeong-uicheol  staff     20  8 11 13:37 .gitignore
drwxr-xr-x   7 jeong-uicheol  staff    224  8 13 17:11 Mission2
drwxr-xr-x   9 jeong-uicheol  staff    288  8 13 17:33 Mission3
-rw-r--r--   1 jeong-uicheol  staff  17461  8  7 19:26 pythonFile2.py
-rw-r--r--   1 jeong-uicheol  staff  41093  8 12 11:53 pythonFile22.py
-rw-r--r--   1 jeong-uicheol  staff  20284  8 10 22:26 pythonFile3.py
drwxr-xr-x   6 jeong-uicheol  staff    192  8 12 12:18 quiz_clone
```
  - 스크린샷
<img width="551" height="185" alt="과제1 ls -la" src="https://github.com/user-attachments/assets/00f2e291-9fe4-4b4b-91ea-8077fb27cfe5" />




- 3.디렉토리 생성
```bash
mkdir Mission1 
```
  - 스크린샷
<img width="873" height="60" alt="과제1 파일,디렉토리 생성" src="https://github.com/user-attachments/assets/ec518bbf-99ad-441c-aa91-c90f8308455c" />



- 4.위치 이동
```bash
cd Mission1
```
  - 스크린샷
<img width="551" height="47" alt="과제1 디렉토리 이동" src="https://github.com/user-attachments/assets/42d8a97b-b087-4e7f-856b-8bde9afa0693" />




- 5.파일, 폴더 복사
```bash
cp test1.txt backup.txt
```

```bash
cp -r Mission1/ Mission1_backup/
```

  - 스크린샷
<img width="994" height="752" alt="과제1 파일,폴더 복사" src="https://github.com/user-attachments/assets/f2353496-b558-4564-9dd1-29b74ef69475" />



- 6.파일 이동/이름변경
```bash
mv test.txt Mission1/
```
  - 스크린샷
<img width="1188" height="771" alt="과제1 파일 이동" src="https://github.com/user-attachments/assets/118a71b8-630e-4100-bf1f-fdd897c5566e" />

```bash
mv test.txt test1.txt
```
  - 스크린샷
<img width="284" height="48" alt="과제1 파일 이름 변경" src="https://github.com/user-attachments/assets/fd083d2e-1db6-4e8a-8f95-45a2f56950ae" />



- 7.빈 파일 생성
```bash
touch test.txt
```
  - 스크린샷
<img width="873" height="60" alt="과제1 파일,디렉토리 생성" src="https://github.com/user-attachments/assets/ec518bbf-99ad-441c-aa91-c90f8308455c" />


- 8.삭제
```bash
rm -r Mission1_backup/
```
```bash
rm backup.txt
```
  - 스크린샷
<img width="973" height="750" alt="과제2 폴더,파일 삭제" src="https://github.com/user-attachments/assets/3f02405c-c810-4ceb-8515-c96cc63a4391" />



- 9.파일에 내용 쓰기
```bash
echo "hello" > test1.txt
```
- 10.파일 내용 확인
```bash
cat test1.txt
```
```bash
hello
```
  - 스크린샷
<img width="615" height="821" alt="과제1 파일 쓰고 풀력" src="https://github.com/user-attachments/assets/1811d2d1-4b0e-44f7-97ad-e5d300ff38c6" />






## 권한 실습
- 1.권한 확인
```bash
ls -la
```
  - 스크린샷
<img width="490" height="75" alt="과제1 권한확인" src="https://github.com/user-attachments/assets/1c91fbb8-87bf-439e-b889-43d20fcab00d" />

```bash
total 8
drwxr-xr-x   3 jeong-uicheol  staff   96  8 13 20:59 .
drwxr-xr-x  12 jeong-uicheol  staff  384  8 13 20:58 ..
-rw-r--r--   1 jeong-uicheol  staff    6  8 14 14:40 test1.txt
```


- 2.권한 변경
```bash
chmod 755 test1.txt
```
```bash
chmod -R 755 Mission1/
```
  - 스크린샷
<img width="598" height="453" alt="과제1 권한 변경" src="https://github.com/user-attachments/assets/9cd537d4-36ca-4a84-8f9c-769f6957a266" />




## Docker 설치, 기본 점검

- 1.버전 확인
```bash
docker --version
```
```bash
Docker version 27.4.1, build b9d17ea
```
  - 스크린샷
<img width="463" height="60" alt="과제1 도커 버전 확인" src="https://github.com/user-attachments/assets/2dea5b1c-0912-4350-9839-fa07fb501850" />


- 2.데몬 동작 확인
```bash
docker info
```
```bash
Client:
 Version:    27.4.1
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.18.0
    Path:     /Users/jeong-uicheol/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.32.4
    Path:     /Users/jeong-uicheol/.docker/cli-plugins/docker-compose

Server:
 Containers: 2
  Running: 1
  Paused: 0
  Stopped: 1
 Images: 3
 Server Version: 27.4.1
 Storage Driver: overlay2
...생략
```
  - 스크린샷
<img width="552" height="445" alt="docker info" src="https://github.com/user-attachments/assets/8b6c1ec0-5bdb-4a94-b3d8-b57733938da8" />




## Docker 기본 운영 명령 수행

- 1.이미지 다운로드
```bash
docker pull nginx
docker pull ubuntu
```

- 2.이미지 목록 확인
```bash
docker images
```
```bash
REPOSITORY        TAG       IMAGE ID       CREATED        SIZE
my-custom-nginx   v1        a92a7f8e2251   47 hours ago   161MB
nginx             latest    5253dc86cc93   9 days ago     161MB
ubuntu            latest    86a1a31fdd84   2 weeks ago    100MB
```
  - 스크린샷
<img width="487" height="87" alt="docker images" src="https://github.com/user-attachments/assets/cf570499-5ecd-4a58-ba0f-eda2059055b9" />



- 3.컨테이너 실행
```bash
docker run -d -p 80:80 --name my-web nginx
```
- 4.컨테이너 중지
```bash
docker stop my-web
```
- 다시 시작
```bash
docker start my-web
```

- 5.컨테이너 목록 확인
```bash
docker ps -a
```

  - 스크린샷
<img width="939" height="311" alt="과제1 컨테이너 점검" src="https://github.com/user-attachments/assets/59659a56-3aec-49ba-8f27-4139c45cc0a3" />


- 6.로그 확인
```bash
docker logs my-web
```
  - 스크린샷
<img width="700" height="577" alt="docker logs" src="https://github.com/user-attachments/assets/4e996b26-5bbf-40f3-80d9-37fc88c483c5" />


- 7.리소스 확인
```bash
docker stats
```
  - 스크린샷
<img width="911" height="53" alt="docker stats" src="https://github.com/user-attachments/assets/5cef42b7-1530-4fc6-8553-a64276e4e42d" />








## 컨테이너 실행 실습
- 1.hello-world 실행 성공을 기록
```bash
docker run hello-world
```
  - 스크린샷
<img width="802" height="427" alt="docker run hello-world" src="https://github.com/user-attachments/assets/ec92146b-520a-43e8-8f34-fe67c4018199" />


- 2.ubuntu 컨테이너를 실행하고 내부 진입 후 간단 명령(예: ls, echo) 수행 결과
```bash
docker run -it ubuntu /bin/bash
```
```bash
ls -l
```
```bash
echo "Hello from Ubuntu Container"
```

  - 스크린샷
<img width="832" height="375" alt="우분투 기본 조작" src="https://github.com/user-attachments/assets/5d96f435-90a0-47e3-b8bb-573d85c54082" />


- 3.컨테이너 종료/유지(attach/exec 등)의 차이를 스스로 관찰하고 간단히 정리한다.
```bash
exit
```
  - 컨테이너 종료
```bash
docker attach my-web
```
  - attach로 들어간 상태에서 그냥 exit를 치고 나오면 메인 터미널이 죽어버리기 때문에 컨테이너 전체가 종료(Stop)

```bash
docker exec -it my-web /bin/bash
```
  - 메인 프로세스와 분리된 독립된 방이므로, 작업이 끝나고 exit를 쳐서 나와도 컨테이너가 죽지 않고 계속 살아있음

- 스크린샷
<img width="852" height="454" alt="과제1 도커 exit, attach, exec" src="https://github.com/user-attachments/assets/44ec5d66-4230-4406-aefe-27a5c9971144" />


- 정리

| 명령어 | 대상 컨테이너 상태 | 핵심 역할 (비유) | 빠져나올 때 (exit) |
| :--- | :--- | :--- | :--- |
| docker run | 없음 (새로 만듦) | 우분투 컴퓨터를 새로 조립하고 전원을 켜서 모니터 앞에 앉는 것 | 컨테이너가 종료됨 |
| docker exec | 이미 실행 중 | 켜져 있는 컴퓨터에 새로운 원격 로그인 창(새 탭)을 열고 들어가는 것 | 컨테이너 유지 (권장) |
| docker attach | 이미 실행 중 | 켜져 있는 컴퓨터의 메인 모니터 화면을 그대로 같이 공유해서 보는 것 | 컨테이너가 종료됨 |





## 기존 Dockerfile 기반 커스텀 이미지 제작
아래 방식 중 하나를 선택하여 기존 Dockerfile/이미지 기반의 커스텀 이미지를 만든다.
(A) 웹 서버 베이스 이미지 활용(예: NGINX/Apache 등) + 정적 콘텐츠/설정만 교체
(B) Linux 베이스 이미지(예: ubuntu/alpine 등) + 기본 기능(패키지/사용자/환경변수/헬스체크 등) 추가
제작 결과는 아래 조건을 만족해야 한다.
커스텀 이미지 빌드 성공 및 컨테이너 실행 성공
기술 문서에 다음을 포함한다.
어떤 “기존 베이스(이미지/예시 Dockerfile)”를 선택했는지
내가 적용한 커스텀 포인트 각각의 목적(간단 요약)
빌드/실행 명령 + 핵심 결과(출력/스크린샷)

- 1.도커 파일 작성
```bash
mkdir custom-ubuntu
cd custom-ubuntu
touch Dockerfile
```

```bash
# 1. 기반이 될 베이스 이미지 지정 (우분투 22.04 버전을 기준)
FROM ubuntu:22.04

# [커스텀 요소 1] 컨테이너 시스템 시간대를 한국 시간(KST)으로 설정
# 패키지 설치 시 대화형 창이 뜨는 것을 방지(DEBIAN_FRONTEND)하며 시간대를 주입합니다.
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul
RUN apt-get update && apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# [커스텀 요소 2] 필수 개발 유틸리티(Vim, Curl) 미리 설치하기
# 나중에 컨테이너 안에서 패키지를 일일이 깔지 않아도 되도록 빌드 시점에 구워둡니다.
RUN apt-get install -y vim curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 3. 컨테이너 내부의 기본 작업 디렉터리 설정 (이동 시 root 폴더로 시작)
WORKDIR /root

# 4. 컨테이너가 켜지자마자 실행할 기본 명령어 (우분투 터미널 실행)
CMD ["/bin/bash"]
```

- 2.빌드, 실행 명령
```bash
docker build -t my-ubuntu:1.0 .
```


- 기존 베이스 : ubuntu:22.04
- 커스텀 포인트의 목적
  - 1.컨테이너 시스템 시간대를 한국 시간(KST)으로 설정
  - 패키지 설치 시 대화형 창이 뜨는 것을 방지(DEBIAN_FRONTEND)하며 시간대를 주입.
```bash
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul
RUN apt-get update && apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```
  
  - 2.필수 개발 유틸리티(Vim, Curl) 미리 설치
  - 나중에 컨테이너 안에서 패키지를 일일이 깔지 않아도 되도록 빌드 시점에 구워둠.
```bash
RUN apt-get install -y vim curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
```

  - 3.컨테이너 내부의 기본 작업 디렉터리 설정 (이동 시 root 폴더로 시작)
```bash
WORKDIR /root
```


  - 4.컨테이너가 켜지자마자 실행할 기본 명령어 (우분투 터미널 실행)
```bash
CMD ["/bin/bash"]
```


- 실행 결과 스크린샷

<img width="1090" height="416" alt="과제1 커스텀 우분투 생성" src="https://github.com/user-attachments/assets/995d18be-e9e7-45bc-9ccf-b468d886d29f" />







## 포트 매핑 및 접속 증거
브라우저 접속 화면(또는 curl 응답)을 기술 문서에 첨부한다.

- 1.
```bash
ls -la
```

- 2.
```bash
ls -la
```



## Docker 볼륨 영속성 검증
Docker 볼륨을 생성하고 컨테이너에 연결한다.
컨테이너 삭제 전/후로 데이터를 확인하여 데이터가 유지됨을 증명한다.
기술 문서에 생성/연결/검증 절차(명령+출력)를 포함한다.

- 1.볼륨 생성
```bash
ls -la
```

- 2.컨테이너에 연결
```bash
ls -la
```

- 3.확인
```bash
ls -la
```

- 4.삭제
```bash
ls -la
```

- 5.삭제 후 확인
```bash
ls -la
```
```bash
ls -la
```



## Git 설정 및 GitHub 연동
Git 사용자 정보/기본 브랜치 설정을 완료하고 git config --list 결과를 기록한다.
* GitHub 로그인 및 저장소 연동을 완료하고, 연동 증거(스크린샷 등)를 기술 문서에 첨부한다.

- 1.설정 후 확인
```bash
ls -la
```

```bash
ls -la
```

- 2.연동
```bash
ls -la
```

```bash
ls -la
```






