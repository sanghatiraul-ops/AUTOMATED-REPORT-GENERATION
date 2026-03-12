# Task 2: Automated PDF Report Generation
import pandas as pd
from fpdf import FPDF

# Step 1: Read data from CSV
data = pd.read_csv("sales_data.csv")

# Step 2: Analyze data
data['Total'] = data['Quantity'] * data['Price']  # Total sales per product
total_sales = data['Total'].sum()
average_sales = data['Total'].mean()
max_sale = data['Total'].max()
best_product = data.loc[data['Total'].idxmax(), 'Product']


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

pdf.cell(0, 10, "Sales Report", ln=True, align="C")
pdf.ln(10)  # Line break

# Table Header
pdf.set_font("Arial", 'B', 12)
pdf.cell(50, 10, "Product", 1)
pdf.cell(30, 10, "Quantity", 1)
pdf.cell(30, 10, "Price($)", 1)
pdf.cell(30, 10, "Total($)", 1)
pdf.ln()

# Table Data
pdf.set_font("Arial", '', 12)
for index, row in data.iterrows():
    pdf.cell(50, 10, str(row['Product']), 1)
    pdf.cell(30, 10, str(row['Quantity']), 1)
    pdf.cell(30, 10, str(row['Price']), 1)
    pdf.cell(30, 10, str(row['Total']), 1)
    pdf.ln()

# Analysis Summary
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Analysis Summary", ln=True)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 8, f"Total Sales: ${total_sales}", ln=True)
pdf.cell(0, 8, f"Average Sale: ${average_sales:.2f}", ln=True)
pdf.cell(0, 8, f"Highest Sale: ${max_sale} ({best_product})", ln=True)

# Step 4: Save PDF
pdf.output("sales_report.pdf")
print("PDF report generated successfully!")
