---
theme: ./slidev-themes/hossam
colorMode: dark
sidebar: true
fontScale: 1
title: 데이터 분석 모듈화 · AI로 내 함수 자가 점검
layout: cover
---

# AI로 내 함수 자가 점검

내 함수의 실행 결과가 정상 결과와 다를 때, ChatGPT에게 어디가 왜 틀렸는지 찾아 달라고 하는 방법

<p class="sub">데이터 분석 모듈화 · 주영아·이광호 강사</p>

---

## #01. 오늘의 실습 흐름

실습 노트북에서 익힌 분석 순서를 함수로 옮기고, 완성 노트북에 주어진 코드로 결과를 맞춰 본다.

<Flow>
<li>📘<b>흐름 익히기</b>완성 노트북의 코드를 위에서부터 실행하며 분석 순서를 익힘</li>
<li>🧩<b>함수 만들기</b>PDF 교안을 보며 모듈 파일(<code>my_plot.py</code> 등)에 함수를 직접 작성함</li>
<li>🧪<b>결과 맞춰 보기</b>노트북의 "모듈화 기능 확인" 코드를 실행해 완성 노트북에 저장된 정상 실행 결과와 비교함</li>
<li>🤖<b>자가 점검</b>함수와 두 결과를 프롬프트에 붙여 ChatGPT에 보냄</li>
<li>🔁<b>고치고 다시 실행</b>답변을 보고 직접 고친 뒤, 정상 실행 결과와 같아질 때까지 다시 실행함</li>
</Flow>

<Core color="ai">AI는 답안지를 대신 써 주는 친구가 아니라 <span class="hl ai">내 답이 정답과 왜 다른지 짚어 주는 채점 조교</span>다.</Core>

---

### #01-1. 확인 코드와 정답은 이미 있음

완성 노트북 끝에는 내가 만든 함수를 부르는 확인 코드와,<br/>그 코드의 정상 실행 결과가 함께 들어 있다.

<span class="kicker">예: [LAB-07] 사후검정 노트북의 마지막 셀</span>

```python
# 4. 모듈화 기능 확인 — 데이터(origin)도 노트북 앞에서 이미 불러옴
my_stats.posthoc_oneway(origin, y='weight', between='group')
```

<Grid class="big" cols="2" gap="12">
<Tile kind="soft" color="ok" title="새로 만들 필요 없음">

- 확인 코드도, 정상 실행 결과도 완성 노트북에 있음
- AI에게 예상 결과를 만들어 달라고 하지 않음

</Tile>
<Tile kind="soft" color="ai" title="AI에게 물을 것">

- 정답과 내 결과가 **왜** 다른가
- 틀린 줄과 이유, 고치는 방법

</Tile>
</Grid>

<Callout kind="warn" title="완성 노트북을 그대로 실행하면 저장된 정상 실행 결과가 내 결과로 바뀌므로, 원본은 두고 복사본에서 실행한다" />



---

## #02. 모듈 다음의 AI 활용

지금 만드는 모듈은 AI를 제대로 쓰기 위한 준비 작업이다.

<Flow>
<li>🧩<b>모듈 만들기</b>분석 흐름을 함수로 옮기고 자가 점검으로 검증함(오늘)</li>
<li>📝<b>docstring 쓰기</b>함수마다 무엇을 하고 무엇을 받고 돌려주는지 적음</li>
<li>🤖<b>에이전트에 전달</b>모듈과 "먼저 쓰라"는 규칙을 에이전트에게 줌</li>
<li>📊<b>에이전트가 분석</b>에이전트가 내 모듈 함수로 분석을 수행함</li>
</Flow>

<Core color="ai">모듈은 과제로 끝나지 않는다. <span class="hl ai">에이전트가 쓰는 나만의 분석 도구</span>가 된다.</Core>

---

### #02-1. 생성형 AI의 한계

채팅창의 생성형 AI는 내 데이터와 내 코드를 직접 보지도, 실행하지도 못한다.

<Grid class="big" cols="2" gap="12">
<Tile kind="soft" color="danger" title="1. 실행하지 못함">

- 코드를 써 줄 뿐, 실행은 내가 함
- 결과가 맞는지 AI는 모름

</Tile>
<Tile kind="soft" color="ai" title="2. 맥락이 끊김">

- 내 데이터 · 모듈을 매번 붙여 넣어야 함
- 붙여 넣은 만큼만 앎

</Tile>
<Tile kind="soft" color="yellow" title="3. 매번 새 코드">

- 같은 분석도 물을 때마다 다른 코드
- 수업 방향과 다른 방식이 섞임

</Tile>
<Tile kind="soft" color="pastel-1" title="4. 검증은 사람 몫">

- 틀린 답도 그럴듯하게 말함
- 그래서 자가 점검이 꼭 필요함

</Tile>
</Grid>

---

### #02-2. 에이전틱 AI

에이전틱 AI는 내 폴더의 데이터와 모듈을 직접 읽고, 코드를 실행하고, 결과를 보고 스스로 고친다.

| 항목 | 생성형 AI (채팅) | 에이전틱 AI |
|:--|:--|:--|
| 코드 실행 | 내가 복사해 실행함 | 에이전트가 직접 실행함 |
| 내 모듈 | 붙여 넣은 함수만 앎 | 폴더에서 읽고 import 해서 씀 |
| 결과 확인 | 내가 보고 다시 물음 | 실행 결과를 보고 스스로 고침 |
| 분석 방식 | 물을 때마다 새 코드 | 내 모듈 함수로 일관되게 |

<Core color="ai">에이전트가 <span class="hl ai">내 모듈로 직접 분석을 수행할 때</span>가 진짜 AI 활용 데이터 분석이다.</Core>

---

### #02-3. 에이전트가 내 모듈을 쓰게 하려면

에이전트는 불러올 수 있고, 설명이 있고, 먼저 쓰라는 규칙이 있는 모듈을 쓴다.

<Grid class="big" cols="2" gap="12">
<Tile kind="soft" color="py" title="1. 불러올 수 있게">

- `from helpers import my_plot` 이 바로 됨
- 모듈 파일을 프로젝트 안에 둠

</Tile>
<Tile kind="soft" color="ok" title="2. docstring으로 설명">

- 함수마다 하는 일 · 받는 값 · 돌려주는 값을 적음
- 에이전트가 읽고 언제 쓸지 판단함

</Tile>
<Tile kind="soft" color="ai" title="3. 규칙으로 먼저 쓰게">

- 규칙 파일(`CLAUDE.md` · `AGENTS.md`)에 적음
- 모듈 함수 먼저, 없는 기능만 직접 구현

</Tile>
<Tile kind="soft" color="yellow" title="4. 검증된 모듈">

- 에이전트는 모듈을 믿고 그대로 씀
- 버그가 있으면 분석 결과도 틀림

</Tile>
</Grid>

<Callout kind="ai" title="에이전트를 사용하는 방법은 선형회귀 이후에 별도 수업으로 진행한다" />

---
class: dense tight
---

### #02-4. docstring이 가장 중요하다

에이전트는 함수 이름이 아니라 docstring을 읽고 언제, 어떻게 쓸지 판단한다.

<Grid cols="3fr 2fr" align="start">
<div class="tight">

<span class="kicker">참고 문서의 docstring (my_qtcheck)</span>

```python
def check_missing_values(data):
    """
    데이터프레임에서 컬럼별 결측치 개수와 비율을
    계산하여 데이터 프레임으로 반환하는 함수

    Args:
        data (DataFrame): 결측치를 점검할 데이터프레임

    Returns:
        DataFrame: 컬럼별 결측치 개수와 비율이 포함된
                   데이터프레임
    """
```

</div>
<div>

<Grid class="md" cols="1" gap="8">
<Tile kind="soft" color="py" title="첫 줄 설명">

- 언제 쓰는 함수인지

</Tile>
<Tile kind="soft" color="ok" title="Args">

- 무엇을 넣어야 하는지

</Tile>
<Tile kind="soft" color="ai" title="Returns">

- 무엇을 돌려받는지

</Tile>
</Grid>

</div>
</Grid>

<Callout kind="warn" title="docstring이 비었거나 실제 동작과 다르면, 에이전트는 함수를 쓰지 않거나 잘못 쓴다" />

---
class: dense tight
---

### #02-5. 정리

모듈을 만드는 과정은 AI를 더 잘 쓰기 위한 준비 작업이다.

<Grid class="big" cols="3" gap="12">
<Tile kind="soft" color="py" title="1. 지금">

- 분석 흐름을 함수로 모듈화
- docstring을 꼼꼼히 작성

</Tile>
<Tile kind="soft" color="ok" title="2. 점검">

- 생성형 AI로 자가 점검
- 정상 결과와 같게 맞춤

</Tile>
<Tile kind="soft" color="ai" title="3. 다음">

- 에이전트에게 모듈을 전달
- 내 모듈로 분석을 맡김

</Tile>
</Grid>

<Core color="yellow">잘 만든 모듈과 잘 쓴 docstring이 <span class="hl warn">에이전트가 쓰는 나만의 분석 도구</span>가 된다.</Core>

---

## #03. 참고 문서 사이트

`https://pyapi.juyounga.kr/` 은 수업에서 만드는 함수들의 사용 설명서다.

모듈 파일 하나당 웹 페이지 하나로 구성되어 있고 페이지마다 각각의 함수를 4가지 측면으로 설명한다.

<Grid class="big" cols="2" gap="8">
<Tile kind="soft" color="py" title="1. 함수 정의">

- 함수 이름 · 받는 값 · 기본값이 적힌 줄
- 예: `def lineplot(...)`

</Tile>
<Tile kind="soft" color="pastel-6" title="2. Parameters 표">

- 받는 값 하나당 한 줄
- 이름 · 자료형 · 설명 · 기본값

</Tile>
<Tile kind="soft" color="ok" title="3. Returns">

- 함수가 돌려주는 값
- 그 값의 자료형과 설명

</Tile>
<Tile kind="soft" color="ai" title="4. Source code">

- 그 함수의 실제 파이썬 코드
- 내 함수와 비교하는 기준

</Tile>
</Grid>



---

### #03-1. 모듈 페이지 주소

모듈 페이지 주소는 `https://pyapi.juyounga.kr/api/<모듈 이름>/` 처럼 끝에 모듈 이름만 바꿔 넣으면 된다.

| 모듈 이름 | 페이지 주소 |
|:--|:--|
| `my_qtcheck` | `https://pyapi.juyounga.kr/api/my_qtcheck/` |
| `my_prep` | `https://pyapi.juyounga.kr/api/my_prep/` |
| `my_plot` | `https://pyapi.juyounga.kr/api/my_plot/` |
| `my_stats` | `https://pyapi.juyounga.kr/api/my_stats/` |

<Callout kind="plain" color="muted" title="사이트에 있는 모듈">

`my_util` · `my_qtcheck` · `my_prep` · `my_plot` · `my_stats` · `my_ols` · `my_logit` · `my_ml` · `my_cluster` · `my_ts` · `my_diag` · `my_gis` · `my_outlier_clipper` · `my_vif_selector`

</Callout>

<p class="text-sm opacity-70">※ 앞으로 수업이 진행되면서 추가되는 모듈도 같은 규칙으로 주소가 구성된다.</p>

---

### #03-2. 그냥 물어보면 생기는 문제

지금 구현해야 하는 범위를 정해 주지 않으면 AI가 오히려 잘못된 결과로 이끌 수 있다.

범위 없이 "이 사이트 보고 내 코드 봐 줘"라고 물으면 AI는 수업보다 너무 깊은 내용이나 수업 방향과 다른 구현 코드까지 제시해, 아래와 같은 문제가 생긴다.

<Grid class="md" cols="2" gap="12">
<Tile kind="soft" color="danger" title="안 배운 기능 추가 권유">교안에 없는 파라미터·처리를 "빠졌다"며 넣으라고 함</Tile>
<Tile kind="soft" color="ai" title="엉뚱한 함수와 비교">이름이 같은 함수가 여러 모듈에 있음(<code>fit_model</code> · <code>predict</code> · <code>test_linear</code> 등)</Tile>
<Tile kind="soft" color="yellow" title="추측 답변">페이지를 실제로 열지 못하고 기억으로 그럴듯하게 답함</Tile>
<Tile kind="soft" color="pastel-6" title="정답 통째 제공">고친 함수 전체를 써 주어 무엇이 틀렸는지 배우지 못함</Tile>
</Grid>

<Core color="py">프롬프트로 <span class="hl">모듈 · 함수 · 비교 기준 · 답변 모양</span>을 정해 볼 곳을 좁혀 준다 → <Chip kind="outline" color="ai">컨텍스트 엔지니어링</Chip></Core>

---
class: tight
---

## #04. 자가 점검 프롬프트

자가 점검 프롬프트는 여섯 부분으로 되어 있다.

<Grid class="big" cols="3" gap="12">
<Tile kind="soft" color="ai" title="1. 역할">

- AI를 코드 리뷰 조교로 정함

</Tile>
<Tile kind="soft" color="pastel-6" title="2. 근거 자료">

- 모듈 페이지 주소와 **내 함수 코드**
- "이름이 같은 함수 하나만" 비교하라는 지시

</Tile>
<Tile kind="soft" color="pastel-1" title="3. 점검 범위">

- 붙여 넣은 함수만 봄
- 안 배운 기능은 추가하지 않음

</Tile>
<Tile kind="soft" color="py" title="4. 비교 기준">

- 파라미터 · 반환값 · 계산
- 원본 변경 · 출력 · 오류 가능성

</Tile>
<Tile kind="soft" color="yellow" title="5. 실행 결과 비교">

- 완성 노트북의 확인 코드
- 정상 실행 결과 · 내 실행 결과

</Tile>
<Tile kind="soft" color="ok" title="6. 출력 형식">

- 판정 → 결과 차이 → 문제 표
- 수정 줄 → 근거

</Tile>
</Grid>

---
class: dense tight
---

### #04-1. 프롬프트 전문 (1/3)

함수 하나씩, `{ }` 로 표시한 칸만 채워 ChatGPT에 보낸다.

<Prompt title="자가 점검 프롬프트 (1/3) — 역할 · 근거 자료 · 점검 범위" cols="2">

````md
## 역할
너는 파이썬 데이터 분석 수업의 코드 리뷰 조교야.
나는 데이터 분석 기능을 함수로 만들어 모듈로 묶는 실습을 하고 있어.

## 근거 자료
### 참고 문서
https://pyapi.juyounga.kr/api/{모듈 이름}/
- 이 페이지에서 아래 내 함수와 이름이 같은 함수 하나만 찾아 비교해.
- 그 함수의 정의(시그니처), Parameters 표, Returns, Source code를 근거로 써.
- 페이지를 열지 못했거나 같은 이름의 함수가 없으면 추측하지 말고 그 사실만 먼저 말해.

### 내 함수 (모듈: {모듈 이름})
```python
{내 함수 코드}
```

## 점검 범위
- 내가 붙여 넣은 함수만 점검해.
- 참고 문서에는 아직 배우지 않은 기능이 많아. 내 함수에 없는 파라미터나 처리를 새로 넣으라고 하지 마.
  참고 문서에만 있는 파라미터는 "참고 문서에는 있음"이라고 한 줄로만 알려 줘.
- 변수 이름, 주석, 줄 바꿈 같은 스타일 차이는 문제로 보지 마.
````

</Prompt>

---
class: dense tight
---

### #04-1. 프롬프트 전문 (2/3)

앞 쪽(1/3)에 이어 붙여 **한 번에** 보낸다.

<Prompt title="자가 점검 프롬프트 (2/3) — 비교 기준 · 실행 결과 비교" cols="2">

````md
## 비교 기준
1. 함수 이름과 파라미터(이름 · 순서 · 기본값)
2. 반환값(자료형 · 컬럼 이름 · 모양)
3. 처리 순서와 계산 결과
4. 원본 데이터를 바꾸는지(copy 여부)
5. print로 출력하는 내용
6. 실행할 때 오류가 날 수 있는 곳

## 실행 결과 비교
아래 확인 코드와 정상 실행 결과는 완성 노트북에 있는 것이야.
새 테스트 코드나 예상 결과를 만들지 말고, 두 결과가 다른 원인을 내 함수에서 찾아 줘.
### 확인 코드
{완성 노트북의 모듈화 기능 확인 코드}
### 정상 실행 결과
{완성 노트북에 저장된 실행 결과}
### 내 실행 결과
{내가 실행한 출력 또는 오류 메시지}
````

</Prompt>

---
class: dense tight
---

### #04-1. 프롬프트 전문 (3/3)

앞 쪽(2/3)에 이어 붙여 **한 번에** 보낸다.

<Prompt title="자가 점검 프롬프트 (3/3) — 출력 형식">

````md
## 출력 형식
1. 판정 한 줄: ✅ 참고 문서와 같음 / ⚠️ 결과는 같지만 처리 방법이 다름 / ❌ 결과가 다르거나 오류가 남
2. 결과 차이: 정상 실행 결과와 내 실행 결과가 다른 곳(같으면 "같음")
3. 문제 표: | 번호 | 위치(해당 코드 한 줄) | 무엇이 다른가 | 왜 문제인가 | 어떻게 고치나 |
4. 수정 코드: 고칠 줄만 "바꾸기 전 → 바꾼 후"로 보여 줘. 함수 전체를 다시 쓰지 마.
5. 근거: 비교에 쓴 참고 문서의 함수 이름과 링크

설명은 고등학생도 이해할 수 있는 쉬운 말로 해 줘.
````

</Prompt>

---

### #04-2. 채울 칸

다섯 칸 중 세 칸은 노트북에서 그대로 복사해 오면 된다.

<Grid cols="3" gap="12">
<Tile kind="soft" color="yellow" title="{모듈 이름}">내가 만든 모듈 파일 이름에서 <code>.py</code> 를 뺀 것<br/>예: <code>my_stats</code></Tile>
<Tile kind="soft" color="ai" title="{내 함수 코드}">내 모듈 파일에서 <code>def</code> 줄부터 함수 끝까지 하나 전체</Tile>
<Tile kind="soft" color="py" title="{완성 노트북의 모듈화 기능 확인 코드}">완성 노트북 "모듈화 기능 확인" 셀의 코드 그대로</Tile>
<Tile kind="soft" color="ok" title="{완성 노트북에 저장된 실행 결과}">실행하기 전 완성 노트북에 저장된 출력 그대로. 그래프는 출력 이미지를 첨부하거나<br/>제목 · 축 · 선 개수 · 범례를 글로 적음</Tile>
<Tile kind="soft" color="pastel-1" title="{내가 실행한 출력 또는 오류 메시지}">같은 셀을 내 함수로 실행한 결과.<br/>오류가 났다면 오류 메시지 마지막 몇 줄까지</Tile>
</Grid>

<p class="text-sm opacity-70">※ <b class="!text-[var(--danger)]">PDF 교안은 복사가 되지 않으므로</b> 프롬프트에 붙일 코드와 결과는 모두 <b class="!text-[var(--ok)] underline decoration-2 decoration-[#5fe3a1] underline-offset-6">내 모듈 파일과 노트북에서 복사</b>한다.</p>

<p class="text-sm opacity-70">※ 칸을 모두 채운 예시는 함께 배포한 <code>점검 예시 (1) - 프롬프트 샘플.md</code> · <code>점검 예시 (2) - 프롬프트 샘플.md</code> 파일을 참고한다.</p>

---

### #04-3. 같은 이름 주의

이름이 같은 함수가 여러 모듈에 있다.

모듈 이름을 틀리게 적으면 AI가 다른 함수와 비교한다.

<Callout kind="warn" title="이름이 겹치는 함수">

- `fit_model` · `predict`: `my_ols` · `my_logit` · `my_ts`
- `test_linear`: `my_ols` · `my_logit`
- `test_independent`: `my_stats` · `my_ols` · `my_logit`
- `fit_pipeline` · `compare_models`: `my_ols` · `my_logit` (`fit_pipeline` 은 `my_ml` 에도 있음)

</Callout>

<Core color="yellow">확인 코드에 적힌 <span class="hl warn">모듈 이름(<code>my_stats.</code> 앞부분)</span>을 그대로 옮겨 적으면 틀리지 않는다.</Core>

---
class: dense tight
---

## #05. 점검 예시 (1)

모듈화 첫 실습인 `my_plot` 모듈의 `lineplot` 을 아래처럼 만들었다고 하자.

```python
# 파라미터 일부 생략(...)
def lineplot(data=None, x=None, y=None, hue=None, ..., ax=None, **params):
    # 그래프 초기화
    fig = None
    if ax is None:
        ax = init(width=width, height=height, title=title, xlabel=xlabel,
                  ylabel=ylabel)
    # 선 그래프 그리기
    sb.lineplot(data=data, x=x, y=y, palette=palette, color=color,
                linewidth=linewidth, linestyle=linestyle, marker=marker,
                markersize=markersize, markeredgewidth=markeredgewidth,
                markeredgecolor=markeredgecolor, markerfacecolor=markerfacecolor,
                ax=ax, **params)
    # 그래프 표시
    if fig is not None:
        show(save_path=save_path)
```

---
class: dense tight
---

### #05-1. 확인 코드 실행

[LAB-06] Line Plot 완성 노트북의 "모듈화 기능 확인" 셀을 내 모듈로 실행한다.

<span class="kicker">완성 노트북의 모듈화 기능 확인 코드</span>

```python
origin = load_data('icecream_sales')  # 노트북 앞에서 이미 불러온 데이터
my_plot.lineplot(data=origin, x='Date', y="Quantity", hue="Topping",
                 title="Topping별 판매수량", xlabel="날짜", ylabel="판매량",
                 marker="o", markersize=10, markeredgewidth=2,
                 markerfacecolor="#000000", markeredgecolor="#ffffff")
```

---
class: dense tight
---

### #05-2. 결과 맞춰 보기

내 실행 결과를 완성 노트북에 저장되어 있던 정상 실행 결과와 나란히 놓고 본다.

<Grid cols="2" align="start">
<div class="tight">

<span class="kicker">정상 실행 결과 (완성 노트북의 그림을 글로 옮김)</span>

<Output>

```text
선 그래프 · 제목 'Topping별 판매수량'
x축 '날짜' · y축 '판매량' · 검은 원 마커
토핑별 선 4개 · 범례 Topping
```

</Output>

</div>
<div class="tight">

<span class="kicker">내 실행 결과 (오류 마지막 줄)</span>

<Output>

```text
AttributeError: 'tuple' object has no attribute 'xaxis'
```

</Output>

</div>
</Grid>

<Core color="ai">그래프 대신 오류가 났다는 것은 눈으로도 보인다. <span class="hl ai">어느 줄이 왜 틀렸는지</span>는 AI에게 묻는다.</Core>

---

### #05-3. AI 답변 (1/4) — 판정과 결과 차이

실수가 있는 함수를 보내면 먼저 ❌ 판정과 함께 결과가 어디서 다른지 짚어 준다.

<Callout kind="ai" title="ChatGPT 답변">

**1. 판정:** ❌ 결과가 다르거나 오류가 남

**2. 결과 차이:** 정상 결과는 토핑별 선 4개가 있는 선 그래프인데, 내 결과는 그래프가 그려지기 전에 `AttributeError` 가 나서 아무것도 보이지 않아요. 지금은 1번 오류에 가려져 2번 문제가 아직 드러나지 않았어요.

</Callout>

---
class: dense tight
---

### #05-4. AI 답변 (2/4) — 문제 표

이어서 틀린 곳을 하나씩 표로 짚어 준다.

<Callout kind="ai" title="ChatGPT 답변 (이어서)">

**3. 문제 표**

| 번호 | 위치 | 무엇이 다른가 | 왜 문제인가 | 어떻게 고치나 |
|:--|:--|:--|:--|:--|
| 1 | `ax = init(width=width, ...` | `init` 이 돌려주는 두 값(fig, ax)을 `ax` 하나에 담았어요 | `ax` 가 그림판이 아니라 두 값을 묶은 튜플이 돼서 `sb.lineplot` 이 그릴 곳을 못 찾고 `'tuple' object has no attribute 'xaxis'` 오류가 나요. `fig` 도 계속 None이라 `show` 도 불리지 않아요 | `fig, ax = init(...)` 처럼 두 변수로 나눠 받아요 |
| 2 | `sb.lineplot(data=data, x=x, y=y, palette=palette,` | `hue=hue` 가 없어요 | 확인 코드가 `hue="Topping"` 을 넘겨도 그래프에 전달되지 않아요. 토핑별 선 4개 대신 선 1개만 그려지고 범례도 생기지 않아요 | `y=y,` 뒤에 `hue=hue,` 를 넣어요 |

</Callout>

---
class: dense tight
---

### #05-5. AI 답변 (3/4) — 수정 코드

답변의 뒷부분은 고칠 줄만 "바꾸기 전 → 바꾼 후"로 보여 준다.

<Callout kind="ai" title="ChatGPT 답변 (이어서)">

**4. 수정 코드:** 고칠 줄만 보여 줄게요.

```python
# 1번 — 바꾸기 전 → 바꾼 후
ax = init(width=width, height=height, title=title, xlabel=xlabel,
fig, ax = init(width=width, height=height, title=title, xlabel=xlabel,

# 2번 — 바꾸기 전 → 바꾼 후
sb.lineplot(data=data, x=x, y=y, palette=palette,
sb.lineplot(data=data, x=x, y=y, hue=hue, palette=palette,
```

</Callout>

---
class: dense tight
---

### #05-6. AI 답변 (4/4) — 근거와 다시 실행 안내

답변의 마지막은 비교에 쓴 근거와 다시 실행하라는 안내다.

<Callout kind="ai" title="ChatGPT 답변 (이어서)">

**5. 근거:** `my_plot` 페이지의 `lineplot` 함수 — https://pyapi.juyounga.kr/api/my_plot/

두 줄을 고친 뒤 jupyter를 재시작하고 확인 코드를 다시 실행해 보세요. 1번만 고치면 오류는 사라지지만 선이 1개뿐이라 여전히 정상 실행 결과와 달라요.

</Callout>

<Core color="yellow">답변대로 고친 뒤에도 <span class="hl warn">다시 실행해 정상 실행 결과와 같은지</span>는 내가 직접 확인한다.</Core>

---
class: dense tight
---

### #05-7. 고친 뒤 다시 실행

고칠 줄만 받아 직접 고친 뒤, 확인 코드를 다시 실행해 완성 노트북의 정상 실행 결과와 같은지 본다.

<Grid cols="2" align="start">
<div class="tight">

<span class="kicker">수정 코드</span>

```python
# 바꾸기 전
ax = init(width=width, height=height, ...)
sb.lineplot(data=data, x=x, y=y,
            palette=palette, ...)
# 바꾼 후
fig, ax = init(width=width, height=height, ...)
sb.lineplot(data=data, x=x, y=y, hue=hue,
            palette=palette, ...)
```

</div>
<div class="tight">

<span class="kicker">다시 실행</span>

<Steps>
<li>모듈 파일을 저장하고 jupyter 커널을 재시작함</li>
<li>노트북을 처음부터 다시 실행해 "모듈화 기능 확인" 셀까지 실행함</li>
<li>완성 노트북에 저장된 그래프와 제목 · 축 · 선 개수 · 범례를 비교함. 같으면 끝, 다르면 새 결과를 붙여 다시 물음</li>
</Steps>

</div>
</Grid>

<Callout kind="warn" title="1번만 고치면 오류는 사라지지만 선이 하나뿐이고 범례가 없어 여전히 정상 결과와 다름" />

---

### #05-8. 올바르게 만들었을 때의 답변

교안대로 만든 함수를 보내면 ✅ 판정과 함께 같다고 본 이유를 짚어 준다.

<Callout kind="ai" title="ChatGPT 답변">

**1. 판정:** ✅ 참고 문서와 같음

**2. 결과 차이:** 같음. 제목 · 축 이름 · 토핑별 선 4개 · 범례 Topping · 검은 면에 흰 테두리 원 마커까지 정상 실행 결과와 모두 일치해요.

**3. 문제 표:** 문제 없음

- `init` 이 돌려주는 두 값을 `fig, ax` 로 나눠 받았어요. 그래서 그래프를 그릴 곳(`ax`)이 제대로 정해져요
- 받은 `hue` 를 `sb.lineplot` 에 그대로 넘겨서 토핑별로 선이 나뉘어요
- `ax` 를 직접 받지 않았을 때만 `show` 를 부르는 흐름도 참고 문서와 같아요

**4. 수정 코드:** 고칠 곳 없음

**5. 근거:** `my_plot` 페이지의 `lineplot` 함수 — https://pyapi.juyounga.kr/api/my_plot/

</Callout>

---
class: dense tight
---

### #05-9. 판정 읽는 법

판정은 세 가지이고, 판정마다 다음에 할 일이 정해져 있다.

<Grid cols="3" gap="12">
<Tile kind="soft" color="ok" title="✅ 참고 문서와 같음">처리 방법과 결과가 모두 같음<br/>다음 함수로 넘어감</Tile>
<Tile kind="soft" color="yellow" title="⚠️ 처리 방법이 다름">결과는 같고 처리 방법만 다름<br/>기능은 재현됨, 고치지 않아도 됨</Tile>
<Tile kind="soft" color="danger" title="❌ 결과가 다름">결과가 틀리거나 오류가 남<br/>표의 "어떻게 고치나"대로 고친 뒤 다시 실행함</Tile>
</Grid>

<Core color="yellow">목표는 교안 코드의 <span class="hl warn">기능을 그대로 재현</span>하는 것이다. 변수 이름이나 줄 바꿈까지 똑같을 필요는 없다.</Core>

---

## #06. 점검 예시 (2)

이번에는 결과가 표인 `my_qtcheck` 모듈의 `check_missing_values` 를 아래처럼 만들었다고 하자.

<span class="kicker">내 함수 (my_qtcheck.py)</span>

```python
def check_missing_values(data):
    na_count = data.isna().sum()
    na_ratio = (na_count / len(data.columns)) * 100
    return DataFrame({'Missing Count': na_count})
```

<Callout kind="plain" color="muted" title="컬럼별 결측치 개수와, 전체 행 중 결측 행의 비율(%)을 표로 돌려주는 함수" />

---
class: dense tight
---

### #06-1. 확인 코드 실행

완성 노트북의 "모듈화 기능 확인" 셀을 내 모듈로 실행한다.

<span class="kicker">완성 노트북의 모듈화 기능 확인 코드</span>

```python
df = DataFrame({
    'a': [1, None, 3, None],
    'b': [1, 2, 3, 4]
})
my_qtcheck.check_missing_values(df)
```

<Callout kind="tip" title="결과가 표나 글이면 그림을 글로 옮길 필요 없이 출력을 그대로 복사해 프롬프트에 붙인다" />

---
class: dense tight
---

### #06-2. 결과 맞춰 보기

내 실행 결과를 완성 노트북에 저장되어 있던 정상 실행 결과와 나란히 놓고 본다.

<Grid cols="2" align="start">
<div class="tight">

<span class="kicker">정상 실행 결과 (완성 노트북)</span>

<Output>

```text
   Missing Count  Missing Ratio (%)
a              2               50.0
b              0                0.0
```

</Output>

</div>
<div class="tight">

<span class="kicker">내 실행 결과</span>

<Output>

```text
   Missing Count
a              2
b              0
```

</Output>

</div>
</Grid>

<Core color="ai">비율 컬럼이 빠진 것은 눈으로도 보인다. <span class="hl ai">왜 빠졌는지, 고치면 값이 맞는지</span>는 AI에게 묻는다.</Core>

---
class: dense tight
---

### #06-3. AI 답변 (1/4) — 판정과 결과 차이

표를 그대로 붙이면 AI가 먼저 ❌ 판정과 함께 빠진 컬럼을 짚어 준다.

<Callout kind="ai" title="ChatGPT 답변">

**1. 판정:** ❌ 결과가 다르거나 오류가 남

**2. 결과 차이:** 정상 실행 결과에는 `Missing Ratio (%)` 컬럼이 있는데, 내 실행 결과에는 `Missing Count` 컬럼 하나만 있어요. 개수(a 2개, b 0개)는 정상 결과와 같아요.

</Callout>

---
class: dense tight
---

### #06-4. AI 답변 (2/4) — 문제 표

이어서 눈에 보이는 문제와, 표에 드러나지 않은 계산 실수까지 하나씩 표로 짚어 준다.

<Callout kind="ai" title="ChatGPT 답변 (이어서)">

**3. 문제 표**

| 번호 | 위치 | 무엇이 다른가 | 왜 문제인가 | 어떻게 고치나 |
|:--|:--|:--|:--|:--|
| 1 | `return DataFrame({...})` | `Missing Ratio (%)` 컬럼이 없어요 | 비율을 계산해 놓고 돌려주지 않아요 | 반환 딕셔너리에 비율 컬럼을 넣어요 |
| 2 | `na_count / len(data.columns)` | 열 수로 나눠요 | 비율은 전체 **행** 중 결측 행의 비율이라 값이 틀려요(a가 50.0이 아니라 100.0) | `len(data)` 로 행 수로 나눠요 |

</Callout>

---
class: dense tight
---

### #06-5. AI 답변 (3/4) — 수정 코드

답변의 뒷부분은 고칠 줄만 "바꾸기 전 → 바꾼 후"로 보여 준다.

<Callout kind="ai" title="ChatGPT 답변 (이어서)">

**4. 수정 코드:** 고칠 줄만 보여 줄게요.

```python
# 1번 — 바꾸기 전 → 바꾼 후
return DataFrame({'Missing Count': na_count})
return DataFrame({'Missing Count': na_count, 'Missing Ratio (%)': na_ratio})

# 2번 — 바꾸기 전 → 바꾼 후
na_ratio = (na_count / len(data.columns)) * 100
na_ratio = (na_count / len(data)) * 100
```

</Callout>

---
class: dense tight
---

### #06-6. AI 답변 (4/4) — 근거와 다시 실행 안내

답변의 마지막은 비교에 쓴 근거와 다시 실행하라는 안내다.

<Callout kind="ai" title="ChatGPT 답변 (이어서)">

**5. 근거:** `my_qtcheck` 페이지의 `check_missing_values` 함수 — https://pyapi.juyounga.kr/api/my_qtcheck/

두 줄을 고친 뒤 jupyter를 재시작하고 확인 코드를 다시 실행해 보세요. 1번만 고치면 비율 컬럼은 생기지만 a가 100.0으로 나와 여전히 정상 실행 결과와 달라요.

</Callout>

<Core color="yellow">답변대로 고친 뒤에도 <span class="hl warn">다시 실행해 정상 실행 결과와 같은지</span>는 내가 직접 확인한다.</Core>

---
class: dense tight
---

### #06-7. 고친 뒤 다시 실행

고칠 줄만 받아 직접 고친 뒤, 확인 코드를 다시 실행해 완성 노트북의 정상 실행 결과와 같은지 본다.

<Grid cols="2" align="start">
<div class="tight">

<span class="kicker">고친 뒤 내 실행 결과</span>

<Output>

```text
   Missing Count  Missing Ratio (%)
a              2               50.0
b              0                0.0
```

</Output>

</div>
<div class="tight">

<span class="kicker">다시 실행</span>

<Steps>
<li>모듈 파일을 저장하고 jupyter 커널을 재시작함</li>
<li>노트북을 처음부터 다시 실행해 "모듈화 기능 확인" 셀까지 실행함</li>
<li>완성 노트북에 저장된 표와 컬럼 이름 · 값을 한 칸씩 비교함. 같으면 끝, 다르면 새 결과를 붙여 다시 물음</li>
</Steps>

</div>
</Grid>

<Callout kind="warn" title="1번만 고치면 비율 컬럼은 생기지만 a가 100.0으로 나와 여전히 정상 결과와 다름" />

---
class: dense tight
---

### #06-8. 올바르게 만들었을 때의 답변

교안대로 만든 함수를 보내면 ✅ 판정과 함께 같다고 본 이유를 짚어 준다.

<Callout kind="ai" title="ChatGPT 답변">

**1. 판정:** ✅ 참고 문서와 같음

**2. 결과 차이:** 같음. 컬럼 이름(`Missing Count` · `Missing Ratio (%)`)과 a · b의 개수 · 비율 값이 정상 실행 결과와 모두 일치해요.

**3. 문제 표:** 문제 없음

- 결측치 개수를 전체 행 수 `len(data)` 로 나눠 비율을 구했어요
- 개수와 비율 두 컬럼을 `DataFrame` 으로 돌려줘요
- 원본 `data` 를 바꾸지 않아요

**4. 수정 코드:** 고칠 곳 없음

**5. 근거:** `my_qtcheck` 페이지의 `check_missing_values` 함수 — https://pyapi.juyounga.kr/api/my_qtcheck/

</Callout>

---

### #06-9. 샘플 파일로 직접 해 보기

함께 배포한 두 샘플 파일을 ChatGPT에 그대로 붙여 넣고, 앞의 답변과 비교해 본다.

실제 답변은 말투나 순서가 조금 다를 수 있다.

<Grid class="big" cols="2" gap="12">
<Tile kind="soft" color="pastel-6" title="1. 점검 예시 (1) - 프롬프트 샘플.md">

- 실수 두 군데가 있는 `lineplot`
- **❌ 판정**과 문제 2개를 기대함

</Tile>
<Tile kind="soft" color="ok" title="2. 점검 예시 (2) - 프롬프트 샘플.md">

- 실수 두 군데가 있는 `check_missing_values`
- **❌ 판정**과 문제 2개를 기대함

</Tile>
</Grid>

<Callout kind="tip" title="파일을 열고 Ctrl + A → Ctrl + C 로 전체를 복사해 새 채팅에 붙여 넣는다" />

<Core color="ai">답변을 볼 때는 <span class="hl ai">판정 → 결과 차이 → 문제 표</span> 순서로 읽는다.</Core>

---

## #07. 답변 다루기

같은 함수를 두고 이어서 물을 때는 새 창을 열지 말고 같은 대화창에서 묻는다.

<Grid cols="3" gap="12" align="start">
<div>

<Prompt title="이유가 이해되지 않을 때" class="small">

````text
2번 문제가 왜 문제인지 작은 예시 데이터로 보여 줘.
````

</Prompt>

</div>
<div>

<Prompt title="스스로 고쳐 보고 싶을 때" class="small">

````text
수정 코드는 빼고 어디를 봐야 하는지 힌트만 줘.
````

</Prompt>

</div>
<div>

<Prompt title="고친 뒤에도 결과가 다를 때" class="small">

````text
고쳤는데 결과가 아직 달라. 같은 기준으로 다시 점검해 줘.
````

</Prompt>

다음 줄에 고친 함수 전체와 새 실행 결과를 붙임

</div>
</Grid>

---

### #07-1. 주의할 점

AI로 점검할 때는 아래 네 가지를 지킨다.

- **AI 답도 틀릴 수 있음**: 고친 뒤 확인 코드를 다시 실행해, 완성 노트북의 정상 실행 결과와 같은지 내 눈으로 확인함
- **교안이 기준**: AI의 수정 코드만 믿지 말고 교안 코드를 다시 보고 같은 기능이 되게 맞춤
- **함수마다 새 채팅**: 다른 함수로 넘어가면 새 채팅을 엶. 앞 함수의 코드와 답변이 대화에 남아 있으면 AI가 두 함수를 섞어 비교하거나 이미 고친 문제를 다시 지적할 수 있음. 새 채팅에서는 지금 함수 하나만 보고 답함
- **Source code 통째 복사 금지**: 참고 문서의 코드를 그대로 붙여 넣으면 무엇이 틀렸는지 배우지 못함

<Callout kind="danger" title="넣지 말 것 — API 키 · 비밀번호 · 개인 정보가 든 데이터는 프롬프트에 붙이지 않음" />

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">데이터 분석 모듈화 · 주영아·이광호 강사</p>
