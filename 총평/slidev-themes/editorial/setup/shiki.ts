// 흰 슬라이드 위의 어두운 코드 상자에 잘 보이도록 고대비 테마를 쓴다(주석도 밝은 회색).
// defineShikiSetup(@slidev/types)은 받은 함수를 그대로 돌려줄 뿐이라 쓰지 않는다.
// 쓰면 테마 폴더를 경로(theme: ./editorial)로 열 때 그 패키지를 찾지 못해 실행이 멈춘다.
import { existsSync, realpathSync } from 'node:fs'
import { createRequire } from 'node:module'
import { delimiter, join } from 'node:path'
import { pathToFileURL } from 'node:url'

// 프롬프트 상자(````md) 안의 ```python 은 python 문법이 먼저 불려 와 있을 때만 칠해진다(빌드마다 들쭉날쭉).
// markdown 을 불러올 때 python 을 함께 불러오게 한다. 'shiki' 를 바로 import 하면 테마 폴더에서 못 찾으므로
// slidev 가 설치된 곳에서 문법 파일을 찾는다. 후보를 차례로 시도하고 전부 실패하면 기본 동작(python 색칠 없음)으로 둔다.
// - SLIDEV_CLI_PATH: 확장(Open with Slidev)이 빌드할 때 넘기는 @slidev/cli 패키지 폴더
// - argv[1] 의 실제 경로: 전역 slidev 는 심볼릭 링크라 링크 경로에서는 못 찾는다
// - 현재 폴더: 프로젝트에 slidev 를 설치한 경우
// - 전역 node_modules(npm root -g 자리): slidev 밖의 스크립트로 띄웠는데 환경 변수도 없는 경우. PATH 에서 node 가 있는 폴더를 찾아
//   그 옆(macOS · Linux 는 ../lib/node_modules, Windows 는 같은 폴더의 node_modules)을 본다. execPath 는 Homebrew 에서 Cellar 를 가리켜 못 쓴다
// 찾기(resolve)는 여기서 바로 한다. 나중에 실행되는 함수 안에서 하면 try/catch 가 못 잡아 빌드 전체가 멈춘다.
function markdownWithPython() {
  const anchors = [
    () => join(process.env.SLIDEV_CLI_PATH || '', 'package.json'),
    () => realpathSync(process.argv[1]),
    () => join(process.cwd(), 'package.json'),
    ...(process.env.PATH || '').split(delimiter)
      .filter(d => d && (existsSync(join(d, 'node')) || existsSync(join(d, 'node.exe'))))
      .flatMap(d => [join(d, '..', 'lib', 'node_modules'), join(d, 'node_modules')])
      .map(root => () => join(root, '@slidev', 'cli', 'package.json')),
  ]
  for (const anchor of anchors) {
    try {
      const req = createRequire(anchor())
      const python = req.resolve('@shikijs/langs/python')
      const md = req.resolve('@shikijs/langs/markdown')
      const load = (file: string) => import(pathToFileURL(file).href).then(m => m.default)
      const markdown = async () => ({ default: [...await load(python), ...await load(md)] })
      return { markdown, md: markdown }
    }
    catch {}
  }
  return undefined
}

export default () => ({
  themes: { dark: 'github-dark-high-contrast', light: 'github-dark-high-contrast' },
  langs: markdownWithPython(),
})
