

===== nstall Ollama< br / >
curl -fsSL https://ollama.com/install.sh | sh< br / >
< br / >
===== Pull models< br / >
ollama pull nomic-embed-text  # embedding model (advanced parser)< br / >
ollama pull mistral-nemo      # 12.2 billion parameter Large Language Model< br / >
< br / >
===== Install Python modules< br / >
pip install langchain-community< br / >
pip install ollama< br / >
pip install chromadb< br / >
pip install pysqlite3< br / >
< br / >
===== check to make sure Ollama model is loaded on GPU< br / >
ollama ps< br / >
< br / >
===== Populate data< br / >
Copy PDFs int data folder< br / >
python3 populate_database.py (this will take a while depending on the number of files)< br / >
< br / >
===== test query< br / >
python3 query.py "why is the sky blue"< br / >
< br / >
+===== install appserver < br / >
sudo apt update< br / >
sudo apt install gunicorn< br / >
< br / >
===== Create a service unit file for Gunicorn (point to your AI directory in path and working directory)< br / >
< br / >
[Unit]< br / >
Description=MentalAI< br / >
After=network.target< br / >
< br / >
[Service]< br / >
User=black< br / >
Group=black< br / >
Type=simple< br / >
Restart=always< br / >
WorkingDirectory=/home/black/RAGAI< br / >
Environment="PATH=/home/black/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/black/RAGAI"< br / >
ExecStart=/usr/bin/gunicorn -b 0.0.0.0:8080 -w 1 app:app &< br / >
< br / >
[Install]< br / >
WantedBy=multi-user.target< br / >
< br / >
 ===== enable service< br / >
sudo systemctl daemon-reload< br / >
sudo systemctl enable RAG.service< br / >
sudo systemctl start RAG.service< br / >
sudo systemctl status RAG.service< br / >
< br / > 
===== modify Ollama service unit file to add GPU support< br / >
< br / >
[Unit]< br / >
Description=Ollama Service< br / >
After=network-online.target< br / >
< br / >
[Service]< br / >
ExecStart=/usr/local/bin/ollama serve< br / >
User=ollama< br / >
Group=ollama< br / >
Restart=always< br / >
RestartSec=3< br / >
Environment="PATH=/home/black/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"< br / >
Environment="__NV_PRIME_RENDER_OFFLOAD=1"< br / >
Environment="_GLX_VENDOR_LIBRARY_NAME=nvidia"< br / >
< br / >
[Install]< br / >
WantedBy=default.target< br / >
 < br / >
===== Reload Ollama Service< br / >
sudo systemctl daemon-reload< br / >
sudo systemctl start Rollama.service< br / >
sudo systemctl status ollama.service< br / >
< br / >
===== Test< br / >
http://localhost:8080< br / >