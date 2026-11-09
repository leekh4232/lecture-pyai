<script setup lang="ts">
// 번호 목록 컴포넌트. 슬롯에 <li> 를 나열한다. Flow · Timeline 은 이 컴포넌트의 짧은 이름이다.
//   type:  list(기본) 번호 상자 세로 목록 | flow 가로 흐름도(번호 상자 + 꺾쇠 화살표, <li> 첫 <b> 가 상자 제목) | timeline 선 위의 네모 점(<li> 첫 <b> 가 시점, <li class="now"> 는 지금 여기)
//   color: py | ai | ok | pastel(항목마다 파스텔 여섯 색을 돌아가며).  <li class="ai"> 처럼 항목에 색 이름을 주면 그 항목만 바뀐다(py · ai · ok · yellow · danger · pastel-1 ~ 6).
//   vertical: timeline 을 세로(왼쪽 선)로.  center: timeline 의 점과 글을 칸 가운데에(가운데 정렬 슬라이드 · 표지).  start: 첫 번호(기본 1, list · flow)
const props = withDefaults(defineProps<{ type?: 'list' | 'flow' | 'timeline'; color?: string; vertical?: boolean; center?: boolean; start?: number | string }>(), { type: 'list', color: 'py', vertical: false, center: false })
const cls = { list: 'steps', flow: 'flow', timeline: 'timeline' }[props.type] ?? 'steps'
const style = props.start !== undefined ? { counterReset: `step ${Number(props.start) - 1}` } : undefined
</script>

<template>
  <ol :class="[cls, color, { vertical, center }]" :style="style"><slot /></ol>
</template>

<style scoped>
.py { --c: var(--py); }
.ai { --c: var(--ai); }
.ok { --c: var(--ok); }
/* pastel: 항목마다 여섯 색을 돌아가며. :where() 로 우선순위를 낮춰 아래 항목별 색(<li class="ok">)이 이기게 한다 */
.pastel :deep(:where(li:nth-child(6n+1))) { --c: var(--pastel-1); }
.pastel :deep(:where(li:nth-child(6n+2))) { --c: var(--pastel-2); }
.pastel :deep(:where(li:nth-child(6n+3))) { --c: var(--pastel-3); }
.pastel :deep(:where(li:nth-child(6n+4))) { --c: var(--pastel-4); }
.pastel :deep(:where(li:nth-child(6n+5))) { --c: var(--pastel-5); }
.pastel :deep(:where(li:nth-child(6n+6))) { --c: var(--pastel-6); }
/* 항목별 색: <li class="ai"> 처럼 준다 */
ol :deep(li.py) { --c: var(--py); }
ol :deep(li.ai) { --c: var(--ai); }
ol :deep(li.ok) { --c: var(--ok); }
ol :deep(li.yellow) { --c: var(--yellow); }
ol :deep(li.danger) { --c: var(--danger); }
ol :deep(li.pastel-1) { --c: var(--pastel-1); }
ol :deep(li.pastel-2) { --c: var(--pastel-2); }
ol :deep(li.pastel-3) { --c: var(--pastel-3); }
ol :deep(li.pastel-4) { --c: var(--pastel-4); }
ol :deep(li.pastel-5) { --c: var(--pastel-5); }
ol :deep(li.pastel-6) { --c: var(--pastel-6); }

/* list: 번호 상자(정사각) 세로 목록 */
.steps { list-style: none; padding: 0; margin: 0.4rem 0; counter-reset: step; }
.steps :deep(li) { counter-increment: step; position: relative; padding-left: 2.6rem; margin: 0.5rem 0; min-height: 2.1rem; font-size: 1rem; }
.steps :deep(li)::before { content: counter(step); position: absolute; left: 0; top: 0; width: 2.1rem; height: 2.1rem; color: #06101f; font-weight: 800; display: grid; place-items: center; font-size: 1rem; background: var(--c); }

/* flow: 가로 흐름도. 번호 상자가 나란히 놓이고 사이에 꺾쇠 화살표가 붙는다 */
.flow { --flow-gap: 2.4rem; list-style: none; margin: 0.4rem 0; padding: 0; display: flex; flex-wrap: wrap; align-items: stretch; row-gap: 1.2rem; counter-reset: step; }
.flow :deep(li) {
  counter-increment: step; position: relative; flex: 1 1 0; min-width: 0;
  display: flex; flex-direction: column; align-items: center; gap: 0.25rem; text-align: center;
  padding: 1rem 0.9rem 1.1rem; font-size: 0.95rem; line-height: 1.4;
  background: var(--card); color: var(--fg); border: 1px solid var(--line); border-top: 4px solid var(--c);
}
.flow :deep(li:not(:last-child)) { margin-right: var(--flow-gap); }
.flow :deep(li)::before { content: counter(step); width: 1.9rem; height: 1.9rem; display: grid; place-items: center; font-size: 0.9rem; font-weight: 800; color: #06101f; background: var(--c); margin-bottom: 0.3rem; }
/* 상자 사이 꺾쇠 화살표 (줄이 바뀌면 그 줄 마지막 상자에도 붙는다) */
.flow :deep(li:not(:last-child))::after { content: ''; position: absolute; top: 50%; right: calc(var(--flow-gap) * -0.5); width: 0.75rem; height: 0.75rem; border-top: 3px solid var(--c); border-right: 3px solid var(--c); transform: translate(50%, -50%) rotate(45deg); opacity: 0.8; }
.flow :deep(li > b) { display: block; font-size: 1.1rem; font-weight: 800; color: var(--heading); }
.flow :deep(li > img) { max-height: 6rem; }

/* timeline: 선 위의 네모 점. 점은 바탕색으로 속을 비우고 테두리만 칠한다 */
.timeline { --dot: 1.2rem; list-style: none; margin: 0.6rem 0; padding: 0; display: flex; }
.timeline :deep(li) { position: relative; flex: 1 1 0; min-width: 0; margin: 0; padding: calc(var(--dot) + 0.8rem) 1rem 0 0; font-size: 0.95rem; line-height: 1.45; color: var(--text); }
.timeline :deep(li)::before { content: ''; position: absolute; top: 0; left: 0; z-index: 1; box-sizing: border-box; width: var(--dot); height: var(--dot); background: var(--bg); border: 3px solid var(--c); }
/* 선: 이 점의 가운데에서 다음 점의 가운데까지. 마지막 점 뒤로는 끝까지 옅어지며 이어진다(끝이 비어 보이지 않게). center 는 대칭이라 꼬리를 그리지 않는다 */
.timeline :deep(li:not(:last-child))::after { content: ''; position: absolute; top: calc(var(--dot) / 2 - 1.5px); left: calc(var(--dot) / 2); width: 100%; height: 3px; background: var(--c); opacity: 0.4; }
.timeline:not(.center) :deep(li:last-child)::after { content: ''; position: absolute; top: calc(var(--dot) / 2 - 1.5px); left: calc(var(--dot) / 2); right: 0; height: 3px; background: linear-gradient(90deg, var(--c), transparent); opacity: 0.4; }
.timeline :deep(li.now)::before { background: var(--c); box-shadow: 0 0 0 5px color-mix(in srgb, var(--c) 28%, transparent); }
.timeline :deep(li > b:first-child) { display: block; margin-bottom: 0.2rem; font-size: 1.05rem; font-weight: 800; color: var(--c); }
.timeline :deep(li.now > b:first-child) { color: var(--heading); }
/* center: 점을 칸 가운데에, 글은 가운데 정렬. 선은 이 점의 가운데에서 다음 점의 가운데까지 → 양 끝이 대칭이 된다 */
.timeline.center :deep(li) { text-align: center; padding-right: 0.5rem; padding-left: 0.5rem; }
.timeline.center :deep(li)::before { left: calc(50% - var(--dot) / 2); }
.timeline.center :deep(li:not(:last-child))::after { left: 50%; }
.timeline.vertical { flex-direction: column; }
.timeline.vertical :deep(li) { padding: 0 0 1rem calc(var(--dot) + 0.9rem); }
.timeline.vertical :deep(li)::before { top: 0.18rem; }   /* 점을 첫 줄(시점) 글자 가운데에 맞춘다 */
.timeline.vertical :deep(li:not(:last-child))::after { top: calc(var(--dot) / 2); left: calc(var(--dot) / 2 - 1.5px); width: 3px; height: 100%; }
.timeline.vertical:not(.center) :deep(li:last-child)::after { top: calc(var(--dot) / 2); left: calc(var(--dot) / 2 - 1.5px); right: auto; width: 3px; height: calc(100% - var(--dot) / 2); background: linear-gradient(180deg, var(--c), transparent); }
</style>
