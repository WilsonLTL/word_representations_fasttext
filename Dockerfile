FROM python:3.6.1
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python","main.py"]



# docker build -t ft_im .
# docker images
# docker run -p 5000:80 ft_im