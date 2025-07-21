"""
Unit tests for the automation components
"""

import pytest
import pandas as pd
import sys
from pathlib import Path

# Add scripts directory to path so we can import our modules
scripts_dir = Path(__file__).parent.parent / 'scripts'
sys.path.insert(0, str(scripts_dir))

import process_data


class TestDataProcessing:
    """Test data processing functions."""
    
    def test_process_invoices_function_exists(self):
        """Test that the main processing function exists."""
        # Check that the function exists and is callable
        assert hasattr(process_data, 'process_invoices'), "process_invoices function should exist"
        assert callable(process_data.process_invoices), "process_invoices should be callable"
    
    def test_process_invoices_with_valid_files(self):
        """Test processing with existing files."""
        input_file = "data/invoice_data.xlsx"
        output_file = "data/test_processed_output.xlsx"
        
        # Test that function runs without error
        try:
            result = process_data.process_invoices(input_file, output_file)
            # Function should return True on success
            assert result is True, "Function should return True on successful processing"
            
            # Check that output file was created
            output_path = Path(output_file)
            assert output_path.exists(), "Output file should be created"
            
            # Clean up test file
            if output_path.exists():
                output_path.unlink()
                
        except Exception as e:
            pytest.fail(f"process_invoices should not raise exception with valid inputs: {e}")
    
    def test_process_invoices_with_invalid_input(self):
        """Test processing with non-existent input file."""
        input_file = "data/nonexistent_file.xlsx"
        output_file = "data/test_output.xlsx"
        
        # Function should handle error gracefully and return False
        result = process_data.process_invoices(input_file, output_file)
        assert result is False, "Function should return False when input file doesn't exist"


class TestDataIntegrity:
    """Test data integrity and consistency."""
    
    def test_sample_data_format(self):
        """Test that our sample data has the correct format."""
        data_file = Path('data/invoice_data.xlsx')
        
        if data_file.exists():
            df = pd.read_excel(data_file)
            
            # Check that actual columns exist (based on the real data format)
            actual_columns = list(df.columns)
            expected_columns = ['InvoiceID', 'Client', 'Amount', 'Status', 'Date']
            
            for col in expected_columns:
                assert col in actual_columns, f"Column {col} should exist in data. Available columns: {actual_columns}"
            
            # Check data types make sense
            assert df['Amount'].dtype in ['float64', 'int64'], "Amount should be numeric"
            assert len(df) > 0, "Should have some data rows"
    
    def test_processing_preserves_data_integrity(self):
        """Test that processing doesn't corrupt data."""
        input_file = "data/invoice_data.xlsx"
        output_file = "data/test_integrity_output.xlsx"
        
        if Path(input_file).exists():
            # Get original data
            original_df = pd.read_excel(input_file)
            original_count = len(original_df)
            
            # Process the data
            result = process_data.process_invoices(input_file, output_file)
            assert result is True, "Processing should succeed"
            
            # Check processed data
            if Path(output_file).exists():
                processed_df = pd.read_excel(output_file)
                
                # Should have same number of records
                assert len(processed_df) == original_count, "Should preserve all records"
                
                # Should have required columns
                required_columns = ['InvoiceID', 'Client', 'Amount', 'Status', 'Date']
                for col in required_columns:
                    assert col in processed_df.columns, f"Column {col} should exist after processing"
                
                # Should have new calculated column
                assert 'DaysOld' in processed_df.columns, "Should add DaysOld column"
                
                # Clean up test file
                Path(output_file).unlink()


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
