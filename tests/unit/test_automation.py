"""
Simple unit tests for the invoice processing automation
"""

import pytest
import pandas as pd
import sys
import os
from pathlib import Path

# Add the scripts directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

# Import the modules to test
import process_data
import generate_report


class TestProcessData:
    """Test the data processing functionality."""
    
    def test_process_invoices_function_exists(self):
        """Test that the process_invoices function exists."""
        assert hasattr(process_data, 'process_invoices')
        assert callable(process_data.process_invoices)
    
    def test_sample_data_processing(self):
        """Test processing with sample data."""
        # Create sample data
        sample_data = pd.DataFrame({
            'InvoiceID': ['INV000001', 'INV000002', 'INV000003'],
            'Client': ['ABC Corp', 'XYZ Ltd', 'DEF Inc'],
            'Amount': [1000.50, 2500.75, 750.25],
            'Status': ['PAID', 'PENDING', 'UNPAID'],
            'Date': ['2025-01-15', '2025-01-16', '2025-01-17']
        })
        
        # Create temp files
        temp_input = 'test_input.xlsx'
        temp_output = 'test_output.xlsx'
        
        try:
            # Save test data
            sample_data.to_excel(temp_input, index=False)
            
            # Process the data
            result = process_data.process_invoices(temp_input, temp_output)
            
            # Verify result
            assert result == True
            assert os.path.exists(temp_output)
            
            # Check processed data
            processed_data = pd.read_excel(temp_output)
            assert len(processed_data) == 3
            assert 'DaysOld' in processed_data.columns
            
        finally:
            # Clean up
            if os.path.exists(temp_input):
                os.remove(temp_input)
            if os.path.exists(temp_output):
                os.remove(temp_output)


class TestReportGeneration:
    """Test the report generation functionality."""
    
    def test_generate_report_function_exists(self):
        """Test that the generate_report function exists."""
        assert hasattr(generate_report, 'generate_report')
        assert callable(generate_report.generate_report)
    
    def test_report_generation_with_sample_data(self):
        """Test report generation with sample data."""
        # Create sample processed data
        sample_data = pd.DataFrame({
            'InvoiceID': ['INV000001', 'INV000002', 'INV000003'],
            'Client': ['ABC Corp', 'XYZ Ltd', 'DEF Inc'],
            'Amount': [1000.50, 2500.75, 750.25],
            'Status': ['PAID', 'PENDING', 'UNPAID'],
            'Date': ['2025-01-15', '2025-01-16', '2025-01-17'],
            'DaysOld': [5, 4, 3]
        })
        
        # Create temp files
        temp_input = 'test_processed.xlsx'
        temp_output = 'test_report.xlsx'
        
        try:
            # Save test data
            sample_data.to_excel(temp_input, index=False)
            
            # Generate report
            result = generate_report.generate_report(temp_input, temp_output)
            
            # Verify result
            assert result == True
            assert os.path.exists(temp_output)
            
            # Check report has multiple sheets
            with pd.ExcelFile(temp_output) as xls:
                assert 'Invoice Data' in xls.sheet_names
                assert 'Summary' in xls.sheet_names
            
        finally:
            # Clean up
            if os.path.exists(temp_input):
                os.remove(temp_input)
            if os.path.exists(temp_output):
                os.remove(temp_output)


class TestIntegration:
    """Integration tests for the complete workflow."""
    
    def test_data_directory_exists(self):
        """Test that the data directory exists with sample data."""
        # Get the project root (two levels up from tests/unit/)
        project_root = Path(__file__).parent.parent.parent
        data_dir = project_root / 'data'
        assert data_dir.exists(), f"Data directory should exist at {data_dir}"
        
        # Check for sample data file
        sample_file = data_dir / 'invoice_data.xlsx'
        assert sample_file.exists(), f"Sample data file should exist at {sample_file}"
    
    def test_scripts_directory_exists(self):
        """Test that all required script files exist."""
        # Get the project root (two levels up from tests/unit/)
        project_root = Path(__file__).parent.parent.parent
        scripts_dir = project_root / 'scripts'
        assert scripts_dir.exists(), f"Scripts directory should exist at {scripts_dir}"
        
        # Check for required script files
        required_scripts = ['main.py', 'process_data.py', 'generate_report.py', 'send_email.py']
        for script in required_scripts:
            script_file = scripts_dir / script
            assert script_file.exists(), f"Script {script} should exist at {script_file}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
