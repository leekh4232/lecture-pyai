<script setup lang="ts">
// 타일. 1px 가는 선과 4px 윗선이 있는 직각 상자에 tag(작은 라벨) → title(굵은 제목) → value(큰 숫자) → 본문(슬롯) 순서로 쌓는다.
// 여러 개는 Grid 로 나란히 두고, 카드형(cards) 레이아웃에서는 그 자체가 칸이 된다.
//   kind:  plain(기본, 카드 바탕) | surface(연한 회색 바탕, 선 없음) | soft(color 를 옅게 깐 바탕) | fill(반전: 밝은 테마에서 어두운 바탕에 밝은 글자, 어두운 테마에서는 그 반대)
//   color: 윗선 · 라벨 · 숫자 색. py(기본) | ai | ok | yellow | warn | danger | muted | pastel-1 ~ 6 또는 CSS 색(#0a7fc2 · tomato …)
//   tag:   위 작은 라벨(분류 · 묶음 이름).  title: 굵은 제목.  value: 큰 숫자(글).  슬롯: 본문(작은 글, 마크다운은 여는 태그와 닫는 태그를 빈 줄로 띄운다)
import { computed } from 'vue'
const props = withDefaults(defineProps<{ kind?: 'plain' | 'surface' | 'soft' | 'fill'; color?: string; tag?: string; title?: string; value?: string | number }>(), { kind: 'plain', color: 'py' })

// 테마 색 이름 → 색 · 옅은 바탕 · 반전 바탕용 색. 없는 이름은 CSS 색으로 그대로 쓴다
const NAMED: Record<string, { c: string; soft?: string; inv?: string }> = {
  py: { c: 'var(--py)', soft: 'var(--py-soft)', inv: 'var(--py-inv)' },
  ai: { c: 'var(--ai)', soft: 'var(--ai-soft)', inv: 'var(--ai-inv)' },
  ok: { c: 'var(--ok)', soft: 'var(--ok-soft)', inv: 'var(--ok-inv)' },
  yellow: { c: 'var(--yellow)', soft: 'var(--yellow-soft)', inv: 'var(--yellow-inv)' },
  warn: { c: 'var(--warn)', inv: 'var(--warn-inv)' },
  danger: { c: 'var(--danger)', soft: 'var(--danger-soft)', inv: 'var(--danger-inv)' },
  muted: { c: 'var(--muted)', inv: 'var(--muted-inv)' },
  'pastel-1': { c: 'var(--pastel-1)' }, 'pastel-2': { c: 'var(--pastel-2)' }, 'pastel-3': { c: 'var(--pastel-3)' },
  'pastel-4': { c: 'var(--pastel-4)' }, 'pastel-5': { c: 'var(--pastel-5)' }, 'pastel-6': { c: 'var(--pastel-6)' },
}
const named = computed(() => NAMED[props.color])
const accent = computed(() => named.value?.c ?? props.color)
// 반전 타일 위의 강조색: 이름 색은 반대 테마의 색, CSS 색은 그대로
const onFill = computed(() => named.value?.inv ?? props.color)
const soft = computed(() => named.value?.soft ?? `color-mix(in srgb, ${accent.value} 12%, transparent)`)
const style = computed(() => ({
  '--c': props.kind === 'fill' ? onFill.value : accent.value,
  '--band': accent.value,
  '--soft': soft.value,
}))
</script>

<template>
  <div class="tile" :class="kind" :style="style">
    <div v-if="tag" class="tile-tag">{{ tag }}</div>
    <div v-if="title" class="tile-title">{{ title }}</div>
    <div v-if="value !== undefined && value !== ''" class="tile-value">{{ value }}</div>
    <div v-if="$slots.default" class="tile-body"><slot /></div>
  </div>
</template>

<style scoped>
.tile { display: flex; flex-direction: column; gap: 0.3rem; min-width: 0; padding: 0.75rem 0.95rem; margin: 0.4rem 0; background: var(--card); color: var(--fg); border: 1px solid var(--line); border-top: 4px solid var(--band); }
.tile.surface { background: var(--surface); border-color: var(--surface); border-top-color: var(--band); }
.tile.soft { background: var(--soft); border-color: transparent; border-top-color: var(--band); }
.tile.fill { background: var(--inv); color: var(--on-inv); border-color: var(--inv); border-top-color: var(--inv); }
.tile-tag { font-size: 0.8rem; font-weight: 700; letter-spacing: 0.02em; color: var(--c); }
.tile-title { font-size: 1.05rem; font-weight: 800; line-height: 1.3; color: var(--heading); }
.tile-value { font-size: 1.6rem; font-weight: 800; line-height: 1.15; letter-spacing: -0.02em; color: var(--c); font-variant-numeric: tabular-nums; }
.tile-body { font-size: 0.9rem; line-height: 1.45; color: var(--fg-2); }
.tile .tile-body :deep(p) { margin: 0; font-size: 0.9rem; }
.tile .tile-body :deep(ul), .tile .tile-body :deep(ol) { margin: 0; padding-left: 1.1em; }
.tile .tile-body :deep(li) { font-size: 0.9rem; line-height: 1.45; }
.tile.fill .tile-title { color: var(--on-inv); }
.tile.fill .tile-body { color: var(--on-inv-2); }
.tile.fill .tile-body :deep(strong), .tile.fill .tile-body :deep(b) { color: var(--on-inv); }
</style>
