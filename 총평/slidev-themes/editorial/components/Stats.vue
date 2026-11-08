<script setup lang="ts">
// 큰 숫자 칸 격자. items: [{ value, unit, label, text }] 를 cols 열(기본 items 수)로 놓는다. 첫 칸이 진한 바탕.
defineProps<{ items: { value: string; unit?: string; label: string; text?: string }[]; cols?: number }>()
</script>

<template>
  <div class="ed-stats" :style="{ '--cols': cols ?? items.length }">
    <div v-for="(it, i) in items" :key="i" class="ed-stat">
      <div class="lab">{{ it.label }}</div>
      <div class="num">{{ it.value }}<span v-if="it.unit" class="unit">{{ it.unit }}</span></div>
      <p v-if="it.text">{{ it.text }}</p>
    </div>
  </div>
</template>
