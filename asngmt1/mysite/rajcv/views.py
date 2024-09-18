from django.shortcuts import render, redirect
from .forms import ResumeForm
import fitz


def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            pdf_file = resume.pdf.path

            # Convert PDF to HTML
            html_content = convert_pdf_to_html(pdf_file)

            return render(request, 'rajcv/resume_preview.html', {'html_content': html_content})
    else:
        form = ResumeForm()

    return render(request, 'rajcv/upload_resume.html', {'form': form})

def convert_pdf_to_html(pdf_file):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)
    html_content = ""

    # Iterate through each page and convert to HTML
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("html")
        html_content += text

    pdf_document.close()
    return html_content