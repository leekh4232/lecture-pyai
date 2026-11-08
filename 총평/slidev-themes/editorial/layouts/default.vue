<script setup lang="ts">
// 본문 슬라이드. 왼쪽 끝에 연세블루 띠, 위에 덱 제목 머리줄, 아래에 가는 바닥선이 붙는다.
import { computed } from 'vue'
import { useNav } from '@slidev/client'
import { useDeckOptions } from '../deck'
useDeckOptions()
const { slides } = useNav()
const deckTitle = computed(() => (slides.value[0]?.meta?.slide?.frontmatter?.title ?? '') as string)
</script>

<template>
  <div class="slidev-layout default">
    <div class="running-head" aria-hidden="true">{{ deckTitle }}</div>
    <slot />
    <div class="foot-rule" aria-hidden="true" />
  </div>
</template>
