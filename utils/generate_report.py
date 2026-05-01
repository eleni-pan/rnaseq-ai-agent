import json
import markdown

def generate_report(data_dict):
    # 2. Define your Aesthetic Principles (CSS)
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: 'Helvetica Neue', sans-serif; background: #f0f2f5; padding: 40px; }}
            .card {{ background: white; border-radius: 12px; padding: 25px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-left: 8px solid #1a73e8; }}
            h2 {{ color: #1a73e8; margin-top: 0; }}
            .gene-box {{ background: #f8f9fa; border: 1px solid #e1e4e8; padding: 10px; border-radius: 6px; font-family: monospace; color: #d73a49; }}
            .text {{ margin-top: 15px; line-height: 1.6; color: #24292e; }}
        </style>
    </head>
    <body>
        <h1>Spatial Transcriptomics Analysis</h1>
        {content}
    </body>
    </html>
    """

    # 3. Assemble the pieces
    content_sections = ""
    for entry in data_dict:
        # Convert the AI's annotation to a string just in case it's a list
        annotation = entry['annotation']
        annotation_text = str(annotation[0]["text"]) if isinstance(annotation, list) else str(annotation)

        # Convert the string to HTML
        html_text = markdown.markdown(annotation_text)
        
        content_sections += f"""
        <div class="card">
            <h2>Cluster: {entry['cluster']}</h2>
            <div class="gene-box"><b>Markers:</b> {entry['genes']}</div>
            <div class="text">{html_text}</div>
        </div>
        """

    # 4. Save the Final Aesthetic Report
    with open("reports/Aesthetic_Report.html", "w") as f:
        f.write(html_template.format(content=content_sections))

    print("✨ Aesthetic Report generated! Check reports/Aesthetic_Report.html")