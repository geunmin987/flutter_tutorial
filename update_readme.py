from datetime import datetime
import re

# 목표일
target_date = datetime(2026, 4, 6, 23, 59, 59)
now = datetime.now()
delta = target_date - now

days_left = delta.days
hours_left = delta.seconds // 3600

if days_left < 0:
    new_dday_content = f"✅ 목표일이 지났습니다! ({abs(days_left)}일 경과)\n\n마지막 업데이트: {now.strftime('%Y-%m-%d %H:%M:%S')}"
else:
    new_dday_content = f"**{days_left}일 {hours_left}시간** 남았습니다!\n\n마지막 업데이트: {now.strftime('%Y-%m-%d %H:%M:%S')}"

# README 수정
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

pattern = r'(<!-- D-DAY-START -->).*?(<!-- D-DAY-END -->)'

def replace_dday(match):
    return f"{match.group(1)}\n{new_dday_content}\n{match.group(2)}"

if "<!-- D-DAY-START -->" not in readme or "<!-- D-DAY-END -->" not in readme:
    raise ValueError("README.md 파일에 D-DAY 마커가 없습니다!")

updated_readme = re.sub(pattern, replace_dday, readme, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_readme)