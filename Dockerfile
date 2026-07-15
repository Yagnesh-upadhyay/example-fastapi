FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

# Fix invalid versions + upgrade pip
RUN pip install --upgrade pip && \
    sed -i 's/alembic.*/alembic==1.16.5/g' requirements.txt && \
    sed -i 's/anyio.*/anyio==4.12.1/g' requirements.txt && \
    cat requirements.txt && \
    pip install --no-cache-dir -r requirements.txt


COPY . .

CMD [ "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000" ]