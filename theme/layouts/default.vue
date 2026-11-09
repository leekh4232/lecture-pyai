<script setup lang="ts">
// 본문 슬라이드. Slidev 기본 본문.
import { useDeckOptions } from '../deck'
useDeckOptions()
</script>

<template>
  <div class="slidev-layout default">
    <slot />
  </div>
</template>
