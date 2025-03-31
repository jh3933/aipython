# 숫자 두개를 입력을 받아서
# +, -, *, / 를 출력 하는 프로그램을 만들어 보자
# 두 숫자의 사칙연산 프로그램

def calculate():
    # 사용자로부터 두 숫자 입력 받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 사용자로부터 수행할 연산 선택받기
    print("수행할 연산을 선택하세요:")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")

    choice = input("연산 선택(1/2/3/4): ")

    # 선택된 연산에 따라 계산 수행
    if choice == '1':
        result = num1 + num2
        print(f"결과: {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"결과: {num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"결과: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"결과: {num1} / {num2} = {result}")
        else:
            print("오류: 0으로 나눌 수 없습니다.")
    else:
        print("잘못된 선택입니다. 올바른 번호를 선택하세요.")

# 함수 호출
calculate()

