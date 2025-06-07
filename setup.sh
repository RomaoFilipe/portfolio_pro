#!/bin/bash

echo "🚀 Atualizar pacotes..."
sudo apt update && sudo apt upgrade -y

echo "🚀 Instalar python3.12-venv..."
sudo apt install python3.12-venv -y

echo "🚀 Criar virtualenv..."
python3 -m venv venv

echo "🚀 Ativar virtualenv..."
source venv/bin/activate

echo "🚀 Instalar requirements com --break-system-packages..."
pip install -r requirements.txt --break-system-packages

echo "🚀 Instalar dependências Node.js (npm install)..."
npm install

echo "🚀 Gerar CSS com Tailwind (build:css)..."
npm run build:css

echo "✅ Setup completo! Agora podes correr:"
echo "    source venv/bin/activate"
echo "    python3 manage.py runserver"
