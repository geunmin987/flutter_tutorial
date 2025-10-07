from datetime import datetime
import re

# D-Day 목표 날짜 설정
target_date = datetime(2026, 4, 6, 23, 59, 59)
now = datetime.now()

# 남은 일수 계산
days_left = (target_date - now).days

# 새로운 D-Day 내용
new_dday_content = f"**{days_left}일** 남았습니다!\n\n마지막 업데이트: {now.strftime('%Y-%m-%d %H:%M:%S')}"

# README.md 읽기
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# 정규식으로 마커 사이 내용만 교체
pattern = r'(<!-- D-DAY-START -->).*?(<!-- D-DAY-END -->)'
replacement = r'\1\n' + new_dday_content + '\n\2'
updated_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)

# README.md 쓰기
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_readme)