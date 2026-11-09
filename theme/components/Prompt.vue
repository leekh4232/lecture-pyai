<script setup lang="ts">
// Callout kind="prompt" 의 짧은 이름. 프롬프트 상자(복사 버튼 · 다단). 안에는 백틱 네 개의 md 또는 text 코드 펜스로 프롬프트를 넣는다.
//   title: 머리말(기본 "프롬프트 실습"), cols: 단 수(기본 1), copy: 복사 버튼(기본 켬)
import Callout from './Callout.vue'
withDefaults(defineProps<{ title?: string; cols?: number | string; copy?: boolean }>(), { cols: 1, copy: true })
</script>

<template>
  <Callout kind="prompt" :title="title" :cols="cols" :copy="copy"><slot /></Callout>
</template>
