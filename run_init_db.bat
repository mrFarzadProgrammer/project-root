@echo off
setlocal

echo Setting PYTHONPATH...
set PYTHONPATH=.

echo Running init_db...
python -m services.shared.init_db

echo Tables created successfully.
pause