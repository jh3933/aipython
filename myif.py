def print_cat():
    cat_art = r"""
     /\_/\  
    ( o.o ) 
     > ^ <
    """
    print(cat_art)

def print_dog():
    dog_art = r"""
     / \__
    (    @\___
    /         O
   /   (_____/
/_____/   U
    """
    print(dog_art)

def print_rabbit():
    rabbit_art = r"""
     (\_/)
     (o.o)
     (> <)
    """
    print(rabbit_art)

run_count = 0  # 전체 실행 횟수를 추적

while True:  # 무한 반복 루프
    session_count = 0  # 현재 세션의 실행 횟수
    print("\n새로운 세션이 시작되었습니다!")
    
    # 각 세션에서 5번 반복
    while session_count < 5:
        print(f"\n그림 출력 프로그램 (세션 내 실행: {session_count+1}/5)")
        print("====================")
        print("0. 프로그램 종료")
        print("1. 고양이")
        print("2. 강아지")
        print("3. 토끼")
        print("====================")

        try:
            n = int(input("선택: "))
            
            if n == 0:  # 0 입력 시 프로그램 즉시 종료
                print("프로그램을 종료합니다.")
                exit()  # 프로그램 완전 종료
            elif n == 1:
                print("고양이 그림")
                print_cat()
                session_count += 1
            elif n == 2:
                print("강아지 그림")
                print_dog()
                session_count += 1
            elif n == 3:
                print("토끼 그림")
                print_rabbit()
                session_count += 1
            else:
                print("잘못 입력했습니다. 1, 2, 3 중에 선택하거나 0을 입력해 종료하세요.")
        except ValueError:
            print("숫자를 입력해주세요.")
    
    # 5번 실행 후 세션 종료 메시지
    run_count += 1
    print(f"\n세션 {run_count}이(가) 완료되었습니다. 5번의 동물 그림을 출력했습니다.")
    print("새로운 세션이 자동으로 시작됩니다. (종료하려면 0 입력)")

