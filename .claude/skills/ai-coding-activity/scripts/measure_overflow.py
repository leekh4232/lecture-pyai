"""덱의 지정한 쪽만 넘침을 재고 화면을 캡처한다. 사용자가 넘침 해결을 요청했을 때만 쓴다.

사용: python3 measure_overflow.py <덱.md> <쪽 번호(쉼표)> <캡처를 둘 폴더>
- slidev 개발 서버를 3188 포트로 잠깐 띄웠다가 끈다(사용자가 띄워 둔 서버는 건드리지 않음)
- 출력의 tag 가 '넘침 없음'이면 통과. kids 는 쪽 안 블록별 아래쪽 좌표(720 이 화면 끝)
- playwright(파이썬)와 chromium 이 필요하다
"""
import sys,time,urllib.request,subprocess
from playwright.sync_api import sync_playwright
deck,pages,shot=sys.argv[1],sys.argv[2].split(','),sys.argv[3]
proc=subprocess.Popen(["npx","slidev",deck,"--port","3188"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
try:
    for _ in range(90):
        try: urllib.request.urlopen("http://localhost:3188/",timeout=2); break
        except Exception: time.sleep(1)
    JS="""()=>{const pg=[...document.querySelectorAll('#slide-content .slidev-page')].find(e=>getComputedStyle(e).display!=='none');const box=pg.getBoundingClientRect();const sc=box.width/1280;const lay=pg.querySelector('.slidev-layout');return {tag:document.querySelector('.over-tag')?.innerText||'넘침 없음',kids:[...lay.children].map(e=>e.tagName+'.'+(e.className||'').toString().slice(0,14)+' '+Math.round((e.getBoundingClientRect().bottom-box.top)/sc))}}"""
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080})
        for n in pages:
            pg.goto(f"http://localhost:3188/{n}",wait_until="load"); time.sleep(4)
            print(n,pg.evaluate(JS)); pg.screenshot(path=f"{shot}/p{n}.png")
        b.close()
finally:
    proc.terminate()
    subprocess.run(["pkill","-f","port 3188"])
