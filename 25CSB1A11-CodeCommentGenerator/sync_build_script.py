with open(r"C:\Users\saksh\OneDrive\Documents\CodeCommentGenerator\SafeDocGen_Expanded_Final_Report.html", "r", encoding="utf-8") as f:
    final_html = f.read()

template_code = f'''import os
import subprocess
import shutil

OUTPUT_HTML = r"C:\\Users\\saksh\\OneDrive\\Documents\\CodeCommentGenerator\\SafeDocGen_Expanded_Final_Report.html"
OUTPUT_PDF = r"C:\\Users\\saksh\\OneDrive\\Documents\\CodeCommentGenerator\\SafeDocGen_Expanded_Final_Report.pdf"
DOWNLOADS_PDF = r"C:\\Users\\saksh\\Downloads\\SafeDocGen_Expanded_Final_Report.pdf"
ARTIFACT_PDF = r"C:\\Users\\saksh\\.gemini\\antigravity\\brain\\3cc6960f-b4ca-4e93-bd73-1c5068f4132b\\SafeDocGen_Expanded_Final_Report.pdf"
CHROME_PATH = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Full expanded HTML with high-resolution authentic embedded figures
html_code = """{final_html}"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Generated HTML:", OUTPUT_HTML)

# Run Chrome Headless to compile into PDF
cmd = [
    CHROME_PATH,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--virtual-time-budget=8000",
    f"--print-to-pdf={{OUTPUT_PDF}}",
    OUTPUT_HTML
]
print("Compiling PDF via Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(OUTPUT_PDF):
    shutil.copyfile(OUTPUT_PDF, DOWNLOADS_PDF)
    shutil.copyfile(OUTPUT_PDF, ARTIFACT_PDF)
    size_kb = os.path.getsize(OUTPUT_PDF) / 1024
    print(f"SUCCESS: Generated PDF ({{size_kb:.1f}} KB) at: {{OUTPUT_PDF}}")
    print(f"COPIED to Downloads: {{DOWNLOADS_PDF}}")
    print(f"COPIED to Artifacts: {{ARTIFACT_PDF}}")
else:
    print("ERROR:", res.stderr)
'''

with open(r"C:\Users\saksh\OneDrive\Documents\CodeCommentGenerator\build_expanded_report.py", "w", encoding="utf-8") as f:
    f.write(template_code)

print("build_expanded_report.py updated successfully.")
