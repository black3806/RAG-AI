

## Heavily Modified version of https://github.com/pixegami/rag-tutorial-v2 <BR>

### Install Ollama<BR>
curl -fsSL https://ollama.com/install.sh | sh<BR>
<BR>
### Pull models<BR>
ollama pull nomic-embed-text  ### embedding model (advanced parser)<BR>
ollama pull mistral-nemo      ### 12.2 billion parameter Large Language Model<BR>
<BR>
### Install Python modules<BR>
pip install langchain-community<BR>
pip install ollama<BR>
pip install chromadb<BR>
pip install pysqlite3 <BR>
pip install flask<BR>
pip install pypdf<BR>
pip install langchain-chroma<BR>

### check to make sure Ollama model is loaded on GPU<BR>
ollama ps<BR>

### Populate data<BR>
Copy PDFs int data folder<BR>
python3 populate_database.py (this will take a while depending on the number of files)<BR>
<BR>
### test query<BR>
python3 query.py "why is the sky blue"<BR>

### install appserver<BR>
sudo apt update<BR>
sudo apt install gunicorn<BR>
<BR>
### Create a service unit file for Gunicorn (point to your AI directory in path and working directory)<BR>
/etc/systemd/system/RAG.service<BR>
<code style="color : green">
[Unit]<BR>
Description=RAGAI<BR>
After=network.target<BR>
<BR>
[Service]<BR>
User=black<BR>
Group=black<BR>
Type=simple<BR>
Restart=always<BR>
WorkingDirectory=/home/black/RAGAI<BR>
Environment="PATH=/home/black/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/black/RAGAI"<BR>
ExecStart=/usr/bin/gunicorn -b 0.0.0.0:8080 -w 1 app:app &<BR>
<BR>
[Install]<BR>
WantedBy=multi-user.target<BR>
</code>
### enable service<BR>
sudo systemctl daemon-reload<BR>
sudo systemctl enable RAG.service<BR>
sudo systemctl start RAG.service<BR>
sudo systemctl status RAG.service<BR>
<BR>
### modify Ollama service unit file to add GPU support<BR>
/etc/systemd/system/ollama.service<BR>
<code style="color : green">
[Unit]<BR>
Description=Ollama Service<BR>
After=network-online.target<BR>
<BR>
[Service]<BR>
ExecStart=/usr/local/bin/ollama serve<BR>
User=ollama<BR>
Group=ollama<BR>
Restart=always<BR>
RestartSec=3<BR>
Environment="PATH=/home/black/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"<BR>
Environment="__NV_PRIME_RENDER_OFFLOAD=1"<BR>
Environment="_GLX_VENDOR_LIBRARY_NAME=nvidia"<BR>
</code>
<BR>
[Install]<BR>
WantedBy=default.target<BR>

### Reload Ollama Service<BR>
sudo systemctl daemon-reload<BR>
sudo systemctl start ollama.service<BR>
sudo systemctl status ollama.service<BR>

### Test<BR>
http://localhost:8080<BR>

