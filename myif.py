# 아스키 코드 그림 출력 하기

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

print("그림 출력 프로그램")
print("====================")
print("1. 고양이")
print("2. 강아지")
print("3. 토끼")
print("====================")

n = int(input("선택: "))

if n == 1:
    print("고양이 그림")
    print_cat()
elif n == 2:
    print("강아지 그림")
    print_dog()
elif n == 3:
    print("토끼 그림")
    print_rabbit()
else:
    print("잘못 입력했습니다.")



