FROM python:3

ENV SECRET_KEY="django-insecure--emq89lz76bn32hh@4j*^r3jd&gn*=1m6o3vaqx-(7@wt^6i_n"
ENV DEBUG True
ENV DB_NAME=postgres
ENV DB_USER=postgres
ENV DB_PASSWORD=LF4d!@54?5CwJCi
ENV DB_HOST=db.okxewfmlrzbcclpqqvfd.supabase.co
ENV DB_PORT=5432

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app