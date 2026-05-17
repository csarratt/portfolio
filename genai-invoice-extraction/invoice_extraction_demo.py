import json
import re

invoice_text = """
Vendor: Northwind Office Supply
Invoice Number: INV-10458
Invoice Date: 2026-04-15
Total Due: $1,284.55
"""

def extract_invoice_fields(text):
    fields = {
        "vendor": re.search(r"Vendor:\s*(.*)", text),
        "invoice_number": re.search(r"Invoice Number:\s*(.*)", text),
        "invoice_date": re.search(r"Invoice Date:\s*(.*)", text),
        "total_due": re.search(r"Total Due:\s*\$(.*)", text),
    }

    return {
        key: match.group(1).strip() if match else None
        for key, match in fields.items()
    }

structured_invoice = extract_invoice_fields(invoice_text)

print("Invoice Extraction Demo")
print(json.dumps(structured_invoice, indent=2))
