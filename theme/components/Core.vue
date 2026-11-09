<script setup lang="ts">
// 핵심 한 줄. 슬라이드의 결론을 왼쪽 세로 막대와 함께 굵고 크게 적는다. 슬라이드의 마지막 블록으로 두면 남은 높이를 건너뛰어 맨 아래에 붙는다(styles/lecture.css).
//   color: 막대 색. py(기본) | ai | ok | yellow | warn | danger | muted 또는 CSS 색
import { computed } from 'vue'
const props = withDefaults(defineProps<{ color?: string }>(), { color: 'py' })
const NAMED = ['py', 'ai', 'ok', 'yellow', 'warn', 'danger', 'muted']
const accent = computed(() => NAMED.includes(props.color) ? `var(--${props.color})` : props.color)
</script>

<template>
  <p class="core" :style="{ '--c': accent }"><slot /></p>
</template>

<style scoped>
.core { margin: 0.6rem 0; padding: 0.15rem 0 0.15rem 0.9rem; border-left: 5px solid var(--c); font-size: 1.2rem; font-weight: 700; line-height: 1.4; color: var(--heading); }
</style>
