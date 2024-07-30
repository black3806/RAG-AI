

===== nstall Ollama
curl -fsSL https://ollama.com/install.sh | sh

===== Pull models
ollama pull nomic-embed-text  # embedding model (advanced parser)
ollama pull mistral-nemo      # 12.2 billion parameter Large Language Model

===== Install Python modules
pip install langchain-community
pip install ollama
pip install chromadb
pip install pysqlite3

===== check to make sure Ollama model is loaded on GPU
ollama ps

===== Populate data
Copy PDFs int data folder
python3 populate_database.py (this will take a while depending on the number of files)

===== test query
python3 query.py "why is the sky blue"

+===== install appserver
sudo apt update
sudo apt install gunicorn

===== Create a service unit file for Gunicorn (point to your AI directory in path and working directory)

[Unit]
Description=MentalAI
After=network.target

[Service]
User=black
Group=black
Type=simple
Restart=always
WorkingDirectory=/home/black/RAGAI
Environment="PATH=/home/black/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/black/RAGAI"
ExecStart=/usr/bin/gunicorn -b 0.0.0.0:8080 -w 1 app:app &

[Install]
WantedBy=multi-user.target

 ===== enable service
sudo systemctl daemon-reload
sudo systemctl enable RAG.service
sudo systemctl start RAG.service
sudo systemctl status RAG.service

 
===== modify Ollama service unit file to add GPU support

[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=/home/black/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"
Environment="__NV_PRIME_RENDER_OFFLOAD=1"
Environment="_GLX_VENDOR_LIBRARY_NAME=nvidia"

[Install]
WantedBy=default.target
 
===== Reload Ollama Service
sudo systemctl daemon-reload
sudo systemctl start Rollama.service
sudo systemctl status ollama.service

 

===== Test
http://localhost:8080