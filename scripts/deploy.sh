#!/bin/bash
# ─────────────────────────────────────────────────────────────
# CalmAid – One-command deploy to Google Cloud Run
# Usage: bash deploy.sh
# Prerequisites: gcloud CLI installed + authenticated
# ─────────────────────────────────────────────────────────────

set -e

PROJECT_ID="your-gcp-project-id"        
REGION="us-central1"
SERVICE_NAME="calmaid-agent"
IMAGE_NAME="gcr.io/$PROJECT_ID/$SERVICE_NAME"

echo "🔧 Setting project..."
gcloud config set project $PROJECT_ID

echo "🔑 Storing API key in Secret Manager..."
echo -n "$GEMINI_API_KEY" | gcloud secrets create gemini-api-key \
    --data-file=- \
    --replication-policy="automatic" 2>/dev/null || \
echo -n "$GEMINI_API_KEY" | gcloud secrets versions add gemini-api-key --data-file=-

echo "🐳 Building Docker image..."
gcloud builds submit --tag $IMAGE_NAME .

echo "🚀 Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
    --image $IMAGE_NAME \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --set-secrets="GEMINI_API_KEY=gemini-api-key:latest" \
    --memory 512Mi \
    --cpu 1 \
    --max-instances 3

echo ""
echo "✅ Deployed! Your URL:"
gcloud run services describe $SERVICE_NAME \
    --platform managed \
    --region $REGION \
    --format 'value(status.url)'
