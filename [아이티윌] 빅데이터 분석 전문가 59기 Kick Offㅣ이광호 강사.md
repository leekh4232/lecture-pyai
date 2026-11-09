---
theme: ./slidev-themes/jussam
title: 빅데이터 분석 전문가 59기 · Kick-Off
manuscript: true
colorMode: dark
exportDark: false
fontScale: 1.2
vivid: true
layout: cover
eyebrow: 아이티윌
footer: 이광호 강사
---

# 빅데이터 분석 전문가 59기<br>**Kick-Off**

---
layout: magazine
---

# 반갑습니다

이 광 호<br>leekh4232@gmail.com

- 연세대학교 공학석사
- 아이티윌 - 데이터분석/머신러닝 강의
- 메가스터디IT아카데미 - 프론트엔드/백엔드/데이터 분석 강의
- KT, U+ 프로젝트 다수 참여
- 모바일 게임 개발

---
eyebrow: communication
---

# **Communication**

<Grid cols="2" gap="80">
<Figure h="300" caption="단톡방">
<img src="./img/kickoff/qr-group-chat.png" alt="단톡방 입장 QR 코드" />
</Figure>
<Figure h="300" caption="1:1 톡방">
<img src="./img/kickoff/qr-direct-chat.png" alt="1:1 톡방 입장 QR 코드" />
</Figure>
</Grid>

---
layout: section
part: 1
eyebrow: Chapter 1
---

# Background

수업 참여에 필요한 기본 배경 지식

---
part: 1
eyebrow: Chapter 1 · Background
class: dense [&_li]:!ml-0
---

# 데이터 분석 부트캠프 **단계별 커리큘럼**

<Grid cols="4" gap="14">
<Stat sm n="920" unit="H" label="총 교육 시간" />
<Stat sm n="115" unit="일" label="교육 기간" />
<Stat sm n="30" unit="%" label="프로젝트 비중" />
<Stat sm n="10" unit="개" label="핵심 교과목" />
</Grid>

<Grid cols="4" gap="14" align="stretch">
<Card sm acc k="step 1" t="기초역량">

- SQL 데이터 다루기
- Python 프로그래밍 기초
- Python 웹 데이터 수집

</Card>
<Card sm acc k="step 2" t="기초 통계">

- NumPy·Pandas
- Python 데이터 시각화
- 탐색적 데이터 분석
- 회귀분석

</Card>
<Card sm acc k="step 3" t="머신러닝 모델링">

- Python 머신러닝
- 딥러닝<br/>(TensorFlow · Keras)

</Card>
<Card sm acc k="step 4" t="실전 프로젝트">

- 기획 · 분석 문제 정의
- 데이터 탐색 · 모델링
- 평가 · 보고서 · 발표 · 포트폴리오

</Card>
</Grid>

---
part: 1
eyebrow: Chapter 1 · Background
eras:
  ticks: ["1950's", "1960's", "1970's", "1980's", "1990's", "2000's", "2010's", "2020's"]
  height: 320
  step: 56
  layers:
    - title: Artificial<br>Intelligence
      from: 0
      items:
        - { t: Rule-Based Systems, d: 규칙 기반 시스템 · 사람이 정한 if-then 규칙으로 판단 }
        - { t: Fuzzy Logic, d: 퍼지 논리 · 참과 거짓 사이의 애매한 정도를 다룸 }
        - { t: Evolutionary Algorithms, d: 진화 알고리즘 · 생물의 진화를 흉내 내 좋은 답을 찾음 }
        - { t: Natural Language Processing, d: 자연어 처리 · 사람의 말과 글을 이해하고 만들어 냄 }
        - { t: Computer Vision, d: 컴퓨터 비전 · 이미지와 영상을 인식 }
    - title: Machine<br>Learning
      from: 3
      items:
        - { t: Supervised Learning, d: 지도학습 · 정답이 있는 데이터로 학습 }
        - { t: Unsupervised Learning, d: 비지도학습 · 정답 없이 패턴과 군집을 찾음 }
        - { t: Reinforcement Learning, d: 강화학습 · 보상을 받으며 행동을 익힘 }
    - title: Deep<br>Learning
      from: 6
      items:
        - { t: 'ANN, CNN, RNN', d: 기본 신경망 · 이미지 · 순서 데이터 }
        - { t: 'GAN, GNN', d: 생성 모델 · 그래프 데이터 }
---

# 데이터 분석을 위한 **머신러닝 분류 방식** (1)

<Eras v-bind="$frontmatter.eras" />

---
part: 1
eyebrow: Chapter 1 · Background
class: '[&_.card_.k]:!text-[14.3px] [&_.card_.t]:!text-[24.7px] [&_.card_.d]:!text-[18.2px]'
---

# 데이터 분석을 위한 **머신러닝 분류 방식** (2)

AI, ML, DL, XAI

<Grid cols="4" gap="18" align="stretch">
<Card lg acc k="Artificial Intelligence" t="AI">인간의 지적 능력을 모방하는 기술</Card>
<Card lg acc k="Machine Learning" t="ML">대규모 데이터를 분석하고 학습하여 패턴을 예측하는 기술</Card>
<Card lg acc k="Deep Learning" t="DL">인공신경망을 기반으로 복잡한 데이터에서 고차원 패턴을 자동으로 학습하는 기술</Card>
<Card lg acc k="Explainable AI" t="XAI">AI의 의사결정 과정을 사람이 이해할 수 있도록 설명해주는 기술 또는 접근 방법</Card>
</Grid>

---
part: 1
eyebrow: Chapter 1 · Background
class: 'dense tight [&_.card-sm]:!p-[12px] [&_.card_.d]:!text-center [&_.item]:!py-[8px] [&_.numlist_.dd]:!mt-0'
---

# 사회과학 연구와 **데이터 분석**

<Grid cols="1fr 1.1fr" gap="36" align="start">
<div>

### 사회과학

- 인간의 사회적 행동과 상호작용,<br>그리고 이를 이루는 집단과 제도를<br>과학적으로 탐구하는 분야
- 자연과학이 자연현상의 법칙을 탐구한다면,<br>사회과학은 인간과 사회 현상을<br>설명・예측하고 개선하는 것을 목표로 함
- 사회 현상을 이해·설명·예측하기 위해<br>질문 → 데이터 → 증거 기반 답변 을 도출하는<br>체계적 탐구

</div>
<div>

### 사회과학 분야의 연구 예시

일반적으로 말하는 데이터 분석 과정을 "연구"라고 함

<Card sm acc>기후 변화 인식이 에너지 소비 행동에 미치는 영향:<br>설문조사와 스마트미터 데이터를 활용한 혼합 방법 연구</Card>

<NumList>
<Item title="질문">기후 위기에 대한 인식 수준이 가정의 에너지 절약 행동에 영향을 주는가?</Item>
<Item title="데이터">전국 설문조사 응답, 스마트미터 전력 사용 기록, 기상 자료</Item>
<Item title="증거 기반 답변">통계 분석 + 머신러닝으로 인식·행동 간 관계를 설명하고<br/>정책 시뮬레이션 제공</Item>
</NumList>

</div>
</Grid>

---
part: 1
eyebrow: Chapter 1 · Background
class: 'tight [&_.kicker.acc]:!mt-[8px] [&_.card]:!pb-[12px]'
---

# 사회 문제 해결을 위한 **머신러닝과 딥러닝**

사회 문제 해결을 위한 인공지능 → 주로 머신러닝을 의미 (Lundberg et al., 2024)

<Kicker lead><b>데이터 분석, 예측 모델 구축, 패턴 인식</b><br>사회 문제 해결(사회 과학)에 인공지능을 활용하기 위해서는 특히 머신러닝에 대한 이해가 필요 (Rahal et al., 2024)</Kicker>

<Grid cols="1fr 1.25fr" gap="20" align="stretch">
<Card k="deep learning" t="DeepLearning의 등장">

- 데이터가 점차 복잡해짐 (텍스트, 이미지 등)
- 다층 신경망(deep neural networks)을 사용하여 복잡한 패턴을 학습하는 기술
- 이미지, 음성, 자연어와 같은 비정형 데이터를 다루는 데 강점

</Card>
<Card acc k="conclusion" t="가장 좋은 것은 보완하여 사용하는 것">

- 얼마전까지 딥러닝이 무조건 성능이 좋은 것으로 여겨짐
- 최근 개발된 머신러닝 알고리즘들은 예측에 있어 상대적으로 더 좋은 성능을 보여줌
- 특히 표 형식의 데이터에서 압도적인 성능 차이를 보여줌 (Grinsztajn, Oyallon, & Varoquaux, 2022; Shwartz-Ziv & Armon, 2022)

</Card>
</Grid>

---
part: 1
eyebrow: Chapter 1 · Background
class: dense
---

# **데이터 분석 프로세스** (1)

본 훈련 과정을 통해 이 프로세스를 단계별로 습득하는 것을 목표로 함

<Grid cols="2" gap="20" align="stretch">
<Card acc k="01" t="데이터 수집・가공">

**수집** · DATABASE(SQL) · API, Crawling(Python)

- **점검·정제** · 데이터 구조 점검 · 품질 문제 해결
- **정리** · 정리/병합 · 재구조화(Re-shaping) · 정보 조합
- **변수 가공** · 파생변수 생성 · 범주형 변수 인코딩
- **변환** · 수학적 변환(로그변환, 스케일링)

</Card>
<Card acc k="02" t="탐색적 데이터 분석">

**목표** · 데이터 구조 이해 및 시각적 요약

- **기초** · 기초 통계량 · 데이터 분포 형태 관찰
- **변량별** · 단변량 · 이변량 · 기본 다변량 분석(pairplot, heatmap)
- **관계** · 변수 간 상관관계 분석 · 시계열 패턴 분석
- **검정** · 통계적 검정(t-test, ANOVA, 카이제곱 등)

</Card>
</Grid>

---
part: 1
eyebrow: Chapter 1 · Background
class: dense
---

# **데이터 분석 프로세스** (2)

본 훈련 과정을 통해 이 프로세스를 단계별로 습득하는 것을 목표로 함

<Grid cols="3" gap="20" align="stretch">
<Card lg acc k="03" t="모델링">

- 통계적 분석 모델(회귀, 분류)
- 머신러닝 분석 모델(Linear, D-Tree, Random Forest, XGBoost, LightGBM,CatBoost 등)

</Card>
<Card lg acc k="04" t="성능평가">

- 설명력, 에러율 점검
- 일반화 성능 확인

</Card>
<Card lg acc k="05" t="해석 및 결론">

- 결과 해석 및 결론 도출
- 활용 방안
- 한계점
- 제언

</Card>
</Grid>

---
part: 1
eyebrow: Chapter 1 · Background
nodemap:
  w: 1600
  h: 580
  nodes:
    - { label: '연구주제 선정', x: 0, y: 0, w: 190, h: 44, kind: term }
    - { label: '데이터 수집', x: 0, y: 84, w: 190, h: 56, kind: io }
    - { label: '탐색적 데이터 분석', x: 0, y: 170, w: 190, h: 56, kind: box }
    - { label: '요인선정<br>(상관분석/분산분석)', x: 0, y: 256, w: 190, h: 60, kind: box }
    - { label: '분위수 분할', x: 260, y: 350, w: 190, h: 56, kind: box }
    - { label: '군집분석<br>(KMeans/DBScan)', x: 260, y: 430, w: 190, h: 56, kind: box }
    - { label: '차원축소<br>(PCA)', x: 260, y: 510, w: 190, h: 56, kind: box }
    - { label: 'K-Fold / GridSearchCV', x: 520, y: 256, w: 210, h: 60, kind: box }
    - { label: 'LinearRegression', x: 800, y: 0, w: 190, h: 56, kind: box }
    - { label: 'KNN Regression', x: 800, y: 72, w: 190, h: 56, kind: box }
    - { label: 'Decision Tree<br>Regression', x: 800, y: 144, w: 190, h: 56, kind: box }
    - { label: 'SGD Regression', x: 800, y: 216, w: 190, h: 56, kind: box }
    - { label: 'Random Forest', x: 800, y: 288, w: 190, h: 56, kind: box }
    - { label: 'Support<br>Vector Machine', x: 800, y: 360, w: 190, h: 56, kind: box }
    - { label: 'LightGBM', x: 800, y: 432, w: 190, h: 56, kind: box }
    - { label: 'CatBoost', x: 800, y: 504, w: 190, h: 56, kind: box }
    - { label: '성능평가<br>(R², MSE, RMSE /<br>Over·Under Fitting)', x: 1060, y: 250, w: 200, h: 72, kind: box }
    - { label: 'feature importance<br>SHAP', x: 1060, y: 400, w: 200, h: 56, kind: box }
    - { label: '결과해석', x: 1060, y: 510, w: 200, h: 56, kind: io }
    - { label: 'Voting', x: 1340, y: 60, w: 150, h: 56, kind: box }
    - { label: 'Bagging', x: 1340, y: 150, w: 150, h: 56, kind: box }
    - { label: 'Boosting', x: 1340, y: 240, w: 150, h: 56, kind: box }
  edges:
    - 'M95,44 L95,84'
    - 'M95,140 L95,170'
    - 'M95,226 L95,256'
    - 'M190,286 L520,286'
    - 'M150,316 L150,378 L260,378'
    - 'M95,316 L95,458 L260,458'
    - 'M40,316 L40,538 L260,538'
    - 'M450,378 L585,378 L585,316'
    - 'M450,458 L625,458 L625,316'
    - 'M450,538 L665,538 L665,316'
    - 'M730,286 L765,286 L765,28 L800,28'
    - 'M990,28 L1025,28 L1025,286 L1060,286'
    - 'M730,286 L765,286 L765,100 L800,100'
    - 'M990,100 L1025,100 L1025,286 L1060,286'
    - 'M730,286 L765,286 L765,172 L800,172'
    - 'M990,172 L1025,172 L1025,286 L1060,286'
    - 'M730,286 L765,286 L765,244 L800,244'
    - 'M990,244 L1025,244 L1025,286 L1060,286'
    - 'M730,286 L765,286 L765,316 L800,316'
    - 'M990,316 L1025,316 L1025,286 L1060,286'
    - 'M730,286 L765,286 L765,388 L800,388'
    - 'M990,388 L1025,388 L1025,286 L1060,286'
    - 'M730,286 L765,286 L765,460 L800,460'
    - 'M990,460 L1025,460 L1025,286 L1060,286'
    - 'M730,286 L765,286 L765,532 L800,532'
    - 'M990,532 L1025,532 L1025,286 L1060,286'
    - 'M1260,270 L1300,270 L1300,88 L1340,88'
    - 'M1490,88 L1540,88 L1540,302 L1260,302'
    - 'M1260,270 L1300,270 L1300,178 L1340,178'
    - 'M1490,178 L1540,178 L1540,302 L1260,302'
    - 'M1260,270 L1300,270 L1300,268 L1340,268'
    - 'M1490,268 L1540,268 L1540,302 L1260,302'
    - 'M1160,322 L1160,400'
    - 'M1160,456 L1160,510'
  height: 340
class: '[&_.nm-node]:!text-[11px]'
---

# **데이터 분석 프로세스** (상세)

<NodeMap v-bind="$frontmatter.nodemap" />

---
layout: section
part: 2
eyebrow: Chapter 2
---

# Curriculum Roadmap

커리큘럼 로드맵

---
part: 2
eyebrow: Chapter 2 · Curriculum Roadmap
roadmap:
  stages: ['데이터 수집・가공', '탐색적 데이터 분석', '모델링', '성능평가', '해석 및 결론']
  bands:
    - { label: 데이터 분석가, from: 0, to: 2.6 }
    - { label: 데이터 사이언티스트, from: 2.45, to: 4 }
  rows:
    - { label: SQL/Database, from: 0.08, to: 1.08 }
    - { label: Python / Library, from: 0.08, to: 4.92 }
    - { label: 기초 수학 및 통계, from: 1, to: 3.18 }
    - { label: EDA / Tablueau, from: 1, to: 2.07 }
    - { label: 머신러닝, from: 2.07, to: 4.92 }
class: '[&_.rm-track]:!h-[32px] [&_.roadmap]:!gap-[6px] [&_.rm-band]:!h-[38px]'
---

# 데이터 분석 프로세스에 따른 **교과목 학습 계획**

<Roadmap v-bind="$frontmatter.roadmap" />

---
part: 2
eyebrow: Chapter 2 · Curriculum Roadmap
---

# 교과목별 **연관 자격증**

| 교과목 | 관련 자격증 |
|:--|:--|
| SQL / Database | SQLD |
| 기초 수학 / 통계 / 머신러닝 | ADSP, ADP, 빅데이터 분석 기사, 사회조사분석사 |

---
part: 2
eyebrow: Chapter 2 · Curriculum Roadmap
---

# 데이터 분석 **수업 예시**

이런걸 합니다…

<Grid cols="1fr 1.1fr" gap="28" align="start">
<div class="tight">
<Figure h="70">
<img src="./img/kickoff/class-code.png" alt="ols 로 dist ~ speed 회귀 모델을 만들고 summary 를 출력하는 코드 세 줄" />
</Figure>
<Figure h="232">
<img src="./img/kickoff/class-ols-summary.png" alt="OLS Regression Results 출력. R-squared, F-statistic, 계수와 p-value 에 번호를 붙여 강조" />
</Figure>
</div>
<div class="tight">
<Figure h="95">
<img src="./img/kickoff/class-result-table.png" alt="코로나19 이후 매출액 차이를 종속변수로 한 회귀분석 결과표" />
</Figure>
<Figure h="207">
<img src="./img/kickoff/class-regression-plot.png" alt="키와 몸무게의 산점도와 회귀식 wgt = 80 + 2(hgt)" />
</Figure>
</div>
</Grid>

---
part: 2
eyebrow: Chapter 2 · Curriculum Roadmap
---

# 데이터 분석 **수업 예시**

그래서 이렇게 설명을 합니다.

<Grid cols="1.5fr 1fr" gap="32" align="center">
<Figure h="322">
<img src="./img/kickoff/regression-types.png" alt="단순회귀, 다중회귀, 로지스틱 회귀, 다항회귀, 곡선회귀, 비선형회귀의 모형과 설명 표" />
</Figure>
<Figure h="265">
<img src="./img/kickoff/reaction.jpg" alt="이게 뭔 소리 하는 거에요 라는 자막이 달린 방송 화면" />
</Figure>
</Grid>

---
part: 2
eyebrow: Chapter 2 · Curriculum Roadmap
class: 'tight [&_.chip]:!text-[12px] [&_.chip]:!py-0 [&_.card-sm]:!p-[14px] [&_.card_.k]:!mb-[6px] [&_.card_.t]:!text-[16px] [&_.card_.t]:!mb-[6px] [&_.card_.d_p+p]:!mt-[6px] [&_.card_.d]:!leading-[1.9]'
---

# 데이터 분석 **수업 예시**

이만큼을 공부해야 합니다. 머신러닝은 크게 세 갈래이고, 갈래마다 문제 유형과 대표 알고리즘이 있습니다.

<Branch src="Machine Learning · 머신러닝" :n="3">
<Card sm acc k="supervised learning" t="지도학습 · 정답이 있는 데이터">

<p><b>회귀</b> 숫자 예측 · <Chip>Linear</Chip><Chip>Ridge</Chip><Chip>Lasso</Chip><Chip>KNN</Chip><Chip>Decision Tree</Chip><Chip>SVM</Chip><Chip>SGD</Chip></p>
<p><b>분류</b> 범주 예측 · <Chip>Logistic</Chip><Chip>KNN</Chip><Chip>Decision Tree</Chip><Chip>SVM</Chip><Chip>SGD</Chip><Chip>Naive Bayes</Chip></p>

</Card>
<Card sm acc k="unsupervised learning" t="비지도학습 · 정답 없이 구조 발견">

<p><b>군집</b> 비슷한 것끼리 묶기 · <Chip color="ok">K-Means</Chip><Chip color="ok">DBSCAN</Chip><Chip color="ok">Hierarchical</Chip></p>
<p><b>차원 축소</b> 변수 줄이기 · <Chip color="ok">PCA</Chip><Chip color="ok">t-SNE</Chip></p>

</Card>
<Card sm acc k="ensemble methods" t="앙상블 · 여러 모델을 합치기">

<p><b>Voting</b> 투표로 결정 · <Chip color="ai">Hard</Chip><Chip color="ai">Soft</Chip></p>
<p><b>Bagging</b> 병렬로 학습해 평균 · <Chip color="ai">Random Forest</Chip></p>
<p><b>Boosting</b> 앞 모델의 오차를 보완 · <Chip color="ai">XGBoost</Chip><Chip color="ai">LightGBM</Chip><Chip color="ai">CatBoost</Chip></p>

</Card>
</Branch>

---
part: 2
eyebrow: Chapter 2 · Curriculum Roadmap
---

# **최종 수업 목표**

<Figure>
<img src="./img/kickoff/final-goal.png" alt="RISS 학위논문 정보. A study on machine learning algorithms for a house market analysis: a case of Seoul" />
</Figure>

---
layout: section
part: 3
eyebrow: Chapter 3
---

# 당부의 말

---
layout: section
part: 1
eyebrow: 당부의 말 · 01 / 07
---

# 마음 단단히 먹으세요. 어렵습니다.

---
layout: section
part: 2
eyebrow: 당부의 말 · 02 / 07
---

# 전공 수준의 이론(수학적 접근)을<br>다루지는 않습니다.

---
layout: section
part: 3
eyebrow: 당부의 말 · 03 / 07
---

# 컴퓨터 기초 활용 능력은<br>각자의 몫 입니다.

---
layout: section
part: 4
eyebrow: 당부의 말 · 04 / 07
---

# GPT등의 AI를 올바르게 사용하세요.

---
layout: section
part: 1
eyebrow: 당부의 말 · 05 / 07
---

# 총 2~3번의 프로젝트가 있습니다.<br>(중간, 파이널)

---
layout: section
part: 2
eyebrow: 당부의 말 · 06 / 07
---

# 훈련기간이 깁니다.<br>1주 이상 슬럼프가 올 수 도 있어요.

---
layout: section
part: 3
eyebrow: 당부의 말 · 07 / 07
---

# 지각, 결석, 조퇴로 인한<br>훈련 공백은 본인의 몫입니다.
