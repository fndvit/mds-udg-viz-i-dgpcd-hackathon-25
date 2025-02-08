if (Test-Path env\) {
    Write-Host "--Environment already exists--"
} else {
    python -m venv env
}

.\env\Scripts\Activate.ps1
pip install -r requirements.txt
$env:_OLD_PYTHONPATH = $env:PYTHONPATH
$env:PYTHONPATH = "${PWD}\src"