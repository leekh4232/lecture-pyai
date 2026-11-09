<script setup lang="ts">
// Steps type="timeline" 의 짧은 이름. 타임라인. color: py | ai | ok, vertical: 세로, center: 점과 글을 칸 가운데에
import Steps from './Steps.vue'
withDefaults(defineProps<{ color?: string; vertical?: boolean; center?: boolean }>(), { color: 'py', vertical: false, center: false })
</script>

<template>
  <Steps type="timeline" :color="color" :vertical="vertical" :center="center"><slot /></Steps>
</template>
