import cairosvg

svg_code = '''
<svg height="100" width="200" xmlns="http://www.w3.org/2000/svg">
  <text x="10" y="50" font-size="30">Olá SVG!</text>
</svg>
'''

cairosvg.svg2pdf(bytestring=svg_code.encode('utf-8'), write_to='teste.pdf')
print("PDF gerado com sucesso!")
