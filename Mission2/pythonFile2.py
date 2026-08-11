# print("Hello World!")
def selectAction(input):
    if input == 1:
        QuizSolving()
    elif input == 2:
        QuizCreating()
    elif input == 3:
        ShowQuizList()
    elif input == 4:
        ShowScoreRecord()
    elif input == 5:
        ProgramQuiting()


class QuizGame:
    def __init__(self):
        pass


class Quiz:
    def __init__(self, question, ex1, ex2, ex3, ex4, hint, answer):
        self.question = question
        self.ex1 = ex1
        self.ex2 = ex2
        self.ex3 = ex3
        self.ex4 = ex4
        self.hint = hint
        self.answer = answer

    def showQuiz(self):
        # global quizIndex
        # print("문제[" + quizIndex + "]")
        print(self.question)
        print("1. " + self.ex1)
        print("2. " + self.ex2)
        print("3. " + self.ex3)
        print("4. " + self.ex4)
        # print("정답 번호 (1-4) : ")
        # self.checkAnswer(self, int(input("")))

    def checkAnswer(self, input):
        # global quizIndex
        # global remainingQuizIndexList

        if input == self.answer:
            return True
            # print("정답입니다!")
            # quizIndex += 1

            ## 남은 문제가 있으면;
            # if len(remainingQuizIndexList) > 0:
            #    rQuiz = pickRandomRemainingQuiz()
            #    rQuiz.showQuiz(rQuiz)
            # else:
            #    print("==================")
            #    print("모든 퀴즈를 완료했습니다.")
            #    print("==================")

            #    PrintScore()

        else:
            return False
            # print("틀렸습니다!")
            # print("=============")
            # PrintScore()


class Record:
    def __init__(self, dateStr, score):
        self.score = score
        self.dateStr = dateStr


def QuizSolving():
    global quizList

    ## 테스트용 코드;
    # quizList = []

    # json에서 값 불러와서 퀴즈리스트 채우기;
    # quizList=[Quiz("문제","보기1","보기2","보기3","보기4","힌트",1)]
    # remainingIndexList = []
    # for i in range(len(quizList)):
    #     remainingIndexList.append(i)

    print("선택: 1")
    print("")

    if len(quizList) == 0:
        print("준비된 퀴즈가 없습니다. 먼저 퀴즈를 생성하세요.")

    else:
        print("퀴즈를 시작합니다! (총 ", len(quizList), "문제)")

        rQuiz = pickRandomRemainingQuiz()
        PrintQuizSolvingPage(rQuiz)


def pickRandomRemainingQuiz():
    global quizList
    global remainingQuizIndexList

    rIndex = random.choice(remainingQuizIndexList)
    rQuiz = quizList[rIndex]
    remainingQuizIndexList.remove(rIndex)
    return rQuiz


def PrintQuizSolvingPage(quiz):
    global quizIndex
    global remainingQuizIndexList
    global highestScore

    print("---------------------------")
    print("문제[" + str(quizIndex) + "]")
    quiz.showQuiz()
    # print(quiz.question)
    # print("1. " + quiz.ex1)
    # print("2. " + quiz.ex2)
    # print("3. " + quiz.ex3)
    # print("4. " + quiz.ex4)
    print("정답 번호 (1-4) : ")

    isCorrect = quiz.checkAnswer(int(input("")))

    if isCorrect == True:
        print("정답입니다!")
        quizIndex += 1

        # 남은 문제가 있으면;
        if len(remainingQuizIndexList) > 0:
            # 최고점수와 비교,갱신;
            solvedQuizCount = quizIndex - 1
            if solvedQuizCount > highestScore:
                highestScore = solvedQuizCount
                SaveDataToJsonFile()

            rQuiz = pickRandomRemainingQuiz()
            # rQuiz.showQuiz()
            PrintQuizSolvingPage(rQuiz)
        else:
            print("==================")
            print("모든 퀴즈를 완료했습니다.")
            print("==================")

            PrintScore()

    else:
        print("틀렸습니다!")
        print("=============")
        PrintScore()


# def checkAnswer(quiz, input):
#    global quizIndex
#    global remainingQuizIndexList

#    if input == quiz.answer:
#        print("정답입니다!")
#        quizIndex += 1

#        # 남은 문제가 있으면;
#        if len(remainingQuizIndexList) > 0:
#            rQuiz = pickRandomRemainingQuiz()
#            showQuiz(rQuiz)
#        else:
#            print("==================")
#            print("모든 퀴즈를 완료했습니다.")
#            print("==================")

#            PrintScore()
#            # solvedQuizCount = quizIndex - 1
#            # point = solvedQuizCount * 20

#            # # 푼 문제수가 기록[0].스코어보다 크면;
#            # if solvedQuizCount > scoreRecordList[0].score:
#            #     # 최고 점수 획득!
#            #     print("최고 점수 획득!")

#            # print(
#            #     len(quizList), "문제 중", solvedQuizCount, "문제 정답!(", point, ")점"
#            # )

#    else:
#        print("틀렸습니다!")
#        print("=============")
#        PrintScore()
#        # solvedQuizCount = quizIndex - 1
#        # point = solvedQuizCount * 20

#        # # 푼 문제수가 기록[0].스코어보다 크면;
#        # if solvedQuizCount > scoreRecordList[0].score:
#        #     # 최고 점수 획득!
#        #     print("최고 점수 획득!")

#        # print(len(quizList), "문제 중", solvedQuizCount, "문제 정답!(", point, ")점")

highestScore = 0


def PrintScore():
    global quizIndex
    global quizList
    global scoreRecordList
    global highestScore

    solvedQuizCount = quizIndex - 1
    slop = 20
    point = solvedQuizCount * slop

    # 푼 문제수가 기록[0].스코어보다 크면;
    if len(scoreRecordList) == 0:
        if solvedQuizCount > 0:
            # 최고 점수 획득!
            print("최고 점수 획득!")

    elif solvedQuizCount > highestScore:  # scoreRecordList[0].score:
        highestScore = solvedQuizCount
        print("최고 점수 획득!")

    print(len(quizList), "문제 중", solvedQuizCount, "문제 정답!(", point, "점)")

    AddNewRecordToRecordListAndSaveRecordList(solvedQuizCount)


def AddNewRecordToRecordListAndSaveRecordList(score):
    global scoreRecordList

    newRecord = Record(str(datetime.datetime.now()), score)

    tmpRecordList = []
    tmpRecordList.extend(scoreRecordList)
    tmpRecordList.append(newRecord)

    sortedList = sorted(tmpRecordList, key=lambda x: x.score, reverse=True)

    scoreRecordList.clear()
    scoreRecordList.extend(sortedList)
    # saveRecordList()
    SaveDataToJsonFile()


def saveQuestion(inputStr):
    # 새퀴즈.질문=문자열;
    newQuiz.question = inputStr
    saveEx1(input("선택지 1: "))


def saveEx1(inputStr):
    # 새퀴즈.보기1=문자열;
    newQuiz.ex1 = inputStr
    saveEx2(input("선택지 2: "))


def saveEx2(inputStr):
    # 새퀴즈.보기2=문자열;
    newQuiz.ex2 = inputStr
    saveEx3(input("선택지 3: "))


def saveEx3(inputStr):
    # 새퀴즈.보기3=문자열;
    newQuiz.ex3 = inputStr
    saveEx4(input("선택지 4: "))


def saveEx4(inputStr):
    # 새퀴즈.보기4=문자열;
    newQuiz.ex4 = inputStr
    saveHint(input("힌트: "))


def saveHint(inputStr):
    # 새퀴즈.힌트=문자열;
    newQuiz.hint = inputStr
    saveAnswer(int(input("정답 번호 (1-4): ")))


def saveAnswer(inputStr):
    global quizList

    # 새퀴즈.정답=문자열;
    newQuiz.answer = inputStr
    # 퀴즈 리스트에 새퀴즈 추가;
    quizList.append(newQuiz)
    print("quizList ", len(quizList))
    # json으로 퀴즈리스트 저장;
    # saveQuizList()
    SaveDataToJsonFile()
    print("퀴즈가 추가되었습니다!")


def SaveDataToJsonFile():
    global highestScore
    global quizList
    quizDictlist = [vars(item) for item in quizList]

    global scoreRecordList
    recordDictlist = [vars(item) for item in scoreRecordList]

    # 두 리스트를 하나의 큰 딕셔너리로 묶기.
    combined_data = {
        "best_score": highestScore,
        "quizzes": quizDictlist,
        "recordData": recordDictlist,
    }

    # 파일 쓰기 (indent=4를 주면 가독성 있게 줄바꿈됩니다)
    with open("state.json", "w", encoding="utf-8") as file:
        json.dump(combined_data, file, ensure_ascii=False, indent=4)


def LoadDataFromJsonFile():
    global highestScore

    try:
        # json파일 읽어들이기
        with open("state.json", "r", encoding="utf-8") as file:
            loaded_data = json.load(file)

            #
            highestScore = loaded_data.get("best_score", 0)
            # 퀴즈 리스트
            quizDictList = loaded_data.get("quizzes", [])
            global quizList
            quizList = [Quiz(**item) for item in quizDictList]

            # 기록 리스트
            recordDictList = loaded_data.get("recordData", [])

    except FileNotFoundError:
        #
        highestScore = 0
        # quizDictList = []
        GenerateDefaultQuizList()
        # 기록 리스트
        recordDictList = []

    except json.JSONDecodeError:
        #
        highestScore = 0

        print("데이터 파일이 손상되어, 기본 퀴즈 데이터로 복구/초기화합니다.")
        GenerateDefaultQuizList()
        # 기록 리스트
        recordDictList = []
        #
        SaveDataToJsonFile()

    finally:
        #
        GenerateRemainingQuizIndexList()
        # 기록 리스트
        global scoreRecordList
        scoreRecordList = [Record(**item) for item in recordDictList]


def GenerateDefaultQuizList():
    global quizList
    quizList.append(
        Quiz(
            "파이썬에서 생성 후 값을 변경할 수 없는(immutable) 데이터 타입은 무엇인가요?",
            "리스트(List)",
            "튜플(Tuple)",
            "딕셔너리(Dictionary)",
            "집합(Set)",
            "소괄호 ()를 사용하여 정의하며, 데이터 요소를 안전하게 보호해야 할 때 유용하게 쓰이는 자료형입니다.",
            2,
        )
    )
    quizList.append(
        Quiz(
            "다음 중 파이썬의 변수명(식별자) 작성 규칙에 어긋나는(사용할 수 없는) 것은 무엇인가요?",
            "my_var",
            "_var",
            "1st_var",
            "var1",
            "파이썬 변수 이름은 첫 글자에 특별한 제약이 있습니다. 특히 일반적인 숫자는 맨 앞에 올 수 없습니다.",
            3,
        )
    )
    quizList.append(
        Quiz(
            "파이썬에서 화면(콘솔 창)에 결과를 출력하기 위해 사용하는 내장 함수는 무엇인가요?",
            "print()",
            "input()",
            "write()",
            "output()",
            " '인쇄하다'라는 뜻을 가진 영어 단어로, 괄호 안에 있는 데이터를 사용자가 볼 수 있도록 텍스트로 보여주는 역할을 합니다.",
            1,
        )
    )
    quizList.append(
        Quiz(
            "파이썬 리스트(List)에서 첫 번째 요소를 가져오기 위해 지정해야 하는 인덱스(Index) 번호는 무엇인가요?",
            "1",
            "0",
            "-1",
            "2",
            "파이썬은 0부터 숫자를 세는 '0-based indexing' 방식을 사용하는 대표적인 언어입니다.",
            2,
        )
    )
    quizList.append(
        Quiz(
            "파이썬에서 정수(int) 형태의 데이터를 문자열(string) 자료형으로 변환할 때 사용하는 함수는 무엇인가요?",
            "int()",
            "float()",
            "list()",
            "str()",
            "'문자열'을 뜻하는 영어 단어 'String'의 앞 세 글자를 따서 만든 함수 이름을 찾아보세요.",
            4,
        )
    )


# def saveQuizList():
# 	global quizList
# 	dictionarylist = [vars(item) for item in quizList]
# 	# dictionarylist = [dict(item) for item in quizList]

# 	with open("quizData.json", "w", encoding="utf-8") as f:
# 		json.dump(dictionarylist, f, ensure_ascii=False, indent=4)


# def LoadQuizList():
#    # FillTmpQuizData()
#    try:
#        with open("quizData.json", "r", encoding="utf-8") as f:
#            dictionarylist = json.load(f)
#    except:
#        dictionarylist = []

#    global quizList
#    quizList = [Quiz(**item) for item in dictionarylist]

#    FillRemainingQuizIndexList()


# def saveRecordList():
# 	global scoreRecordList
# 	dictionarylist = [vars(item) for item in scoreRecordList]

# 	with open("recordData.json", "w", encoding="utf-8") as f:
# 		json.dump(dictionarylist, f, ensure_ascii=False, indent=4)


# def LoadRecordList():
#    # FillTmpRecordData()
#    try:
#        with open("recordData.json", "r", encoding="utf-8") as f:
#            dictionarylist = json.load(f)

#    except:
#        dictionarylist = []

#    global scoreRecordList
#    scoreRecordList = [Record(**item) for item in dictionarylist]


def QuizCreating():
    print("선택: 2")
    print("")
    print("새로운 퀴즈를 추가합니다.")
    print("")
    saveQuestion(input("문제를 입력하세요: "))


def ShowQuizList():
    global quizList

    ## 테스트용 코드;
    # quizList = []

    print("등록된 퀴즈 목록(총", len(quizList), "개)")
    print("--------------")

    if len(quizList) == 0:
        print("준비된 퀴즈가 없습니다. 먼저 퀴즈를 생성하세요.")

    else:
        index = 1
        for quiz in quizList:
            print("[" + str(index) + "] " + quiz.question)
            index += 1

    print("--------------")


def ShowScoreRecord():
    global scoreRecordList
    global quizList

    ## 테스트용 코드;
    # scoreRecordList = []

    print("플레이 기록(총", len(scoreRecordList), "회)")
    print("--------------")

    if len(scoreRecordList) == 0:
        print("플레이 기록이 없습니다.")

    else:
        index = 1
        slope = 20

        # for record in scoreRecordList:
        for record in scoreRecordList:
            # print("[", index, "] 점수 ", record.score, " 날짜 ", record.date)
            # 점수 : 100점 환산(5문제 중 5문제 정답) 날짜;
            point = slope * record.score
            print(
                f"[{index}] 점수: {point} 점({len(quizList)}문제 중 {record.score}문제 정답), 날짜: {record.dateStr}"
            )

            index += 1

    print("--------------")


import sys


def ProgramQuiting():
    sys.exit("프로그램 종료")


# from random import *
import random
import datetime
import json

# import numpy as np

quizList = []
quizIndex = 1  # 1부터 시작해야함!
remainingQuizIndexList = []

# recordList = []


def GenerateRemainingQuizIndexList():

    global quizList
    global remainingQuizIndexList

    remainingQuizIndexList = []
    for i in range(len(quizList)):
        remainingQuizIndexList.append(i)
    # global remainingQuizIndexList = [i for i in range(len(quizList))]

    # print("quizIndexList ", len(remainingQuizIndexList))
    # print("quizIndexList ", remainingQuizIndexList)


# newQuiz = Quiz
newQuiz = Quiz("", "", "", "", "", "", 0)

scoreRecordList = []


# def FillTmpRecordData():
#    global scoreRecordList

#    tmpRecordList = []
#    tmpRecordList.append(Record(datetime.datetime.now(), 1))
#    tmpRecordList.append(Record(datetime.datetime.now(), 2))
#    # tmpRecordList.append(Record(datetime.datetime.now(), 3))
#    # tmpRecordList.append(Record(datetime.datetime.now(), 4))
#    tmpSortedList = sorted(tmpRecordList, key=lambda x: x.score, reverse=True)
#    # scoreRecordList.append(tmpSortedList)
#    scoreRecordList.extend(tmpSortedList)
#    # print("scoreRecordList", len(scoreRecordList))
#    # print("scoreRecordList", scoreRecordList)


# def FillTmpQuizData():
#    global quizList

#    quizList.append(Quiz("문제1", "보기11", "보기12", "보기13", "보기14", "힌트1", 1))
#    quizList.append(Quiz("문제2", "보기21", "보기22", "보기23", "보기24", "힌트2", 2))
#    quizList.append(Quiz("문제3", "보기31", "보기32", "보기33", "보기34", "힌트3", 3))
#    quizList.append(Quiz("문제4", "보기41", "보기42", "보기43", "보기44", "힌트4", 4))
#    # print("quizList", len(quizList))


def PrintMenu():
    global quizList
    global quizIndex
    global scoreRecordList

    quizIndex = 1
    # json에서 값 불러와서 퀴즈리스트 채우기;
    LoadDataFromJsonFile()
    # LoadQuizList()
    # quizList = [Quiz("문제", "보기1", "보기2", "보기3", "보기4", "힌트", 1)]
    # totalQuizCount=len(quizList)

    # newQuiz = Quiz
    # json에서 값 불러와서 기록리스트 채우기;
    # LoadRecordList()
    # print("scoreRecordList1", len(scoreRecordList))
    # recordList = [Record(date, 3)]

    print("==============")
    print("나만의 퀴즈 게임")
    print("==============")

    if len(scoreRecordList) > 0:
        print(
            "저장된 데이터를 불러왔습니다.(퀴즈",
            len(quizList),
            "개, 최고점수",
            scoreRecordList[0].score,
            "점)",
        )
        print("==============")

    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("==============")

    # print("re00", remainingQuizIndexList)
    selectAction(int(input("선택:")))


PrintMenu()
