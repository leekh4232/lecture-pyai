<script setup lang="ts">
// 블록형. ## 제목과 그 아래 리드문은 위에 두고, ### 제목마다 그 아래 내용을 한 칸으로 묶어 cols 열(기본 2)에 위에서 아래로 채운다.
// 원고는 평범한 마크다운(### 소제목 + 본문) 그대로 쓰면 된다. 묶기는 화면에 그린 뒤 DOM 에서 한다.
import { computed, onMounted, ref } from 'vue'
import { useNav } from '@slidev/client'
import { useDeckOptions } from '../deck'
withDefaults(defineProps<{ cols?: number | string }>(), { cols: 2 })
useDeckOptions()
const { slides } = useNav()
const deckTitle = computed(() => (slides.value[0]?.meta?.slide?.frontmatter?.title ?? '') as string)
const root = ref<HTMLElement | null>(null)
onMounted(() => {
  const el = root.value
  if (!el || el.querySelector(':scope > .blocks-grid')) return
  const kids = Array.from(el.children).filter(c => !c.classList.contains('running-head') && !c.classList.contains('foot-rule')) as HTMLElement[]
  const firstH3 = kids.findIndex(c => c.tagName === 'H3')
  if (firstH3 < 0) return
  const grid = document.createElement('div')
  grid.className = 'blocks-grid'
  let cell: HTMLElement | null = null
  for (const c of kids.slice(firstH3)) {
    if (c.tagName === 'H3') { cell = document.createElement('section'); cell.className = 'block'; grid.appendChild(cell) }
    cell!.appendChild(c)
  }
  el.insertBefore(grid, el.querySelector(':scope > .foot-rule'))
})
</script>

<template>
  <div ref="root" class="slidev-layout blocks" :style="{ '--blocks-cols': cols }">
    <div class="running-head" aria-hidden="true">{{ deckTitle }}</div>
    <slot />
    <div class="foot-rule" aria-hidden="true" />
  </div>
</template>
