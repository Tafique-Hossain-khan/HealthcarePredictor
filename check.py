import os

# Create this script in your project root and run it
def check_files():
    # Check templates folder
    if os.path.exists('templates'):
        print("✅ templates folder exists")
        template_files = os.listdir('templates')
        print(f"Templates found: {template_files}")
    else:
        print("❌ templates folder not found")

    # Check static folder
    if os.path.exists('static/css'):
        print("✅ static/css folder exists")
        css_files = os.listdir('static/css')
        print(f"CSS files found: {css_files}")
    else:
        print("❌ static/css folder not found")

check_files()
