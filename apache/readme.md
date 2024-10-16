#Build image
docker build -t apache-demo-image .
docker run -d -p 8080:80 -v ./pages:/usr/local/apache2/htdocs/ --name apache-demo-container apache-demo-image