<script setup lang="ts">
// 흐름도. steps: [{ kicker, title, text }] 를 왼쪽에서 오른쪽으로 화살표 모양(직각 꺾쇠) 머리띠와 함께 놓는다.
// text 는 문자열 하나 또는 문자열 배열(배열이면 목록으로 그린다). 마지막 단계가 강조색.
defineProps<{ steps: { kicker?: string; title: string; text?: string | string[] }[] }>()
</script>

<template>
  <div class="ed-flow" :style="{ '--n': steps.length }">
    <div v-for="(s, i) in steps" :key="i" class="ed-flow-step" :class="{ last: i === steps.length - 1 }">
      <div class="head"><span class="no">{{ String(i + 1).padStart(2, '0') }}</span><span v-if="s.kicker" class="kicker">{{ s.kicker }}</span></div>
      <div class="body">
        <div class="ttl">{{ s.title }}</div>
        <ul v-if="Array.isArray(s.text)"><li v-for="(t, j) in s.text" :key="j">{{ t }}</li></ul>
        <p v-else-if="s.text">{{ s.text }}</p>
      </div>
    </div>
  </div>
</template>
