<script setup lang="ts">
// 카드형. 제목 아래의 칸(<div>)들을 카드 격자로 놓고 남은 높이를 나눠 채운다. cols: 열 수(기본 3). 칸에 py | ai | ok 클래스를 주면 윗선 색.
import { useDeckOptions } from '../deck'
withDefaults(defineProps<{ cols?: number | string }>(), { cols: 3 })
useDeckOptions()
</script>

<template>
  <div class="slidev-layout cards" :style="{ '--cards-cols': cols }">
    <slot />
  </div>
</template>
