<script setup lang="ts">
// 유튜브 영상(썸네일형). 내장 <Youtube> 와 프롭이 같다(id · width · height). 내장 이름은 테마에서 덮어쓸 수 없어 이름을 달리했다.
// 처음엔 썸네일과 재생 버튼만 보여 주고, 누르면 그 자리에서 재생한다. 내보낸 HTML 을 파일로 직접 열면(file://) 유튜브가 리퍼러 없는 임베드를
// "구성 오류"로 막으므로, 그때는 유튜브 페이지를 새 탭으로 연다. PDF·PNG 내보내기에도 썸네일이 찍힌다.
import { computed, ref } from 'vue'
const props = defineProps<{ id: string; width?: number | string; height?: number | string }>()
const size = (v?: number | string) => v === undefined ? undefined : /^\d+(\.\d+)?$/.test(String(v)) ? `${v}px` : String(v)
const style = computed(() => ({ width: size(props.width) ?? '100%', height: size(props.height) ?? '315px' }))
const thumb = ref(`https://i.ytimg.com/vi/${props.id}/maxresdefault.jpg`)
function fallback() { if (!thumb.value.endsWith('hqdefault.jpg')) thumb.value = `https://i.ytimg.com/vi/${props.id}/hqdefault.jpg` }   // 고화질 썸네일이 없는 영상
const playing = ref(false)
function play() {
  if (typeof location !== 'undefined' && location.protocol.startsWith('http')) playing.value = true
  else window.open(`https://www.youtube.com/watch?v=${props.id}`, '_blank', 'noopener')
}
</script>

<template>
  <iframe
    v-if="playing" class="youtube" :style="style"
    :src="`https://www.youtube.com/embed/${id}?autoplay=1`" title="YouTube" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
  />
  <button v-else class="youtube yt-thumb" :style="style" type="button" title="재생" @click="play">
    <img :src="thumb" alt="" @error="fallback">
    <span class="yt-play" aria-hidden="true"><svg viewBox="0 0 68 48" width="68" height="48"><path d="M66.5 7.7c-.8-2.9-3-5.2-5.9-6C55.4.3 34 .3 34 .3s-21.4 0-26.6 1.4c-2.9.8-5.1 3.1-5.9 6C.3 13 .3 24 .3 24s0 11 1.4 16.3c.8 2.9 3 5.2 5.9 6C12.6 47.7 34 47.7 34 47.7s21.4 0 26.6-1.4c2.9-.8 5.1-3.1 5.9-6C67.7 35 67.7 24 67.7 24s0-11-1.2-16.3z" fill="#f00"/><path d="M27 34.5l17.5-10.5L27 13.5z" fill="#fff"/></svg></span>
    <span class="yt-hint">YouTube에서 재생</span>
  </button>
</template>

<style scoped>
.yt-thumb { position: relative; display: block; padding: 0; margin: 0; border: 1px solid var(--line, rgba(10,20,40,.1)); overflow: hidden; background: #000; cursor: pointer; }
.yt-thumb img { width: 100%; height: 100%; object-fit: cover; display: block; margin: 0; max-width: none; opacity: .92; }
.yt-play { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); filter: drop-shadow(0 2px 8px rgba(0,0,0,.4)); transition: transform .15s; }
.yt-thumb:hover .yt-play { transform: translate(-50%, -50%) scale(1.08); }
.yt-hint { position: absolute; right: 10px; bottom: 8px; padding: 3px 8px; background: rgba(0,0,0,.55); color: #fff; font-size: 12px; font-weight: 600; }
iframe.youtube { display: block; }
</style>
