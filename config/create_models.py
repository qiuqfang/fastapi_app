import os

os.system("sqlacodegen mysql+pymysql://root:123456@127.0.0.1:3306/fastapi_db --outfile=models.py")
