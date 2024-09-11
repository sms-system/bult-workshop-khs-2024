# bult-workshop-khs-2024


  - API
    ---
    имя:    ollama
    имедж:  ollama/ollama
    порт:   11434
    волюм:  /root/.ollama
    20000 / 28000

    TERMINAL: ollama run llama3.1

  - WEB_UI
    ---
    имя:         open-webui
    имедж:       ghcr.io/open-webui/open-webui:main
    порт:        8080
    соединение:  ollama:11434
    енв:         OLLAMA_BASE_URL=http://ollama:11434
    2000 / 2000

  - APP
    ---
    имя:         app
    имедж:       python:3.9
    соединение:  ollama:11434
    волюм:       /root/.local
                 /app
    cmd:         sleep infinity
                 /root/.local/bin/fastapi run /app/main.py
    2000 / 2000


    TERMINAL: pip install --user "fastapi[standard]" ollama



              git clone https://github.com/sms-system/bult-workshop-khs-2024.git app


api-adapter:v0.0.34




https://github.com/sms-system/bult-workshop-khs-2024




https://app-5-181-20-2.at.bult.pro --> app:8000
https://gpt-5-181-20-2.at.bult.pro --> openwebui:8080



