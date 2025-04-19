#!/bin/bash

HOST=$1
PORT=22
KNOWN_HOSTS="/root/.ssh/known_hosts"

echo "Verificando conexão com $HOST na porta $PORT..."
if nc -z -w 5 "$HOST" "$PORT"; then
    echo "✅ Conexão com $HOST:$PORT bem-sucedida."
    
    echo "🔍 Obtendo chave pública com ssh-keyscan..."
    KEY=$(ssh-keyscan -T 5 -p $PORT $HOST 2>/dev/null | grep -v '^#')

    if [ -n "$KEY" ]; then
        echo "🔐 Chave obtida com sucesso:"
        echo "$KEY"
        
        # Adiciona a chave ao known_hosts se ainda não estiver lá
        if ! grep -q "$HOST" "$KNOWN_HOSTS"; then
            echo "$KEY" >> "$KNOWN_HOSTS"
            echo "✅ Chave adicionada ao $KNOWN_HOSTS"
        else
            echo "ℹ️ A chave já está presente no $KNOWN_HOSTS"
        fi
    else
        echo "❌ Não foi possível obter a chave do host."
    fi
else
    echo "❌ Falha ao conectar na porta $PORT de $HOST."
fi
