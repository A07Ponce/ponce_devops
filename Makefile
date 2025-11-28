IMAGE_NAME=alisson
GHCR_USER=a07ponce
VERSION=3.0.0

build:
	docker build -t $(IMAGE_NAME) -f alisson .

run:
	docker run -p 5000:5000 $(IMAGE_NAME)

tag:
	docker tag $(IMAGE_NAME) ghcr.io/$(GHCR_USER)/$(IMAGE_NAME):$(VERSION)

push: tag
	docker push ghcr.io/$(GHCR_USER)/$(IMAGE_NAME):$(VERSION)
