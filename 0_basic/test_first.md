# 190527 기초 설치 및 사용법 학습

## markdown 작성하기

### 제목 작성하기

제목은 Semantic하게 작성한다.

### 나열(리스트) 작성하기

#### 순서가있는 리스트

1. WeMakeO 앱 다운로드
2. 회원가입
   * 카카오
   * 네이버
   * 페북
3. W카페 찾기
4. 커피 주문
5. 알림 시 픽업하기

#### 순서가 없는 리스트

* 파이썬 설치
* 타이포라 설치
* Git 설치

### 일반 문단 작성하기

자동으로

Enter가 두번 들어감

### 코드 블럭 작성하기

터미널에서 `python-e` 라고 입력하면, **코드가 실행**됩니다.

```python
def index () :
    return 'hi'
```

###  수식작성

LaTex ( Ctrl + Shift + m )
$$

$$

### 셀 작성

Ctrl + t

혹은 | 'pipe'로 작성

|      |      |                         |
| ---- | ---- | ----------------------- |
|      |      |                         |
|      |      |                         |
|      |      | Ctrl + Enter하면 행추가 |



## CLI-terminal 명령어 학습

```sh
$ touch a.txt # a.txt를 생성한다.
$ mkdir test # test 폴더/디렉토리를 생성한다. Make Directory
$ cd test # test 디렉토리로 이동한다. Change Directory
$ cd .. # 한단계 위의 디렉토리로 이동한다.
$ cd ~ # home 으로 이동한다.
$ cd - # 뒤로 가기
$ rm a.txt # 파일 a.txt 를 삭제한다.
$ rm -r # 폴더 지우는 것
$ ls # List 현재 디렉토리 안의 파일/디렉토리 목록을 표시한다.
$ ls -a # 
$ pwd # 현재 내가 위치한 디렉토리를 표시한다. Present Working Directory

$ git init # 버전 관리 시작
```

## git 기초명령

``` sh
$ git init # pwd  관리자 추가
$ git remote -v # 원격 백업을 확인하는 것,드라이브 연동

$ pwd
/c/Users/student/TIL # TIL에 있는 걸 확인하자

# 수업중간 중간
$ git add directory #  사진 찍기 위해서 프레임 안으로 들어오라는 것
$ git commint -m '코멘트' # 특정 파일/dir 관리 시작
# 적절한 타이밍에 add와 commit의 반복

# 집에 가기 전에
$ git push origin master

$ git log # 확인하기
```



## Python 기초

``` sh
$ pwd
/c/Users/student/TIL

$ git add.
```

