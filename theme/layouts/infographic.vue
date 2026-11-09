<script setup lang="ts">
// 인포그래픽. 제목은 위, 나머지는 연한 점 무늬 위에 가운데 정렬된 무대. Flow · Stat · Grid · 카드를 올려 놓는다.
import { useDeckOptions } from '../deck'
useDeckOptions()
</script>

<template>
  <div class="slidev-layout infographic">
    <slot />
  </div>
</template>
