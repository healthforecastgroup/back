# Folder for backend codes

Instruction:
------------------
1. Pull codes:
------------------
    https://github.com/healthforecastgroup/back.git

2. Setup environment:
------------------

2.1 Download and install WinPython-64bit-3.3.5.7.

    http://sourceforge.net/projects/winpython/files/WinPython_3.3/3.3.5.7/

3. Run back-end services:
------------------

3.1 Create python environment by running below in command line.

    python.exe {winpython}/scripts/env.bat

3.2 Run below to start 'predict' backend service.

    {back}/apps/predict/predict.py
	
4. Using backend service:
------------------

4.1 Predict backend service:

    http://localhost:8888/coronaryheartdiseaserisk/gender/1/age/60/dbp/150/smoker/1/tcl/100/hdl/50/diabetes/1

TODOS:

1. Create convenience script for easy deploying to AWS.
