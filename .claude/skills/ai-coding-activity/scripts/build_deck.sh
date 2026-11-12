#!/bin/bash
# 사용: build_deck.sh "<문제 폴더>" "<번호 목록>" "<덱 파일>" "<LAB 표기 예: [LAB-04] 그룹조회>" "<단원 번호>"
set -e
SRC="$1"; IDS="$2"; DECK="$3"; LAB="$4"; N="$5"
TMP=$(mktemp)
python3 .claude/skills/ai-coding-activity/scripts/gen_problem_slides.py "$SRC" "$IDS" 1 1 "$TMP" >/dev/null
{ cat <<H
---
theme: ./theme
manuscript: true
colorMode: dark
fontScale: 1
title: 데이터베이스 · AI 활용 학습 활동
layout: cover
---

# AI 활용 학습 활동

코딩 테스트 문제의 풀이 과정을 AI의 도움으로 찾아가기

<p class="sub">$LAB ($N) / ITWILL - 주영아·이광호 강사</p>

---
layout: section
---

# SQL 코딩 테스트

앞서 배운 상황별 템플릿으로 프롬프트를 직접 작성하여 문제를 풀어보세요

H
cat "$TMP"
cat <<H

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">$LAB $N · ITWILL · {teacher} 강사</p>
H
} > "$DECK"
rm "$TMP"; grep -c "^## #" "$DECK"
