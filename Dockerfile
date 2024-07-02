FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

RUN pip3 install opencv-python-headless==4.9.0.80 \
    && pip3 install opencv-contrib-python-headless==4.9.0.80

COPY my_function.py ./

CMD ["my_function.lambda_handler"]