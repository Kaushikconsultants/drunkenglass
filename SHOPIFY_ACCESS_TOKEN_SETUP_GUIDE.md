# Shopify Admin API Access Token — Complete Step-by-Step Setup Guide

**Reference Video:** [YouTube — Shopify Access Token Process](https://youtu.be/8dymQjcylv8)  
**Word (.docx) Document:** [SHOPIFY_ACCESS_TOKEN_SETUP_GUIDE.docx](file:///c:/Projects/01_Ecommerce_and_Themes/DRUNKEN-GLASS-Developer-Handover/SHOPIFY_ACCESS_TOKEN_SETUP_GUIDE.docx)

---

## 📌 What is a Shopify Admin API Access Token?
A **Shopify Admin API Access Token** (format: `shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`) gives your external applications, custom apps, automation scripts, inventory ERPs, or headless storefronts secure programmatic access to your store's backend without needing store passwords.

---

## ⚙️ Step-by-Step Walkthrough

### STEP 1: Open App Development in Shopify Admin
1. **Log in** to your Shopify Admin (`https://admin.shopify.com` or `https://{your-store}.myshopify.com/admin`).
2. Click the **Settings** gear icon (⚙️) located at the bottom-left corner of the sidebar.
3. In the left-hand navigation menu, click **Apps and sales channels**.
4. At the top-right corner of the page, click the button labeled **Develop apps**.

> [!NOTE]
> **First-Time Setup Banner:** If custom app development has not yet been activated on your store, you will see a banner with a button saying **"Allow custom app development"**. Click it, read the disclaimer, and confirm by clicking **"Allow custom app development"**.

---

### STEP 2: Create a New Custom App
1. Click the **Create an app** button in the top-right corner.
2. In the modal that appears:
   * **App name:** Enter a recognizable name (e.g., `Drunken Glass Admin Sync` or `ERP Integration`).
   * **App developer:** Select your account email from the dropdown.
3. Click **Create app**.

---

### STEP 3: Configure Admin API Scopes (Permissions)
1. You are now inside your app's dashboard. Click on the **Configuration** tab.
2. Under the **Admin API integration** section, click **Configure**.
3. In the permissions list, search and check the boxes for the scopes your integration needs:
   * **Products & Collections:** `read_products`, `write_products`
   * **Inventory & Stock:** `read_inventory`, `write_inventory`
   * **Orders & Transactions:** `read_orders`, `write_orders`, `read_all_orders` (if needed)
   * **Customers:** `read_customers`, `write_customers`
   * **Discounts & Price Rules:** `read_discounts`, `write_discounts`, `read_price_rules`
   * **Themes & Assets:** `read_themes`, `write_themes`
4. In the **Webhook API version** dropdown, ensure the latest stable version (e.g., `2024-10` or latest) is selected.
5. Click **Save** in the top-right corner.

---

### STEP 4: Install the App & Reveal the Access Token
1. Go to the **API credentials** tab (or click **Install app** at the top right).
2. Click the green **Install app** button.
3. A confirmation popup will ask *"Install app?"* — click **Install**.
4. In the **Admin API access token** card, you will now see:
   ```text
   Admin API access token: ••••••••••••••••••••••••••••••••
   [ Reveal token once ]
   ```
5. Click **Reveal token once**.

> [!CAUTION]
> **CRITICAL SECURITY WARNING:**  
> The token begins with `shpat_...`.  
> Shopify **ONLY reveals this token ONE TIME**. Once you refresh the browser tab or navigate away, Shopify permanently masks it for security reasons.  
> **Immediately copy the token** and paste it into your secure password manager, `.env` file, or credentials safe!

---

### STEP 5: Collect & Save Your Credentials
Save the following details together in your secure vault:
* **Admin API Access Token:** `shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (Secret)
* **API Key:** 32-character string (Public identifier)
* **API Secret Key:** `shpss_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (Secret)
* **Store Domain:** `your-store-handle.myshopify.com` (Always use the `.myshopify.com` domain for API endpoints, not custom domains).

---

## 🧪 STEP 6: Verification (Quick Test)

You can verify that your token is active and working properly by running this `cURL` request in your terminal:

```bash
curl -X GET "https://{your-store}.myshopify.com/admin/api/2024-10/shop.json" \
  -H "X-Shopify-Access-Token: shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
  -H "Content-Type: application/json"
```

If successful, Shopify will return an HTTP 200 JSON response containing your store details (name, email, currency, country, etc.).

---

## ❓ Frequently Asked Questions & Troubleshooting

| Issue | Cause & Solution |
|---|---|
| **I forgot to copy the token and closed the tab.** | You cannot reveal the token again once the tab is closed. Go back to your App, click **Uninstall app**, and then click **Install app** again. A fresh token will be generated for you to reveal once. |
| **HTTP 401 Unauthorized** | Verify that the header name is exactly `X-Shopify-Access-Token` and that you are using your permanent `{store-name}.myshopify.com` domain, not a custom domain like `brand.com`. |
| **HTTP 403 Forbidden** | The endpoint you are calling requires a scope that was not granted. Go to **Configuration** > **Admin API integration**, enable the missing scope (e.g. `read_products`), click **Save**, and retry. |
