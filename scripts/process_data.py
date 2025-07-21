"""
Simple Invoice Data Processing
"""
import pandas as pd
import os

def process_invoices(input_file, output_file):
    """Process invoice data from Excel file and save to output file."""
    try:
        # Read the input data
        print(f"Reading data from: {input_file}")
        df = pd.read_excel(input_file)
        
        # Clean and standardize data
        df['Status'] = df['Status'].str.upper()
        df['Amount'] = df['Amount'].apply(lambda x: round(x, 2))
        df['Client'] = df['Client'].str.title()
        
        # Add calculated fields
        df['DaysOld'] = (pd.Timestamp.now() - pd.to_datetime(df['Date'])).dt.days
        
        # Save processed data
        df.to_excel(output_file, index=False)
        print(f"Processed data saved to: {output_file}")
        print(f"Processed {len(df)} records")
        
        return True
        
    except Exception as e:
        print(f"Error processing data: {e}")
        return False

if __name__ == "__main__":
    input_file = "data/invoice_data.xlsx"
    output_file = "data/processed_invoice_data.xlsx"
    
    process_invoices(input_file, output_file)
