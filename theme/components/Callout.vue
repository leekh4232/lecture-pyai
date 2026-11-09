<script setup lang="ts">
// 상자 컴포넌트. 콜아웃 · 프롬프트 · 출력 · 번호 머리띠를 한 컴포넌트가 그린다. Prompt · Output 은 이 컴포넌트의 짧은 이름이다.
//   kind:  eli5 | real | tip | warn | danger | ai | prompt | output | plain — 머리말 · 아이콘 · 색 · 바탕의 묶음(아래 PRESETS).
//          생략하면 eli5. 단, n 이나 color 만 주면 plain(아이콘 없는 민무늬 상자).
//   title: 머리말 글(묶음의 기본 머리말을 바꾼다). icon: 머리말 앞 아이콘(이모지 · 글자). "" 를 주면 아이콘을 뺀다.
//   color: 테두리 · 머리말 색. py | ai | ok | yellow | warn | danger | muted | pastel-1 ~ 6 또는 CSS 색(#0a7fc2 · tomato …). 바탕은 그 색을 옅게 깐다.
//   본문(슬롯) 없이 title 만 주면 머리말 한 줄짜리 상자가 되고 위아래 여백이 같아진다.
//   n:     왼쪽에 붙는 번호 상자(템플릿 번호 · 단계 번호). tag: 머리말 오른쪽 작은 테두리 글(패턴 이름 · 분류).
//   copy:  오른쪽 위 복사 버튼(본문 글을 클립보드로). prompt 는 기본 켬. cols: 본문을 여러 단으로 이어 흘린다(긴 프롬프트).
//   class="small": 본문 글자를 0.82rem 로(프롬프트 · 출력 포함). 상자를 Grid 칸 같은 좁은 자리에 넣을 때.
//   프롬프트 글 안의 {...}(치환할 자리)는 노랑 굵은 글로 칠한다.
import { computed, onMounted, onUpdated, ref } from 'vue'

const props = withDefaults(defineProps<{
  kind?: string; title?: string; icon?: string; color?: string
  n?: string | number; tag?: string; copy?: boolean; cols?: number | string
}>(), { cols: 1 })

// 묶음(preset): 아이콘 · 머리말 · 색 이름 · 바탕. bg 가 없으면 색을 옅게 깐다.
const PRESETS: Record<string, { icon: string; title: string; color: string; bg?: string }> = {
  eli5:   { icon: '💡', title: '풀이',          color: 'yellow' },
  real:   { icon: '🧭', title: '현업에서는',     color: 'py' },
  tip:    { icon: '✅', title: '막히면',         color: 'ok' },
  warn:   { icon: '⚠️', title: '주의',           color: 'warn',   bg: 'var(--surface)' },
  danger: { icon: '⛔', title: 'AI에게 주면 안 되는 것', color: 'danger' },
  ai:     { icon: '🤖', title: 'AI와 함께',      color: 'ai' },
  prompt: { icon: '📋', title: '프롬프트 실습',  color: 'ai' },
  output: { icon: '',   title: '출력',           color: 'ok',     bg: '#0f1830' },
  plain:  { icon: '',   title: '',               color: 'py',     bg: 'var(--card)' },
}
// 테마 색 이름 → CSS 변수. 옅은 바탕(-soft)이 있는 색은 그것을, 없으면 색을 섞어 만든다.
const NAMED: Record<string, { c: string; soft?: string }> = {
  py: { c: 'var(--py)', soft: 'var(--py-soft)' }, ai: { c: 'var(--ai)', soft: 'var(--ai-soft)' }, ok: { c: 'var(--ok)', soft: 'var(--ok-soft)' },
  yellow: { c: 'var(--yellow)', soft: 'var(--yellow-soft)' }, warn: { c: 'var(--warn)' }, danger: { c: 'var(--danger)', soft: 'var(--danger-soft)' },
  muted: { c: 'var(--muted)' },
  'pastel-1': { c: 'var(--pastel-1)' }, 'pastel-2': { c: 'var(--pastel-2)' }, 'pastel-3': { c: 'var(--pastel-3)' },
  'pastel-4': { c: 'var(--pastel-4)' }, 'pastel-5': { c: 'var(--pastel-5)' }, 'pastel-6': { c: 'var(--pastel-6)' },
}

const kind = computed(() => props.kind ?? ((props.n !== undefined || props.color) ? 'plain' : 'eli5'))
const preset = computed(() => PRESETS[kind.value] ?? PRESETS.plain)
const colorKey = computed(() => props.color ?? preset.value.color)
const accent = computed(() => NAMED[colorKey.value]?.c ?? colorKey.value)
const bg = computed(() => {
  if (!props.color && preset.value.bg) return preset.value.bg            // 묶음이 바탕을 정해 둔 경우(warn · output · plain)
  if (props.color && kind.value === 'plain') return 'var(--card)'        // 색만 준 민무늬 상자는 카드 바탕
  return NAMED[colorKey.value]?.soft ?? `color-mix(in srgb, ${accent.value} 12%, transparent)`
})
const icon = computed(() => props.icon ?? (props.n !== undefined ? '' : preset.value.icon))
const title = computed(() => props.title ?? preset.value.title)
const showCopy = computed(() => props.copy ?? kind.value === 'prompt')
const headText = computed(() => icon.value ? `${icon.value} ${title.value}` : title.value)
const hasHead = computed(() => !!(headText.value || props.tag))

const box = ref<HTMLElement | null>(null)
const done = ref(false)
async function copyText() {
  const text = box.value?.innerText ?? ''
  try { await navigator.clipboard.writeText(text) } catch { /* 클립보드 불가 환경 무시 */ }
  done.value = true; setTimeout(() => (done.value = false), 1500)
}

// 프롬프트의 치환 자리 {...} 를 span.ph 로 감싼다. Shiki 가 한 자리를 여러 span 으로 쪼갤 수 있어 줄(.line) 단위로 글자 위치를 모아 감싼다.
// 글은 그대로라 복사 결과는 같다. 이미 감싼 글은 건너뛰므로 다시 불려도 안전하다.
const PH = /\{[^{}\n]+\}/g
function markPlaceholders() {
  if (kind.value !== 'prompt' || !box.value) return
  const lines = box.value.querySelectorAll('.line')
  for (const line of lines.length ? lines : [box.value]) {
    const nodes: Text[] = []
    const walker = document.createTreeWalker(line, NodeFilter.SHOW_TEXT)
    while (walker.nextNode()) nodes.push(walker.currentNode as Text)
    const ranges = [...nodes.map(n => n.data).join('').matchAll(PH)].map(m => [m.index!, m.index! + m[0].length])
    if (!ranges.length) continue
    let pos = 0
    for (const node of nodes) {
      const start = pos
      pos += node.data.length
      if (node.parentElement?.closest('.ph')) continue
      const cuts = ranges.map(([a, b]) => [Math.max(a, start), Math.min(b, pos)]).filter(([a, b]) => a < b)
      for (const [a, b] of cuts.reverse()) {   // 뒤에서부터 잘라야 앞쪽 위치가 그대로다
        const mid = node.splitText(a - start)
        mid.splitText(b - a)
        const span = document.createElement('span')
        span.className = 'ph'
        mid.replaceWith(span)
        span.append(mid)
      }
    }
  }
}
onMounted(markPlaceholders)
onUpdated(markPlaceholders)
</script>

<template>
  <div class="callout" :class="[kind, { 'has-n': n !== undefined, 'head-only': !$slots.default }]" :style="{ '--c': accent, background: bg }">
    <div v-if="n !== undefined" class="callout-n">{{ n }}</div>
    <div class="callout-main">
      <div v-if="hasHead" class="callout-head" :class="{ 'prompt-head': kind === 'prompt', 'output-label': kind === 'output' }">
{{ headText }}<span v-if="tag" class="callout-tag">{{ tag }}</span>
      </div>
      <button v-if="showCopy" class="copy" @click="copyText">{{ done ? '복사됨 ✓' : '복사' }}</button>
      <div v-if="$slots.default" ref="box" class="callout-body" :class="{ 'prompt-body': kind === 'prompt', 'output-pre': kind === 'output' }" :style="{ '--prompt-cols': cols }"><slot /></div>
    </div>
  </div>
</template>

<style scoped>
.callout { position: relative; display: flex; align-items: center; gap: 1rem; border: 1px solid var(--line); border-left: 5px solid var(--c); padding: 0.7rem 1rem; margin: 0.6rem 0; }   /* 직각 상자 */
.callout-main { min-width: 0; flex: 1 1 auto; }
.callout-head { font-size: 1.1rem; font-weight: 800; letter-spacing: 0.02em; margin-bottom: 0.2rem; color: var(--c); }   /* 본문(1rem)보다 크게 */
.callout.head-only .callout-head { margin-bottom: 0; }   /* 제목만 있는 상자: 위아래 여백을 같게 */
.callout-body { font-size: 1rem; }
.callout-body :deep(p) { margin: 0; }
/* 상자 안 목록은 카드 안 목록과 같게: 줄 간격 1.3, 항목 사이 0.3rem (lecture.css 의 본문 목록 규칙보다 우선하도록 .callout 을 앞에 붙인다) */
.callout .callout-body :deep(li) { line-height: 1.3; }
.callout .callout-body :deep(:is(ul, ol) > li + li) { margin-top: 0.3rem; }
/* class="small": 좁은 자리용. 본문 · 프롬프트 글 · 출력 글을 작게 */
.callout.small .callout-body, .callout.small .prompt-body :deep(code), .callout.small .prompt-body :deep(.line) { font-size: 0.82rem; }
.callout.small .prompt-body :deep(.line) { vertical-align: top; }   /* inline-block 줄의 기준선 여백을 없애 줄 간격을 줄인다 */
.callout.small .output-pre, .callout.small .output-pre :deep(pre) { font-size: 0.95rem; }
/* 분류(tag): 머리말 옆, 직각 테두리만 색 */
.callout-tag { margin-left: 0.6rem; vertical-align: 0.15em; font-size: 0.8rem; font-weight: 700; color: var(--c); border: 1px solid var(--c); padding: 0.05em 0.6em; white-space: nowrap; }

/* 번호 머리띠(n): 왼쪽 번호 상자(정사각), 머리말은 제목색, 본문은 작게 */
.callout.has-n { padding: 0.4rem 1rem; margin: 0.3rem 0; border-left-width: 6px; }
.callout-n { flex: none; width: 2.6rem; height: 2.6rem; display: grid; place-items: center; font-size: 1.45rem; font-weight: 900; color: #06101f; background: var(--c); font-variant-numeric: tabular-nums; }
.callout.has-n .callout-head { font-size: 1.2rem; color: var(--heading); line-height: 1.2; margin-bottom: 0.15rem; }
.callout.has-n .callout-body { font-size: 0.9rem; color: var(--fg-2); line-height: 1.4; }
.callout.has-n .callout-body :deep(b:first-child) { color: var(--c); margin-right: 0.4em; }

/* 프롬프트(kind="prompt"): 복사 버튼, 다단 본문, 코드 펜스를 본문 글꼴로 */
.copy { position: absolute; top: 0.5rem; right: 0.6rem; font-size: 0.85rem; font-weight: 700; color: var(--muted); background: var(--surface-2); border: 1px solid var(--line); padding: 0.2em 0.65em; cursor: pointer; }
.copy:hover { color: var(--text); }
.callout.prompt { padding-bottom: 0.5rem; margin: 0.5rem 0; }
.prompt-body :deep(pre), .prompt-body :deep(.slidev-code) { background: transparent !important; border: none !important; padding: 0 !important; margin: 0 !important; font-family: inherit !important; }
.prompt-body :deep(pre) { column-count: var(--prompt-cols, 1); column-gap: 2rem; column-rule: 1px solid var(--line); }   /* cols 가 2 이상이면 다단 */
.prompt-body :deep(code), .prompt-body :deep(.line) { font-family: "Pretendard Variable", Pretendard, sans-serif !important; font-size: 1rem; line-height: 1.6; color: var(--text) !important; white-space: pre-wrap; word-break: keep-all; overflow-wrap: anywhere; }
.prompt-body :deep(span) { color: var(--text) !important; }
.prompt-body :deep(.ph) { color: var(--yellow) !important; font-weight: 800; }   /* 치환 자리 {...} */
/* 상자 바탕이 밝은 테마에서도 밝으므로 Shiki 색(어두운 바탕용)을 테마 색으로 바꿔 강조한다: 제목·함수 / 연산자·키워드 / 문자열 / 목록 기호 / 주석 */
.prompt-body :deep(span[style*="#91CBFF" i]) { color: var(--py) !important; }
.prompt-body :deep(span[style*="#FF9492" i]) { color: var(--danger) !important; }
.prompt-body :deep(span[style*="#ADDCFF" i]) { color: var(--ok) !important; }
.prompt-body :deep(span[style*="#FFB757" i]) { color: var(--warn) !important; }
.prompt-body :deep(span[style*="#BDC4CC" i]) { color: var(--muted) !important; }

/* 출력(kind="output"): 어두운 바탕, 왼쪽 위에 떠 있는 라벨, 고정폭 글꼴 */
.callout.output { border-left-width: 4px; padding: 1.5rem 1rem 0.8rem; margin: 0.4rem 0; }
.output-label { position: absolute; top: 0; left: 1rem; margin: 0; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.06em; color: var(--c); background: var(--surface-2); padding: 0.15em 0.6em; }
.output-pre, .output-pre :deep(pre) { margin: 0; padding: 0; background: none; font-family: "JetBrains Mono", Consolas, "Apple SD Gothic Neo", "Malgun Gothic", monospace; font-size: 1.1rem; line-height: 1.55; white-space: pre-wrap; color: #dbe4f3; font-variant-ligatures: none; }
</style>
