---
theme: ./theme
manuscript: true
colorMode: dark
fontScale: 1
title: AI 활용 시작하기 · Markdown의 이해와 활용
layout: cover
---

# Markdown의 이해와 활용

기호 몇 개로 글에 제목, 목록, 표, 코드를 붙이는 법

<p class="sub">AI 활용 시작하기 (2) / ITWILL - 주영아·이광호 강사</p>

---
class: tight
---

## #01. 마크다운이란 — AI와 주고받는 글의 서식

<p>기호 몇 개로 서식을 표시하는 <span class="hl py">글쓰기 규칙</span>. 사람도 AI도 그대로 읽는 <b>공용 서식</b>이다.</p>

<Grid cols="2" gap="16" align="start">
<div>

<div class="kicker">이렇게 쓰면</div>

```md
# 오늘 할 일
- 데이터 결측치 확인
- 결과는 **표로** 정리
```

</div>
<div>

<div class="kicker ok">이렇게 보인다</div>

<Tile kind="soft" color="ok" title="오늘 할 일"><ul><li>데이터 결측치 확인</li><li>결과는 <b>표로</b> 정리</li></ul></Tile>

</div>
</Grid>

<Flow color="pastel">
<li><carbon:user-avatar /><b>사람이 쓴다</b><span><code>#</code> <code>-</code> <code>**</code> 기호로 서식을 표시</span></li>
<li><carbon:document /><b>.md 파일</b><span>메모장에서도 열리는 단순 텍스트</span></li>
<li><carbon:bot /><b>AI · 도구가 읽는다</b><span>ChatGPT · Claude · GitHub · 노션</span></li>
</Flow>

---
class: tight
---

### #01-1. AI 시대, 마크다운의 의미

<p>"가벼운 서식 문법"에서 <span class="hl py">사람과 AI의 공용어</span>로. AI와 글을 주고받는 자리마다 마크다운이 있다.</p>

<Timeline color="pastel">
<li><b>AI 답변</b>마크다운으로 온다</li>
<li><b>프롬프트</b>마크다운으로 쓴다</li>
<li><b>출력 형식</b>표 · 체크리스트로 지정한다</li>
</Timeline>

<span class="kicker">왜 마크다운인가</span>

<Grid cols="3" gap="12">
<Tile kind="soft" color="py" tag="LLM의 모국어" title="읽는 것도, 답하는 것도">학습 자료의 대부분이 마크다운. 제목 · 목록으로 구조를 주면 더 정확히 이해한다</Tile>
<Tile kind="soft" color="ok" tag="그냥 텍스트" title="어디서든 그대로">메모장에서도 열리는 평문이라 프로그램에 묶이지 않는다. 복사해서 바로 쓴다</Tile>
<Tile kind="soft" color="warn" tag="원본은 한 벌" title="변환은 AI에게">내용은 마크다운 한 벌로 쓰고, PPT · PDF · 노션으로 바꾸는 일은 AI에게 맡긴다</Tile>
</Grid>

<Core color="py">서식은 선택지일 뿐, 남는 자산은 <span class="hl py">구조를 가진 텍스트</span>다.</Core>

---
class: dense
---

### #01-2. 프롬프트를 마크다운으로 쓰면

<Grid cols="4">
<div class="card py"><h3><carbon:split-screen /> 지시 · 자료 분리</h3><p>코드 상자가 자료의 경계</p></div>
<div class="card py"><h3><carbon:checkbox-checked /> 할 일 누락 없음</h3><p>목록 한 줄 = 할 일 하나</p></div>
<div class="card ok"><h3><carbon:table /> 결과 모양 지정</h3><p>표 머리글대로 채워 온다</p></div>
<div class="card ok"><h3><carbon:renew /> 다시 쓰기 쉬움</h3><p><code>.md</code> 저장, 자료만 교체</p></div>
</Grid>

<Grid cols="2">
<div>

<div class="kicker">평문 프롬프트</div>

```text
아래 데이터에서 결측치를 찾아서
표로 정리하고 원인도 추측해 줘
이름 나이 철수 비어있음 영희 21
```

- 어디까지가 지시고 어디부터가 자료인지 흐리다
- 할 일이 한 문장에 섞여 하나를 빠뜨리기 쉽다

</div>
<div>

<div class="kicker">마크다운 프롬프트</div>

````md
## 할 일
- 결측치를 찾아 표로 정리
- 원인을 한 줄씩 추측

## 데이터
```csv
이름,나이
철수,
영희,21
```

## 출력 형식
| 열 | 결측 수 | 원인 |
````

</div>
</Grid>

---

### #01-3. 기호로 하는 서식

- `#` 을 붙이면 제목, `**` 로 감싸면 굵은 글씨가 된다
- 파일은 그냥 텍스트라서 메모장에서도 열리고 미리보기를 켜면 서식이 입혀진다

<Callout kind="eli5">
문자 메시지에 ㅋㅋ나 ^^를 붙이면 말투가 달라 보이는 것과 비슷하다. 글자 몇 개를 덧붙이는 것만으로 "여기는 제목", "여기는 강조"라고 표시한다.
</Callout>

<Callout kind="real">
GitHub의 README, 주피터 노트북의 설명 셀, 노션도 모두 마크다운으로 쓴다. 한 번 익혀 두면 여기저기서 그대로 쓸 수 있다.
</Callout>

<Callout kind="warn">
마크다운이 그려지지 않는 곳(문자, 카톡, 일반 메일)에 AI 답을 붙이면 <code>**</code>, <code>#</code> 같은 기호가 그대로 보인다. 그럴 때는 "서식 없이 평문으로 써 줘"라고 따로 요청한다.
</Callout>

---

## #02. VS Code 준비 — Visual Studio Code 설치하기

- **Visual Studio Code**는 Microsoft가 만들어 무료로 배포하는 IDE(코딩 작업 통합 프로그램)다
- 여러 프로그래밍 언어를 지원해서 IDE 중에서 가장 인기가 높다
- 익스텐션(확장팩)을 설치해 기능을 늘릴 수 있다

<div class="fill-img"><img src="./img/002/vscode-overview.png" alt="Visual Studio Code에서 코드를 편집하는 화면" /></div>

---

### #02-1. VS Code 내려받기

<Steps>
<li><a href="https://code.visualstudio.com">https://code.visualstudio.com</a> 에 접속한다</li>
<li>화면의 <b>Download</b> 버튼을 눌러 설치 프로그램을 내려받는다</li>
<li>내려받은 프로그램을 실행해 설치를 진행한다 (특별한 설정은 없다)</li>
</Steps>

<div class="fill-img"><img src="./img/002/vscode-download.png" alt="VS Code 홈페이지의 Download 버튼. 누르면 페이지가 이동하고 2~3초 뒤 다운로드가 시작된다" /></div>

---

### #02-2. VS Code 설치 과정

<Grid cols="3">
<div>

<div class="kicker">1. 사용권 계약 동의 → 다음</div>

<img src="./img/002/vscode-install-step1.png" alt="사용권 계약에서 동의합니다를 고르고 다음 누르기" class="max-h-[190px]" />

</div>
<div>

<div class="kicker">2. 설치 위치 확인 → 다음</div>

<img src="./img/002/vscode-install-step2.png" alt="설치 위치를 그대로 두고 다음 누르기" class="max-h-[190px]" />

</div>
<div>

<div class="kicker">3. 시작 메뉴 폴더 → 다음</div>

<img src="./img/002/vscode-install-step3.png" alt="시작 메뉴 폴더를 그대로 두고 다음 누르기" class="max-h-[190px]" />

</div>
<div>

<div class="kicker">4. 추가 작업 모두 체크 → 다음</div>

<img src="./img/002/vscode-install-step4.png" alt="바탕 화면 바로가기, Code로 열기, PATH에 추가 항목을 모두 체크하고 다음 누르기" class="max-h-[190px]" />

</div>
<div>

<div class="kicker">5. 설치 누르기</div>

<img src="./img/002/vscode-install-step5.png" alt="설치 준비 완료 화면에서 설치 누르기" class="max-h-[190px]" />

</div>
<div>

<div class="kicker">6. 설치 진행 중</div>

<img src="./img/002/vscode-install-step6.png" alt="설치 진행 막대가 차오르는 화면" class="max-h-[190px]" />

</div>
</Grid>

---

### #02-3. 설치 종료 및 실행

설치 프로그램에서 **종료**를 누르면 Visual Studio Code가 바로 실행된다.

<div class="fill-img"><div class="fill-in">
<figure><div class="pic"><img src="./img/002/vscode-install-finish.png" alt="설치 마법사 완료 화면에서 Visual Studio Code 실행에 체크하고 종료 누르기" /></div></figure>
<figure><div class="pic"><img src="./img/002/vscode-first-run.png" alt="처음 실행된 VS Code의 Welcome 화면" /></div></figure>
</div></div>

---

### #02-4. 익스텐션 설치 — 한국어

익스텐션은 VS Code의 기능을 늘리기 위해 설치하는 작은 프로그램이다.

<div class="fill-img"><div class="fill-in">
<div class="fill-text">

<Steps>
<li>왼쪽의 익스텐션 아이콘(네모 네 개)을 누른다</li>
<li>검색창에 <b>Korean</b>을 입력한다</li>
<li>Microsoft가 만든 <b>Korean Language Pack</b>을 설치한다</li>
<li>오른쪽 아래에 뜨는 <b>Change Language and Restart</b>를 눌러 다시 실행한다</li>
</Steps>

</div>
<figure class="grow-1.5"><div class="pic"><img src="./img/002/ext-korean.png" alt="익스텐션 창에서 Korean을 검색해 한국어 팩을 설치하고 재시작 버튼 누르기" /></div></figure>
</div></div>

---

### #02-5. 환경 설정 — 글자 크기

기본 글자 크기가 조금 작으니 **16**으로 바꾼다. 코딩하면서 내 눈에 맞게 다시 조절해도 된다.

<div class="fill-img"><div class="fill-in">
<div class="fill-text">

<Steps>
<li>왼쪽 아래 톱니바퀴를 누른다</li>
<li><b>설정</b>을 고른다</li>
<li><b>Editor: Font Size</b> 칸에 <code>16</code>을 입력한다</li>
</Steps>

</div>
<figure class="grow-1.5"><div class="pic"><img src="./img/002/setting-font-size.png" alt="톱니바퀴 → 설정 → Editor: Font Size에 16 입력" /></div></figure>
</div></div>

---

### #02-6. 환경 설정 — 아이콘 테마 설치

- 검색해 보면 여러 아이콘 테마가 있다. 가장 많이 쓰는 것은 **Material Icon Theme**다
- 설치가 끝나면 화면 위쪽에 테마를 고르는 목록이 뜬다

<div class="fill-img"><div class="fill-in">
<div class="fill-text">

<Steps>
<li>익스텐션 아이콘을 누른다</li>
<li>검색창에 <b>Icon</b>을 입력한다</li>
<li><b>Material Icon Theme</b>을 설치한다</li>
</Steps>

</div>
<figure class="grow-1.5"><div class="pic"><img src="./img/002/ext-material-icon.png" alt="익스텐션 창에서 Icon을 검색해 Material Icon Theme 설치하기" /></div></figure>
</div></div>

---

### #02-7. 환경 설정 — 아이콘 테마 고르기

이미 설치된 아이콘 테마 중에서 고를 때는 아래 순서로 연다.

<div class="fill-img"><div class="fill-in">
<figure><div class="kicker">톱니바퀴 → 테마 → 파일 아이콘 테마</div><div class="pic"><img src="./img/002/icon-theme-menu.png" alt="톱니바퀴 메뉴에서 테마, 파일 아이콘 테마 순서로 열기" /></div></figure>
<figure><div class="kicker">목록에서 Material Icon Theme 선택</div><div class="pic"><img src="./img/002/icon-theme-select.png" alt="파일 아이콘 테마 목록에서 Material Icon Theme 고르기" /></div></figure>
</div></div>

---

### #02-8. 환경 설정 — 아이콘 테마 확인

기본 상태에서는 폴더와 파일을 구분하기 어렵지만, 아이콘 테마를 적용하면 **파일 종류가 한눈에 보인다**.

<div class="fill-img"><div class="fill-in">
<figure><div class="kicker">설치 전</div><div class="pic"><img src="./img/002/icon-theme-before.png" alt="아이콘 테마 적용 전 탐색기. 폴더와 파일이 글자만으로 구분된다" /></div></figure>
<figure><div class="kicker">설치 후</div><div class="pic"><img src="./img/002/icon-theme-after.png" alt="아이콘 테마 적용 후 탐색기. 폴더와 파일마다 종류별 아이콘이 붙는다" /></div></figure>
</div></div>

---

### #02-9. 환경 설정 — 색상 테마

데이터 분석 코드는 **밝은 테마**에서 더 잘 읽히므로 바꾸는 것을 추천한다. 취향에 따라 어두운 테마를 써도 된다.

<div class="fill-img"><div class="fill-in">
<figure><div class="kicker">톱니바퀴 → 테마 → 색 테마</div><div class="pic"><img src="./img/002/color-theme-menu.png" alt="톱니바퀴 메뉴에서 테마, 색 테마 순서로 열기" /></div></figure>
<figure><div class="kicker">밝게(Visual Studio) 선택</div><div class="pic"><img src="./img/002/color-theme-select.png" alt="색 테마 목록에서 밝게(Visual Studio) 고르기" /></div></figure>
</div></div>

---

### #02-10. VS Code 삭제하기 — 설정 앱 열기

윈도우의 **설정** 앱을 실행하고 **앱**으로 들어간다.

<div class="fill-img"><img src="./img/002/uninstall-settings-app.png" alt="윈도우 설정 앱에서 앱 메뉴 선택" /></div>

---

### #02-11. VS Code 삭제하기 — 프로그램 제거

**앱 및 기능** 목록에서 **Microsoft Visual Studio Code**를 찾아 **제거**를 누른다.

<div class="fill-img"><img src="./img/002/uninstall-apps.png" alt="앱 및 기능 목록에서 Microsoft Visual Studio Code 제거" /></div>

---

### #02-12. VS Code 삭제하기 — 설정 폴더 지우기

<div class="fill-img"><div class="fill-in">
<div class="fill-text">

<Steps>
<li>사용자 홈 폴더(<code>C:\사용자\계정명</code> 또는 <code>C:\Users\계정명</code>)를 연다</li>
<li><code>.vscode</code> 폴더를 삭제한다</li>
</Steps>

<Callout kind="warn">
프로그램만 지우면 설정과 익스텐션이 이 폴더에 남는다. 다시 설치했을 때 예전 문제가 그대로 따라오지 않게 <b>반드시</b> 함께 지운다.
</Callout>

</div>
<figure class="grow-1.5"><div class="pic"><img src="./img/002/uninstall-vscode-folder.png" alt="사용자 홈 폴더에서 .vscode 폴더 삭제" /></div></figure>
</div></div>

---

### #02-13. 마크다운을 위한 익스텐션 설치

| 확장 | 만든 사람 | 하는 일 |
|:--|:--|:--|
| Markdown All in One | Yu Zhang | 문법 강조, 단축키, 목차 자동 생성 |
| Markdown Preview Github Styling | Matt Bierner | 미리보기를 GitHub 화면처럼 보여 줌 |
| Ipynb PDF converter | leekh | 마크다운 파일을 pdf 문서로 변환 |

VS Code 왼쪽의 확장 아이콘(네모 네 개)을 누르고 이름으로 검색해 설치한다.

<Callout kind="tip" title="미리보기 여는 법">

- 옆 창에 띄우기: `Ctrl + K` 를 누른 뒤 `V` (Mac은 `Cmd + K` → `V`)
- 같은 창에서 바꿔 보기: `Ctrl + Shift + V` (Mac은 `Cmd + Shift + V`)

</Callout>

---

## #03. 마크다운 뷰어 설정 — 크롬으로 md 파일 보기

VS Code를 열지 않아도 `.md` 파일을 **더블클릭만으로** 서식이 입혀진 화면으로 볼 수 있게 만든다.

<Steps>
<li>크롬 웹 스토어에서 <b>Markdown Reader</b> 익스텐션을 설치한다</li>
<li>Markdown Reader가 내 컴퓨터의 파일을 읽을 수 있게 허용한다</li>
<li><code>.md</code> 파일의 기본 연결 프로그램을 <b>Chrome</b>으로 바꾼다</li>
<li>취향에 맞게 색상 테마를 고른다</li>
</Steps>

<Callout kind="warn">
이 설정은 반드시 <b>크롬(Chrome) 웹 브라우저</b>에서 진행한다. 엣지 등 다른 브라우저에서는 화면과 메뉴가 다르다.
</Callout>

---

### #03-1. 크롬 웹 스토어 접속

구글에서 "**크롬 웹 스토어**"를 검색해 들어간다. (반드시 크롬 웹 브라우저 사용)

<div class="fill-img"><img src="./img/002/md-reader-webstore.png" alt="구글에서 크롬 웹 스토어를 검색해 접속하는 화면" /></div>

---

### #03-2. 설치할 익스텐션 검색

크롬 웹 스토어에서 "**Markdown Reader**"를 검색한다.

<div class="fill-img"><img src="./img/002/md-reader-search.png" alt="크롬 웹 스토어 검색창에 Markdown Reader 입력" /></div>

---

### #03-3. 익스텐션 설치

오른쪽 위의 "**Chrome에 추가**" 버튼을 누른다.

<div class="fill-img"><img src="./img/002/md-reader-install.png" alt="Markdown Reader 페이지에서 Chrome에 추가 버튼 누르기" /></div>

---

### #03-4. 익스텐션 관리 페이지로 이동

설치가 끝나면 확장 프로그램 아이콘 → **Markdown Reader** 옆 점 세 개 → **확장 프로그램 관리**를 누른다.

<div class="fill-img"><img src="./img/002/md-reader-manage.png" alt="크롬 확장 프로그램 목록에서 Markdown Reader 메뉴를 열고 확장 프로그램 관리 누르기" /></div>

---

### #03-5. 컴퓨터 파일 접근 허용

**파일 URL에 대한 액세스 허용** 옵션을 켠다. 이걸 켜야 내 컴퓨터의 md 파일을 열 수 있다.

<div class="fill-img"><img src="./img/002/md-reader-file-access.png" alt="Markdown Reader 세부정보에서 파일 URL에 대한 액세스 허용 켜기" /></div>

---

### #03-6. md 파일의 연결 프로그램 바꾸기

아무 md 파일이나 마우스 오른쪽 버튼으로 누르고 **연결 프로그램 → 다른 앱 선택**을 누른다.

<div class="fill-img"><img src="./img/002/md-open-with.png" alt="파일 탐색기에서 md 파일을 우클릭해 연결 프로그램, 다른 앱 선택 누르기" /></div>

---

### #03-7. 항상 크롬으로 열기

목록에서 **Google Chrome**을 고르고 **항상**을 눌러 늘 크롬으로 열리게 한다. 목록에 크롬이 없으면 **PC에서 앱 선택**을 눌러 `C:\Program Files\Google\Chrome\Application\chrome.exe` 를 고른다.

<div class="fill-img"><img src="./img/002/md-open-with-chrome.png" alt="연결 프로그램 선택 창에서 Google Chrome을 고르고 항상 누르기. 크롬이 없으면 PC에서 앱 선택으로 chrome.exe 지정" /></div>

---

### #03-8. md 파일을 크롬으로 열어 보기

`*.md` 파일을 더블클릭했을 때 크롬에서 서식이 입혀진 화면으로 열리는지 확인한다.

<div class="fill-img"><img src="./img/002/md-open-in-chrome.png" alt="md 파일이 크롬에서 목차와 서식이 적용된 문서로 열린 화면" /></div>

---

### #03-9. 색상 테마 설정 — 옵션 열기

md 파일을 연 상태에서 확장 프로그램 아이콘 → **Markdown Reader**를 눌러 옵션 화면을 연다.

<div class="fill-img"><img src="./img/002/md-reader-options-menu.png" alt="md 파일을 연 크롬에서 확장 프로그램 아이콘을 누르고 Markdown Reader 선택" /></div>

---

### #03-10. 색상 테마 설정 — 테마 고르기

글자 크기, 밝은/어두운 테마, 코드 블록 테마를 **각자 취향에 맞춰** 설정한다.

<div class="fill-img"><img src="./img/002/md-reader-theme.png" alt="Markdown Reader 옵션 화면에서 테마와 글자 크기 고르기" /></div>

---

## #04. 마크다운 작성 규칙

기호 몇 개만 익히면 제목, 목록, 표, 코드, 수식까지 쓸 수 있다.

<Grid cols="3">
<Card sm k="문서 뼈대" t="3.1 ~ 3.7">

- 새 마크다운 파일 만들기
- 제목
- 본문과 줄바꿈
- 목록

</Card>
<Card sm k="글자와 연결" t="3.8 ~ 3.12">

- 글자 강조
- 링크 · 이미지
- 표
- 인용문과 구분선

</Card>
<Card sm k="특수 블록" t="3.13 ~ 3.20">

- 체크박스
- 코드 블록
- 수식
- 기호를 글자 그대로 쓰기

</Card>
</Grid>

<Callout kind="tip">
각 규칙은 왼쪽에 쓰는 법, 오른쪽에 미리보기로 보여 준다. VS Code에서 <code>Ctrl + K</code> → <code>V</code> 로 미리보기를 띄워 두고 따라 써 본다.
</Callout>

---

### #04-1. 새 마크다운 파일 만들기

<Steps>
<li><code>파일 → 새 텍스트 파일</code>을 고른다. 단축키는 <code>Ctrl + N</code> (Mac은 <code>Cmd + N</code>)</li>
<li>저장(<code>Ctrl + S</code>)할 때 파일 이름 끝을 <code>.md</code> 로 정한다. 예: <code>note.md</code></li>
<li>오른쪽 아래 상태 표시줄에 <b>Markdown</b>이 보이면 준비 끝</li>
</Steps>

<Callout kind="warn">
확장자를 <code>.txt</code> 로 저장하면 미리보기도 문법 강조도 동작하지 않는다.
</Callout>

---

### #04-2. 제목 — `#` 의 개수가 크기

````md
# 문서 제목 (가장 큼)
## 큰 단원
### 작은 단원
#### 더 작은 단원
##### 거의 본문 크기
###### 가장 작음
````

- `#` 다음에 **한 칸 띄우고** 제목을 쓴다. `#제목` 처럼 붙이면 제목이 되지 않는다
- 1개부터 6개까지 쓸 수 있다. 개수가 적을수록 크다
- `#` 하나짜리 제목은 보통 문서 맨 위에 한 번만 쓴다

<Callout kind="eli5">
책의 목차를 떠올리면 된다. <code>#</code> 은 책 제목, <code>##</code> 는 장, <code>###</code> 은 절이다.
</Callout>

---

### #04-3. 본문과 줄바꿈

<Grid cols="2">
<div>

```md
그냥 쓰면 본문이 된다.

엔터를 한 번 치면
줄이 바뀌지 않고 이어 붙는다.

빈 줄을 하나 두면
새 문단이 된다.
```

</div>
<div>

<div class="kicker">미리보기</div>

그냥 쓰면 본문이 된다.

엔터를 한 번 치면
줄이 바뀌지 않고 이어 붙는다.

빈 줄을 하나 두면
새 문단이 된다.

<Callout kind="tip" title="문단은 그대로, 줄만 바꾸고 싶으면">
줄 끝에 스페이스를 두 칸 넣거나 <code>&lt;br&gt;</code> 를 쓴다.
</Callout>

</div>
</Grid>

---
class: tight
---

### #04-4. 순서 있는 목록 · 순서 없는 목록

<Grid cols="2" gap="32" align="start">
<div>

<div class="kicker">순서 있는 목록 — 숫자와 점</div>

<Grid cols="2" gap="28" align="start">
<div>

```md
1. 재료 준비
1. 물 끓이기
1. 면 넣기
1. 3분 기다리기
```

</div>
<div>

<div class="kicker">미리보기</div>

1. 재료 준비
2. 물 끓이기
3. 면 넣기
4. 3분 기다리기

</div>
</Grid>

- `1.` 다음에 **한 칸 띄운다**
- 번호를 모두 `1.` 로 써도 화면에는 1, 2, 3, 4로 나온다. 연속 번호로 써도 되고, VS Code가 번호를 자동 완성한다
- 중간에 항목을 끼워 넣어도 번호를 고칠 필요가 없다

</div>
<div>

<div class="kicker ai">순서 없는 목록 — 기호</div>

<Grid cols="2" gap="28" align="start">
<div>

```md
- 사과
- 배
- 오이
- 당근
```

</div>
<div>

<div class="kicker">미리보기</div>

- 사과
- 배
- 오이
- 당근

</div>
</Grid>

- `-` 다음에 **한 칸 띄운다**
- `*` 를 써도 결과가 같다
- 순서가 상관없는 것(준비물 · 재료 · 후보)을 적을 때 쓴다

</div>
</Grid>

---
class: tight
---

### #04-5. 목록 안에 목록 넣기 · 섞어 쓰기

<Grid cols="2" gap="32" align="start">
<div>

<div class="kicker">안쪽으로 밀어 넣기</div>

<Grid cols="2" gap="28" align="start">
<div>

```md
1. 아침
    1. 세수
    1. 밥 먹기
1. 점심
    1. 수업
    1. 산책
```

</div>
<div>

<div class="kicker">미리보기</div>

1. 아침
    1. 세수
    1. 밥 먹기
1. 점심
    1. 수업
    1. 산책

</div>
</Grid>

- 하위 항목은 `Tab` 키(스페이스 4칸)로 **안쪽으로 밀어** 쓴다
- 위아래 항목과 들여쓰기 칸 수를 맞춘다

</div>
<div>

<div class="kicker ai">두 목록을 섞어 쓰기</div>

<Grid cols="2" gap="28" align="start">
<div>

```md
1. 준비물
    * 노트북
    * 충전기
1. 실습 순서
    1. 파일 만들기
    1. 저장하기
```

</div>
<div>

<div class="kicker">미리보기</div>

1. 준비물
    * 노트북
    * 충전기
1. 실습 순서
    1. 파일 만들기
    1. 저장하기

</div>
</Grid>

<Callout kind="eli5">
큰 순서는 번호로, 그 안의 준비물처럼 순서가 상관없는 것은 점으로 적는다. 장보기 목록을 쓸 때와 같다.
</Callout>

</div>
</Grid>

---

### #04-6. 글자 강조

<Grid cols="2">
<div>

```md
**굵게**

*기울임*

***굵게 + 기울임***

~~취소선~~

`인라인 코드`
```

- 기호로 글자를 **양쪽에서 감싼다**
- 인라인 코드는 문장 안에서 코드나 파일 이름을 보여 줄 때 쓴다

</div>
<div>

<div class="kicker">미리보기</div>

**굵게**

*기울임*

***굵게 + 기울임***

~~취소선~~

`인라인 코드`

<Callout kind="warn">
각 줄 사이에 빈 줄이 없으면 다섯 개가 한 줄로 이어 붙는다. 3.3 본문과 줄바꿈의 규칙이 여기에도 그대로 적용된다.
</Callout>

</div>
</Grid>

---

### #04-7. 링크와 이미지

<Grid cols="2" align="start">
<div>

<div class="kicker">링크 <code>[글자](주소)</code></div>

```md
[구글](https://www.google.com "검색 엔진") 에서 검색한다.

[구글][g] 에서 검색한다.

[g]: https://www.google.com
```

- `[화면에 보일 글자](주소)`. 큰따옴표 안 글자는 마우스를 올렸을 때 뜨는 설명
- 두 번째 방법은 주소를 글 아래쪽에 따로 모아 둔다. 같은 주소를 여러 번 쓸 때 편하다

<div class="kicker">미리보기</div>

[구글](https://www.google.com "검색 엔진") 에서 검색한다.

</div>
<div>

<div class="kicker ai">이미지 <code>![설명](경로)</code></div>

```md
![고양이 사진](images/cat.png)
```

- 링크 앞에 **느낌표 `!`** 하나만 붙이면 이미지가 된다
- 대괄호 안 글자는 그림이 안 열릴 때 대신 보이는 설명이다
- 주소 자리에 인터넷 주소 대신 내 컴퓨터의 파일 경로를 써도 된다. md 파일이 있는 폴더를 기준으로 적는다

</div>
</Grid>

---

### #04-8. 표

<Grid cols="2">
<div>

```md
| 이름 | 과목 | 점수 |
|:-----|:----:|-----:|
| 철수 | 수학 |   90 |
| 영희 | 영어 |  100 |
```

</div>
<div>

<div class="kicker">미리보기</div>

| 이름 | 과목 | 점수 |
|:-----|:----:|-----:|
| 철수 | 수학 |   90 |
| 영희 | 영어 |  100 |

</div>
</Grid>

- `|` 로 칸을 나누고 둘째 줄의 `---` 로 제목 줄과 내용을 가른다
- 콜론 `:` 위치로 정렬을 정한다. `:---` 왼쪽, `:---:` 가운데, `---:` 오른쪽

<Callout kind="tip">
칸 너비를 꼭 맞추지 않아도 표는 잘 나온다. 
</Callout>

---

### #04-9. 인용문과 구분선

<Grid cols="2">
<div>

```md
> 아는 것이 힘이다.
>
> 기능은 인용문이지만, 실제로는 강조 박스를 만들 때 사용한다.
```

<div class="kicker">미리보기</div>

> 아는 것이 힘이다.
>
> 기능은 인용문이지만, 실제로는 강조 박스를 만들 때 사용한다.

</div>
<div>

```md
***
___
```

- 셋 중 아무거나 한 줄에 쓰면 가로 구분선이 된다. 셋째 방법은 하이픈 세 개(`---`)다

<div class="kicker">미리보기</div>

***

<Callout kind="warn">

- <code>---</code> 바로 위 줄에 글자가 붙어 있으면 그 글자가 제목으로 바뀐다. 
- 구분선 위아래는 빈 줄로 띄운다.

</Callout>

</div>
</Grid>

---

### #04-10. 체크박스

<Grid cols="2">
<div>

```md
- [x] 확장 설치하기
- [x] md 파일 만들기
- [ ] 표 만들어 보기
- [ ] 수식 써 보기
```

- `- [ ]` 는 빈 칸, `- [x]` 는 체크된 칸
- 대괄호 안에 **스페이스 한 칸**이 있어야 빈 칸으로 인식된다

</div>
<div>

<div class="kicker">미리보기</div>

- [x] 확장 설치하기
- [x] md 파일 만들기
- [ ] 표 만들어 보기
- [ ] 수식 써 보기

<Callout kind="real">
할 일 목록이나 과제 제출 전 점검표를 이렇게 만든다. 
</Callout>

</div>
</Grid>

---

### #04-11. 코드 블록

역따옴표(`` ` ``) 세 개로 코드를 위아래에서 감싸고 여는 쪽 뒤에 언어 이름을 쓴다. 역따옴표는 키보드 `1` 왼쪽, `~` 와 같은 키에 있다.

<Grid cols="2">
<div>

<div class="kicker">Python</div>

````md
```python
for i in range(3):
    print("Hello", i)
```
````

<div class="kicker">미리보기</div>

```python
for i in range(3):
    print("Hello", i)
```

</div>
<div>

<div class="kicker">SQL</div>

````md
```sql
SELECT name, score
FROM students
WHERE score >= 90;
```
````

<div class="kicker">미리보기</div>

```sql
SELECT name, score
FROM students
WHERE score >= 90;
```

</div>
</Grid>

---

### #04-12. 언어 이름 적는 법

<Grid cols="2" align="start">
<div>

| 언어 | 적는 이름 |
|:--|:--|
| Python | `python` 또는 `py` |
| JavaScript | `javascript` 또는 `js` |
| HTML · CSS | `html` · `css` |
| SQL | `sql` |
| 터미널 명령 | `bash` 또는 `shell` |
| 데이터 파일 | `json` · `xml` · `yaml` |
| 마크다운 자체 | `markdown` 또는 `md` |

</div>
<div>

<Callout kind="eli5">

- 언어 이름은 "이건 파이썬이야"라고 알려 주는 이름표다. 
- 이름표를 보고 예약어, 문자열, 숫자에 각각 다른 색을 입힌다. 
- 이름을 빼면 코드는 나오지만 전부 한 가지 색이다.

</Callout>

</div>
</Grid>

---

### #04-13. 수식 — 문장 안에 넣기

달러 기호 `$` 한 개로 감싸면 문장 속에 수식이 들어간다.

```md
이차방정식의 해는 $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ 이다.
```

<div class="kicker">미리보기</div>

이차방정식의 해는 $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ 이다.

<Callout kind="eli5">

- 수식은 LaTeX(레이텍)이라는 수식 전용 규칙으로 쓴다. 
- <code>\frac{위}{아래}</code> 는 분수, <code>\sqrt{}</code> 는 루트처럼 명령어 하나가 기호 하나다.

</Callout>

---

### #04-14. 수식 — 따로 한 줄에 크게

- `$$` 두 개로 위아래를 감싸면 수식이 가운데에 크게 놓인다. 
- `&` 는 줄을 맞출 기준점, `\\` 는 줄바꿈이다.

```md
$$
\begin{aligned}
E &= mc^2 \\
F &= ma
\end{aligned}
$$
```

<div class="kicker">미리보기</div>

$$
\begin{aligned}
E &= mc^2 \\
F &= ma
\end{aligned}
$$

---

### #04-15. 자주 쓰는 수학 기호

<Grid cols="2" align="start">
<div>

| 보이는 모양 | 쓰는 법 | 뜻 |
|:--:|:--|:--|
| $x^2$ | `x^2` | 제곱 (위첨자) |
| $x_2$ | `x_2` | 아래첨자 |
| $\bar{x}$ | `\bar{x}` | 평균 |
| $\sqrt{x}$ | `\sqrt{x}` | 제곱근 |
| $\frac{a}{b}$ | `\frac{a}{b}` | 분수 |
| $\sum$ | `\sum` | 모두 더하기 |
| $\log_{2}$ | `\log_{2}` | 로그 (밑이 2) |
| $\leq$ · $\geq$ | `\leq` · `\geq` | 작거나 같음 · 크거나 같음 |
| $\varepsilon$ | `\varepsilon` | 아주 작은 양수 (오차를 나타낼 때 자주 씀) |

</div>
<div>

<Callout kind="warn">

- 첨자가 두 글자 이상이면 중괄호로 묶는다. 
- `x^10` 은 $x^10$ 으로 보이고 `x^{10}` 이라고 써야 $x^{10}$ 이 된다.

</Callout>

</div>
</Grid>

---

### #04-16. 통계에서 쓰는 기호

| 기호 | 쓰는 법 | 뜻 |
|:--:|:--|:--|
| $\Omega$ | `\Omega` | 모집단 (조사하고 싶은 전체) |
| $\mu$ | `\mu` | 모평균 |
| $\sigma^2$ | `\sigma^2` | 모분산 |
| $\sigma$ | `\sigma` | 모표준편차 |
| $\bar{X}$ | `\bar{X}` | 표본평균 |
| $s^2$ | `s^2` | 표본분산 |
| $s$ | `s` | 표본표준편차 |
| $n$ | `n` | 표본 크기 (뽑은 데이터 개수) |

---

### #04-17. 기호를 글자 그대로 쓰고 싶을 때

`*` 이나 `#` 를 서식이 아니라 글자로 보여 주려면 앞에 **역슬래시 `\`** 를 붙인다.

<Grid cols="2">
<div>

```md
\*별표\* 가 그대로 보인다.

\# 이건 제목이 아니다.

가격은 \$5 이다.
```

</div>
<div>

<div class="kicker">미리보기</div>

\*별표\* 가 그대로 보인다.

\# 이건 제목이 아니다.

가격은 \$5 이다.

</div>
</Grid>

<Callout kind="tip">
한글 키보드에서는 역슬래시가 <code>₩</code>(원화 기호)로 보이기도 한다. 같은 키다.
</Callout>

---

## #05. 자주 틀리는 것

| 증상 | 원인 | 고치는 법 |
|:--|:--|:--|
| `#제목` 이 그냥 글자로 나옴 | `#` 뒤에 공백 없음 | `# 제목` |
| 목록이 안 만들어짐 | `-`, `1.` 뒤에 공백 없음 | `- 항목` |
| 두 줄이 한 줄로 붙음 | 엔터를 한 번만 침 | 빈 줄 하나 넣기 |
| 하위 목록이 안 들어감 | 들여쓰기 칸 수가 다름 | 위 항목과 칸 수 맞추기 |
| 코드 블록이 끝나지 않음 | 닫는 역따옴표 세 개 빠짐 | 코드 끝에 ```` ``` ```` 추가 |

---

## #06. 실습하기 — 자기소개 페이지

<Grid cols="2">
<div>

<Steps color="ok">
<li><code>me.md</code> 파일을 만든다</li>
<li><code>#</code> 으로 이름을 제목으로 쓴다</li>
<li>좋아하는 것 세 가지를 목록으로 쓴다</li>
<li>이번 주 할 일을 체크박스로 쓴다</li>
<li>미리보기를 열어 오른쪽과 비슷하면 성공</li>
</Steps>

</div>
<div>

```md
# 홍길동

## 좋아하는 것

- 산책
- **음악 감상**
- 떡볶이

## 이번 주 할 일

- [x] VS Code 설치
- [ ] 마크다운 정리
```

</div>
</Grid>

---

## #07. 학습정리 — 한 장 요약

| 하고 싶은 것 | 쓰는 법 |
|:--|:--|
| 제목 | `# ` ~ `###### ` |
| 새 문단 | 빈 줄 하나 |
| 목록 | `1. ` · `- ` · `* ` |
| 강조 | `**굵게**` · `*기울임*` · `~~취소~~` |
| 링크 · 이미지 | `[글자](주소)` · `![설명](주소)` |
| 표 | `\| 칸 \| 칸 \|` + `\|---\|---\|` |
| 체크박스 | `- [ ] ` · `- [x] ` |
| 코드 | `` `한 줄` `` · ```` ```언어 ```` |
| 수식 | `$문장 속$` · `$$따로 한 줄$$` |

<span class="muted">기호 뒤 공백 한 칸과 빈 줄 하나, 이 두 가지만 지켜도 대부분 제대로 나온다.</span>
