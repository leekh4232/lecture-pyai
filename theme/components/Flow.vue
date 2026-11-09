<script setup lang="ts">
// Steps type="flow" 의 짧은 이름. 가로 흐름도. color: py | ai | ok, start: 첫 번호
import Steps from './Steps.vue'
withDefaults(defineProps<{ color?: string; start?: number | string }>(), { color: 'py' })
</script>

<template>
  <Steps type="flow" :color="color" :start="start"><slot /></Steps>
</template>
