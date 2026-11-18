#!/usr/bin/env python3
"""Build index.html (deployable, standalone) from source/portfolio.html.
Usage:  python3 build.py
Edit LINKS / PRICING at the top of the <script> in source/portfolio.html, then run this again."""
import os,sys
here=os.path.dirname(os.path.abspath(__file__))
src=os.path.join(here,'source','portfolio.html')
out=os.path.join(here,'index.html')
s=open(src,encoding='utf-8').read()
start=s.index('<a class="skip"')
head=s[:s.index('<style>')].replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
TITLE='Phạm Văn Nhơn | Mobile, Web & Full-stack Developer'
DESC='Phạm Văn Nhơn, lập trình viên mobile, web và full-stack: React Native, Flutter, Next.js, WordPress, NestJS. Nhận app, landing page, website WordPress và trang quản trị.'
FAV="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23070B18'/%3E%3Ctext x='32' y='43' text-anchor='middle' font-family='Arial' font-weight='800' font-size='30' fill='%23FF6B8B'%3En.%3C/text%3E%3C/svg%3E"
head=head.replace('<title>Phạm Văn Nhơn Portfolio</title>','<title>%s</title>'%TITLE)
meta=('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
 '<meta name="description" content="%s">\n<meta name="theme-color" content="#070B18">\n'
 '<meta property="og:type" content="website">\n<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n'
 '<link rel="icon" href="%s">\n')%(DESC,TITLE,DESC,FAV)
css=s[s.index('<style>'):start]
out_html=meta+head[head.index('<title>'):]+css+'</head>\n<body>\n'+s[start:]+'\n</body>\n</html>\n'
open(out,'w',encoding='utf-8').write(out_html)
print('built',out,len(out_html),'bytes')
