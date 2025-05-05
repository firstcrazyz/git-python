source : https://github.com/codemobiles/cm_fastapi_cmstock_workshop

Installing packages using pip and virtual environments
1.Installing pip
    Windows
        py -m pip --version
        pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)
        py -m pip install --upgrade pip
    Linux and macOS
        python3 -m pip install --user --upgrade pip
        python3 -m pip --version
2.Installing virtualenv
    On macOS and Linux:
        python3 -m pip install --user virtualenv
    On Windows:
        py -m pip install --user virtualenv
3.Creating a virtual environment
    On macOS and Linux:
        python3 -m venv env
    On Windows:
        py -m venv env
4.Activating a virtual environment
    On macOS and Linux:
        source env/bin/activate
    On Windows:
        .\env\Scripts\activate 
5.You can confirm you’re in the virtual environment by checkin
    On macOS and Linux:
        which python
        .../env/bin/python
    On Windows:
        where python
        .../env/bin/python.exe 
6.Leaving the virtual environment
    deactivate

- .\env\Scripts\activate 
- pipenv shell
- pipenv install fastapi sqlalchemy pydantic
- uvicorn main:app --reload --port 8081
- pipenv install aiofiles
- install : pip3 install "passlib[bcrypt]"  
- install : pip3 install python-multipart
- npx serve webserver -p 80
- master account
  username: admin, password: 1234
- https://www.youtube.com/watch?v=ttd4zOgCJdc
- npx serve webserver -p 8085 -s
- https://www.youtube.com/watch?v=bHvl9BhufXs
- pip3 install "python-jose[cryptography]"
- pip3 install pymysql
- pip3 install psycopg2-binary

- pip freeze > requirements.txt                 #Create lib ที่ใช้ทั้งหมดใส่ใน requirements.txt
- pip install -r <file.txt>                     #install Lib ทั้งหมดในไฟล์ .txt
- .\env\Scripts\activate                        #เข้า env
- .\env\Scripts\deactivate                      #ออกจาก env
- uvicorn app.main:app --reload --port 8081     #Run Backend
- npx serve webserver -p 80 -s                  #Run node_js Fontend
- pip3 install --no-cache-dir -r requirements.txt