import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'

OLD = '<p>&copy; 2025 Danny McVey. All rights reserved.</p>'
NEW = '<p>&copy; <span id="copyright-year"></span> Danny McVey. All rights reserved.</p>'

changed = 0
for p in DOCS.rglob('*.html'):
    txt = p.read_text(encoding='utf-8')
    if OLD in txt:
        p.write_text(txt.replace(OLD, NEW), encoding='utf-8')
        changed += 1

print(f"updated {changed} file(s)")
