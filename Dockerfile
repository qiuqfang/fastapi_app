# 使用 Python3.10.8 环境进行构建
FROM python:3.10.8
# 工作目录
WORKDIR /app
# 复制依赖文件
COPY requirements.txt requirements.txt
# 安装依赖
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# 暴露端口
EXPOSE 8000
# 复制所有文件
COPY . .
# 执行命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]