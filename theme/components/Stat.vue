<script setup lang="ts">
// 큰 숫자 타일. value: 숫자(글), unit: 단위(작게), label: 아래 한 줄 설명, color: py | ai | ok. 슬롯에 보충 설명을 넣을 수 있다. 여러 개는 Grid 로 나란히 둔다.
withDefaults(defineProps<{ value: string | number; unit?: string; label?: string; color?: string }>(), { color: 'py' })
</script>

<template>
  <div class="stat" :class="color">
    <div class="stat-value">{{ value }}<span v-if="unit" class="stat-unit">{{ unit }}</span></div>
    <div v-if="label" class="stat-label">{{ label }}</div>
    <div v-if="$slots.default" class="stat-body"><slot /></div>
  </div>
</template>

<style scoped>
.stat { display: flex; flex-direction: column; justify-content: center; text-align: center; padding: 1.2rem 1.4rem; margin: 0.4rem 0; background: var(--card); border: 1px solid var(--line); border-top: 4px solid var(--c); }   /* 직각 타일 */
.stat.py { --c: var(--py); }
.stat.ai { --c: var(--ai); }
.stat.ok { --c: var(--ok); }
.stat-value { font-size: 3rem; font-weight: 900; letter-spacing: -0.03em; line-height: 1.1; color: var(--c); font-variant-numeric: tabular-nums; }
.stat-unit { font-size: 1.2rem; font-weight: 700; margin-left: 0.2em; color: var(--muted); letter-spacing: 0; }
.stat-label { font-size: 1rem; font-weight: 600; color: var(--fg); margin-top: 0.4rem; }
.stat-body { font-size: 0.9rem; color: var(--fg-2); margin-top: 0.3rem; }
.stat-body :deep(p) { margin: 0; font-size: 0.9rem; }
</style>
