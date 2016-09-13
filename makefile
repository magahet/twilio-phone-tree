build:
	docker build -t phone-tree:latest .
run:
	docker run -d -p 5000:5000 phone-tree
dev:
	docker run -d -p 5000:5000 -v webapp:/webapp phone-tree
