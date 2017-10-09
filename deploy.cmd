echo Upgrade pip package.
env\scripts\python -m pip install pip --upgrade
IF !ERRORLEVEL! NEQ 0 goto error
echo Pip install requirements.
env\scripts\pip install -r requirements.txt
