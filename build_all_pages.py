import os
import re

src_dir = r"D:\Desktop\Admin-Integration\My Web"
out_dir = r"D:\Desktop\zain-portfolio\demos\admin-panel"

templates_dir = os.path.join(src_dir, "Templates")

with open(os.path.join(templates_dir, "header.html"), "r", encoding="utf-8", errors="ignore") as f:
    header_base = f.read()

with open(os.path.join(templates_dir, "footer.html"), "r", encoding="utf-8", errors="ignore") as f:
    footer_base = f.read()

# Map of (template_filename, output_filename, active_route)
pages = [
    ("index.html", "index.html", "/"),
    ("Orders.html", "orders.html", "/orders"),
    ("New-Order.html", "new-order.html", "/new-order"),
    ("Products.html", "products.html", "/products"),
    ("add-products.html", "add-products.html", "/add-products"),
    ("Categories.html", "categories.html", "/categories"),
    ("add-categories.html", "add-categories.html", "/add-categories"),
    ("Customers.html", "customers.html", "/customers"),
    ("add-customers.html", "add-customers.html", "/add-customers"),
    ("staff.html", "staff.html", "/staff"),
    ("add-staff.html", "add-staff.html", "/add-staff"),
    ("Stock-Alerts.html", "stock-alerts.html", "/stock-alerts"),
    ("add-inventory-item.html", "add-inventory-item.html", "/add-inventory"),
    ("Suppliers.html", "suppliers.html", "/modals"),
    ("add-supplier.html", "add-supplier.html", "/add-modals"),
    ("Reports.html", "reports.html", "/blank"),
    ("Profile.html", "profile.html", "/profile"),
    ("setting.html", "settings.html", "/settings"),
    ("login.html", "login.html", "/login"),
    ("register.html", "register.html", "/register"),
    ("forgot-password.html", "forgot-password.html", "/forget"),
]

# URL replacements
url_replacements = [
    (r'href="/"', 'href="index.html"'),
    (r'href="/orders"', 'href="orders.html"'),
    (r'href="/new-order"', 'href="new-order.html"'),
    (r'href="/products"', 'href="products.html"'),
    (r'href="/add-products"', 'href="add-products.html"'),
    (r'href="/categories"', 'href="categories.html"'),
    (r'href="/add-categories"', 'href="add-categories.html"'),
    (r'href="/customers"', 'href="customers.html"'),
    (r'href="/add-customer"', 'href="add-customers.html"'),
    (r'href="/staff"', 'href="staff.html"'),
    (r'href="/add-staff"', 'href="add-staff.html"'),
    (r'href="/stock-alerts"', 'href="stock-alerts.html"'),
    (r'href="/add-inventory"', 'href="add-inventory-item.html"'),
    (r'href="/modals"', 'href="suppliers.html"'),
    (r'href="/add-modals"', 'href="add-supplier.html"'),
    (r'href="/blank"', 'href="reports.html"'),
    (r'href="/profile"', 'href="profile.html"'),
    (r'href="/settings"', 'href="settings.html"'),
    (r'href="/login"', 'href="login.html"'),
    (r'href="/register"', 'href="register.html"'),
    (r'href="/forget"', 'href="forgot-password.html"'),
]

top_banner = """
<div style="background:#0f4c75; color:#ffffff; padding:10px 20px; font-family:'Plus Jakarta Sans',sans-serif; font-size:14px; display:flex; justify-content:space-between; align-items:center; position:sticky; top:0; z-index:999999; box-shadow:0 2px 10px rgba(0,0,0,0.3);">
    <span><i class="bi bi-shield-check" style="margin-right:6px;"></i><strong>adminZQ</strong> &mdash; Restaurant Command Center &amp; Management Suite (Zain Qazi)</span>
    <a href="https://zainqazi.netlify.app#projects" style="color:#ffffff; text-decoration:none; background:rgba(255,255,255,0.2); padding:6px 16px; border-radius:6px; font-weight:600; transition:all 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.35)'" onmouseout="this.style.background='rgba(255,255,255,0.2)'">&larr; Back to Portfolio</a>
</div>
"""

def clean_jinja_static(text):
    return re.sub(r"\{\{\s*url_for\(\s*['\"]static['\"]\s*,\s*filename\s*=\s*['\"]([^'\"]+)['\"]\s*\)\s*\}\}", r"static/\1", text)

def apply_routes(text):
    for pattern, target in url_replacements:
        text = text.replace(pattern, target)
    return text

for tpl_name, out_name, active_route in pages:
    tpl_path = os.path.join(templates_dir, tpl_name)
    if not os.path.exists(tpl_path):
        print(f"Skipping {tpl_name}, not found.")
        continue

    with open(tpl_path, "r", encoding="utf-8", errors="ignore") as f:
        body = f.read()

    # Check if page already has its own <html> / <head> (e.g. login/register)
    has_full_html = "<!DOCTYPE" in body or "<html" in body

    if has_full_html:
        page_html = clean_jinja_static(body)
        page_html = apply_routes(page_html)
        if "<body>" in page_html:
            page_html = page_html.replace("<body>", "<body>\n" + top_banner)
    else:
        # Page uses header/footer include
        # Set active class on the corresponding nav item in header
        curr_header = header_base
        # Remove any existing active
        curr_header = curr_header.replace('class="azq-nav-link active"', 'class="azq-nav-link"')
        # Set active on matching route
        curr_header = curr_header.replace(f'href="{active_route}" class="azq-nav-link"', f'href="{active_route}" class="azq-nav-link active"')

        # Clean includes
        body_clean = re.sub(r"\{%\s*include\s*[^%]+%\}", "", body)

        page_html = curr_header + "\n" + body_clean + "\n" + footer_base
        page_html = clean_jinja_static(page_html)
        page_html = apply_routes(page_html)
        page_html = page_html.replace("<body>", "<body>\n" + top_banner)

    out_file = os.path.join(out_dir, out_name)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(page_html)

    print(f"Compiled: {tpl_name} -> {out_name}")

print("\nAll admin pages compiled successfully!")
