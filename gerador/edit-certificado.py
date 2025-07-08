import pandas as pd
import os
import base64
import cairosvg  # converter SVG para PDF

# === Função para gerar o certificado a partir do template SVG ===
def gerar_certificado_svg(nome, template_path="certificado_template.svg", output_dir="certificados"):
    os.makedirs(output_dir, exist_ok=True)

    with open(template_path, "r", encoding="utf-8") as f:
        svg_template = f.read()

    # Substituir as tags do SVG
    svg_personalizado = (
        svg_template.replace("<<nome>>", nome)
    )

    # Gerar caminho do arquivo PDF
    nome_arquivo = f"{nome.replace(' ', '_')}.pdf"
    caminho_pdf = os.path.join(output_dir, nome_arquivo)

    # Converter SVG para PDF
    cairosvg.svg2pdf(bytestring=svg_personalizado.encode("utf-8"), write_to=caminho_pdf)
    return caminho_pdf



# === Execução principal com CrewAI ===
if __name__ == "__main__":
    nome="Antonio Carlos da Silva"
    gerar_certificado_svg(nome)
    
