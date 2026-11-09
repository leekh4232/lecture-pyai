// 빌드(HTML 내보내기) 전용 Vite 설정. 테마는 npm 패키지를 import 하지 않는다(경로로 열 때 못 찾는다) → Node 내장 모듈만 쓴다.
import { readFileSync } from 'node:fs'

const IMG = /\.(png|jpe?g|gif|webp|svg)$/i
const MIME = { png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', gif: 'image/gif', webp: 'image/webp', svg: 'image/svg+xml' }

export default {
  // 그림을 파일로 떼어 내지 않고 데이터 URI 로 묻는다 → 내보낸 HTML 을 이미지 파일 없이 옮겨도 그림이 보인다.
  build: { assetsInlineLimit: 100 * 1024 * 1024 },
  plugins: [{
    name: 'hossam-inline-images',
    apply: 'build',
    enforce: 'pre',
    load(id) {
      const file = id.split('?')[0]
      const m = file.match(IMG)
      if (!m || file.includes('/node_modules/')) return
      const ext = m[1].toLowerCase()
      return `export default ${JSON.stringify(`data:${MIME[ext]};base64,${readFileSync(file).toString('base64')}`)}`
    },
  }],
}
