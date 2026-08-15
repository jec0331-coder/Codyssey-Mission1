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
