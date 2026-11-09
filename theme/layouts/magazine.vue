<script setup lang="ts">
// 웹진형. 왼쪽은 큰 제목 + 리드문(제목 다음 문단) + 본문, 오른쪽은 ::right:: 슬롯(그림 · 콜아웃 · 카드)이 연한 바탕 칸에 놓인다. ::right:: 가 없으면 한 단.
import { useSlots } from 'vue'
import { useDeckOptions } from '../deck'
useDeckOptions()
const slots = useSlots()
</script>

<template>
  <div class="slidev-layout magazine" :class="{ 'no-side': !slots.right }">
    <div class="mag-main stagger"><slot /></div>
    <aside v-if="slots.right" class="mag-side stagger"><slot name="right" /></aside>
  </div>
</template>
