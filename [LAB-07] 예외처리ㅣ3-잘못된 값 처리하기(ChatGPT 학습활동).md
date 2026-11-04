---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 예외처리 — 잘못된 값 처리하기
layout: cover
---

# 잘못된 값 처리하기

직접 시도하고, 코드를 받고, 4단 확인으로 내 코드로 만드는 연습

<p class="sub">[LAB-07] 예외처리 3 · ITWILL · {teacher} 강사</p>

<!--
「예외처리의 이해」 교안과 실습 코드를 마치고, LAB-07-2 「AI에게 답을 받는 법」에서 지침을 「ChatGPT 지침(답 받기).md」로 바꾼 학생이 하는 첫 답 받기 실습. 2교시 약 100분.
결과물: A-1 ~ A-3 코드(4단 확인 표시), 변형 문제 풀이, 템플릿 ⑰ · ⑱.
-->

---

## #01. 오늘의 진행 — 100분

<Flow color="pastel">
<li><carbon:code /><b>A 구현 · 40분</b>15분 직접 시도 → 답 받기 → 받은 코드 4단 확인</li>
<li><carbon:search /><b>B 결과가 이상할 때 · 25분</b>강사가 준 "AI 답"의 함정(실행은 되지만 틀린 값)을 찾는다</li>
<li><carbon:warning-alt /><b>C 에러 수정 · 25분</b>받은 코드를 내 노트북에 붙였을 때 나는 에러를 고친다</li>
<li><carbon:document /><b>D 정리 · 10분</b>새 템플릿을 「내 프롬프트 템플릿.md」에 추가, 오늘 고친 실수 한 줄 기록</li>
</Flow>

<Grid cols="2" gap="12">
<Tile kind="soft" color="py" tag="오늘 새로 만드는 템플릿" title="⑰ 코드 받기 · ⑱ 내 코드 고쳐 받기">「내 프롬프트 템플릿.md」의 ⑯ 뒤에 이어 붙인다</Tile>
<Tile kind="soft" color="ok" tag="오늘의 결과물" title="A-1 ~ A-3 코드 + 변형 문제 풀이">코드마다 4단 확인을 통과했는지 표시한다</Tile>
</Grid>

<!--
진행 순서는 ① 조언 받기 단계와 같지만 A의 방식이 바뀐다. 문제를 끝까지 직접 푸는 대신, 15분 직접 시도한 뒤 코드를 받고 4단 확인으로 내 코드로 만든다.
B · C의 코드는 강사가 미리 준비해 나눠 준다.
-->

---

## #02. 오늘의 규칙과 4단 확인

<Callout kind="real" title="세 가지 규칙">

- **먼저 직접 시도**: 문제마다 15분 직접 풀어 본다. 막힌 코드를 `## 내 시도`에 붙여 답을 받는다
- **배운 범위만**: `## 제약`에 배운 문법 범위를 적는다. 배우지 않은 문법이 나오면 범위 안으로 다시 요청한다
- **받은 코드 4단 확인**: 아래 네 가지를 통과해야 내 코드가 된다

</Callout>

| 단계 | 확인 | 통과 기준 |
|:--|:--|:--|
| ① 실행 | 내 노트북에서 실행해 정답과 대조 | 정답과 같은 값 |
| ② 범위 | 배우지 않은 문법이 있는지 | 모두 배운 문법 |
| ③ 설명 | 줄마다 무슨 일을 하는지 말로 설명 | 막힘없이 설명 |
| ④ 변형 | 조건 하나를 바꾼 변형 문제를 AI 없이 풀기 | 직접 풀어 정답 |

<!--
LAB-07-2에서 배운 단계 공통 규칙을 다시 짚는다. 시작 전에 지침이 「ChatGPT 지침(답 받기).md」로 바뀌었는지 확인한다. ## 내 시도 없이 보냈는데 코드가 바로 오면 지침 2-1이 적용되지 않은 것이므로, 설정을 확인하고 새 대화로 간다.
AI는 리스트 컴프리헨션 · lambda처럼 아직 배우지 않은 문법을 자주 쓴다. ② 범위에서 걸리면 범위 안으로 다시 요청한다.
-->

---

## #03. 연습 재료와 `## 제약` 범위

<div class="kicker">연습 데이터 · 수집된 판매량 원본</div>

```python
raw = ["120", " 95", "N/A", "", "1,200", "abc", "80"]   # 수집된 판매량 원본
```

<p><Chip color="py">공백</Chip> <code>" 95"</code> <Chip color="ai">쉼표</Chip> <code>"1,200"</code> <Chip color="danger">숫자가 아님</Chip> <code>"N/A"</code> · <code>""</code> · <code>"abc"</code></p>

<div class="kicker">`## 제약`에 쓰는 범위</div>

| 단원 | 범위 |
|:--|:--|
| 1 예외처리의 이해 | 문법 에러와 실행 에러, if로 대비하기, try · except, 예외 종류별 처리, 에러 메시지 변수 저장, finally, Exception 통합 처리 |
| 이전 LAB | 조건문 · 반복문 · 리스트 · 문자열 · 딕셔너리 · 함수 |

<!--
A · B · C 모두 이 raw 하나로 진행한다. 학생에게 노트북 맨 위 셀에 raw를 그대로 만들어 두게 한다. 변수 이름을 바꾸면 C의 NameError 상황을 재현하기 어렵다.
오늘 쓰는 모든 프롬프트의 ## 제약은 이 표에서 가져온다.
-->

---

## #04. 프롬프트 여섯 섹션

<div class="kicker">LAB-02부터 쓴 다섯 섹션 + <code>## 내 시도</code></div>

| 섹션 | 작성 내용 |
|:--|:--|
| `## 맥락` | 배우는 단원과 배운 범위 |
| `## 상황` | 문제 · 데이터 · 정답. 변수 이름 `raw`처럼 내 노트북 정보를 그대로 |
| `## 내 시도` | 15분 동안 내가 쓴 코드와 막힌 지점. ⑱에서는 내가 생각한 원인 |
| `## 질문` | 이번에 받을 것 한 가지 |
| `## 제약` | 배운 문법 범위(#03 표) · 쓰지 말 문법 · 지킬 변수 이름 |
| `## 출력 형식` | 코드 · 줄별 설명 표 · 내가 확인할 방법 |

<Callout kind="warn" title="## 내 시도를 비워 보내면">
지침 2-1에 따라 코드 대신 처리 순서만 온다. 시도 없이 받지 않는다
</Callout>

<!--
② 단계의 프롬프트는 여섯 섹션이다. ⑰은 ## 내 시도에 코드와 막힌 지점을, ⑱은 내가 생각한 원인을 적는다. ## 상황에 내 변수 이름을 적는 것이 C의 NameError를 막는 방법이다.
-->

---
layout: section
---

# A. 구현

15분 직접 시도 → 답 받기 → 받은 코드 4단 확인

<!--
40분. 문제 세 개. 문제마다 15분 타이머를 먼저 켜고, 시간이 끝나기 전에는 ChatGPT를 열지 않게 한다. 15분 안에 풀었다면 받지 않고 다음 문제로 간다.
-->

---

## #05. A-1 변환 가능한 값만 합계

<Callout icon="🎯" title="공백 · 쉼표를 정리해 정수로 바꾸고, 바꿀 수 없는 값은 따로 모은다. 중간에 멈추면 안 된다." color="pastel-1"></Callout>

<Grid cols="2" gap="16" align="start">
<div>

```python
raw = ["120", " 95", "N/A", "", "1,200", "abc", "80"]
```

<Output title="정답 · 합계와 실패 값">

```
1495
['N/A', '', 'abc']
```

</Output>

<p><Chip kind="outline" color="ai">템플릿</Chip> ⑰ 코드 받기</p>

</div>
<div>

<Tile kind="soft" color="yellow" tag="④ 변형 · AI 없이" title="실패한 위치(인덱스) 목록">실패 값 대신 실패한 <b>위치(인덱스)</b> 목록을 만든다

<Output title="변형 정답">

```
[2, 3, 5]
```

</Output>
</Tile>

</div>
</Grid>

<!--
정답: 합계 1495(120 + 95 + 1200 + 80), 실패 값 ['N/A', '', 'abc']. 학생 코드가 반복 도중 멈추면 try · except가 반복문 바깥에 있는 것이다(B의 함정 ③과 같은 모양).
④ 변형은 받은 코드를 보지 않고 직접 푼다. 반복할 때 위치를 함께 세어야 하므로, 받은 코드를 줄마다 설명할 수 있어야 풀린다.
-->

---
class: dense
---

## ⑰ 코드 받기

<Callout icon="💡" title="15분 직접 시도했는데 끝까지 못 풀어서, 내 시도를 이어서 완성한 코드를 받고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2">

````md
## 맥락
파이썬 예외처리 단원을 배우는 중이야. 배운 범위: 조건문 · 반복문 · 리스트 · 문자열 · 딕셔너리 · 함수 · try/except.

## 상황
리스트 raw의 값을 정수로 바꿔 합계를 구하고, 바꿀 수 없는 값은 따로 모으고 싶어.
raw = ["120", " 95", "N/A", "", "1,200", "abc", "80"]
정답: 합계 1495, 실패 값 ['N/A', '', 'abc']

## 내 시도
{내가 쓴 코드와 막힌 지점}

## 질문
내 시도를 이어서 완성한 코드를 줘.

## 제약
- 배운 범위의 문법만 써. 리스트 컴프리헨션 · lambda는 쓰지 마
- 변수 이름은 내 코드(raw)를 그대로 써

## 출력 형식
1. 코드
2. 줄마다 무슨 일을 하는지 표로 | 줄 | 하는 일 |
3. 정답과 맞는지 내가 확인할 방법 2줄
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 사용 방법</h3>

- `{내가 쓴 코드와 막힌 지점}`에 15분 동안 쓴 코드를 붙인다
- `## 상황`에 정답을 적어 두고, 받은 코드를 내 노트북에서 실행해 대조한다
- 받은 줄별 설명 표로 ③ 설명을 연습한다

</div>

<Callout kind="warn" title="주의">

- 받은 코드를 붙여 넣는 것으로 끝내지 않는다
- 4단 확인을 통과해야 내 코드다

</Callout>

</div>
</Grid>

<!--
LAB-07 새 템플릿. 지침 3-1에 따라 AI는 학생 시도에서 맞은 부분과 막힌 지점을 먼저 짚고, 그 시도를 이어서 완성한다. 처음부터 다른 방식으로 새로 쓴 코드가 오면 지침을 확인한다.
## 상황에 정답을 적는 이유: ① 실행 단계에서 바로 대조하기 위해서다. 출력 형식 3번의 "확인할 방법 2줄"은 지침 2-5와 같다.
-->

---

## #06. A-2 안전한 비율 함수

<Callout icon="🎯" title="ratio(a, b)가 a ÷ b × 100을 돌려준다. b가 0이면 에러 대신 None을 돌려준다." color="pastel-2"></Callout>

<Grid cols="2" gap="16" align="start">
<div>

<div class="kicker">확인</div>

```python
print(ratio(30, 120))
print(ratio(5, 0))
```

<Output title="정답">

```
25.0
None
```

</Output>

<p><Chip kind="outline" color="ai">템플릿</Chip> 막힌 모양에 따라 ⑰ 코드 받기 · ⑱ 내 코드 고쳐 받기</p>

</div>
<div>

<Tile kind="soft" color="yellow" tag="④ 변형 · AI 없이" title="0일 때 &quot;계산 불가&quot; 돌려주기">b가 0이면 <code>None</code> 대신 문자열 <code>"계산 불가"</code>를 돌려준다

<Output title="변형 정답">

```
ratio(5, 0) → '계산 불가'
```

</Output>
</Tile>

<Callout kind="tip" title="⑰ · ⑱ 고르기">
끝까지 못 썼으면 ⑰, 다 썼는데 에러나 틀린 값이 나오면 ⑱
</Callout>

</div>
</Grid>

<!--
확인 값: ratio(30, 120) → 25.0, ratio(5, 0) → None. if로 b가 0인지 먼저 검사하는 방법(if로 대비하기)과 ZeroDivisionError를 except로 잡는 방법 모두 교안 범위 안이다. 두 방법이 함께 오면 어느 쪽이 교안의 어느 절인지 말하게 한다.
④ 변형은 return 값 한 곳만 바뀐다. 받은 코드에서 None을 돌려주는 줄이 어디인지 설명할 수 있으면 바로 풀린다.
-->

---

## #07. A-3 에러 종류별 메시지

<Callout icon="🎯" title="문자열 리스트의 평균을 구하는 함수에서, 숫자가 아닌 값과 빈 리스트에 서로 다른 메시지를 출력한다." color="pastel-3"></Callout>

<Grid cols="2" gap="12">
<Tile kind="soft" color="danger" tag="경우 1" title="숫자가 아닌 값 → ValueError">리스트에 숫자로 바꿀 수 없는 문자열이 섞여 있을 때</Tile>
<Tile kind="soft" color="warn" tag="경우 2" title="빈 리스트 → ZeroDivisionError">값이 하나도 없어 개수로 나눌 수 없을 때</Tile>
</Grid>

<Steps color="ok">
<li>평균 함수를 <b>내가 먼저</b> 쓴다</li>
<li>except를 어디에 둘지 막히면 <b>⑱ 내 코드 고쳐 받기</b>로 보낸다</li>
<li>두 경우를 각각 넣어 <b>서로 다른 메시지</b>가 나오는지 내 노트북에서 확인한다</li>
</Steps>

<Core color="ai">예외 종류별 처리: except 하나로 뭉치지 않고, 종류마다 따로 받는다.</Core>

<!--
템플릿은 ⑱(내가 쓴 함수에 except를 어디에 둘지 막혔을 때). 교안의 "예외 종류별 처리" 절 재료다. 받은 코드가 except Exception 하나로 두 경우를 함께 처리하면 문제의 요구(서로 다른 메시지)와 맞지 않는다.
원고에 A-3의 변형 문제는 따로 없다. 시간이 남으면 강사가 조건 하나를 바꿔 AI 없이 다시 풀게 한다.
-->

---
class: dense
---

## ⑱ 내 코드 고쳐 받기

<Callout icon="💡" title="내가 쓴 코드에서 에러가 나거나 값이 틀렸고, 원인을 짐작해 봤는데 어떻게 고칠지 막힌 경우" color="pastel-3"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2">

````md
## 맥락
파이썬 예외처리 단원을 배우는 중이야.

## 상황
{내 코드}
{에러 원문 또는 틀린 결과}

## 내 시도
내가 생각한 원인: {내 생각}

## 질문
내 코드를 고친 코드를 줘.

## 제약
- 내 코드에서 바꾼 줄만 바꿔. 나머지는 그대로 둬
- 배운 범위의 문법만 써

## 출력 형식
1. 고친 코드 (바꾼 줄 끝에 # 변경 표시)
2. | 바꾼 줄 | 바꾼 이유 | 표로
3. 내가 생각한 원인이 맞았는지 한 줄
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 사용 방법</h3>

- 내 코드와 에러 원문(또는 틀린 결과)을 그대로 붙인다
- 내가 생각한 원인을 한 줄로 먼저 적는다
- `# 변경` 표시된 줄만 내 코드와 비교한다

</div>

<Callout kind="warn" title="주의">
원인을 비워 두지 않는다. 출력 형식 3번에서 내 짐작이 맞았는지 확인받는 것이 이 템플릿의 핵심
</Callout>

</div>
</Grid>

<!--
LAB-07 새 템플릿. 지침 2-6에 따라 AI는 바꾼 줄만 바꾸고 # 변경 주석과 이유 표를 붙인다. 코드 전체가 다른 모양으로 바뀌어 오면 제약의 "바꾼 줄만"을 다시 요청한다.
A-3에서는 except의 위치와 종류에 대한 학생의 짐작을 ## 내 시도에 적게 한다. C의 에러 수정에서도 같은 템플릿을 쓸 수 있다.
-->

---

### #07-1. A 마무리 — 4단 확인 표시

| 문제 | ① 실행 (정답) | ② 범위 | ③ 설명 | ④ 변형 (정답) |
|:--|:--|:--:|:--:|:--|
| A-1 | 합계 `1495`, 실패 값 `['N/A', '', 'abc']` | ☐ | ☐ | 실패 위치 `[2, 3, 5]` |
| A-2 | `ratio(30, 120)` → `25.0`, `ratio(5, 0)` → `None` | ☐ | ☐ | `"계산 불가"` |
| A-3 | 두 경우에 서로 다른 메시지 | ☐ | ☐ | 강사가 정한 조건 |

<Grid cols="2" gap="12">
<Callout kind="tip" title="② 범위에서 걸리면">
배우지 않은 문법을 `## 제약`에 적어 범위 안으로 다시 요청한다
</Callout>
<Callout kind="ai" title="③ 설명은 소리 내어">
받은 줄별 설명 표를 덮고, 줄마다 하는 일을 옆 사람에게 말한다
</Callout>
</Grid>

<!--
결과물 확인 쪽. 코드마다 네 칸을 모두 채웠는지 본다. 자주 막히는 곳: 4단 확인 중 ④ 변형을 건너뛴다. 변형 문제를 AI 없이 풀었는지 꼭 확인한다.
-->

---
layout: section
---

# B. 결과가 이상할 때

강사가 미리 AI로 받아 둔 코드. 실행은 되지만 값이 틀리다

<!--
25분. 네 개의 "AI 답"을 나눠 준다. 모두 에러 없이 실행되므로, 정답과 대조하지 않으면 함정을 알아채지 못한다.
-->

---

## #08. "AI 답"의 함정 찾기

<Steps>
<li>받은 코드를 내 노트북에 붙여 <b>raw</b>로 실행한다</li>
<li>A-1의 정답(합계 <code>1495</code>, 실패 값 <code>['N/A', '', 'abc']</code>)과 <b>대조</b>한다</li>
<li>4단 확인 중 <b>어느 단계에서 걸리는지</b> 적는다</li>
<li>찾은 함정을 한 줄로 메모한다. D 정리의 "오늘 고친 실수"에 쓴다</li>
</Steps>

| | AI 답 | 증상 |
|:--:|:--|:--|
| ① | `if r.isdigit():` 인 값만 더함 | 1495가 아니라 `200` |
| ② | try 안에서 변수 이름 오타(`totl += n`), `except: pass` | 에러 없이 합계 `0` |
| ③ | try · except를 반복문 바깥에 둠 | 합계 `215`에서 멈춤 |
| ④ | 리스트 컴프리헨션 한 줄로 작성 | 값은 맞음 |

<!--
강사용 원인(학생 자료에는 없음):
① " 95", "1,200"처럼 정리하면 쓸 수 있는 값까지 버림. 정답 대조로 잡는다.
② 넓은 except가 NameError까지 삼킴. 잡을 예외 종류를 적어야 함.
③ 첫 실패에서 반복 전체가 끝남.
④ ② 범위 위반. 배운 문법으로 다시 요청.
④는 값이 맞아서 ① 실행을 통과한다. 4단 확인이 실행 하나로 끝나지 않는 이유를 보여 주는 함정이다.
-->

---

### #08-1. 함정 ① · ②

<Grid cols="2" gap="16" align="start">
<div>

<div class="kicker">① isdigit로 거른 답</div>

```python
total = 0
for r in raw:
    if r.isdigit():
        total += int(r)
print(total)
```

<Output title="실행 결과">

```
200
```

</Output>

</div>
<div>

<div class="kicker">② 오타와 except: pass</div>

```python
total = 0
for r in raw:
    try:
        n = int(r.strip().replace(",", ""))
        totl += n
    except:
        pass
print(total)
```

<Output title="실행 결과">

```
0
```

</Output>

</div>
</Grid>

<Core color="danger">두 코드 모두 에러 없이 실행된다. 정답 1495와 대조해야 드러난다.</Core>

<!--
강사용 원인: ①은 isdigit()가 " 95"(앞 공백)와 "1,200"(쉼표)을 숫자가 아니라고 판정해 120 + 80 = 200만 더한다. 정리하면 쓸 수 있는 값까지 버린 것.
②는 totl이 정의되지 않아 매번 NameError가 나는데, 종류를 적지 않은 except가 그것까지 삼킨다. total은 0 그대로. except ValueError로 종류를 적으면 NameError가 그대로 드러난다.
-->

---

### #08-2. 함정 ③ · ④

<Grid cols="2" gap="16" align="start">
<div>

<div class="kicker">③ 반복문 바깥의 try</div>

```python
total = 0
try:
    for r in raw:
        n = int(r.strip().replace(",", ""))
        total += n
except ValueError:
    pass
print(total)
```

<Output title="실행 결과">

```
215
```

</Output>

</div>
<div>

<div class="kicker">④ 리스트 컴프리헨션 한 줄</div>

```python
total = sum([int(r.replace(",", "")) for r in raw if r.strip().replace(",", "").isdigit()])
failed = [r for r in raw if not r.strip().replace(",", "").isdigit()]
print(total, failed)
```

<Output title="실행 결과">

```
1495 ['N/A', '', 'abc']
```

</Output>

</div>
</Grid>

<Core color="warn">④는 값이 맞다. 그래도 4단 확인 중 한 단계를 통과하지 못한다.</Core>

<!--
강사용 원인: ③은 "N/A"에서 ValueError가 나는 순간 반복 전체가 끝나 120 + 95 = 215에서 멈춘다. 첫 실패에서 반복 전체가 끝남. try를 반복문 안으로 옮겨야 한 값의 실패가 다음 값으로 넘어간다.
④는 ② 범위 위반. 리스트 컴프리헨션은 아직 배우지 않은 문법이므로 배운 문법(반복문 · try · except)으로 다시 요청한다. 학생이 "어느 단계에서 걸리는지"를 ②라고 답하면 맞다.
-->

---
layout: section
---

# C. 에러 수정

받은 코드를 내 노트북에 붙였을 때 나는 에러를 고친다

<!--
25분. AI는 내 노트북을 보지 못한다. 받은 코드를 붙였을 때 나는 에러는 대부분 AI 답과 내 노트북이 맞지 않아서 생긴다.
-->

---

## #09. 붙였더니 에러 — 세 가지 상황

<Grid cols="3" gap="12" align="start">
<Tile kind="soft" color="pastel-1" tag="상황 1" title="AI 답은 data, 내 노트북은 raw">

<Output title="에러">

```
NameError: name 'data' is not defined
```

</Output>

</Tile>
<Tile kind="soft" color="pastel-2" tag="상황 2" title="함수를 정의만 하고 호출하지 않음">

<Output title="결과">

```
(아무것도 출력되지 않음)
```

</Output>

</Tile>
<Tile kind="soft" color="pastel-3" tag="상황 3" title="트레이스백이 여러 줄">

<Output title="맨 아래 줄">

```
ValueError: invalid literal for int() with base 10: 'N/A'
```

</Output>

</Tile>
</Grid>

<Steps color="ai">
<li>받은 코드를 내 노트북에 붙여 실행하고 <b>에러 원문</b>을 그대로 둔다</li>
<li>에러가 가리키는 곳과 <b>내 노트북의 변수 · 호출</b>을 비교한다</li>
<li>고치지 못하면 <b>⑱ 내 코드 고쳐 받기</b>에 에러 원문과 내 짐작을 붙여 보낸다</li>
</Steps>

<!--
강사용 원인(학생 자료에는 없음):
상황 1: AI는 내 변수 이름을 모름. ## 상황에 내 변수 이름을 적는다(⑰의 제약 "변수 이름은 raw를 그대로").
상황 2: 정의와 호출 구분. 함수 정의 셀은 실행해도 아무것도 출력하지 않는다. 호출하는 줄을 더한다.
상황 3: 맨 아래 줄 → 위로 올라가며 내 코드 줄 찾기.
-->

---

### #09-1. 상황 1 · 2의 받은 코드

<Grid cols="2" gap="16" align="start">
<div>

<div class="kicker">상황 1 · 변수 이름이 다름</div>

```python
total = 0
failed = []
for value in data:
    try:
        text = value.strip().replace(",", "")
        total += int(text)
    except ValueError:
        failed.append(value)
print(total, failed)
```

</div>
<div>

<div class="kicker">상황 2 · 정의만 있음</div>

```python
def sum_valid(raw):
    total = 0
    for r in raw:
        try:
            text = r.strip().replace(",", "")
            total += int(text)
        except ValueError:
            pass
    return total
```

</div>
</Grid>

<Callout kind="tip" title="고친 뒤에는">
고친 코드도 받은 코드와 같다. A-1 정답(합계 <code>1495</code>)과 대조하는 ① 실행부터 다시 한다
</Callout>

<!--
상황 1: data를 raw로 바꾸면 1495 ['N/A', '', 'abc']가 나온다. 강사용 원인: AI는 내 변수 이름을 모름. ## 상황에 내 변수 이름을 적는다.
상황 2: 마지막에 print(sum_valid(raw))를 더하면 1495가 나온다. 강사용 원인: 정의와 호출 구분.
-->

---

### #09-2. 상황 3의 받은 코드

<Grid cols="2" gap="16" align="start">
<div>

<div class="kicker">상황 3 · 함수 안에서 에러</div>

```python
def to_int(text):
    return int(text.strip().replace(",", ""))

total = 0
for r in raw:
    total += to_int(r)
```

</div>
<div>

<Output title="트레이스백 맨 아래 줄">

```
ValueError: invalid literal for int() with base 10: 'N/A'
```

</Output>

<Callout kind="warn" title="여러 줄이어도 당황하지 않기">
에러 원문은 줄이지 않고 그대로 둔다. ⑱로 보낼 때도 트레이스백 전체를 붙인다
</Callout>

</div>
</Grid>

<!--
강사용 원인: 맨 아래 줄 → 위로 올라가며 내 코드 줄 찾기. 트레이스백은 for 반복의 total += to_int(r) 줄 → to_int 안의 return 줄 → 맨 아래 ValueError 순서로 찍힌다. 맨 아래 줄을 먼저 읽고 위로 올라가며 내 코드 줄을 찾는다.
고치는 방향: to_int 호출을 try · except ValueError로 감싸 반복 안에서 처리한다. 고친 뒤 1495가 나오는지 대조한다.
-->

---
layout: section
---

# D. 정리

새 템플릿을 모으고, 오늘 고친 실수를 한 줄로 남긴다

<!--
10분. 결과물을 확인하고 마친다.
-->

---
layout: cards
cols: 3
---

## #10. 오늘의 정리

<div class="py">

#### 📄 템플릿 추가

- 「내 프롬프트 템플릿.md」에 ⑰ 코드 받기 · ⑱ 내 코드 고쳐 받기를 붙인다
- 다음 LAB부터 `## 상황` · `## 내 시도`만 바꿔 쓴다

</div>
<div class="ai">

#### ✏️ 실수 한 줄

- 오늘 고친 실수를 한 줄로 기록한다
- B의 함정, C의 에러 중 내가 직접 겪은 것을 적는다

</div>
<div class="ok">

#### ✅ 결과물 확인

- A-1 ~ A-3 코드(4단 확인 표시)
- 변형 문제 풀이
- 템플릿 ⑰ · ⑱

</div>

<Core color="ok">받은 코드는 4단 확인을 통과해야 내 코드다.</Core>

<!--
결과물: A-1 ~ A-3 코드(4단 확인 표시), 변형 문제 풀이, 템플릿 ⑰ · ⑱. 걷지는 않고 확인만 한다.
자주 막히는 곳: 4단 확인 중 ④ 변형을 건너뜀. 변형 문제를 AI 없이 풀었는지 꼭 확인한다.
데이터 분석 연결: 실제 데이터에는 결측값 · 잘못된 값이 섞여 있다. 한 행 때문에 전체 처리가 멈추지 않게 하는 것이 데이터 처리의 기본이다. 다음 LAB-08(CSV 읽고 집계하기)로 이어진다.
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-07] 예외처리 3 · ITWILL · {teacher} 강사</p>
