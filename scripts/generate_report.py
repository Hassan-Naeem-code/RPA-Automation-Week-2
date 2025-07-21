"""
Simple Report Generator for Invoice Data
"""
import pandas as pd
from datetime import datetime
import os

def generate_report(processed_data_file, output_file):
    """Generate a simple Excel report from processed invoice data."""
    try:
        # Read processed data
        df = pd.read_excel(processed_data_file)
        
        # Create basic summary statistics
        total_invoices = len(df)
        total_amount = df['Amount'].sum()
        avg_amount = df['Amount'].mean()
        
        # Create report
        report_data = {
            'Summary': [
                f'Report Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                f'Total Invoices: {total_invoices}',
                f'Total Amount: ${total_amount:,.2f}',
                f'Average Amount: ${avg_amount:,.2f}'
            ]
        }
        
        # Save to Excel with original data and summary
        with pd.ExcelWriter(output_file) as writer:
            df.to_excel(writer, sheet_name='Invoice Data', index=False)
            
            summary_df = pd.DataFrame(report_data)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
        
        print(f"Report generated successfully: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error generating report: {e}")
        return False

if __name__ == "__main__":
    input_file = "data/processed_invoice_data.xlsx"
    output_file = "data/report.xlsx"
    
    # Ensure input file exists
    if os.path.exists(input_file):
        generate_report(input_file, output_file)
    else:
        print(f"Input file not found: {input_file}")