import os
import re
import subprocess
import markdown

SOURCE_MD = r"C:\Users\saksh\OneDrive\Documents\CodeCommentGenerator\REPORT_EXPANSION_SECTIONS.md"
TARGET_HTML = r"C:\Users\saksh\OneDrive\Documents\CodeCommentGenerator\SafeDocGen_Report_Expansion.html"
TARGET_PDF = r"C:\Users\saksh\OneDrive\Documents\CodeCommentGenerator\SafeDocGen_Report_Expansion.pdf"
DOWNLOADS_PDF = r"C:\Users\saksh\Downloads\SafeDocGen_Report_Expansion.pdf"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

with open(SOURCE_MD, "r", encoding="utf-8") as f:
    raw_md = f.read()

# Replace mermaid code blocks with <div class="mermaid">
def replace_mermaid(match):
    code = match.group(1).strip()
    return f'<div class="mermaid">\n{code}\n</div>'

processed_md = re.sub(r'```mermaid\s*\n(.*?)\n```', replace_mermaid, raw_md, flags=re.DOTALL)

# Convert markdown to HTML
html_body = markdown.markdown(
    processed_md,
    extensions=['tables', 'fenced_code']
)

# Custom post-processing for badges in tables
html_body = re.sub(r'<td>\s*\*\*Critical\*\*\s*</td>', '<td><span class="badge badge-critical">Critical</span></td>', html_body)
html_body = re.sub(r'<td>\s*\*\*High\*\*\s*</td>', '<td><span class="badge badge-high">High</span></td>', html_body)
html_body = re.sub(r'<td>\s*\*\*Medium\*\*\s*</td>', '<td><span class="badge badge-medium">Medium</span></td>', html_body)
html_body = re.sub(r'<td>\s*\*\*Low\*\*\s*</td>', '<td><span class="badge badge-low">Low</span></td>', html_body)
html_body = re.sub(r'<td>\s*\*\*BLOCK\*\*\s*</td>', '<td><span class="badge badge-block">BLOCK</span></td>', html_body)
html_body = re.sub(r'<td>\s*\*\*SANITIZE\*\*\s*</td>', '<td><span class="badge badge-sanitize">SANITIZE</span></td>', html_body)

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SafeDocGen: Academic Report Expansion</title>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'neutral',
      flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: 'basis' }}
    }});
  </script>
  <style>
    @page {{
      size: A4;
      margin: 18mm 16mm 18mm 16mm;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-size: 10.5pt;
      line-height: 1.55;
      color: #1f2937;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }}
    .header-box {{
      border-bottom: 2px solid #2563eb;
      padding-bottom: 12px;
      margin-bottom: 24px;
    }}
    h1 {{
      font-size: 19pt;
      font-weight: 800;
      color: #1e3a8a;
      margin: 0 0 8px 0;
      letter-spacing: -0.02em;
    }}
    .metadata {{
      font-size: 9.5pt;
      color: #4b5563;
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-top: 6px;
    }}
    .metadata span {{
      display: inline-block;
    }}
    .metadata strong {{
      color: #111827;
    }}
    h2 {{
      font-size: 13.5pt;
      font-weight: 700;
      color: #1e40af;
      border-bottom: 1px solid #e5e7eb;
      padding-bottom: 5px;
      margin-top: 28px;
      margin-bottom: 12px;
      page-break-after: avoid;
    }}
    h3 {{
      font-size: 11.5pt;
      font-weight: 700;
      color: #1f2937;
      margin-top: 18px;
      margin-bottom: 8px;
      page-break-after: avoid;
    }}
    h4 {{
      font-size: 10.5pt;
      font-weight: 600;
      color: #374151;
      margin-top: 14px;
      margin-bottom: 6px;
      page-break-after: avoid;
    }}
    p {{
      margin: 0 0 10px 0;
      text-align: justify;
    }}
    ul, ol {{
      margin: 0 0 12px 0;
      padding-left: 22px;
    }}
    li {{
      margin-bottom: 4px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0 18px 0;
      font-size: 9pt;
      page-break-inside: auto;
    }}
    tr {{
      page-break-inside: avoid;
      page-break-after: auto;
    }}
    thead tr {{
      background-color: #f1f5f9;
      border-top: 1px solid #cbd5e1;
      border-bottom: 2px solid #94a3b8;
    }}
    th {{
      font-weight: 700;
      text-align: left;
      padding: 7px 8px;
      color: #0f172a;
    }}
    td {{
      padding: 6px 8px;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: top;
    }}
    tbody tr:nth-child(even) {{
      background-color: #f8fafc;
    }}
    code {{
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 9pt;
      background-color: #f1f5f9;
      color: #0f172a;
      padding: 1px 4px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }}
    pre {{
      background-color: #0f172a;
      color: #f8fafc;
      padding: 10px 14px;
      border-radius: 6px;
      overflow-x: auto;
      font-size: 8.5pt;
      line-height: 1.45;
      margin: 10px 0 14px 0;
      page-break-inside: avoid;
    }}
    pre code {{
      background: none;
      color: inherit;
      padding: 0;
      border: none;
      font-size: inherit;
    }}
    .badge {{
      display: inline-block;
      font-size: 7.5pt;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }}
    .badge-critical {{ background: #fee2e2; color: #991b1b; border: 1px solid #f87171; }}
    .badge-high {{ background: #ffedd5; color: #9a3412; border: 1px solid #fb923c; }}
    .badge-medium {{ background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }}
    .badge-low {{ background: #e0f2fe; color: #075985; border: 1px solid #7dd3fc; }}
    .badge-block {{ background: #fee2e2; color: #b91c1c; font-weight: 800; border: 1px solid #ef4444; }}
    .badge-sanitize {{ background: #fef9c3; color: #854d0e; font-weight: 800; border: 1px solid #eab308; }}
    .mermaid {{
      text-align: center;
      margin: 16px 0;
      page-break-inside: avoid;
    }}
    blockquote {{
      margin: 10px 0;
      padding: 8px 14px;
      background: #eff6ff;
      border-left: 4px solid #3b82f6;
      color: #1e40af;
      font-size: 9.5pt;
    }}
  </style>
</head>
<body>
  {html_body}
</body>
</html>
"""

with open(TARGET_HTML, "w", encoding="utf-8") as f:
    f.write(full_html)

print("HTML written:", TARGET_HTML)

# Run Chrome Headless to produce PDF
cmd = [
    CHROME_PATH,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--virtual-time-budget=6000",
    f"--print-to-pdf={TARGET_PDF}",
    TARGET_HTML
]
print("Generating PDF via Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(TARGET_PDF):
    size_kb = os.path.getsize(TARGET_PDF) / 1024
    print(f"SUCCESS: Generated PDF ({size_kb:.1f} KB) at: {TARGET_PDF}")
    
    # Also copy to Downloads for user convenience
    import shutil
    shutil.copyfile(TARGET_PDF, DOWNLOADS_PDF)
    print(f"COPIED to Downloads: {DOWNLOADS_PDF}")
else:
    print("ERROR: PDF was not created. Stderr:", res.stderr)
