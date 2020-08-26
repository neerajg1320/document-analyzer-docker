FROM nginx
# Required for AWS Elastic Beanstalk
EXPOSE 4000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./frontend-jquery /usr/share/nginx/html
