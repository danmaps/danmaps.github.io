import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'

SNIPPET = """<script>
  (function(){
    var el = document.getElementById('copyright-year');
    if (el) el.textContent = new Date().getFullYear();
  })();
</script>
"""

changed = 0
for p in DOCS.rglob('*.html'):
    txt = p.read_text(encoding='utf-8')
    if 'id="copyright-year"' not in txt:
        continue
    if 'document.getElementById(\'copyright-year\')' in txt or 'document.getElementById("copyright-year")' in txt:
        continue
    if '</body>' not in txt:
        continue
    txt2 = txt.replace('</body>', SNIPPET + '\n</body>')
    p.write_text(txt2, encoding='utf-8')
    changed += 1

print(f"injected script into {changed} file(s)")
