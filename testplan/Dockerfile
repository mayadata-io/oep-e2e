#-----------------------------
# build testplan site
#-----------------------------
FROM node:10.9.0 AS build-env

WORKDIR /website

EXPOSE 3000 35729

COPY . /website

RUN yarn install
RUN yarn build

CMD ["yarn", "start"]

#---------------------------------
# Follow below steps to test this Dockerfile
#
# run docker build from root of this project
# docker build -t mayadataio/oep-e2eplan ./testplan/
#
# docker run -it -p 3000:3000 mayadataio/oep-e2eplan:latest yarn start --host 0.0.0.0
#
# open your browser & type localhost:3000
#---------------------------------
