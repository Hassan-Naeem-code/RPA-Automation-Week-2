#!/usr/bin/env python3
"""
Generate sample data for testing
"""
import pandas as pd
import os

def create_sample_data():
    """Create sample invoice data for testing."""
    os.makedirs('data', exist_ok=True)
    
    df = pd.DataFrame({
        'InvoiceID': ['INV000001', 'INV000002', 'INV000003'],
        'Client': ['Test Corp', 'Demo Inc', 'Sample LLC'],
        'Amount': [1000.50, 2500.75, 750.25],
        'Status': ['PAID', 'PENDING', 'OVERDUE'],
        'Date': ['2025-01-01', '2025-01-15', '2025-01-30']
    })
    
    df.to_excel('data/invoice_data.xlsx', index=False)
    print('Sample data created successfully')

if __name__ == "__main__":
    create_sample_data()
