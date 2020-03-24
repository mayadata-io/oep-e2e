#-----------------------------
# build testplan site
#-----------------------------
FROM node:8.11.4 AS build-env

WORKDIR /app/website

EXPOSE 3000 35729

COPY ./docs /app/docs
COPY ./website /app/website

RUN yarn install
RUN yarn build

CMD ["yarn", "start"]

#---------------------------------
# sample usage
# docker run -it -p 3000:3000 mayadata/plan:latest npm start --host 0.0.0.0
# open your browser & type localhost:3000
#---------------------------------
