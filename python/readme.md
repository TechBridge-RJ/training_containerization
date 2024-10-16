# Build and run image
docker build -t python-demo-image .
docker run -d -p 5000:5000 -v ./backend_api:/app --name python-demo-container python-demo-image:latest