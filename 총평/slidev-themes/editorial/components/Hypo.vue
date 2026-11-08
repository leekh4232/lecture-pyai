<script setup lang="ts">
// 가설 비교표. items: [{ label, tag, h0, h1, note }] 를 한 줄씩, 왼쪽 이름 칸 · "차이가 없다" 칸 · "차이가 있다" 칸으로 나란히 놓는다.
// tag 는 이름 아래 작은 글(예: Q1), note 는 줄 아래 보충 한 줄.
defineProps<{ items: { label: string; tag?: string; h0: string; h1: string; note?: string }[]; h0Label?: string; h1Label?: string }>()
</script>

<template>
  <div class="ed-hypo">
    <div class="ed-hypo-head"><span /><span>{{ h0Label ?? '차이가 없다' }}</span><span class="yes">{{ h1Label ?? '차이가 있다' }}</span></div>
    <div v-for="(it, i) in items" :key="i" class="ed-hypo-row">
      <div class="name"><span class="no">{{ String(i + 1).padStart(2, '0') }}</span><b>{{ it.label }}</b><small v-if="it.tag">{{ it.tag }}</small></div>
      <div class="nodiff">{{ it.h0 }}</div>
      <div class="yes">{{ it.h1 }}<em v-if="it.note">{{ it.note }}</em></div>
    </div>
  </div>
</template>
