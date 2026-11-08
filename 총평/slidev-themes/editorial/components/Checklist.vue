<script setup lang="ts">
// 점검 목록. rows: [{ value, unit, label, text }] 를 가로줄로 쌓는다. 왼쪽 금색 세로선 옆 큰 값, 가운데 이름, 오른쪽 설명.
defineProps<{ rows: { value: string; unit?: string; label: string; text: string }[] }>()
</script>

<template>
  <div class="ed-check">
    <div v-for="(r, i) in rows" :key="i" class="row">
      <div class="val"><b>{{ r.value }}</b><span v-if="r.unit">{{ r.unit }}</span></div>
      <div class="lab">{{ r.label }}</div>
      <p>{{ r.text }}</p>
    </div>
  </div>
</template>
