# Steps

1. Install [Python](https://www.python.org/downloads/)
2. Add python to [path](https://datatofish.com/add-python-to-windows-path/)
3. Open command prompt
4. Verify python installation by running `python --version'`
5. Create a project directory. Use following commands  
   `mkdir project`  
   `cd project`
6. Extract `version_1.zip`
7. Create a virtual environment
   On windows run  
   `python -m venv env`  
   On Max/Linux run  
   `python3 -m venv env`
8. Activate virtual environment
   On windows run  
   `env\Scripts\activate`  
   On Max/Linux run  
   `source env/bin/activate`
9. Install Libraries  
   Windows - `pip install requirements.txt`  
   Max/Linux - `pip3 install requirements.txt`
10. Run the app  
    Windows - `python app.py`  
    Max/Linux - `python3 app.py`
