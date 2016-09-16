build:
	docker build -t phone-tree:latest .
test:
	docker run -i phone-tree nosetests
dev:
	docker run -d -p 5000:5000 -v conf:/etc/phone-tree -v webapp:/webapp phone-tree
prod:
	docker run -d -p 5000:5000 -v conf:/etc/phone-tree phone-tree
