from jinja2 import Template
from weasyprint import HTML
from datetime import datetime

# Data for the newsletter
top_sellers = [
    {"SKU": "Product A", "sales_value": "$1000"},
    {"SKU": "Product B", "sales_value": "$850"}
]
low_stock_alerts = [
    {"SKU": "Product X", "warehouse": "LOCAD Bekasi FC"},
    {"SKU": "Product Y", "warehouse": "LOCAD Tangerang FC"}
]
current_date = datetime.now().strftime("%d/%m/%Y")

# Load the HTML template
with open("/Users/KuyaBani/code/CapybaraFirst/newsletter_template.html", "r") as template_file:
    html_template = template_file.read()

# Render the HTML with dynamic data
template = Template(html_template)
html_content = template.render(date=current_date, top_sellers=top_sellers, low_stock_alerts=low_stock_alerts)

# Save the rendered HTML
with open("newsletter.html", "w") as f:
    f.write(html_content)

# Convert HTML to PDF
HTML("newsletter.html").write_pdf("newsletter.pdf")

print("Newsletter PDF generated successfully!")
