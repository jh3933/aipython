# 숫자 두개를 입력을 받아서
# +, -, *, / 를 출력 하는 프로그램을 만들어 보자
# 두 숫자의 사칙연산 프로그램

def calculate():
    try:
    # 두 숫자 입력 받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    
    # 사칙연산 결과 계산
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # 나눗셈은 0으로 나누는 경우를 처리해야 함
    if num2 == 0:
        division = "0으로 나눌 수 없습니다"
    else:
        division = num1 / num2
    
    # 결과 출력
    print("\n===== 계산 결과 =====")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")
    print("=====================")
    
except ValueError:
    print("오류: 유효한 숫자를 입력해주세요.")
    # 다시 입력받기
    calculate()

# 프로그램 실행
calculate()
