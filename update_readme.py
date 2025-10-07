from datetime import datetime

# D-Day 목표 날짜 설정
target_date = datetime(2025, 12, 31, 23, 59, 59)
now = datetime.now()

# 남은 일수 계산
days_left = (target_date - now).days

# README 내용 생성
readme_content = f"""# D-Day 타이머

## 목표일까지

**{days_left}일** 남았습니다!

- 목표 날짜: 2025년 12월 31일
- 마지막 업데이트: {now.strftime('%Y-%m-%d %H:%M:%S')}
"""

# README.md 파일에 쓰기
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)