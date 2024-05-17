import os


def generate_index_html(css_file: str, js_file: str):
    html = f"""
    <!DOCTYPE html>
    <html lang="nl">
    <head>
    <title>Curriculum Vitae Kristien Dauwe</title>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta name="author" content="Kristien Dauwe"/>
    <link rel="stylesheet" href="{css_file}">
    <script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4=" crossorigin="anonymous"></script>
    <script src="{js_file}"></script>
    </head>
    <body>
    <div class="page">
    <header>
    <h1>Een kleine kennismaking</h1>
    <h2>Klik op de cirkels voor details</h2>
    </header>
    <div class="circles-container">
    <div class="circle" id="hobby"><span>Hobby's</span></div>
    <div class="circle" id="werkervaring"><span>Werkervaring</span></div>
    <div class="circle" id="opleiding"><span>Opleiding</span></div>
    </div>
    <div id="data_container"></div>
    </div>
    </body>
    </html>
    """
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'index.html')
    with open(file_path, 'w') as f:
        f.write(html)