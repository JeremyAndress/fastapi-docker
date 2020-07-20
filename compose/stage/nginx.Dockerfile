FROM nginx:1.19.1-alpine
ADD /nginx/site.conf /etc/nginx/conf.d/default.conf
