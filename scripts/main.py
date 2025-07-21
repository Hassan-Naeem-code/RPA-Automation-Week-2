"""
Main automation script for invoice processing
"""
from process_data import process_invoices
from generate_report import generate_report
from send_email import send_email
import os

def main():
    """Main automation workflow."""
    print("Starting Invoice Processing Automation...")
    
    # File paths
    input_file = "data/invoice_data.xlsx"
    processed_file = "data/processed_invoice_data.xlsx"
    report_file = "data/report.xlsx"
    
    # Step 1: Process invoice data
    print("\n1. Processing invoice data...")
    if os.path.exists(input_file):
        if process_invoices(input_file, processed_file):
            print("✓ Data processing completed")
        else:
            print("✗ Data processing failed")
            return False
    else:
        print(f"✗ Input file not found: {input_file}")
        return False
    
    # Step 2: Generate report
    print("\n2. Generating report...")
    if generate_report(processed_file, report_file):
        print("✓ Report generation completed")
    else:
        print("✗ Report generation failed")
        return False
    
    # Step 3: Send email (optional)
    print("\n3. Email notification...")
    if send_email(report_file):
        print("✓ Email sent successfully")
    else:
        print("✗ Email sending failed (configure SMTP to enable)")
    
    print("\n🎉 Automation completed successfully!")
    print(f"Report saved: {report_file}")
    return True

if __name__ == "__main__":
    main()
