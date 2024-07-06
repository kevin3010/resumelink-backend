import fitz

def read_pdf(content_stream):
    
   
    pdf_document = fitz.open(stream=content_stream, filetype="pdf")
    
    pdf_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pdf_text += page.get_text()
        
    pdf_document.close()
    
    return pdf_text