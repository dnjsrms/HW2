#연습문제 4.1, 4.2
#사용자 정의 함수부
def fahrenheit_to_celsius() :
    return 5/9*(Fahrenheit-32)

def get_real(prompt) :
    F=float(input(prompt))
    return F
    
#주 프로그램부
Fahrenheit = get_real('변환하고자 하는 화씨온도? ')
Celsius = fahrenheit_to_celsius()
print('화씨', Fahrenheit, '도는 섭씨', Celsius, '도')
