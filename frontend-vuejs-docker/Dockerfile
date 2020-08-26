# We name the phase as builder
# We are only going to use build directory in the next phase

# Build Phase
FROM node:alpine

RUN mkdir /app
WORKDIR /app

COPY ./frontend-vue/package.json ./
RUN npm install

COPY ./frontend-vue/ ./
RUN npm build

# The build directory is going to be created in working directory /app
# The path to build directory is /app/build

# Just putting a FROM statement mean that new phase has started
# Run Phase
FROM nginx
# Required for AWS Elastic Beanstalk
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=0 /app/build /usr/share/nginx/html

# We don't need start command
# The default start command of the nginx container starts nginx
