# hossam-pyai 작업 지침

ITWILL 파이썬·AI 강의의 Slidev 슬라이드 덱 저장소입니다. 루트의 `.md` 하나가 덱 하나이고, 테마는 git submodule `slidev-themes`(hossam 테마)를 경로로 씁니다.

## 강의 구성 — AI 도구 범위

- 이 덱들은 Dropbox `E:\Dropbox\[01] 아이티윌\[022] 호쌤ㅣPython Basic` 폴더의 파이썬 교안(`[LAB-NN] 단원ㅣN-제목` 폴더마다 pptx·pdf·실습코드 ipynb)과 병합됩니다.
- 교안 폴더 안 파일 구분 (파일명이 같으면 같은 내용):
  - `▶︎`가 붙은 pptx: **원본**. 교안 내용은 이 파일로 확인합니다.
  - `▶︎`가 붙은 pdf: 원본 pptx를 변환한 **강사용**.
  - `▶︎`가 없는 pptx·pdf: 주요 단어를 빈칸 처리한 **학생 배포용**. 살펴볼 필요가 없습니다.
  - `(실습코드).ipynb`: pptx·pdf에서 설명하는 내용의 실습 파일.
  - pptx·pdf는 암호가 걸려 있습니다. pptx 암호 `Wnduddk1!@#`, pdf 암호 `it123!@#`
- 수업 순서: 기존 파이썬 교안으로 단원을 먼저 진행하고, 그 단원과 이어지는 AI 사용 실습을 이 덱으로 합니다. AI 덱을 만들 때는 해당 단원 교안·실습코드를 먼저 읽고 그 내용에 맞춥니다.
- **AI 유료 버전을 전제로 합니다.** 학생은 ChatGPT 유료 플랜(Plus 이상), 에이전트 단계에서는 Claude 유료 플랜(Claude Code)을 씁니다.
- **AI 실습은 세 단계로 진행합니다.** 자세한 내용은 `AI 실습 커리큘럼.md`.
  - ① 조언 받기(LAB-02~06): 코드는 학생이 쓰고 ChatGPT는 개념·순서·해석·에러 원인만. 「ChatGPT 지침.md」
  - ② 답 받기(LAB-07~09): ChatGPT가 코드를 주고 학생이 4단 확인(실행·범위·설명·변형). 「ChatGPT 지침(답 받기).md」. 전환 개요 덱은 LAB-07-2
  - ③ 에이전트(LAB-10~13): Claude Code. 전환 개요 덱은 LAB-10-5
  - 단계가 바뀌는 LAB에는 실습 덱 앞에 LAB-01-4 같은 개요 덱을 하나 둡니다.
- **기본 문법 단원(라이브러리 활용 전)에서는 ChatGPT만 씁니다.** ChatGPT는 웹 브라우저에서 채팅으로 쓰는 형태만 뜻합니다(데스크톱 앱·Codex·API 제외). 실습·예시·프롬프트·캡처는 모두 이 형태로 만들고, Claude·Claude Code·`CLAUDE.md`·`AGENTS.md`·에이전트 실습은 넣지 않습니다.
  - 하네스·맥락 파일 예시는 ChatGPT 개인 맞춤 설정의 지침, ChatGPT 프로젝트의 지침·파일로 듭니다.
  - ChatGPT는 학생 컴퓨터에서 코드를 실행하지 못하므로, 확인 절차는 "학생이 직접 실행해 확인"으로 씁니다.
  - 예외: LAB-01 4강(「바이브 코딩을 위한 AI 사용 방법」)의 AI 유형 소개·로드맵 쪽(생성형 → 에이전틱 → 피지컬)은 앞으로 배울 단계를 보여 주는 개념 설명이라 에이전트 이름이 나올 수 있습니다.
- 에이전트(코딩 에이전트) 내용은 라이브러리 활용 단원(LAB-10 이후)부터 다룹니다.

## 폴더

| 경로 | 내용 |
|:--|:--|
| `[LAB-NN] 단원ㅣN-제목.md` | 강의 덱. 새 덱은 `slidev-deck` 스킬로 만듭니다 |
| `AI 실습 커리큘럼.md` | LAB별 마지막 단원으로 붙일 AI 실습의 원고(덱 아님). 문제·정답·버그 코드·템플릿 ⑬~㉑. 새 AI 덱은 이 파일을 원고로 만듭니다 |
| `ChatGPT 지침.md` | ① 조언 받기 단계 지침(코드 출력 금지). 학생이 ChatGPT 맞춤 지침에 붙여 넣는 원문. 덱(LAB-01 4·6)에서 인용하므로 고치면 덱도 맞춥니다 |
| `ChatGPT 지침(답 받기).md` | ② 답 받기 단계 지침. 「ChatGPT 지침.md」에서 1·2·3·9절만 다릅니다. 한쪽의 공통 절(0·4~8)을 고치면 다른 쪽도 맞춥니다 |
| `img/001`, `img/002` … | 덱별 그림. 덱 순번 폴더에 넣고 `img/002/xxx.png`처럼 상대 경로로 씁니다 |
| `slidev-themes/` | 테마 submodule. 자체 `CLAUDE.md`가 있습니다 |

## 파일 이름

- 형식: `[LAB-02] 변수・함수ㅣ5-AI에게 묻는 법(ChatGPT 학습활동).md`
- 단원 번호와 이름은 Dropbox 교안 폴더 이름을 따릅니다. 교안 폴더 이름이 바뀌면 덱 파일 이름과 표지·마지막 장의 `[LAB-NN] 단원 N` 표기도 맞춥니다.
- `ㅣ`는 한글 모음 U+3163(세로선 `|` 아님), `・`는 U+30FB 가운뎃점입니다. 새 파일도 같은 글자를 씁니다.

## 덱 작성 규칙

- 프런트매터는 아래를 기본으로 합니다.

  ```yaml
  ---
  theme: ./slidev-themes/hossam
  manuscript: true
  colorMode: dark
  fontScale: 1
  title: 파이썬 기초 · <단원 제목>
  layout: cover
  ---
  ```

- 표지와 마지막 장(`# 감사합니다`, `hideInToc: true`)에 `<p class="sub">[LAB-NN] 단원 N · ITWILL · {teacher} 강사</p>`를 둡니다.
- 쪽 제목은 `## #01. 제목`처럼 두 자리 번호를 붙입니다. 간지는 `layout: section`입니다.
- 각 쪽 아래 `<!-- -->` 주석이 강사 원고(manuscript)입니다. 내용을 바꾸면 원고도 함께 맞춥니다.
- 자리 표시는 `{teacher}`, `{name}`처럼 중괄호로 씁니다.
- `<style>` 블록과 `style=""` 속성을 쓰지 않습니다. 테마 클래스(`py` · `ai` · `ok`, `kicker`, `card`, `dense` · `tight` · `compact` 등)와 테마 컴포넌트(`Callout` · `Grid` · `Prompt` · `Steps` · `Tile` …), UnoCSS 유틸리티로 해결합니다. 필요한 기능이 테마에 없으면 테마를 고칩니다.
- 한 쪽은 16:9 한 화면을 넘지 않게 하고, 넘치면 내용을 줄이지 않고 쪽을 나눕니다.
- 컴포넌트는 최대한 다양하게 씁니다. 같은 모양이 이어지지 않도록 테마 컴포넌트(`Callout` · `Chip` · `Core` · `Flow` · `Grid` · `Output` · `Prompt` · `Stat` · `Steps` · `Tile` · `Timeline` · `YoutubeCard`)와 레이아웃(`cover` · `section` · `cards` · `infographic` · `magazine` · `default`)을 내용에 맞게 골고루 고릅니다.

## 빌드 — 강사별 두 버전

덱을 빌드할 때는 항상 아래 두 버전을 모두 만듭니다. 각 버전마다 html과 pdf를 만듭니다.

| 버전 | `{teacher}` 치환 | 산출물 | pdf 비밀번호 |
|:--|:--|:--|:--|
| hossam | `이광호` | html · pdf | `it123!@#` |
| jussam | `주영아` | html · pdf | `ju123!@#` |

- 치환은 원본 덱 md를 고치지 않고 빌드용 복사본에서 합니다. 원본에는 `{teacher}`를 그대로 둡니다.
- `{teacher}`만 치환합니다. `{name}` 같은 다른 자리 표시는 학생이 채우는 칸이므로 그대로 둡니다.
- 산출물 이름은 기존 예(`[LAB-00] AI의 이해ㅣ1-바이브 코딩을 위한 AI 사용 방법.hossam.html`)처럼 `<덱 파일 이름>.hossam.html`, `<덱 파일 이름>.jussam.pdf` 형식으로 붙입니다.
- pdf는 비밀번호를 건 뒤, 비밀번호 없이는 열리지 않고 해당 비밀번호로는 열리는지 확인합니다.
- 산출물은 이 폴더(저장소 루트)에 저장합니다. Dropbox 교안 폴더로는 사용자가 직접 옮깁니다.
- 산출물(html · pdf)은 커밋하지 않습니다(`.gitignore`에 `*.html` · `*.pdf`).

## 테마를 고칠 때

1. `slidev-themes/` 안에서 그 저장소의 `CLAUDE.md` 절차(문서 갱신 → 빌드 테스트 → push)를 따릅니다.
2. 그다음 이 저장소에서 submodule 포인터를 커밋합니다(`chore: update slidev-themes (...)`).

## 커밋 · push · pull — submodule 항상 함께

이 저장소를 커밋·push·pull할 때는 `slidev-themes` submodule도 **항상 함께** 처리합니다.

- **pull**: `git pull --recurse-submodules` 후 `git submodule update --init --recursive`. 테마를 최신으로 올릴 때는 `git submodule update --remote slidev-themes`
- **커밋 · push**: submodule에 변경이 있으면 `slidev-themes/` 안에서 먼저 커밋·push하고(테마 `CLAUDE.md` 절차), 그다음 이 저장소에서 포인터 변경까지 함께 커밋해 push합니다. push는 `git push --recurse-submodules=on-demand`
- submodule 커밋을 push하지 않은 채 이 저장소만 push하지 않습니다. 다른 컴퓨터에서 테마를 받지 못합니다.

## 커밋 메시지

- 영어 Conventional Commits(`feat:` · `fix:` · `chore:`)를 씁니다.
- 내보낸 HTML·PDF는 커밋하지 않습니다(`*.pdf`는 `.gitignore`에 있음).
- `auto commit <날짜>` 커밋은 자동 백업이 만든 것이니 손대지 않습니다.
