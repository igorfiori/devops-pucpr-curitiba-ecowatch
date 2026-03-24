FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Usar o -m garante que o Python reconheça os teus módulos (app e backend) corretamente
CMD ["python", "-m", "backend.main"]