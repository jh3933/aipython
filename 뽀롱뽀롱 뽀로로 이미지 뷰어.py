import tkinter as tk
from PIL import Image, ImageTk
import os

def show_image(character):
    """선택된 캐릭터의 이미지를 화면에 표시합니다."""
    image_path = f"images/{character}.jpg"  # 이미지 파일 경로 (.jpg 형식으로 변경)
    try:
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo  # 이미지 객체 유지
    except FileNotFoundError:
        tk.messagebox.showerror("오류", f"{character} 이미지를 찾을 수 없습니다: {image_path}")
    except Exception as e:
        tk.messagebox.showerror("오류", f"{character} 이미지 로딩 오류: {e}")

# 메인 윈도우 생성
window = tk.Tk()
window.title("뽀롱뽀롱 뽀로로 이미지 뷰어")

# 이미지 표시를 위한 Label 위젯 생성
image_label = tk.Label(window)
image_label.pack(padx=10, pady=10)

# 버튼 프레임 생성 (버튼들을 가로로 배치하기 위해)
button_frame = tk.Frame(window)
button_frame.pack()

# 뽀로로 버튼
pororo_button = tk.Button(button_frame, text="뽀로로", command=lambda: show_image("pororo"))
pororo_button.pack(side=tk.LEFT, padx=5)

# 크롱 버튼
crong_button = tk.Button(button_frame, text="크롱", command=lambda: show_image("crong"))
crong_button.pack(side=tk.LEFT, padx=5)

# 에디 버튼
eddy_button = tk.Button(button_frame, text="에디", command=lambda: show_image("eddy"))
eddy_button.pack(side=tk.LEFT, padx=5)

# 프로그램 실행
window.mainloop()