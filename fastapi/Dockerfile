FROM python:3.11-slim
RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /product_categorization
COPY . .
RUN pipenv install --dev
EXPOSE 8080
CMD ["pipenv", "run", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]