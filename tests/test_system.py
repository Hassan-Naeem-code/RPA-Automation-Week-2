"""
Simple system tests for the invoice processing automation
"""

import pytest
import os
import subprocess
from pathlib import Path


class TestAutomationSystem:
    """Test the complete automation system."""
    
    def test_data_files_exist(self):
        """Test that required data files exist."""
        data_dir = Path('data')
        assert data_dir.exists(), "Data directory should exist"
        
        invoice_file = data_dir / 'invoice_data.xlsx'
        assert invoice_file.exists(), "Invoice data file should exist"
    
    def test_script_files_exist(self):
        """Test that all script files exist."""
        scripts_dir = Path('scripts')
        assert scripts_dir.exists(), "Scripts directory should exist"
        
        required_scripts = ['main.py', 'process_data.py', 'generate_report.py', 'send_email.py']
        for script in required_scripts:
            script_path = scripts_dir / script
            assert script_path.exists(), f"Script {script} should exist"
    
    def test_config_files_exist(self):
        """Test that configuration files exist."""
        config_dir = Path('config')
        assert config_dir.exists(), "Config directory should exist"
        
        settings_file = config_dir / 'settings.yaml'
        assert settings_file.exists(), "Settings file should exist"
    
    def test_requirements_file_exists(self):
        """Test that requirements file exists."""
        requirements_file = Path('requirements.txt')
        assert requirements_file.exists(), "Requirements file should exist"
    
    def test_readme_exists(self):
        """Test that README file exists."""
        readme_file = Path('README.md')
        assert readme_file.exists(), "README file should exist"
    
    def test_automation_runs_successfully(self):
        """Test that the main automation script runs without errors."""
        try:
            # Run the main automation script
            result = subprocess.run(
                ['python', 'scripts/main.py'],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Check that it completed successfully
            assert result.returncode == 0, f"Automation failed with error: {result.stderr}"
            
            # Check that success message appears in output
            assert "🎉 Automation completed successfully!" in result.stdout
            
            # Check that report was generated
            report_file = Path('data/report.xlsx')
            assert report_file.exists(), "Report file should be generated"
            
        except subprocess.TimeoutExpired:
            pytest.fail("Automation script took too long to complete")
        except Exception as e:
            pytest.fail(f"Failed to run automation: {str(e)}")
    
    def test_individual_components_exist(self):
        """Test that individual components can be imported."""
        scripts_dir = Path('scripts')
        
        # Test that Python files are valid by checking syntax
        for script_file in scripts_dir.glob('*.py'):
            try:
                with open(script_file, 'r') as f:
                    content = f.read()
                compile(content, str(script_file), 'exec')
            except SyntaxError as e:
                pytest.fail(f"Syntax error in {script_file}: {str(e)}")
    
    def test_generated_files_exist_after_run(self):
        """Test that all expected files are generated after running automation."""
        data_dir = Path('data')
        
        # Files that should exist after running automation
        expected_files = [
            'invoice_data.xlsx',
            'processed_invoice_data.xlsx',
            'report.xlsx'
        ]
        
        for filename in expected_files:
            file_path = data_dir / filename
            assert file_path.exists(), f"Expected file {filename} should exist after automation run"


class TestProjectStructure:
    """Test the overall project structure."""
    
    def test_enterprise_structure_exists(self):
        """Test that project structure directories exist."""
        expected_dirs = [
            'scripts',
            'config', 
            'templates',
            'tests',
            'docs',
            '.github'
        ]
        
        for dirname in expected_dirs:
            dir_path = Path(dirname)
            assert dir_path.exists(), f"Project directory {dirname} should exist"
    
    def test_scripts_structure(self):
        """Test the scripts directory structure."""
        scripts_dir = Path('scripts')
        assert scripts_dir.exists(), "Scripts directory should exist"
        
        expected_files = [
            'main.py',
            'process_data.py',
            'generate_report.py',
            'send_email.py',
            'create_sample_data.py'
        ]
        
        for filename in expected_files:
            file_path = scripts_dir / filename
            assert file_path.exists(), f"Script file {filename} should exist in scripts directory"
    
    def test_documentation_exists(self):
        """Test that documentation files exist."""
        docs_dir = Path('docs')
        if docs_dir.exists():
            pdd_file = docs_dir / 'PDD.md'
            assert pdd_file.exists(), "Process Definition Document should exist"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
