<script setup lang="ts">
// 가로 막대 차트. items: [{ label, value }] · max(기본 100) · unit(기본 '%') · title(차트 제목) · note(아래 출처 · 설명 한 줄)
// digits(기본 1): 값의 소수 자릿수. 마지막 막대가 강조색(highlight: 강조할 순번, 기본 마지막). 막대와 칸은 모두 직각이다.
const props = withDefaults(defineProps<{
  items: { label: string; value: number }[]
  max?: number; unit?: string; title?: string; note?: string; highlight?: number; digits?: number
}>(), { max: 100, unit: '%', digits: 1 })
const hi = (i: number) => (props.highlight ?? props.items.length - 1) === i
</script>

<template>
  <figure class="ed-bars">
    <figcaption v-if="title" class="ed-bars-title">{{ title }}</figcaption>
    <div v-for="(it, i) in items" :key="it.label" class="ed-bars-row" :class="{ hi: hi(i) }">
      <span class="lab">{{ it.label }}</span>
      <span class="track"><span class="fill" :style="{ width: `${Math.min(100, (it.value / max) * 100)}%` }" /></span>
      <span class="val">{{ it.value.toFixed(digits) }}{{ unit }}</span>
    </div>
    <div v-if="note" class="ed-bars-note">{{ note }}</div>
  </figure>
</template>
