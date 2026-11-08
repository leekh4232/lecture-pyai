<script setup lang="ts">
// 표지. 왼쪽은 연세블루 색면 위에 머리말(eyebrow) · 아주 굵은 흰 제목 · 부제(제목 다음 문단),
// 오른쪽은 겹친 직각 사각형 장식과 작성자 · 날짜. author 는 첫 슬라이드 프런트매터에서 읽는다.
import { computed } from 'vue'
import { useNav } from '@slidev/client'
import { useDeckOptions } from '../deck'
defineProps<{ eyebrow?: string; date?: string }>()
useDeckOptions()
const { slides } = useNav()
const author = computed(() => (slides.value[0]?.meta?.slide?.frontmatter?.author ?? '') as string)
</script>

<template>
  <div class="slidev-layout cover">
    <div class="cover-panel">
      <div v-if="eyebrow" class="cover-eyebrow">{{ eyebrow }}</div>
      <div class="cover-title"><slot /></div>
    </div>
    <div class="cover-side">
      <div class="cover-rings" aria-hidden="true"><span /><span /><span /><span /></div>
      <div class="cover-meta">
        <span v-if="author" class="cover-author">{{ author }}</span>
        <span v-if="date" class="cover-date">{{ date }}</span>
      </div>
    </div>
  </div>
</template>
