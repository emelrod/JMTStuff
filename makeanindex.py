import os

# Automatically anchor paths to the folder where this script is saved (Repository Root)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

THUMB_DIR = os.path.join(BASE_DIR, "thumbnails")
IMAGE_DIR = os.path.join(BASE_DIR, "images")
OUTPUT_FILE = os.path.join(BASE_DIR, "index.html")

if os.path.exists(THUMB_DIR):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    files = sorted([f for f in os.listdir(THUMB_DIR) if f.lower().endswith(valid_extensions)])
    
    print(f"Found {len(files)} images in thumbnails folder.")
    
    rows_html = ""
    for index, file in enumerate(files, start=5):
        rows_html += f"""
        <tr>
            <td>{index}</td>
            <td>
                <a href="images/{file}" target="_blank" rel="noopener">
                    <img src="thumbnails/{file}" alt="{file}" loading="lazy">
                </a>
            </td>
            <td>{file}</td>
        </tr>"""

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JMT Image Gallery</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 12px; border-bottom: 1px solid #ddd; text-align: left; vertical-align: middle; }}
        th {{ background-color: #f6f8fa; }}
        img {{ width: 150px; height: auto; border-radius: 4px; display: block; }}
        tr:hover {{ background-color: #f9f9f9; }}
    </style>
</head>
<body>
    <h2>Photo Gallery</h2>
    <p>Click any thumbnail to open the full-size image in a new tab.</p>
    <table>
        <thead>
            <tr>
                <th style="width: 60px;">#</th>
                <th style="width: 170px;">Thumbnail</th>
                <th>Filename</th>
            </tr>
        </thead>
        <tbody>{rows_html}
        </tbody>
    </table>
</body>
</html>
"""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Successfully created {OUTPUT_FILE}!")
else:
    print(f"Error: Could not find 'thumbnails' directory at: {THUMB_DIR}")
    print("Ensure this script is saved in the root directory of your JMTStuff repository.")