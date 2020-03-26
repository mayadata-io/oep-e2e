#-----------------------------
# build testplan site
#-----------------------------
FROM node:10.9.0 AS build-env

WORKDIR /app/website

EXPOSE 3000 35729

COPY ./docs /app/docs
#Docusauraus v2 has changed the directory structure. Contents inside website directory have been brought to the root folder. Check the following line
#COPY ./website /app/website

RUN yarn install
RUN yarn build

CMD ["yarn", "start"]

#---------------------------------
# sample usage
# docker run -it -p 3000:3000 mayadata/plan:latest npm start --host 0.0.0.0
# open your browser & type localhost:3000
#---------------------------------
