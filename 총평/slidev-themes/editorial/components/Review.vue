<script setup lang="ts">
// 총평 대조판. good: 잘된 점 문장 목록(왼쪽 흰 칸 · 금색 체크), limits: [{ text, sub }] 한계 목록(오른쪽 연세블루 칸), foot: 아래 띠 한 줄.
defineProps<{ good: string[]; limits: { text: string; sub?: string }[]; goodLabel?: string; limitLabel?: string; foot?: string }>()
</script>

<template>
  <div class="ed-review">
    <section class="good">
      <h4>{{ goodLabel ?? '잘된 부분' }}</h4>
      <ol><li v-for="(g, i) in good" :key="i"><span class="mk">✓</span><span>{{ g }}</span></li></ol>
    </section>
    <section class="limit">
      <h4>{{ limitLabel ?? '한계점' }}</h4>
      <ol>
        <li v-for="(l, i) in limits" :key="i">
          <span class="mk">{{ String(i + 1).padStart(2, '0') }}</span>
          <span>{{ l.text }}<em v-if="l.sub">{{ l.sub }}</em></span>
        </li>
      </ol>
    </section>
    <div v-if="foot" class="foot">{{ foot }}</div>
  </div>
</template>
