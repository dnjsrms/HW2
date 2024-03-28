#연습문제 4.3
#사용자 정의 함수부
def convert_time() :
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    remaining_seconds %= 60
    print(seconds, '초는', hours, '시간', minutes, '분', remaining_seconds, '초이다.')

    
def get_integer(prompt) :
    S = int(input(prompt))
    return S

#주 프로그램부
seconds = get_integer('변환하고자 하는 시간(초)? ')
Time = convert_time()
