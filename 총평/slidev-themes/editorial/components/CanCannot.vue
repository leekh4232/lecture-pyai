<script setup lang="ts">
// 해석 범위 판. can: 말할 수 있는 문장(왼쪽 연세블루 윗선), cannot: 말할 수 없는 문장(오른쪽 빨간 윗선 · 취소선 없음), notes: 아래 근거 목록.
defineProps<{ can: string[]; cannot: string[]; notes?: string[]; canLabel?: string; cannotLabel?: string }>()
</script>

<template>
  <div class="ed-cancannot">
    <div class="col can"><h4><span>○</span>{{ canLabel ?? '말할 수 있는 것' }}</h4><p v-for="(c, i) in can" :key="i">{{ c }}</p></div>
    <div class="col cannot"><h4><span>✕</span>{{ cannotLabel ?? '말할 수 없는 것' }}</h4><p v-for="(c, i) in cannot" :key="i">{{ c }}</p></div>
    <ul v-if="notes?.length" class="notes"><li v-for="(n, i) in notes" :key="i">{{ n }}</li></ul>
  </div>
</template>
