"""Turn web/index.html (the claude.ai artifact page) into the app's offline page.
Swaps Google Fonts for the bundled fonts and wraps it in a full HTML document.
Run from the repo root:  python3 tools/make_app_html.py"""
import re
src = open('web/index.html', encoding='utf-8').read()
src = re.sub(r'<link rel="preconnect"[^>]*>\n', '', src)
src = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>\n', '', src)
faces = [('Sora', w, f'fonts/sora-latin-{w}-normal.woff2') for w in (300, 400, 500, 600)] + \
        [('Figtree', w, f'fonts/figtree-latin-{w}-normal.woff2') for w in (400, 500, 600)]
css = '\n'.join(f'@font-face{{font-family:"{f}";font-style:normal;font-weight:{w};font-display:swap;src:url("{u}") format("woff2")}}' for f, w, u in faces)
src = src.replace('<style>\n', '<style>\n' + css + '\n', 1)
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">
<meta name="theme-color" content="#000000">
<style>html,body{margin:0}body{-webkit-user-select:none;user-select:none}</style>
'''
i = src.index('</style>') + len('</style>')
doc = head + src[:i] + '\n</head>\n<body>\n' + src[i:] + '\n</body>\n</html>\n'
open('app/src/main/assets/index.html', 'w', encoding='utf-8').write(doc)
print('wrote app/src/main/assets/index.html')
