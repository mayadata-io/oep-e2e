#-----------------------------
# build testplan site
#-----------------------------
FROM node:10.18.0 AS build-env

WORKDIR /app/

EXPOSE 3000 35729

COPY blog/ /app/blog/
COPY docs/ /app/docs/
COPY src/ /app/src/
COPY static/ /app/static/
COPY docusaurus.config.js /app/
COPY nginx-custom.conf /app/
COPY package.json /app/
COPY sidebars.js /app/
COPY tag.py /app/

# remove shared cache files
RUN yarn cache clean

# install project dependencies
RUN yarn install
RUN yarn build

#---------------------------------
# sample usage
# docker run -it -p 3000:3000 mayadata/plan:latest npm start --host 0.0.0.0
# open your browser & type localhost:3000
#---------------------------------

# Second stage build to deploy above built site into nginx
FROM nginx:1.13
COPY --from=build-env ./app/build /usr/share/nginx/html
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf
