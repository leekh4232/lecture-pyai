<script setup lang="ts">
// 간지(파트 표지). 표지와 같은 계열의 장식(빛 덩이 · 점 무늬 · 원호)을 하나씩만 두고 왼쪽에 정렬한다.
// 머리말은 덱 제목(과정 · 단원), 제목 왼쪽에 세로 그라디언트 막대, 아래에 세 색 막대. 제목 뒤 문단은 부제가 된다.
import { computed } from 'vue'
import { useNav } from '@slidev/client'
import { useDeckOptions } from '../deck'
useDeckOptions()
const { slides } = useNav()
const deckTitle = computed(() => (slides.value[0]?.meta?.slide?.frontmatter?.title ?? '') as string)
</script>

<template>
  <div class="slidev-layout section">
    <div class="section-bg" aria-hidden="true"><span class="blob" /><span class="dots" /><span class="ring" /></div>
    <div class="section-eyebrow" :class="{ 'is-empty': !deckTitle }"><span v-if="deckTitle">{{ deckTitle }}</span></div>
    <div class="section-body"><slot /></div>
    <span class="section-bar" aria-hidden="true" />
  </div>
</template>
