FROM public.ecr.aws/lambda/python:3.10

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN pip install opencv-python-headless==4.9.0.80 \
    && pip install opencv-contrib-python-headless==4.9.0.80

COPY my_function.py ./

CMD ["my_function.lambda_handler"]