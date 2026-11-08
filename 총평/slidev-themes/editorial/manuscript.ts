// 덱 원고(md 파일)를 슬라이드가 아닌 깃헙 스타일 일반 마크다운 페이지로 보여 준다. 덱 헤더 manuscript: true 일 때만 쓴다.
//  - Slidev 는 빌드 결과에서 슬라이드 원문을 비우므로, 덱 폴더의 md 원문을 ?raw 로 따로 묶는다(누를 때 받는 별도 조각이라 평소 로딩에는 영향 없음)
//  - 테마는 패키지를 import 하지 않으므로 마크다운 렌더러(marked)와 깃헙 CSS 는 원고를 처음 열 때 CDN 에서 받는다 → 오프라인에서는 열리지 않는다
//  - 원문을 그대로 그리면 <Tile title="…"> 같은 컴포넌트의 속성(제목 등)이 사라지므로, 먼저 일반 마크다운/HTML 로 바꾼다
const MARKED_URL = 'https://cdn.jsdelivr.net/npm/marked@15.0.12/lib/marked.esm.js'
export const GITHUB_CSS_URL = 'https://cdn.jsdelivr.net/npm/github-markdown-css@5.8.1/github-markdown-light.css'

// 덱 폴더(Vite 루트)의 md 파일들. 덱 파일 이름이 정해져 있지 않아 모두 잡고, 열 때 덱 제목으로 고른다
const sources = import.meta.glob('/*.md', { query: '?raw', import: 'default' }) as Record<string, () => Promise<string>>
// 원고의 상대 경로 그림(./img/…, ./images/…)은 빌드 결과에 원래 경로로 남지 않으므로 해시된 주소로 바꿔 준다
const images = import.meta.glob('/{img,images}/**/*.{png,jpg,jpeg,gif,svg,webp,PNG,JPG,JPEG}', { query: '?url', import: 'default', eager: true }) as Record<string, string>

async function loadSource(deckTitle: string): Promise<string> {
  const entries = Object.entries(sources)
  if (!entries.length) throw new Error('원고 파일을 찾지 못했어요')
  if (entries.length === 1) return entries[0][1]()
  const texts = await Promise.all(entries.map(async ([path, load]) => ({ path, text: await load() })))
  const byTitle = deckTitle && texts.find(t => t.text.includes(`title: ${deckTitle}`))
  return (byTitle || texts.find(t => t.path === '/slides.md') || texts[0]).text
}

const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
function attrs(s: string) {
  const out: Record<string, string> = {}
  for (const m of s.matchAll(/([\w-]+)="([^"]*)"/g)) out[m[1]] = m[2]
  return out
}
const isYamlBlock = (lines: string[]) =>
  lines.some(l => l.trim()) && lines.every(l => !l.trim() || /^[A-Za-z_][\w-]*\s*:/.test(l) || /^\s+\S/.test(l) || /^\s*-\s/.test(l))

// Slidev 원고 → 일반 마크다운. 머리말·슬라이드 프런트매터는 빼고, 슬라이드 경계는 가로줄, 슬롯 표시(::right::)와 <style> 은 지운다
export function toPlainMarkdown(raw: string): string {
  const lines = raw.replace(/\r\n?/g, '\n').split('\n')
  const out: string[] = []
  let i = 0, fence = false, first = true
  while (i < lines.length) {
    const line = lines[i]
    if (/^\s*(```|~~~)/.test(line)) fence = !fence
    if (!fence && line.trim() === '---') {
      let j = i + 1
      while (j < lines.length && lines[j].trim() !== '---') j++
      const block = lines.slice(i + 1, j)
      const fm = j < lines.length && isYamlBlock(block)
      if (!first) out.push('', '<hr>', '')
      first = false
      i = fm ? j + 1 : i + 1
      continue
    }
    first = false
    out.push(line)
    i++
  }
  let md = out.join('\n')
    .replace(/<style[\s\S]*?<\/style>/g, '')
    .replace(/^::[\w-]+::\s*$/gm, '')
    .replace(/<\/b>(?=[^\s<])/g, '</b> ')   // 타임라인 · 흐름의 <b>01</b>제목 처럼 붙은 이름표를 띄어 쓴다
  // 컴포넌트(대문자로 시작하는 태그): 칩 → 코드, 타임라인·흐름·단계 → 번호 목록, 격자 → 묶음,
  //  그 밖에 tag/title 속성이 있으면 굵은 제목을 단 인용문, 없으면 인용문. 닫는 태그는 짝이 되는 여는 태그에 맞춰 닫는다(중첩 대비 스택)
  const stack: string[] = []
  md = md.replace(/<(\/?)([A-Z]\w*)\b([^>]*?)(\/?)>/g, (_m, close, name, a, self) => {
    if (close) return stack.pop() ?? ''
    const at = attrs(a), head = [at.tag, at.title].filter(Boolean).map(esc).join(' · ')
    let open: string, end: string
    if (name === 'Chip') { open = '<code>'; end = '</code>' }
    else if (/^(Timeline|Flow|Steps)$/.test(name)) { open = '<ol>'; end = '</ol>' }
    else if (name === 'Grid') { open = '<div>'; end = '</div>' }
    else if (head) { open = `<blockquote><p><strong>${head}</strong><br>`; end = '</p></blockquote>' }
    else { open = '<blockquote>'; end = '</blockquote>' }
    if (self) return head ? `<p><strong>${head}</strong></p>` : ''
    stack.push(end)
    return open
  })
  // 그림 경로: ./img/a.jpg · img/a.jpg → 빌드된 주소
  const fix = (p: string) => images['/' + p.replace(/^\.?\//, '')] ?? p
  md = md
    .replace(/(<img\b[^>]*\bsrc=")([^"]+)(")/g, (_m, a, p, b) => a + fix(p) + b)
    .replace(/(!\[[^\]]*\]\()([^)\s]+)/g, (_m, a, p) => a + fix(p))
  return md
}

let markedP: Promise<{ parse: (md: string) => string | Promise<string> }> | null = null
export async function renderManuscript(deckTitle: string): Promise<string> {
  markedP ??= import(/* @vite-ignore */ MARKED_URL).then(m => m.marked)
  const [raw, marked] = await Promise.all([loadSource(deckTitle), markedP])
  return marked.parse(toPlainMarkdown(raw))
}
