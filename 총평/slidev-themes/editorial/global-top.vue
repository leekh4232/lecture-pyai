<script setup lang="ts">
// 덱 헤더의 sidebar 가 켜져 있으면 발표 화면 왼쪽에 고정되는 목차 사이드바를 그린다.
//  - 사이드바는 슬라이드(16:9 캔버스) 바깥, 브라우저 창에 붙는다(Teleport → body). 슬라이드는 사이드바를 뺀 나머지 창에 비율대로 맞춰진다(editorial.css 의 #page-root)
//  - 제목이 있는 슬라이드를 나열하고 현재 위치를 강조, 클릭하면 이동
//  - 오른쪽 가장자리를 드래그해 폭 조절(더블클릭 = 기본 폭), ◀/☰ 버튼 또는 s 키로 접기/펼치기.
//    접으면 왼쪽 위에 반투명한 ☰ 버튼만 남고, 거기에 마우스를 올리면(또는 키보드 포커스) 선명해지면서 애니메이션 · 테마 · 확대/축소 버튼이 오른쪽으로 펼쳐진다
//  - 본문 확대/축소(＋/－ 버튼, + - 0 키): 캔버스는 그대로, 글자·여백만 바뀐다
//  - 넘침 표시: 현재 슬라이드의 내용이 캔버스를 벗어나면 빨간 테두리와 넘친 길이를 띄운다(발표 화면에서만, 등장 애니메이션이 끝난 뒤에 잰다)
//  - 처음 열면 접힌 채 시작한다(☰ 버튼 · s 키로 펼침). 폭·접힘·배율은 브라우저에 기억되므로 한 번 펼쳐 두면 다음에도 펼친 채 열린다
//  - 📄 원고 버튼(기본 켬, 덱 헤더 manuscript: false 면 뺀다): 덱 원고(md)를 깃헙 스타일 일반 페이지로 덮어 보여 준다(Esc · ✕ 로 닫기, manuscript.ts)
//  - 스마트폰(터치 · 1024px 이하): 사이드바는 접힌 채 시작하고 펼치면 슬라이드 위에 덮인다. 떠 있는 버튼은 ☰ 하나, 세로 화면이면 가로로 돌리라는 안내를 띄운다
import { computed, nextTick, onMounted, onUnmounted, ref, watch } from 'vue'
import { useDarkMode, useNav, useSlideContext } from '@slidev/client'
import { useDeckOptions } from './deck'
import { GITHUB_CSS_URL, renderManuscript } from './manuscript'

const { sidebar, exportDark, colorMode, fontScale, manuscript } = useDeckOptions()

const { currentPage, total, slides, go, nextSlide, prevSlide, clicks, clicksTotal } = useNav()
// ---- 밝음/어두움 테마 (Slidev 내장 다크 모드를 그대로 쓴다: d 키와 같은 동작, 브라우저에 기억됨) ----
const { isDark, toggleDark } = useDarkMode()
// ---- 쪽 번호: 모든 슬라이드 오른쪽 아래에 현재/전체 ----
//  발표 화면은 전역 nav 를, PDF·PNG 내보내기(/export)는 페이지마다 따로 받는 nav 를 읽어야 쪽마다 번호가 맞다 → 슬라이드 컨텍스트의 nav 를 쓴다
const { $slidev } = useSlideContext()
const pageNo = computed(() => $slidev.nav.currentPage)
const pageTotal = computed(() => $slidev.nav.total)
// 목차용 짧은 제목: 앞의 이모지 제거(번호 "#01." 의 # 은 남긴다), "—" 이후의 부제는 뗀다 ("#05. 문자열 변수 — 글자를 담기" → "#05. 문자열 변수")
function shortTitle(raw: string) {
  return raw.replace(/<[^>]+>/g, '').replace(/[`*]/g, '').replace(/^[^\p{L}\p{N}#]+/u, '').split(/\s+[—–-]\s+/)[0].trim()   // HTML 태그·마크다운 기호(` **) 제거
}
// 표지(1쪽)와 프런트매터 hideInToc: true 인 슬라이드(종료 페이지 등)는 목록에 넣지 않는다
const items = computed(() =>
  slides.value
    .map(s => ({ no: s.no, title: s.no === 1 || s.meta?.slide?.frontmatter?.hideInToc ? '' : shortTitle(s.meta?.slide?.title ?? ''), sub: (s.meta?.slide?.level ?? 2) >= 3 }))
    .filter(s => s.title),
)
// ---- ### 항목 접기: 바로 위 ## 항목(parent) 아래로 묶고, 펼친 묶음만 보인다 ----
const tocItems = computed(() => {
  let parent = 0
  const list = items.value.map(it => { if (!it.sub) parent = it.no; return { ...it, parent } })
  const kids = new Set(list.filter(it => it.sub).map(it => it.parent))
  return list.map(it => ({ ...it, hasKids: kids.has(it.no) }))
})
// 한 번에 한 묶음만 펼친다 (-1 = 모두 접힘). 다른 묶음을 열면 앞의 묶음은 닫힌다
const openGroup = ref(-1)
function toggleGroup(no: number) { openGroup.value = openGroup.value === no ? -1 : no }
// 현재 슬라이드가 접힌 묶음 안에 있으면 그 ## 항목을 현재 위치로 강조
const hiddenCurParent = computed(() => {
  const cur = tocItems.value.find(it => it.no === currentPage.value)
  return cur?.sub && openGroup.value !== cur.parent ? cur.parent : -1
})
// 슬라이드를 옮기면 그 슬라이드가 든 묶음을 펼친다 (묶음이 없으면 모두 접는다)
watch([currentPage, tocItems], () => {
  const cur = tocItems.value.filter(it => it.no <= currentPage.value).pop()
  openGroup.value = !cur ? -1 : cur.sub ? cur.parent : cur.hasKids ? cur.no : -1
}, { immediate: true })
// 목차를 현재 위치로 자동 스크롤 (현재 항목을 목록 가운데로)
const listEl = ref<HTMLElement | null>(null)
function scrollToCurrent(behavior: ScrollBehavior = 'smooth') {
  const list = listEl.value, li = list?.querySelector<HTMLElement>('li.current')
  if (list && li) list.scrollTo({ top: li.offsetTop - (list.clientHeight - li.offsetHeight) / 2, behavior })
}
watch([currentPage, openGroup], () => nextTick(() => scrollToCurrent()))
const deckTitle = computed(() => (slides.value[0]?.meta?.slide?.frontmatter?.title ?? '') as string)
const lab = computed(() => deckTitle.value.split(' · ')[0])
const unit = computed(() => deckTitle.value.split(' · ').slice(1).join(' · '))

// ---- 사이드바는 메인 발표 화면에서만 그린다. 발표자 모드·개요·PDF·PNG 내보내기(/export)·인쇄(/print)에는 없고 슬라이드가 창 전체를 쓴다 ----
const isPlay = typeof location !== 'undefined' && !/^\/(presenter|overview|print|export|notes|entry)/.test(location.pathname)
const showSidebar = computed(() => sidebar.value && isPlay)
// PDF·PNG 내보내기(/export, /print)는 발표 화면과 같이 어두운 테마로 찍는다(덱 헤더 exportDark: false 면 밝게). 내보내기 브라우저는 저장값이 없다
const isExport = typeof location !== 'undefined' && /^\/(print|export)/.test(location.pathname)
if (isExport) isDark.value = exportDark.value

// ---- 스마트폰(터치 · 좁은 창) 판정 ----
//  손가락으로 쓰는 좁은 화면에서는 사이드바를 기본으로 접고, 펼치면 슬라이드를 밀지 않고 그 위에 덮는다(슬라이드가 더 작아지지 않게).
//  떠 있는 버튼은 ☰ 하나만 두고(슬라이드가 창을 다 쓰므로 내용을 가리지 않게), 애니메이션 · 테마 · 확대 버튼은 사이드바 안의 것을 쓴다.
//  세로로 들고 있으면 가로로 돌리라는 안내를 한 번 띄운다. 넘기기는 Slidev 의 좌우 스와이프(터치)를 그대로 쓴다
const phoneMq = typeof window !== 'undefined' ? window.matchMedia('(pointer: coarse) and (max-width: 1024px)') : null
const isPhone = ref(!!phoneMq?.matches)
phoneMq?.addEventListener?.('change', e => { isPhone.value = e.matches })
const portraitMq = typeof window !== 'undefined' ? window.matchMedia('(orientation: portrait)') : null
const isPortrait = ref(!!portraitMq?.matches)
portraitMq?.addEventListener?.('change', e => { isPortrait.value = e.matches })
const hintClosed = ref(false)
const showRotateHint = computed(() => isPhone.value && isPortrait.value && !hintClosed.value && isPlay)

// ---- 폭·접힘 상태 ----
const MIN_W = 180, MAX_W = 520, DEFAULT_W = 260
const panelW = ref(DEFAULT_W)
// 기본은 접힌 채 시작. 브라우저에 '펼침'이 기억되어 있을 때만 펼친 채 연다(스마트폰은 늘 접힌 채). 마운트 전에 읽어야 첫 그림부터 여백이 맞는다
const storedOpen = (() => { try { return localStorage.getItem('pyai-sidebar-open') } catch { return null } })()
const open = ref(!isPhone.value && storedOpen === '1')
// --sidebar-w 는 슬라이드 영역(#page-root)의 왼쪽 여백 → 슬라이드는 그 나머지에 16:9 로 맞춰진다. 사이드바가 없거나 접혀 있으면 0, 펼친 채 열면 마운트 전에도 기본 폭을 비워 둔다.
//  스마트폰에서는 사이드바가 슬라이드를 덮으므로 여백을 두지 않는다
if (typeof document !== 'undefined') document.documentElement.style.setProperty('--sidebar-w', showSidebar.value && open.value ? `${DEFAULT_W}px` : '0px')
function apply() {
  // 접히면 0 → 슬라이드가 창 전체로 커진다. 스마트폰에서는 덮는 방식이라 항상 0
  document.documentElement.style.setProperty('--sidebar-w', open.value && !isPhone.value ? `${panelW.value}px` : '0px')
  try {
    localStorage.setItem('pyai-sidebar-w', String(panelW.value))
    if (!isPhone.value) localStorage.setItem('pyai-sidebar-open', open.value ? '1' : '0')   // 스마트폰의 접힘은 기억하지 않는다(늘 접힌 채 시작)
  } catch { /* 저장 불가 환경 무시 */ }
}
watch(isPhone, apply)
// 스마트폰에서 목차 항목을 고르면 사이드바를 닫아 슬라이드가 바로 보이게 한다
function pick(no: number) { goTo(no); if (isPhone.value) open.value = false }
watch([panelW, open], apply)
function setWidth(px: number) { panelW.value = Math.round(Math.min(MAX_W, Math.max(MIN_W, px))) }
function toggle() { open.value = !open.value }
function resetWidth() { setWidth(DEFAULT_W) }

// ---- 본문 확대/축소: 캔버스(1280×720)는 그대로 두고 .slidev-layout 에 CSS zoom(editorial.css 의 --zoom) → 글자·여백만 커지거나 작아지고, 넘치면 잘린다(넘침 표시가 알려 준다) ----
const zoom = ref(1)
function applyZoom() {
  document.documentElement.style.setProperty('--zoom', String(zoom.value))
  try { localStorage.setItem('pyai-zoom', String(zoom.value)) } catch { /* 무시 */ }
}
function setZoom(z: number) { zoom.value = Math.round(Math.min(2, Math.max(0.6, z)) * 10) / 10; applyZoom() }
function zoomIn() { setZoom(zoom.value + 0.1) }
function zoomOut() { setZoom(zoom.value - 0.1) }
function zoomReset() { setZoom(fontScale.value ?? 1) }
// 덱 헤더에 fontScale 이 있으면 사이드바 유무·내보내기와 상관없이 그 배율로 연다(브라우저에 기억된 배율보다 우선)
if (typeof document !== 'undefined' && fontScale.value) { zoom.value = fontScale.value; document.documentElement.style.setProperty('--zoom', String(zoom.value)) }

// ---- 넘침 표시: 현재 슬라이드의 모든 요소 중 가장 아래·오른쪽 끝이 캔버스(.slidev-page 상자)를 넘는 길이를 잰다(캔버스 px, 축소 배율로 되돌림).
//  표지·간지의 장식(aria-hidden)은 일부러 밖으로 나가 있으므로 뺀다. 슬라이드 전환·클릭·배율·글꼴 로딩 때마다 다시 재되, 애니메이션이 모두 끝난 뒤에 잰다. 발표 화면에서만 (내보내기에는 없다) ----
const over = ref<{ y: number; x: number } | null>(null)
function measureOverflow() {
  const pg = document.querySelector<HTMLElement>(`#slide-content .slidev-page[data-slidev-no="${currentPage.value}"]`)
  const layout = pg?.querySelector<HTMLElement>('.slidev-layout')
  if (!pg || !layout) { over.value = null; return }
  const scale = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--slidev-slide-scale')) || 1
  const box = pg.getBoundingClientRect()
  let maxB = -Infinity, maxR = -Infinity
  for (const el of layout.querySelectorAll<HTMLElement>('*')) {
    if (el.closest('[aria-hidden="true"]')) continue
    const r = el.getBoundingClientRect(); if (!r.width && !r.height) continue
    if (r.bottom > maxB) maxB = r.bottom
    if (r.right > maxR) maxR = r.right
  }
  const y = Math.round((maxB - box.bottom) / scale), x = Math.round((maxR - box.right) / scale)
  over.value = y > 0 || x > 0 ? { y, x } : null
}
// 등장 애니메이션(lecture-rise · cover-rise · v-click 전환 등)이 도는 동안은 요소가 제자리에 없어 잘못 잰다 → 현재 슬라이드 안의
//  애니메이션 · 전환이 모두 끝난 뒤에만 잰다. 끝나기 전에는 표시를 지운다. 무한 반복(표지 장식 cover-drift · cover-spin)은 끝나지 않으므로 기다리지 않는다
let overRaf = 0, overToken = 0
function pendingAnimations(pg: HTMLElement): Animation[] {
  if (typeof pg.getAnimations !== 'function') return []
  return pg.getAnimations({ subtree: true }).filter(a => {
    if (a.playState === 'finished' || a.playState === 'idle') return false
    const t = a.effect?.getTiming?.()
    if (t && t.iterations === Infinity) return false
    const target = (a.effect as KeyframeEffect | null)?.target as Element | null
    if (target?.closest?.('[aria-hidden="true"]')) return false
    return true
  })
}
function scheduleOverflow() {
  cancelAnimationFrame(overRaf)
  const token = ++overToken
  overRaf = requestAnimationFrame(() => {
    const pg = document.querySelector<HTMLElement>(`#slide-content .slidev-page[data-slidev-no="${currentPage.value}"]`)
    const anims = pg ? pendingAnimations(pg) : []
    if (!anims.length) { measureOverflow(); return }
    over.value = null
    Promise.allSettled(anims.map(a => a.finished)).then(() => { if (token === overToken) scheduleOverflow() })
  })
}
watch([currentPage, clicks, zoom], () => nextTick(scheduleOverflow))

// ---- 애니메이션 켬/끔 ----
//  끔: 클릭 단계 없이 슬라이드의 모든 내용이 바로 보이고(클릭 수를 최대로), →/← 가 슬라이드 단위로 이동, 전환 효과 없음
const CLICKS_MAX = 99999
const anim = ref(true)
function applyAnim() {
  document.documentElement.classList.toggle('no-anim', !anim.value)
  try { localStorage.setItem('pyai-anim', anim.value ? '1' : '0') } catch { /* 무시 */ }
  if (!anim.value) go(currentPage.value, CLICKS_MAX, true)
}
function toggleAnim() { anim.value = !anim.value; applyAnim() }
function goTo(no: number) { go(no, anim.value ? 0 : CLICKS_MAX) }
watch(currentPage, () => { if (!anim.value && clicks.value < clicksTotal.value) go(currentPage.value, CLICKS_MAX) })
// ---- 방향키: 애니메이션 끔이면 클릭 단계를 건너뛰고 슬라이드 단위로 움직인다 (켬이면 Slidev 기본 동작: 다음 클릭/슬라이드) ----
const NEXT_KEYS = ['ArrowRight', 'ArrowDown', ' ', 'PageDown', 'Enter']
const PREV_KEYS = ['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace']
function onKeyCapture(e: KeyboardEvent) {
  if (anim.value) return
  if (e.ctrlKey || e.metaKey || e.altKey) return
  const t = e.target as HTMLElement | null
  if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return
  const next = NEXT_KEYS.includes(e.key), prev = PREV_KEYS.includes(e.key)
  if (!next && !prev) return
  e.preventDefault(); e.stopImmediatePropagation(); next ? nextSlide(true) : prevSlide(true)
}

function startDrag(e: PointerEvent) {
  e.preventDefault()
  const handle = e.currentTarget as HTMLElement
  handle.setPointerCapture(e.pointerId)
  const left = (handle.parentElement as HTMLElement).getBoundingClientRect().left
  document.body.style.userSelect = 'none'; document.body.style.cursor = 'col-resize'
  const move = (ev: PointerEvent) => setWidth(ev.clientX - left)
  const stop = () => {
    handle.removeEventListener('pointermove', move); handle.removeEventListener('pointerup', stop)
    document.body.style.userSelect = ''; document.body.style.cursor = ''
  }
  handle.addEventListener('pointermove', move); handle.addEventListener('pointerup', stop)
}
// ---- 원고 보기: 원고 화면이 떠 있는 동안에는 슬라이드 단축키(방향키 · s · a · d …)를 막고, Esc 로 닫는다 ----
const msOpen = ref(false), msHtml = ref(''), msError = ref('')
const msEl = ref<HTMLElement | null>(null)
async function openManuscript() {
  msOpen.value = true
  if (isPhone.value) open.value = false
  if (!document.querySelector('link[data-ms-css]')) {
    const l = document.createElement('link'); l.rel = 'stylesheet'; l.href = GITHUB_CSS_URL; l.dataset.msCss = ''; document.head.appendChild(l)
  }
  nextTick(() => msEl.value?.focus())
  if (msHtml.value) return
  msError.value = ''
  try { msHtml.value = await renderManuscript(deckTitle.value) }
  catch { msError.value = '원고를 불러오지 못했어요. 인터넷 연결을 확인해 주세요.' }
}
function closeManuscript() { msOpen.value = false }
function onMsKey(e: KeyboardEvent) {
  if (!msOpen.value) return
  if (e.key === 'Escape') { e.preventDefault(); closeManuscript() }
  e.stopImmediatePropagation()   // 기본 동작(스크롤)은 두고, Slidev · 테마 단축키로는 보내지 않는다
}
function onKey(e: KeyboardEvent) {
  const t = e.target as HTMLElement | null
  if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return
  if (e.ctrlKey || e.metaKey || e.altKey) return
  if (e.key === 's') { e.preventDefault(); toggle() }
  if (e.key === 'a') { e.preventDefault(); toggleAnim() }
  if (e.key === '+' || e.key === '=') { e.preventDefault(); zoomIn() }
  if (e.key === '-' || e.key === '_') { e.preventDefault(); zoomOut() }
  if (e.key === '0') { e.preventDefault(); zoomReset() }
}

// ---- 표 첫 열: 기본은 nowrap(항목 열). 첫 열이 표 폭의 30% 를 넘을 만큼 길면 table.first-long 을 붙여 줄바꿈을 허용한다.
//  슬라이드 프런트매터 class: tbl-wrap / tbl-nowrap 이면 자동 판정을 건너뛴다(CSS 가 강제). 슬라이드 전환·창 크기 변화마다 다시 잰다.
const FIRST_COL_MAX = 0.3
function measureTables() {
  const tables = document.querySelectorAll<HTMLTableElement>('#slide-content .slidev-layout table, #slide-content .slidev-layout .first-long')
  tables.forEach(t => {
    if (t.closest('.tbl-wrap, .tbl-nowrap')) return
    t.classList.remove('first-long')
    const cell = t.querySelector<HTMLElement>('tr > :first-child')
    const tw = t.getBoundingClientRect().width
    if (!cell || tw <= 0) return
    if (cell.getBoundingClientRect().width / tw > FIRST_COL_MAX) t.classList.add('first-long')
  })
}
function scheduleMeasure() { nextTick(() => requestAnimationFrame(measureTables)) }
watch(currentPage, scheduleMeasure)
onMounted(() => {
  scheduleMeasure(); setTimeout(measureTables, 400)   // 글꼴 로딩 뒤 한 번 더
  window.addEventListener('resize', scheduleMeasure)
  if (typeof document !== 'undefined' && 'fonts' in document) (document as any).fonts?.ready?.then(() => { measureTables(); scheduleOverflow() })
  if (!isPlay) return
  // 처음 한 번만 어두운 테마로 시작한다(pyai-dark-init 표시). 그 뒤 d 키·🌙 버튼으로 고른 값은 Slidev 가 기억한다(slidev-color-schema —
  // 시스템 설정과 같은 값을 고르면 'auto' 로 저장되므로, 그 값을 보고 판단하면 사용자의 선택을 되돌리게 된다)
  // 덱 헤더에 colorMode 가 있으면 열 때마다 그 테마로 시작한다(d 키로 바꾼 값은 다시 열면 헤더 값으로 돌아간다)
  if (colorMode.value) isDark.value = colorMode.value === 'dark'
  else try { if (!localStorage.getItem('pyai-dark-init')) { isDark.value = true; localStorage.setItem('pyai-dark-init', '1') } } catch { /* 무시 */ }
  scheduleOverflow(); setTimeout(scheduleOverflow, 400)
  // 반응형 상태 변화 없이 시작된 애니메이션(hover 등)이 끝났을 때도 다시 잰다(scheduleOverflow 가 남은 애니메이션을 또 기다린다)
  document.addEventListener('animationend', scheduleOverflow, true)
  document.addEventListener('transitionend', scheduleOverflow, true)
})
onUnmounted(() => {
  window.removeEventListener('resize', scheduleMeasure)
  document.removeEventListener('animationend', scheduleOverflow, true)
  document.removeEventListener('transitionend', scheduleOverflow, true)
  cancelAnimationFrame(overRaf)
})

onMounted(() => {
  if (!showSidebar.value) return
  try {
    const w = Number(localStorage.getItem('pyai-sidebar-w')); if (w) panelW.value = Math.min(MAX_W, Math.max(MIN_W, w))
    if (localStorage.getItem('pyai-anim') === '0') anim.value = false
    const z = Number(localStorage.getItem('pyai-zoom')); if (z && !fontScale.value) zoom.value = z
  } catch { /* 무시 */ }
  apply(); applyAnim(); applyZoom()
  setTimeout(() => scrollToCurrent('auto'), 300)   // 새로 열었을 때도 현재 항목이 보이게
  window.addEventListener('keydown', onMsKey, true)   // onKeyCapture 보다 먼저 받아야 원고 화면에서 슬라이드가 넘어가지 않는다
  window.addEventListener('keydown', onKey)
  window.addEventListener('keydown', onKeyCapture, true)
})
onUnmounted(() => {
  window.removeEventListener('keydown', onMsKey, true)
  window.removeEventListener('keydown', onKey)
  window.removeEventListener('keydown', onKeyCapture, true)
  document.documentElement.classList.remove('no-anim')
})
</script>

<template>
  <div class="page-no" aria-label="쪽 번호">{{ pageNo }}/{{ pageTotal }}</div>
  <!-- 넘침 표시: 캔버스 안쪽 빨간 테두리 + 오른쪽 위에 넘친 길이. 발표 화면에서만 -->
  <div v-if="isPlay && over" class="over-frame" aria-hidden="true">
    <span class="over-tag">내용 넘침 <template v-if="over.y > 0">↓{{ over.y }}px</template><template v-if="over.x > 0"> →{{ over.x }}px</template></span>
  </div>
  <!-- 사이드바는 슬라이드 캔버스(#slide-content, 비율 축소됨) 바깥에 두어야 하므로 body 로 보낸다 -->
  <Teleport v-if="showSidebar" to="body">
  <div v-if="isPhone && open" class="toc-backdrop" aria-hidden="true" @click="toggle" />
  <aside class="toc" :class="{ collapsed: !open, phone: isPhone }" :style="{ width: isPhone ? undefined : panelW + 'px' }">
    <button class="toc-toggle" title="사이드바 접기 (s)" @click="toggle">◀</button>
    <div class="toc-head" title="표지로 이동" @click="goTo(1)">
      <div class="toc-lab" :title="lab">{{ lab }}</div>
      <div class="toc-unit" :title="unit">{{ unit }}</div>
    </div>
    <ol ref="listEl" class="toc-list">
      <template v-for="it in tocItems" :key="it.no">
        <li
          v-if="!it.sub || openGroup === it.parent"
          :class="{ current: it.no === currentPage || (it.no === hiddenCurParent), done: it.no < currentPage, sub: it.sub }"
          @click="pick(it.no)"
        >
          <span class="txt" :title="it.title">{{ it.title }}</span>
          <button v-if="it.hasKids" class="caret" :class="{ open: openGroup === it.no }" title="하위 항목 펼치기/접기" @click.stop="toggleGroup(it.no)">▸</button>
        </li>
      </template>
    </ol>
    <div class="toc-foot">
      <span>{{ currentPage }} / {{ total }}</span>
      <span class="foot-btns">
        <button class="anim-btn" :class="{ off: !anim }" :title="anim ? '애니메이션 끄기 (a)' : '애니메이션 켜기 (a)'" @click="toggleAnim">{{ anim ? '애니메이션 켬' : '애니메이션 끔' }}</button>
        <button class="anim-btn" :title="isDark ? '밝은 테마 (d)' : '어두운 테마 (d)'" @click="toggleDark()">{{ isDark ? '밝게' : '어둡게' }}</button>
      </span>
    </div>
    <div class="toc-zoom">
      <span>확대/축소</span>
      <span class="foot-btns">
        <button class="anim-btn" title="축소 (-)" @click="zoomOut">－</button>
        <button class="anim-btn" title="기본 크기 100% 로 (0)" @click="zoomReset">{{ Math.round(zoom * 100) }}%</button>
        <button class="anim-btn" title="확대 (+)" @click="zoomIn">＋</button>
      </span>
    </div>
    <div v-if="manuscript" class="toc-zoom">
      <span>원고 보기</span>
      <button class="anim-btn" title="원고(md)를 일반 문서로 보기" @click="openManuscript">원고</button>
    </div>
    <div v-if="!isPhone" class="resizer" title="드래그해서 폭 조절 · 더블클릭하면 기본 폭" @pointerdown="startDrag" @dblclick="resetWidth" />
  </aside>
  <!-- 접힌 상태: ☰ 만 보이고, 마우스를 올리면 나머지 버튼이 오른쪽으로 펼쳐진다 -->
  <div v-if="!open" class="toc-float" :class="{ phone: isPhone }">
    <button class="toc-open" title="사이드바 펼치기 (s) · 올리면 조작 버튼" @click="toggle">☰</button>
    <div v-if="!isPhone" class="float-tray">
      <button class="toc-open" :class="{ off: !anim }" :title="anim ? '애니메이션 끄기 (a)' : '애니메이션 켜기 (a)'" @click="toggleAnim">{{ anim ? '▶' : 'Ⅱ' }}</button>
      <button class="toc-open" :title="isDark ? '밝은 테마 (d)' : '어두운 테마 (d)'" @click="toggleDark()">{{ isDark ? '밝게' : '어둡게' }}</button>
      <button class="toc-open" title="축소 (-)" @click="zoomOut">－</button>
      <button class="toc-open zoom-reset" title="기본 크기 100% 로 (0)" @click="zoomReset">{{ Math.round(zoom * 100) }}%</button>
      <button class="toc-open" title="확대 (+)" @click="zoomIn">＋</button>
      <button v-if="manuscript" class="toc-open" title="원고(md)를 일반 문서로 보기" @click="openManuscript">≡</button>
    </div>
  </div>
  <!-- 스마트폰 세로 화면: 가로로 돌리라는 안내(한 번 닫으면 다시 안 뜸) -->
  <div v-if="showRotateHint" class="rotate-hint" role="status">
    <span>가로로 돌리면 슬라이드가 커져요 · 좌우로 밀어 넘기세요</span>
    <button title="닫기" @click="hintClosed = true">✕</button>
  </div>
  <!-- 원고 보기: 창 전체를 덮는 깃헙 스타일 문서 -->
  <div v-if="msOpen" ref="msEl" class="ms-view" tabindex="-1" role="dialog" aria-label="원고 보기">
    <div class="ms-bar">
      <span class="ms-title">{{ unit || lab }} · 원고</span>
      <button class="anim-btn" title="슬라이드로 돌아가기 (Esc)" @click="closeManuscript">✕ 슬라이드로</button>
    </div>
    <p v-if="msError" class="ms-msg">{{ msError }}</p>
    <p v-else-if="!msHtml" class="ms-msg">원고를 불러오는 중…</p>
    <article v-else class="markdown-body" v-html="msHtml" />
  </div>
  </Teleport>
</template>

<style scoped>
.page-no {
  position: absolute; right: 16px; bottom: 10px; z-index: 4;
  font-family: "Pretendard Variable", Pretendard, -apple-system, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  font-size: 0.75rem; font-weight: 600; letter-spacing: .02em; color: var(--muted, #5d6b85);
  font-variant-numeric: tabular-nums; pointer-events: none; user-select: none;
}
/* 사이드바와 떠 있는 버튼은 body 에 붙으므로 창 기준(fixed). 슬라이드 축소 배율과 무관하게 실제 픽셀 크기 그대로 보인다 */
.toc {
  position: fixed; left: 0; top: 0; bottom: 0; width: var(--sidebar-w, 260px);
  background: var(--surface, #f3f6fb); border-right: 1px solid var(--line, rgba(10,20,40,.1));
  display: flex; flex-direction: column; padding: 18px 14px 12px; z-index: 5;
  font-family: "Pretendard Variable", Pretendard, -apple-system, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  color: var(--text, #16213a);
  transition: transform .2s ease;
}
.toc.collapsed { transform: translateX(-100%); }
.toc-toggle, .toc-open {
  width: 30px; height: 30px; border: 1px solid var(--line, rgba(10,20,40,.1));
  background: var(--card-bg, #fff); color: var(--muted, #5d6b85); cursor: pointer; font-size: 0.8rem; line-height: 1;
  display: grid; place-items: center;
}
.toc-toggle { position: absolute; top: 12px; right: 12px; }
.toc-toggle:hover, .toc-open:hover { color: var(--py, #0a7fc2); border-color: var(--py, #0a7fc2); }
@media print { .toc, .toc-float { display: none !important; } }
/* 접힌 상태의 떠 있는 버튼 묶음: 창 왼쪽 위에 고정. ☰ 은 늘 보이고, 묶음에 마우스를 올리거나 안의 버튼에 포커스가 가면 쟁반(.float-tray)이 오른쪽으로 펼쳐진다 */
.toc-float { position: fixed; top: 14px; left: 14px; z-index: 6; display: flex; align-items: center; gap: 8px; opacity: 0.45; transition: opacity .2s ease; }   /* 평소에는 반투명, 올리면 선명 */
.toc-float:hover, .toc-float:focus-within { opacity: 1; }
.float-tray { display: flex; align-items: center; gap: 8px; max-width: 0; overflow: hidden; opacity: 0; transform: translateX(-10px); transition: max-width .25s ease, opacity .18s ease, transform .25s ease; }
.toc-float:hover .float-tray, .toc-float:focus-within .float-tray { max-width: 320px; opacity: 1; transform: none; }
.float-tray .toc-open { flex: none; }
.float-tray .zoom-reset { width: auto; padding: 0 8px; font-weight: 700; font-variant-numeric: tabular-nums; }
.float-tray .toc-open.off { color: var(--ai, #d9611f); }
.toc-head { padding: 0 44px 10px 4px; border-bottom: 1px solid var(--line, rgba(10,20,40,.1)); margin-bottom: 8px; cursor: pointer; }   /* 클릭하면 표지(1쪽)로. 표지는 목록에 넣지 않는다 */
.toc-head:hover .toc-unit { color: var(--py, #0a7fc2); }
.toc-lab { font-size: 0.9rem; font-weight: 800; letter-spacing: .08em; color: var(--py, #0a7fc2); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.toc-unit { font-size: 1.05rem; font-weight: 700; line-height: 1.25; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.toc-list { position: relative; list-style: none; margin: 0; padding: 0; flex: 1; overflow-y: auto; }   /* relative: 자동 스크롤이 li.offsetTop 을 목록 기준으로 잰다 */
.toc-list li .txt { flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }   /* 항목은 한 줄, 넘치면 말줄임 (전체 제목은 마우스를 올리면 보인다) */
.toc-list li {
  display: flex; align-items: flex-start; gap: 9px; padding: 6px 8px; margin: 2px 0;
  font-size: 0.9rem; line-height: 1.3; cursor: pointer; color: var(--muted, #5d6b85);
}
.toc-list li:hover { background: rgba(10,127,194,.08); }
.toc-list li.sub { padding-left: 24px; }   /* ### 슬라이드: 한 단계 들여쓰기 */
.toc-list li.sub .txt { font-size: .93em; }
.toc-list li .caret {
  margin-left: auto; flex: 0 0 auto; width: 20px; height: 20px; border: none; background: none; padding: 0;
  color: var(--muted, #5d6b85); font-size: .8rem; line-height: 20px; cursor: pointer; transition: transform .15s;
}
.toc-list li .caret:hover { background: rgba(10,127,194,.12); color: var(--py, #0a7fc2); }
.toc-list li .caret.open { transform: rotate(90deg); }
.toc-list li.current { background: var(--py-soft, rgba(10,127,194,.1)); color: var(--text, #16213a); font-weight: 700; }
.resizer {
  position: absolute; top: 0; bottom: 0; right: -4px; width: 8px; cursor: col-resize; z-index: 6;
  background: transparent; transition: background .15s;
}
.resizer:hover, .resizer:active { background: rgba(10,127,194,.35); }
.toc-foot { font-size: 0.9rem; color: var(--muted, #5d6b85); padding: 8px 6px 0; border-top: 1px solid var(--line, rgba(10,20,40,.1)); font-variant-numeric: tabular-nums; display: flex; align-items: center; justify-content: space-between; gap: 6px; }
.foot-btns { display: flex; gap: 4px; }
.anim-btn { font-size: 0.8rem; font-weight: 700; padding: 4px 8px; border: 1px solid var(--line, rgba(10,20,40,.1)); background: var(--card-bg, #fff); color: var(--py, #0a7fc2); cursor: pointer; white-space: nowrap; }
.anim-btn.off { color: var(--ai, #d9611f); }
.anim-btn:hover { border-color: currentColor; }
.toc-zoom { font-size: 0.9rem; color: var(--muted, #5d6b85); padding: 6px 6px 0; display: flex; align-items: center; justify-content: space-between; gap: 6px; white-space: nowrap; }
/* 스마트폰: 사이드바는 슬라이드 위에 덮이는 서랍(창의 82%, 최대 320px), 뒤에 반투명 배경막. 떠 있는 버튼은 ☰ 하나뿐이고 손가락 크기(36px) · 반투명 */
.toc-backdrop { position: fixed; inset: 0; z-index: 4; background: rgba(10,20,40,.35); }
.toc.phone { width: min(82vw, 320px); box-shadow: 0 0 24px rgba(0,0,0,.25); }
.toc.phone .toc-list li { padding: 10px 8px; font-size: 1rem; }
.toc.phone .toc-toggle, .toc.phone .anim-btn { min-height: 36px; min-width: 36px; }
.toc-float.phone { top: 8px; left: 8px; opacity: 0.6; }
.toc-float.phone .toc-open { width: 36px; height: 36px; font-size: 1rem; }
.rotate-hint {
  position: fixed; left: 12px; right: 12px; bottom: 12px; z-index: 6; display: flex; align-items: center; justify-content: space-between; gap: 10px;
  padding: 10px 12px; background: var(--py, #0a7fc2); color: #fff; font-size: 0.9rem; font-weight: 600;
  font-family: "Pretendard Variable", Pretendard, -apple-system, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
}
.rotate-hint button { flex: none; width: 32px; height: 32px; border: 1px solid rgba(255,255,255,.6); background: transparent; color: #fff; cursor: pointer; }
/* 원고 보기: 사이드바 · 떠 있는 버튼보다 위. 깃헙 마크다운 CSS(.markdown-body)는 열 때 CDN 에서 받는다 */
.ms-view { position: fixed; inset: 0; z-index: 20; overflow-y: auto; background: #fff; outline: none; }
.ms-bar {
  position: sticky; top: 0; z-index: 1; display: flex; align-items: center; justify-content: space-between; gap: 12px;
  padding: 10px 20px; background: #f6f8fa; border-bottom: 1px solid #d0d7de;
  font-family: "Pretendard Variable", Pretendard, -apple-system, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
}
.ms-title { font-size: 0.95rem; font-weight: 700; color: #1f2328; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.ms-view .markdown-body { box-sizing: border-box; max-width: 900px; margin: 0 auto; padding: 32px 24px 80px; font-family: "Pretendard Variable", Pretendard, -apple-system, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif; }
.ms-view .markdown-body :deep(img), .ms-view .markdown-body :deep(svg) { max-width: 100%; height: auto; }
.ms-msg { max-width: 900px; margin: 40px auto; padding: 0 24px; color: #59636e; font-family: "Pretendard Variable", Pretendard, sans-serif; }
/* 넘침 표시: 캔버스(#slide-content) 안에 있어 캔버스와 함께 축소된다 */
.over-frame { position: absolute; inset: 0; z-index: 7; pointer-events: none; box-shadow: inset 0 0 0 5px var(--danger, #c8323f); }
.over-tag {
  position: absolute; top: 12px; right: 12px; padding: 6px 12px;
  background: var(--danger, #c8323f); color: #fff;
  font-family: "Pretendard Variable", Pretendard, -apple-system, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  font-size: 0.75rem; font-weight: 700; letter-spacing: .02em; font-variant-numeric: tabular-nums;
}
</style>
