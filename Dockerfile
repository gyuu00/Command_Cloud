# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Flask 및 코드 복사
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# creds.json은 여기서 직접 생성하거나 EC2에서는 메타데이터로 대체 가능
# RUN curl ... 로 작성 가능 (테스트용 정적 creds.json만 쓸 수도 있음)

EXPOSE 5000
CMD ["python", "app.py"]
