#-----------------------------
# build testplan site
#-----------------------------
FROM node:10.9.0 AS build-env

WORKDIR /app/

EXPOSE 3000 35729

COPY . /app
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
FROM nginx:1.13
COPY --from=build-env ./app/website/build /usr/share/nginx/html
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf
