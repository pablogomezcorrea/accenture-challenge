FROM python:3.11-slim

WORKDIR /app

# Instalar dependências necessárias para xvfb e Streamlit
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    xvfb \
    x11-utils \
    x11-xserver-utils \
    xauth \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libgl1 \
    python3-tk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Evita prompt do Streamlit
ENV STREAMLIT_DISABLE_EMAIL_PROMPT=true
ENV DISPLAY=:99

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["xvfb-run", "-a", "python", "-m", "streamlit", "run", "app.py", "--server.fileWatcherType=none"]