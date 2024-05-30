from xhtml2pdf import pisa
from io import BytesIO

class Pdf:
    def render_pdf(self, html):
        pdf = BytesIO()

        # Assurez-vous que la chaîne HTML est correctement encodée en UTF-8
        encoded_html = html.encode('utf-8')

        # Créer le PDF à partir de la chaîne HTML encodée
        pisa.CreatePDF(BytesIO(encoded_html), pdf)

        return pdf.getvalue()