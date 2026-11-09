<script setup lang="ts">
// 칩. 글 사이에 끼우는 작은 직각 라벨(분류 · 검색어 · 상태). 문단 안에 <Chip>…</Chip> 으로 쓴다.
// 줄 맨 앞에 오면 Slidev 가 그 줄을 HTML 블록으로 취급해 문단(<p>)을 만들지 않으므로, 그때는 줄 전체를 <p> 로 감싼다.
//   kind:  soft(기본, 1px 색 테두리에 옅은 바탕) | outline(2px 색 테두리만) | dashed(2px 점선 테두리) | fill(연한 회색 바탕, 테두리 없음)
//   color: py(기본) | ai | ok | yellow | warn | danger | muted | ink(본문 글자색) 또는 CSS 색
import { computed } from 'vue'
const props = withDefaults(defineProps<{ kind?: 'soft' | 'outline' | 'dashed' | 'fill'; color?: string }>(), { kind: 'soft', color: 'py' })
const NAMED: Record<string, { c: string; soft?: string }> = {
  py: { c: 'var(--py)', soft: 'var(--py-soft)' }, ai: { c: 'var(--ai)', soft: 'var(--ai-soft)' }, ok: { c: 'var(--ok)', soft: 'var(--ok-soft)' },
  yellow: { c: 'var(--yellow)', soft: 'var(--yellow-soft)' }, warn: { c: 'var(--warn)' }, danger: { c: 'var(--danger)', soft: 'var(--danger-soft)' },
  muted: { c: 'var(--muted)' }, ink: { c: 'var(--heading)' },
}
const accent = computed(() => NAMED[props.color]?.c ?? props.color)
const soft = computed(() => NAMED[props.color]?.soft ?? `color-mix(in srgb, ${accent.value} 12%, transparent)`)
</script>

<template>
  <span class="chip" :class="kind" :style="{ '--c': accent, '--soft': soft }"><slot /></span>
</template>

<style scoped>
.chip { display: inline-block; vertical-align: 0.1em; margin: 0 0.15em; padding: 0.1em 0.6em; font-size: 0.8rem; font-weight: 700; line-height: 1.4; white-space: nowrap; color: var(--c); background: var(--soft); border: 1px solid var(--c); }
.chip.outline { background: transparent; border-width: 2px; }
.chip.dashed { background: transparent; border: 2px dashed var(--c); }
.chip.fill { color: var(--text); background: var(--surface-2); border-color: var(--surface-2); }
</style>
