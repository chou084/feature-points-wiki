"""渲染檢查：內容是否超出投影片、是否壓到頁尾、公式是否有渲染。
用法：python tools/check_render.py [輸出截圖資料夾]"""
import sys, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
url = (ROOT / "docs/slides/index.html").as_uri()
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
JS = """(i)=>{
  const st=document.getElementById('stage'); st.style.transform='none';
  const s=document.querySelectorAll('.slide')[i]; const r=s.getBoundingClientRect();
  const foot=s.querySelector('.foot').getBoundingClientRect();
  const bad=[];
  for(const el of s.querySelectorAll('*')){
    if(el.closest('.foot')||el.closest('svg')&&el.tagName!=='svg') continue;
    const b=el.getBoundingClientRect(); if(!b.width&&!b.height) continue;
    const name=el.tagName.toLowerCase()+(el.className&&typeof el.className==='string'?'.'+el.className.split(' ')[0]:'');
    if(b.right>r.right+1||b.left<r.left-1) bad.push('水平超出 '+name+' '+Math.round(b.right-r.right)+'px');
    if(b.bottom>foot.top-4) bad.push('壓到頁尾 '+name+' 超出 '+Math.round(b.bottom-foot.top+4)+'px：'+(el.textContent||'').trim().slice(0,18));
    if(el.scrollWidth>el.clientWidth+2 && getComputedStyle(el).overflowX!=='visible' && el.clientWidth>0) bad.push('內部捲動 '+name);
  }
  const maths=[...s.querySelectorAll('math')].map(m=>m.getBoundingClientRect());
  const mathBad=maths.filter(b=>b.width<5||b.height<5).length;
  if(mathBad) bad.push('公式未渲染 '+mathBad+' 個');
  return {n:bad.length?[...new Set(bad)]:[], maths:maths.length};
}"""
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 800})
    pg.goto(url); pg.wait_for_timeout(300)
    total = pg.eval_on_selector_all(".slide", "e=>e.length")
    issues = 0; maths = 0
    for i in range(total):
        pg.evaluate(f"location.hash='#s{i+1}'"); pg.wait_for_timeout(120)
        res = pg.evaluate(JS, i); maths += res["maths"]
        for x in res["n"]:
            print(f" - [第 {i+1} 張] {x}"); issues += 1
    # 各種螢幕：投影片必須完整落在可視範圍內、不被導覽列蓋住
    for vw, vh, name in [(1280, 800, "桌面"), (1920, 1080, "大螢幕"), (390, 844, "手機直式"), (844, 390, "手機橫式")]:
        q = b.new_page(viewport={"width": vw, "height": vh}, is_mobile=vw < 900, has_touch=vw < 900)
        q.goto(url + "#s6"); q.wait_for_timeout(300)
        r = q.evaluate("""()=>{const s=document.getElementById('stage').getBoundingClientRect();
          const c=document.getElementById('chrome').getBoundingClientRect();
          return {x:s.x,y:s.y,r:s.right,b:s.bottom,ct:c.top,w:innerWidth,h:innerHeight}}""")
        if r["x"] < -1 or r["r"] > r["w"] + 1 or r["y"] < -1 or r["b"] > r["ct"] + 1:
            print(f" - [{name} {vw}×{vh}] 投影片超出可視範圍或被導覽列蓋住：{ {k: round(v) for k, v in r.items()} }"); issues += 1
        q.close()
    print(f"渲染檢查 {total} 張、{maths} 個公式、4 種螢幕，發現 {issues} 個問題")
    if out:
        out.mkdir(parents=True, exist_ok=True)
        for scheme in ("light", "dark"):
            pg2 = b.new_page(viewport={"width": 1280, "height": 780}, color_scheme=scheme)
            pg2.goto(url)
            for i in range(total):
                pg2.evaluate(f"location.hash='#s{i+1}'"); pg2.wait_for_timeout(500)  # 等淡入動畫結束
                pg2.screenshot(path=str(out / f"{scheme}-{i+1:02d}.png"))
        m = b.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
        m.goto(url + "#s6"); m.wait_for_timeout(600); m.screenshot(path=str(out / "mobile-06.png"))
    b.close()
    sys.exit(1 if issues else 0)
