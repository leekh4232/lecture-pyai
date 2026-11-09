<script setup lang="ts">
// Callout kind="output" 의 짧은 이름. 프로그램 출력 상자. 슬롯에 출력 텍스트(또는 코드 펜스)를 그대로 넣는다.
//   label(또는 title): 왼쪽 위 라벨(기본 "출력")
import Callout from './Callout.vue'
defineProps<{ label?: string; title?: string }>()
</script>

<template>
  <Callout kind="output" :title="title ?? label"><slot /></Callout>
</template>
