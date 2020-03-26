#-----------------------------
# build testplan site
#-----------------------------
FROM node:8.11.4 AS build-env

WORKDIR /app/website

COPY ./docs /app/docs
COPY ./website /app/website
RUN yarn install
RUN yarn build
FROM nginx:1.13
COPY --from=build-env ./app/website/build/oeptestplan /usr/share/nginx/html
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf
# sample usage
# docker run -it -p 3000:3000 mayadata/plan:latest npm start --host 0.0.0.0
# open your browser & type localhost:3000
#---------------------------------

