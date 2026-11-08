// 덱 헤더(첫 슬라이드 프런트매터)의 테마 옵션을 읽는다.
//   sidebar: true | false (기본: 켬) — 켜도 처음에는 접힌 채 열리고, ☰ 버튼 · s 키로 펼친다(펼침은 브라우저에 기억)
//   exportDark: true | false (기본: 켬) — PDF·PNG 내보내기를 어두운 테마로. 생략하고 colorMode 를 적으면 내보내기도 colorMode 를 따른다
//   colorMode: light | dark (생략: 처음 한 번만 어둡게, 그 뒤엔 브라우저에 기억된 값) — 덱을 열 때의 테마. d 키로 바꿀 수 있다
//   fontScale: 숫자 0.6~2 (생략: 브라우저에 기억된 배율) — 덱을 열 때의 본문 배율이자 0 키·배율 버튼이 돌아가는 값. 내보내기에도 적용
//   manuscript: true | false (기본: 켬) — 사이드바에 📄 원고 버튼을 둔다. 누르면 덱 원고(md)를 깃헙 스타일 일반 페이지로 본다
// 테마 CSS 는 <html> 의 editorial 클래스 아래에 묶여 있어서, 이 함수를 쓰는 곳(레이아웃·global-top)이 클래스를 붙인다.
import { computed } from 'vue'
import { useNav } from '@slidev/client'

export function useDeckOptions() {
  const { slides } = useNav()
  const fm = computed(() => (slides.value[0]?.meta?.slide?.frontmatter ?? {}) as Record<string, unknown>)
  const flag = (key: string) => computed(() => {
    const v = fm.value[key]
    if (v === undefined || v === null || v === '') return true
    return v === true || v === 'true'
  })
  const sidebar = flag('sidebar')
  const exportDark = computed(() => {
    const v = fm.value.exportDark
    if (v === undefined || v === null || v === '') return colorMode.value ? colorMode.value === 'dark' : true
    return v === true || v === 'true'
  })
  const colorMode = computed(() => {
    const v = String(fm.value.colorMode ?? '').toLowerCase()
    return v === 'light' || v === 'dark' ? v : null
  })
  const fontScale = computed(() => {
    const v = Number(fm.value.fontScale)
    return v ? Math.round(Math.min(2, Math.max(0.6, v)) * 10) / 10 : null
  })
  const manuscript = computed(() => fm.value.manuscript !== false && fm.value.manuscript !== 'false')
  if (typeof document !== 'undefined') document.documentElement.classList.add('editorial')
  return { sidebar, exportDark, colorMode, fontScale, manuscript }
}
