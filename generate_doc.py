import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_callout(doc, text, title="PRO-TIP / CRITICAL NOTE", border_color="008060", bg_color="F0FDF4"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    
    cell = tbl.cell(0, 0)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border styling
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single')
    left.set(qn('w:sz'), '24')
    left.set(qn('w:space'), '0')
    left.set(qn('w:color'), border_color)
    tcBorders.append(left)
    
    for side in ['top', 'bottom', 'right']:
        edge = OxmlElement(f'w:{side}')
        edge.set(qn('w:val'), 'none')
        tcBorders.append(edge)
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run_title = p.add_run(f"[{title}] ")
    run_title.bold = True
    run_title.font.name = 'Segoe UI'
    run_title.font.size = Pt(10)
    run_title.font.color.rgb = RGBColor(0x00, 0x80, 0x60) if border_color == "008060" else RGBColor(0xDC, 0x26, 0x26)
    
    run_text = p.add_run(text)
    run_text.font.name = 'Segoe UI'
    run_text.font.size = Pt(9.5)
    run_text.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "1E293B")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.1
    run = p.add_run(code_text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0xF1, 0xF5, 0xF9)

def build_docx(filename):
    doc = docx.Document()
    
    # Page Margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Segoe UI'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0x24, 0x24, 0x24)
    normal_style.paragraph_format.line_spacing = 1.2
    normal_style.paragraph_format.space_after = Pt(6)

    # Document Header / Badge
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(4)
    run_badge = p_meta.add_run("OFFICIAL STEP-BY-STEP SOP | CODING WITH JAN TUTORIAL EXACT TRANSCRIPT")
    run_badge.font.size = Pt(8.5)
    run_badge.bold = True
    run_badge.font.color.rgb = RGBColor(0x00, 0x80, 0x60)

    # Document Title
    h1 = doc.add_heading(level=1)
    h1.paragraph_format.space_before = Pt(0)
    h1.paragraph_format.space_after = Pt(4)
    run_h1 = h1.add_run("Shopify Admin API Access Token 2026")
    run_h1.font.name = 'Segoe UI'
    run_h1.font.size = Pt(22)
    run_h1.bold = True
    run_h1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(14)
    run_sub = p_sub.add_run("How to get an Admin API Access Token via Shopify Dev Dashboard + Manual OAuth Flow + Postman")
    run_sub.font.size = Pt(12)
    run_sub.italic = True
    run_sub.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    # Reference Box
    ref_table = doc.add_table(rows=2, cols=2)
    ref_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    ref_table.columns[0].width = Inches(2.0)
    ref_table.columns[1].width = Inches(4.5)
    
    meta_rows = [
        ("Source Video", "Coding with Jan - Shopify Developer (YouTube)"),
        ("Video URL", "https://youtu.be/8dymQjcylv8")
    ]
    for i, (k, v) in enumerate(meta_rows):
        r = ref_table.rows[i]
        c0 = r.cells[0]
        c1 = r.cells[1]
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "F8FAFC")
        p0 = c0.paragraphs[0]
        p0.add_run(k).bold = True
        p0.runs[0].font.size = Pt(9)
        p1 = c1.paragraphs[0]
        p1.add_run(v)
        p1.runs[0].font.size = Pt(9)
        p1.runs[0].font.color.rgb = RGBColor(0x25, 0x63, 0xEB) if "http" in v else RGBColor(0x1E, 0x29, 0x3B)
    
    doc.add_paragraph()

    # Introduction
    p_intro = doc.add_paragraph()
    p_intro.add_run("Why this exact workflow is required:\n").bold = True
    p_intro.add_run(
        "Shopify no longer displays permanent Admin API access tokens directly on their Developer Dashboard or Admin Custom App page. "
        "When connecting third-party software, custom backends, headless storefronts, or automation scripts, you must register the app, "
        "execute the standard OAuth 2.0 authorization handshake, capture the temporary authorization code, and exchange it via a POST request "
        "for the permanent Access Token. This document transcribes Jan's exact tutorial step-by-step."
    )

    # Core Analogy
    add_callout(
        doc,
        "Jan's Core Analogy for App Credentials:\n"
        "• Client ID = Your App's Username or Passport (identifies who you are, public).\n"
        "• Client Secret = Your App's Private Password (proves you really are who you say you are; never share publicly).\n"
        "• Authorization Code = Short-lived 2-minute exchange ticket returned in the browser redirect URL.\n"
        "• Access Token = The final master key (shpat_...) returned by Shopify via Postman.",
        title="UNDERSTANDING THE SECURITY ARCHITECTURE",
        border_color="2563EB",
        bg_color="EFF6FF"
    )
    doc.add_paragraph()

    # PHASE 1
    h2_1 = doc.add_heading("Phase 1: Register New App in Shopify Dev Dashboard", level=2)
    h2_1.paragraph_format.space_before = Pt(12)
    h2_1.runs[0].font.size = Pt(14)
    h2_1.runs[0].font.color.rgb = RGBColor(0x00, 0x80, 0x60)

    p1 = doc.add_paragraph()
    p1.add_run("1. Navigate to Dev Dashboard:\n").bold = True
    p1.add_run("   • Start in the Admin area of your Shopify store.\n")
    p1.add_run("   • Click on your Profile Icon (top right/top left).\n")
    p1.add_run("   • Click on ")
    p1.add_run("Dev Dashboard").bold = True
    p1.add_run(" (or directly visit ")
    p1.add_run("dev.shopify.com").italic = True
    p1.add_run(").\n\n")

    p1.add_run("2. Create New App Record:\n").bold = True
    p1.add_run("   • Click the ")
    p1.add_run("Create app").bold = True
    p1.add_run(" button.\n")
    p1.add_run("   • ")
    p1.add_run("App Name: ").bold = True
    p1.add_run("Enter a descriptive name (e.g. ")
    p1.add_run("my-custom-app-123").italic = True
    p1.add_run(" or name of your external software).\n")
    p1.add_run("   • Click ")
    p1.add_run("Create").bold = True
    p1.add_run(".\n\n")

    p1.add_run("3. Configure App Settings & URLs:\n").bold = True
    p1.add_run("   • ")
    p1.add_run("App URL: ").bold = True
    p1.add_run("Set to ")
    p1.add_run("http://localhost/new-install").bold = True
    p1.add_run(" (In production this is where users land after install to trigger onboarding/welcome emails).\n")
    p1.add_run("   • ")
    p1.add_run("Embedded App: ").bold = True
    p1.add_run("UNCHECK ").bold = True
    p1.add_run("this box. (Jan explicitly unchecks it because we only need an API access token, not an iframe inside Shopify admin).\n")
    p1.add_run("   • ")
    p1.add_run("API Version: ").bold = True
    p1.add_run("Leave on the most recent release.\n\n")

    p1.add_run("4. Select Access Scopes (Permissions):\n").bold = True
    p1.add_run("   • Under ")
    p1.add_run("Access Scopes").bold = True
    p1.add_run(", select only the permissions your external software requires.\n")
    p1.add_run("   • Jan's example: Select ")
    p1.add_run("write_products").bold = True
    p1.add_run(" (Note: selecting write_products automatically covers read_products as well).\n")
    p1.add_run("   • Best Practice: Keep scopes as narrow as possible to maintain tight security.\n")
    p1.add_run("   • Optional Scopes: Leave blank / not needed.\n\n")

    p1.add_run("5. Whitelist Redirect URLs:\n").bold = True
    p1.add_run("   • Under ")
    p1.add_run("Redirect URLs").bold = True
    p1.add_run(", enter: ")
    p1.add_run("http://localhost").bold = True
    p1.add_run("\n   • Why? This is a critical security whitelist. Shopify will only trust and redirect to URLs specified here during OAuth.\n\n")

    p1.add_run("6. Release App & Note Credentials:\n").bold = True
    p1.add_run("   • Click ")
    p1.add_run("Release / Save").bold = True
    p1.add_run(" to publish this app version.\n")
    p1.add_run("   • Go to the ")
    p1.add_run("Settings").bold = True
    p1.add_run(" tab of the app.\n")
    p1.add_run("   • Copy your ")
    p1.add_run("Client ID").bold = True
    p1.add_run(" (e.g. 37549832049...) and your ")
    p1.add_run("Client Secret").bold = True
    p1.add_run(" (app private password).")

    doc.add_paragraph()

    # PHASE 2
    h2_2 = doc.add_heading("Phase 2: Install App on Your Store & Accept Permissions", level=2)
    h2_2.paragraph_format.space_before = Pt(12)
    h2_2.runs[0].font.size = Pt(14)
    h2_2.runs[0].font.color.rgb = RGBColor(0x00, 0x80, 0x60)

    p2 = doc.add_paragraph()
    p2.add_run("Even though the app record exists, you must install it onto your store so the store officially accepts the requested permissions.\n\n")
    p2.add_run("1. Click ")
    p2.add_run("Home").bold = True
    p2.add_run(" in the Dev Dashboard navigation.\n")
    p2.add_run("2. Scroll down to ")
    p2.add_run("Installs").bold = True
    p2.add_run(" and click ")
    p2.add_run("Install the app").bold = True
    p2.add_run(".\n")
    p2.add_run("3. Select your development or target store from the dropdown (e.g. ")
    p2.add_run("Coding with Yandev").italic = True
    p2.add_run(" or your store handle).\n")
    p2.add_run("4. Shopify redirects you to the standard merchant install grant screen:\n")
    p2.add_run("   URL: ")
    p2.add_run("https://admin.shopify.com/store/{shop}/app/grant?client_id={CLIENT_ID}").italic = True
    p2.add_run("\n5. Shopify warns: ")
    p2.add_run('"This app hasn\'t been reviewed"').italic = True
    p2.add_run(" (Normal for private apps). You will see the requested permissions (e.g. View and edit store data products).\n")
    p2.add_run("6. Click the green ")
    p2.add_run("Install").bold = True
    p2.add_run(" button.\n\n")

    p2.add_run("What happens immediately after clicking Install:\n").bold = True
    p2.add_run("Shopify redirects the browser to:\n")
    add_code_block(doc, "http://localhost/new-install?hmac=...&host=...&shop=your-store.myshopify.com&timestamp=...")
    doc.add_paragraph()
    
    add_callout(
        doc,
        "The browser will show 'This site can't be reached' or 'Unable to connect' at localhost/new-install. "
        "Jan explains this is 100% normal because you do not have a live server running on your computer on port 80. "
        "The important milestone is that Shopify has recorded the store installation!",
        title="NORMAL BEHAVIOR: SITE CANNOT BE REACHED",
        border_color="008060",
        bg_color="F0FDF4"
    )

    doc.add_paragraph()

    # PHASE 3
    h2_3 = doc.add_heading("Phase 3: Construct OAuth Authorization URL & Extract Auth Code", level=2)
    h2_3.paragraph_format.space_before = Pt(12)
    h2_3.runs[0].font.size = Pt(14)
    h2_3.runs[0].font.color.rgb = RGBColor(0x00, 0x80, 0x60)

    p3 = doc.add_paragraph()
    p3.add_run("Now you initiate the OAuth 2.0 authorization step manually by constructing the authorization URL in Notepad or any text editor.\n\n")
    p3.add_run("1. URL Structure (Construct in Notepad):\n").bold = True
    
    add_code_block(doc, "https://{shop}.myshopify.com/admin/oauth/authorize?client_id={CLIENT_ID}&redirect_uri=http://localhost")
    doc.add_paragraph()

    # Parameter Table
    p3_tbl = doc.add_table(rows=4, cols=2)
    p3_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    p3_tbl.columns[0].width = Inches(2.0)
    p3_tbl.columns[1].width = Inches(4.5)
    
    url_params = [
        ("Parameter", "Value / Description"),
        ("{shop}.myshopify.com", "Your store's permanent myshopify domain (e.g. codingwithyandev.myshopify.com)"),
        ("client_id", "Your App Client ID copied from Dev Dashboard Settings (starts with question mark ?client_id=...)"),
        ("redirect_uri", "Must match your whitelisted URL exactly: http://localhost (preceded by ampersand &redirect_uri=...)")
    ]
    for i, (k, v) in enumerate(url_params):
        r = p3_tbl.rows[i]
        c0 = r.cells[0]
        c1 = r.cells[1]
        set_cell_background(c0, "0F172A" if i == 0 else "F8FAFC")
        set_cell_background(c1, "0F172A" if i == 0 else "F8FAFC")
        
        p_c0 = c0.paragraphs[0]
        p_c0.add_run(k).bold = (i == 0)
        p_c0.runs[0].font.size = Pt(9)
        if i == 0:
            p_c0.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            
        p_c1 = c1.paragraphs[0]
        p_c1.add_run(v).bold = (i == 0)
        p_c1.runs[0].font.size = Pt(9)
        if i == 0:
            p_c1.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    doc.add_paragraph()

    p3_sub = doc.add_paragraph()
    p3_sub.add_run("2. Jan's Example from the Video:\n").bold = True
    add_code_block(doc, "https://codingwithyandev.myshopify.com/admin/oauth/authorize?client_id=37549832049...&redirect_uri=http://localhost")
    doc.add_paragraph()

    p3_sub2 = doc.add_paragraph()
    p3_sub2.add_run("3. Execute in Browser & Extract Code:\n").bold = True
    p3_sub2.add_run("   • Remove all line breaks so the URL is on a single continuous line.\n")
    p3_sub2.add_run("   • Paste the URL into your browser window where you are logged into Shopify and hit ")
    p3_sub2.add_run("Enter").bold = True
    p3_sub2.add_run(".\n")
    p3_sub2.add_run("   • The browser will redirect to ")
    p3_sub2.add_run("http://localhost/?code=...").bold = True
    p3_sub2.add_run(" and say 'This site can't be reached'.\n")
    p3_sub2.add_run("   • Look closely at the browser address bar. The URL looks like this:\n")

    add_code_block(doc, "http://localhost/?code=94a5c88b712398fd128a3910c...&hmac=...&host=...&shop=codingwithyandev.myshopify.com&timestamp=...")
    doc.add_paragraph()

    p3_sub3 = doc.add_paragraph()
    p3_sub3.add_run("   • ")
    p3_sub3.add_run("COPY THE CODE: ").bold = True
    p3_sub3.add_run("Copy only the character string between ")
    p3_sub3.add_run("code=").bold = True
    p3_sub3.add_run(" and the next ")
    p3_sub3.add_run("&hmac=").bold = True
    p3_sub3.add_run(".\n")
    p3_sub3.add_run("   • This string is your ")
    p3_sub3.add_run("Authorization Code").bold = True
    p3_sub3.add_run(".")

    add_callout(
        doc,
        "CRITICAL WARNING (Jan's Live Demonstration Pitfall):\n"
        "This authorization code is SHORT-LIVED. It expires in roughly 2 to 5 minutes! "
        "If it takes you too long to open Postman or configure the request, Shopify will reject it with: 'oauth error: invalid request'. "
        "If that happens, DO NOT PANIC. Simply re-paste your authorize URL into the browser, hit enter, copy the fresh code, and paste it into Postman.",
        title="CRITICAL EXPIRATION WINDOW (2 MINUTES)",
        border_color="DC2626",
        bg_color="FEF2F2"
    )

    doc.add_paragraph()

    # PHASE 4
    h2_4 = doc.add_heading("Phase 4: Exchange Auth Code for Permanent Access Token in Postman", level=2)
    h2_4.paragraph_format.space_before = Pt(12)
    h2_4.runs[0].font.size = Pt(14)
    h2_4.runs[0].font.color.rgb = RGBColor(0x00, 0x80, 0x60)

    p4 = doc.add_paragraph()
    p4.add_run("1. Open Postman:\n").bold = True
    p4.add_run("   • Open Postman (Free Desktop app or web version; free Google account signup takes 1 minute).\n")
    p4.add_run("   • Create a new HTTP Request.\n\n")

    p4.add_run("2. Request Method & Endpoint:\n").bold = True
    p4.add_run("   • Method: Select ")
    p4.add_run("POST").bold = True
    p4.add_run("\n   • Endpoint URL: ")
    p4.add_run("https://{shop}.myshopify.com/admin/oauth/access_token").bold = True
    p4.add_run("\n     (Replace {shop} with your myshopify domain, e.g. codingwithyandev.myshopify.com)\n\n")

    p4.add_run("3. Request Parameters / Body:\n").bold = True
    p4.add_run("   Pass the following 3 parameters (Jan enters them in structured key-value format):\n")

    # Postman params table
    p4_tbl = doc.add_table(rows=4, cols=2)
    p4_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    p4_tbl.columns[0].width = Inches(2.0)
    p4_tbl.columns[1].width = Inches(4.5)
    
    postman_params = [
        ("Key", "Value Description"),
        ("client_id", "Your App Client ID (from Dev Dashboard Settings)"),
        ("client_secret", "Your App Client Secret (the private password)"),
        ("code", "The short-lived authorization code copied from the browser in Phase 3")
    ]
    for i, (k, v) in enumerate(postman_params):
        r = p4_tbl.rows[i]
        c0 = r.cells[0]
        c1 = r.cells[1]
        set_cell_background(c0, "008060" if i == 0 else "F8FAFC")
        set_cell_background(c1, "008060" if i == 0 else "F8FAFC")
        
        p_c0 = c0.paragraphs[0]
        p_c0.add_run(k).bold = True
        p_c0.runs[0].font.size = Pt(9)
        if i == 0:
            p_c0.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            
        p_c1 = c1.paragraphs[0]
        p_c1.add_run(v)
        p_c1.runs[0].font.size = Pt(9)
        if i == 0:
            p_c1.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    doc.add_paragraph()

    p4_send = doc.add_paragraph()
    p4_send.add_run("4. Send Request & Inspect Response:\n").bold = True
    p4_send.add_run("   • Click the blue ")
    p4_send.add_run("Send").bold = True
    p4_send.add_run(" button in Postman.\n")
    p4_send.add_run("   • If successful (Status 200 OK), Shopify returns the JSON payload:\n")

    add_code_block(doc, '{\n  "access_token": "shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",\n  "scope": "write_products"\n}')
    doc.add_paragraph()

    p4_token = doc.add_paragraph()
    p4_token.add_run("5. Secure Your Permanent Access Token:\n").bold = True
    p4_token.add_run("   • The ")
    p4_token.add_run("shpat_...").bold = True
    p4_token.add_run(" string is your permanent Shopify Admin API Access Token!\n")
    p4_token.add_run("   • Copy and store it securely in your ")
    p4_token.add_run(".env").bold = True
    p4_token.add_run(" file or secrets vault.\n")
    p4_token.add_run("   • Jan's Security Warning: Never broadcast this token or commit it publicly to GitHub. This token has full access to the scopes granted (e.g. creating/deleting store products).")

    doc.add_paragraph()

    # PHASE 5
    h2_5 = doc.add_heading("Phase 5: Verification & Making Your First API Request", level=2)
    h2_5.paragraph_format.space_before = Pt(12)
    h2_5.runs[0].font.size = Pt(14)
    h2_5.runs[0].font.color.rgb = RGBColor(0x00, 0x80, 0x60)

    p5 = doc.add_paragraph()
    p5.add_run("To prove your access token works immediately, make a test GET call to the Shopify Admin REST or GraphQL endpoint.\n\n")
    p5.add_run("REST API Test (cURL / Postman):\n").bold = True
    
    add_code_block(doc, "curl -X GET https://{shop}.myshopify.com/admin/api/2026-01/shop.json \\\n  -H \"Content-Type: application/json\" \\\n  -H \"X-Shopify-Access-Token: shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"")
    doc.add_paragraph()

    p5_gql = doc.add_paragraph()
    p5_gql.add_run("GraphQL Admin API Test:\n").bold = True
    add_code_block(doc, "curl -X POST https://{shop}.myshopify.com/admin/api/2026-01/graphql.json \\\n  -H \"Content-Type: application/json\" \\\n  -H \"X-Shopify-Access-Token: shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\" \\\n  -d '{\"query\": \"{ shop { name email myshopifyDomain } }\"}'")
    doc.add_paragraph()

    # SUMMARY CHECKLIST
    h2_sum = doc.add_heading("Quick Reference Checklist", level=2)
    h2_sum.runs[0].font.size = Pt(14)
    h2_sum.runs[0].font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    check_table = doc.add_table(rows=5, cols=3)
    check_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    check_table.columns[0].width = Inches(0.8)
    check_table.columns[1].width = Inches(2.2)
    check_table.columns[2].width = Inches(3.5)

    check_items = [
        ("Step", "Action", "Key Output / Details"),
        ("1", "Dev Dashboard App Record", "Client ID, Client Secret, Redirect URI: http://localhost"),
        ("2", "Store Installation", "Grant permissions (write_products), App installed on store"),
        ("3", "Browser OAuth URL", "Visit /admin/oauth/authorize, copy temporary 'code' parameter"),
        ("4", "Postman POST Exchange", "POST to /admin/oauth/access_token, receive permanent 'access_token'")
    ]
    for i, (col1, col2, col3) in enumerate(check_items):
        r = check_table.rows[i]
        for c_idx, text in enumerate([col1, col2, col3]):
            cell = r.cells[c_idx]
            set_cell_background(cell, "1E293B" if i == 0 else "FFFFFF")
            p = cell.paragraphs[0]
            p.add_run(text).bold = (i == 0 or c_idx == 0)
            p.runs[0].font.size = Pt(9)
            if i == 0:
                p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    doc.add_paragraph()
    p_end = doc.add_paragraph()
    p_end.paragraph_format.space_before = Pt(14)
    run_end = p_end.add_run("Document generated strictly aligned with Coding with Jan (Shopify Developer Tutorial 2026).")
    run_end.font.size = Pt(8.5)
    run_end.italic = True
    run_end.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

    # Save
    doc.save(filename)
    print(f"Successfully generated: {filename}")

if __name__ == "__main__":
    local_path = "SHOPIFY_ACCESS_TOKEN_SETUP_GUIDE.docx"
    build_docx(local_path)
    
    downloads_dir = r"C:\Users\hawk1\Downloads"
    dest_path = os.path.join(downloads_dir, "SHOPIFY_ACCESS_TOKEN_SETUP_GUIDE.docx")
    shutil.copyfile(local_path, dest_path)
    print(f"Successfully copied to: {dest_path}")
