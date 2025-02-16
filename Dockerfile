FROM python:3.11-slim
RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /product_categorization_training

COPY notebooks /product_categorization_training/notebooks
COPY Pipfile Pipfile.lock /product_categorization_training/
COPY data/datasets /product_categorization_training/data/datasets

RUN pipenv install --dev
RUN pipenv run jupyter nbconvert --to script ./notebooks/model_train.ipynb

WORKDIR /product_categorization_training/notebooks

VOLUME ["/product_categorization_training/data/models"]

CMD ["pipenv", "run", "python", "model_train.py"]