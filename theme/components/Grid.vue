<script setup lang="ts">
// 격자 배치. cols: 열 수(2, 3) 또는 grid-template-columns 값("1fr 400px"), align: start 등, title: 위에 붙는 작은 제목.
// gap: 칸 사이 간격. 숫자 하나면 가로·세로 모두(px, 기본 32), 두 개면 "세로 가로"(예: "8 32" → 행 8px · 열 32px). 단위를 붙이면(0.5rem) 그대로 쓴다.
// 칸 안에 마크다운(코드 블록·목록)을 넣으려면 칸마다 <div> 로 감싸고 위아래에 빈 줄을 둔다. 칸 안 블록 간격은 칸에 tight · flush 클래스를 주어 줄인다(styles/lecture.css).
import { computed } from 'vue'
const props = withDefaults(defineProps<{ cols?: number | string; gap?: number | string; align?: string; title?: string }>(), { cols: 2 })
const columns = /^\d+$/.test(String(props.cols)) ? `repeat(${props.cols}, minmax(0, 1fr))` : String(props.cols)
// "8" → 8px, "8 32" → 8px 32px(행 열), "0.5rem 2rem" → 그대로
const gap = computed(() => props.gap === undefined ? undefined
  : String(props.gap).trim().split(/\s+/).map(v => /^\d+(\.\d+)?$/.test(v) ? `${v}px` : v).join(' '))
</script>

<template>
  <div class="grid-box stagger-box">
    <div v-if="title" class="chart-title">{{ title }}</div>
    <div class="grid-cells stagger" :style="{ gridTemplateColumns: columns, gap, alignItems: align }">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.grid-cells { gap: var(--grid-gap, 20px); }
/* 칸이 내용(긴 코드 줄) 때문에 넓어지지 않게: 코드 상자는 칸 안에서 가로 스크롤 */
.grid-cells > :deep(*) { min-width: 0; }
/* 칸의 첫 요소는 윗여백 없이 → 칸끼리 윗면이 맞는다. Callout(프롬프트 · 출력 상자)의 scoped 여백보다 우선하도록 .grid-box 를 앞에 붙인다 */
.grid-box .grid-cells > :deep(*) > :first-child { margin-top: 0; }
</style>
