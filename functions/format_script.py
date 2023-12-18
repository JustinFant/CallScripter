from docx import Document
from io import BytesIO
from docx2pdf import convert


def format_script(greeting, recruiter_name, recruiter_email, recruiter_phone, candidate_name, application_location, pay_rate, contract_length, client_name, work_location) -> BytesIO:
  script = Document("helpers/call_script.docx")
  
  replacements = {
        'greeting': greeting,
        'recruiter_name': recruiter_name,
        'recruiter_email': recruiter_email,
        'recruiter_phone': recruiter_phone,
        'candidate_name': candidate_name,
        'application_location': application_location,
        'pay_rate': str(pay_rate),
        'contract_length': str(contract_length),
        'client_name': client_name,
        'work_location': work_location
        }
  
  for paragraph in script.paragraphs:
    for run in paragraph.runs:
      for key, value in replacements.items():
        if key in run.text:
          run.text = run.text.replace(key, value)
          break

  script.save("outputs/formatted_call_script.docx") # Save Formatted Script
  convert("outputs/formatted_call_script.docx") # Convert to PDF

  with open("outputs/formatted_call_script.pdf", "rb") as f:
    script = f.read()

  byto_io = BytesIO(script) # Convert to BytesIO Object for Download
  byto_io.seek(0)

  return byto_io