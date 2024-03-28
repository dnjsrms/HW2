#연습문제 4.6
#사용자 정의 함수부
def set_all_bits(n) :
    all_bits = (1 << n) - 1
    return all_bits


def get_integer(prompt) :
    B = int(input(prompt))
    return B

#주 프로그램부
bits = get_integer('설정할 비트 수는? ')
output_bits = set_all_bits(bits)
print(bits, '비트를 모두 1로 설정한 수는', output_bits, '0b', bin(output_bits), '이다.')
