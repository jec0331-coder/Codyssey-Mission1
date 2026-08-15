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






## 도커 이미지와 컨테이너 비교

| 비교 측면 | 이미지 (Image) | 컨테이너 (Container) |
| :--- | :--- | :--- |
| **기본 개념** | 컨테이너를 생성하기 위한 정적 **설계도/스냅샷** (Read-Only) | 이미지를 바탕으로 독립된 자원에서 격리되어 돌아가는 **살아있는 컴퓨터** (Read-Write) |
| **비유** | 프로그램 설치 파일(EXE), 붕어빵 틀, 설계도 | 실행된 프로그램 프로세스, 붕어빵, 실제 건축물 |
| **빌드 (Build)** | • `Dockerfile`을 기반으로 **새롭게 구워내어 생성**<br>• 소스 코드나 패키지 변경 시 **매번 다시 빌드** 필요 (명령어: `docker build`) | • 빌드 개념이 없음<br>• 이미 존재하는 이미지를 가져와 기반 주소 위에 **순식간에 생성 및 시작** (명령어: `docker run`) |
| **실행 (Execution)** | • 정적인 상태로 **스스로 실행될 수 없음**<br>• 하나의 이미지로 **수십, 수백 개의 컨테이너를 복제하여 동시에 실행** 가능 | • 프로세스로서 **살아서 작동하거나 멈출 수 있음**<br>• `Up` (실행 중), `Exited` (종료됨) 등의 상태를 가짐 |
| **변경 (Modification)** | • **절대 변경 불가능 (Immutable)**<br>• 한 번 빌드된 이미지는 내부 파일을 수정하거나 수정 내용을 누적할 수 없음 | • **실시간 변경 가능 (Mutable)**<br>• 실행 중에 내부 파일을 쓰거나 수정 가능<br>• 단, 컨테이너가 **삭제되면 변경 데이터도 소멸** (Volume 연동 필요) |



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

- 1.터미널에서 확인
```bash
docker ps
```
스크린샷
<img width="916" height="86" alt="스크린샷 2026-08-15 오후 2 16 05" src="https://github.com/user-attachments/assets/f54e5c99-eaa8-46ee-9ba9-4315f294a802" />


- 2.웹페이지로 확인
<img width="736" height="372" alt="스크린샷 2026-08-15 오후 2 18 37" src="https://github.com/user-attachments/assets/978997ba-fc3a-4646-9452-28843943a946" />


## 컨테이너 포트 노출과 네트워크 매핑의 핵심 메커니즘

### 1. 네트워크 네임스페이스 (Network Namespace) 관점의 격리
* **독립된 네트워크 환경**: 도커 컨테이너는 리눅스 커널의 `Network Namespace` 기술을 통해 호스트 PC와 완전히 격리된 독립적인 네트워크 공간을 부여받음.
* **격리되는 요소들**: 각 컨테이너는 자신만의 가상 네트워크 인터페이스(`eth0`), 독립된 라우팅 테이블, 그리고 **별도의 포트(Port) 공간**을 독립적으로 소유.
* **통신의 단절**: 이 격리 특성 때문에, 호스트 PC나 다른 컨테이너가 컨테이너 내부 네트워크 주소(예: `172.17.0.x`)로 직접 패킷을 전송하는 것은 기본적으로 불가능함. 마치 사설 공유기 뒤에 숨은 컴퓨터처럼 외부 접근이 원천 차단됨.

### 2. 포트 노출 및 매핑의 필요성 (접근성)
* **포트 노출 (EXPOSE)**: Dockerfile의 `EXPOSE 80` 지시어는 가상 환경 내부의 웹서버가 80번 포트를 사용해 대기(Listen)하고 있음을 도커 엔진과 개발자에게 알리는 '명시적 선언'. 그러나 이것만으로는 호스트 외부에서 접속할 수 없음.
* **포트 매핑 (Port Mapping, -p)**: 격리된 네트워크 장벽을 허물고 통로를 뚫어주는 가교 역할을 함. `docker run -p 8080:80` 명령을 실행하면 다음과 같은 메커니즘이 작동.
  1. 호스트 PC의 실제 포트(`8080`)와 컨테이너 내부 격리된 포트(`80`) 사이에 **가상 터널**이 뚫림.
  2. 도커 엔진이 리눅스 커널의 `iptables` 규칙을 조작하여 호스트 8080으로 들어오는 데이터 패킷을 컨테이너 80으로 포워딩(NAT).
  3. 이 구조 덕분에 외부 사용자는 호스트 IP의 8080번 포트(`http://localhost:8080`)만 알면 격리된 컨테이너 내부 서비스에 안정적으로 접근할 수 있게됨.

### 3. 보안 고려사항 (Security Considerations)
* **최소 권한의 원칙 (Least Privilege)**: 포트 매핑은 필요한 포트만 선별적으로 외부에 개방하므로 보안상 매우 강력합니다. 데이터베이스(`3306`)나 관리 도구 포트는 가두어 두고, 오직 대외 서비스용 웹 포트(`80`, `443`)만 매핑하여 호스트 인프라의 노출 표면적(Attack Surface)을 최소화함.
* **호스트 포트 충돌 방지**: 여러 컨테이너가 내부적으로는 모두 동일한 `80`번 기본 포트를 사용하더라도, 호스트 쪽에서 `8081:80`, `8082:80`과 같이 서로 다른 포트로 우회하여 맵핑할 수 있어서 이를 통해 단일 호스트 서버 내에서 자원 충돌 없이 수많은 격리 웹서비스를 안전하게 다중 구동할 수 있음.



## Docker 볼륨 영속성 검증

- 1.볼륨 생성
```bash
docker volume create my-db-vol
```

- 2.컨테이너에 연결
```bash
docker run -it --name container-A -v my-db-vol:/app ubuntu:22.04
```

- 3.확인
```bash
cd /app
echo "This is important data saved in 2026" > secrets.txt
cat secrets.txt
exit
```

- 4.삭제
```bash
docker rm container-A
```

- 5.삭제 후 확인
```bash
docker run -it --name container-B -v my-db-vol:/app ubuntu:22.04
cd /app
ls -l
cat secrets.txt
```

```bash
This is important data saved in 2026
```

- 스크린샷
<img width="830" height="370" alt="스크린샷 2026-08-15 오후 3 01 23" src="https://github.com/user-attachments/assets/ebef4e0d-5716-4e59-8550-561b1f682e51" />



## Git 설정 및 GitHub 연동
Git 사용자 정보/기본 브랜치 설정을 완료하고 git config --list 결과를 기록한다.
* GitHub 로그인 및 저장소 연동을 완료하고, 연동 증거(스크린샷 등)를 기술 문서에 첨부한다.

- 1.설정 후 확인
```bash
git config --list
```

  - 출력 스크린샷
<img width="689" height="158" alt="스크린샷 2026-08-15 오후 3 09 45" src="https://github.com/user-attachments/assets/653f9b1c-1918-4237-958c-85e84f591df6" />


- 2.연동
```bash
git remote set-url origin https://github.com/jec0331-coder/Codyssey-Mission1/tree/main
```

  - 출력 스크린샷
<img width="1001" height="72" alt="스크린샷 2026-08-15 오후 3 07 32" src="https://github.com/user-attachments/assets/21ddef20-da99-478a-b553-07272a1df6cc" />


- 깃허브에 push
```bash
git push origin main
```
  - 스크린샷
<img width="632" height="146" alt="스크린샷 2026-08-15 오후 3 31 30" src="https://github.com/user-attachments/assets/f5d4d08a-26b9-4e76-a48e-0bf5ea91ccde" />





