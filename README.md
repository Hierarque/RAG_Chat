# RAG_Chat
Problème avec open-webUI depuis le 22/11/2024

Pour télécharger le modèle une fois les conteneurs lancés :  
curl http://localhost:11434/api/pull -d '{
  "name": "llama3"
}'

Modifier la variable PDF_URL dans le docker-compose.yml pour télécharger le document et l'upload