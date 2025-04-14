from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Rich Console 객체 생성
console = Console()

# 1. 간단한 색상 텍스트 출력
console.print("[bold blue]Rich[/bold blue]를 사용한 [red]예쁜[/red] [green]출력[/green] 예제입니다!")

# 2. 간단한 패널 만들기
console.print(Panel("중요한 메시지", title="알림", border_style="red"))

# 3. 기본 테이블 만들기
table = Table(show_header=True)
table.add_column("이름")
table.add_column("점수")
table.add_column("등급")

table.add_row("홍길동", "85", "B+")
table.add_row("김철수", "92", "A")
table.add_row("이영희", "78", "C+")

console.print(table)

from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.tree import Tree
import time

# Rich Console 객체 생성
console = Console()

# 1. 기본적인 Rich print 사용 (색상과 스타일)
console.print("\n[bold]Rich 라이브러리 예제[/bold]\n", style="cyan underline")

print("[bold red]빨간색 굵은 텍스트[/bold red]")
print("[blue]파란색[/blue] 텍스트와 [green]초록색[/green] 텍스트 혼합")
print("[yellow on black]노란색 텍스트에 검은 배경[/yellow on black]")
print("[bold italic cyan]굵고 기울어진 청록색[/bold italic cyan]")

# 2. 패널 만들기
console.print(Panel("이것은 멋진 [bold magenta]패널[/bold magenta]입니다!",
                   title="패널 예제", 
                   subtitle="Rich 라이브러리"))

# 3. 테이블 만들기
table = Table(title="프로그래밍 언어", show_header=True, header_style="bold magenta")
table.add_column("언어", style="dim")
table.add_column("연도", justify="right")
table.add_column("특징", justify="center")

table.add_row("Python", "1991", "간결함, 가독성")
table.add_row("JavaScript", "1995", "웹 프로그래밍")
table.add_row("Go", "2009", "동시성, 성능")
table.add_row("Rust", "2010", "메모리 안전성")

console.print(table)

# 4. 진행 표시줄
console.print("\n[bold]진행 표시줄 예제:[/bold]")
for step in track(range(10), description="처리 중..."):
    time.sleep(0.1)  # 작업 시뮬레이션

# 5. 마크다운 렌더링
markdown = """
# Rich로 마크다운 표시하기

Rich는 **마크다운**을 터미널에서 렌더링할 수 있습니다.

## 특징
* 텍스트 스타일링
* 테이블 생성
* 코드 강조
* 그리고 더 많은 기능!
"""

console.print(Markdown(markdown))

# 6. 코드 구문 강조
code = """
def hello_world():
    print("Hello, Rich World!")
    
    for i in range(10):
        # 숫자 출력
        print(f"Number: {i}")
        
hello_world()
"""

console.print(Syntax(code, "python", theme="monokai", line_numbers=True))

# 7. 트리 구조 만들기
tree = Tree("📁 프로젝트")
code_folder = tree.add("📁 src")
code_folder.add("📄 main.py")
code_folder.add("📄 utils.py")

docs_folder = tree.add("📁 docs")
docs_folder.add("📄 README.md")
docs_folder.add("📄 CONTRIBUTING.md")

tests_folder = tree.add("📁 tests")
tests_folder.add("📄 test_main.py")
tests_folder.add("📄 test_utils.py")

console.print(tree)

# 8. 로그 수준에 따른 출력
console.print("\n[bold]로그 수준 예제:[/bold]")
console.log("일반 로그 메시지")
console.info("정보 메시지")
console.warning("경고 메시지")
console.error("오류 메시지")

# 9. 텍스트 줄 바꿈 및 정렬
console.print(Panel("이 텍스트는 자동으로 줄 바꿈됩니다. 너무 길면 터미널 너비에 맞게 자동으로 조정됩니다. Rich는 이런 기능도 제공합니다.", 
                   title="텍스트 줄 바꿈",
                   width=60))

print("[cyan]이것은 하늘색 글자입니다![/cyan]")