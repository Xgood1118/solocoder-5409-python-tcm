@echo off
echo ========================================
echo  中医辅助辨证开方系统 - 启动脚本
echo ========================================
echo.

if not exist .env (
    echo [提示] 未找到 .env 文件，使用默认配置...
)

echo [1/3] 检查 Python 环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到 Python，请先安装 Python 3.8+
    pause
    exit /b 1
)
echo       Python 环境就绪
echo.

echo [2/3] 检查依赖...
pip show fastapi >nul 2>&1
if errorlevel 1 (
    echo       正在安装依赖...
    pip install -r requirements.txt
) else (
    echo       依赖已安装
)
echo.

echo [3/3] 启动服务...
echo.
echo ========================================
echo  服务启动中...
echo  访问地址: http://localhost:8000
echo  API 文档: http://localhost:8000/docs
echo ========================================
echo.

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause
