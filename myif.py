from rich.console import Console
from rich.panel import Panel

# Rich Console 객체 생성
console = Console()

def print_cat():
    # 고양이 ASCII 아트
    cat_art = r"""
     /\_/\  
    ( o.o ) 
     > ^ <
    """
    # 주황색 패널에 고양이 출력
    console.print(Panel(cat_art, title="고양이", border_style="orange1", style="orange1"))

def print_dog():
    # 강아지 ASCII 아트
    dog_art = r"""
     / \__
    (    @\___
    /         O
   /   (_____/
/_____/   U
    """
    # 갈색 계열로 변경 (dark_orange -> 갈색에 가까운 색상)
    console.print(Panel(dog_art, title="강아지", border_style="dark_orange", style="dark_orange"))

def print_rabbit():
    # 토끼 ASCII 아트
    rabbit_art = r"""
     (\_/)
     (o.o)
     (> <)
    """
    # 분홍색을 자홍색으로 변경 (magenta)
    console.print(Panel(rabbit_art, title="토끼", border_style="magenta", style="magenta"))

def print_menu(session_count):
    # 메뉴 출력
    console.print()
    console.print(Panel(
        f"[bold]그림 출력 프로그램[/bold] (세션 내 실행: {session_count+1}/5)\n\n"
        "[bright_red]0.[/bright_red] 프로그램 종료\n"
        "[bright_orange]1.[/bright_orange] 고양이\n"
        "[dark_orange]2.[/dark_orange] 강아지\n"
        "[magenta]3.[/magenta] 토끼",  # pink를 magenta로 변경
        border_style="cyan",
        title="메뉴"
    ))

# 전체 실행 횟수를 추적
run_count = 0

try:
    while True:  # 무한 반복 루프
        session_count = 0  # 현재 세션의 실행 횟수
        console.print("\n[bold green]새로운 세션이 시작되었습니다![/bold green]")
        
        # 각 세션에서 5번 반복
        while session_count < 5:
            print_menu(session_count)

            try:
                choice = input("선택: ")  # 일반 input 사용
                n = int(choice)
                
                if n == 0:  # 0 입력 시 프로그램 즉시 종료
                    console.print("[bold red]프로그램을 종료합니다.[/bold red]")
                    exit()  # 프로그램 완전 종료
                elif n == 1:
                    print_cat()
                    session_count += 1
                elif n == 2:
                    print_dog()
                    session_count += 1
                elif n == 3:
                    print_rabbit()
                    session_count += 1
                else:
                    console.print("[bold red]잘못 입력했습니다. 1, 2, 3 중에 선택하거나 0을 입력해 종료하세요.[/bold red]")
            except ValueError:
                console.print("[bold red]숫자를 입력해주세요.[/bold red]")
        
        # 5번 실행 후 세션 종료 메시지
        run_count += 1
        console.print(f"\n[green]세션 {run_count}이(가) 완료되었습니다. 5번의 동물 그림을 출력했습니다.[/green]")
        console.print("[bright_green]새로운 세션이 자동으로 시작됩니다. (종료하려면 0 입력)[/bright_green]")
except KeyboardInterrupt:
    # Ctrl+C로 종료 시 메시지 출력
    console.print("\n[bold red]사용자에 의해 프로그램이 종료되었습니다.[/bold red]")
except Exception as e:
    # 기타 예외 처리
    console.print(f"\n[bold red]오류가 발생했습니다: {str(e)}[/bold red]")
