import pandas as pd

def process_invoices(file_path):
    """Process invoice data from Excel file."""
    df = pd.read_excel(file_path)
    
    # Clean and standardize data
    df['Status'] = df['Status'].str.upper()
    df['Amount'] = df['Amount'].apply(lambda x: round(x, 2))
    df['Client'] = df['Client'].str.title()
    
    # Add calculated fields
    df['DaysOld'] = (pd.Timestamp.now() - pd.to_datetime(df['Date'])).dt.days
    
    return df
