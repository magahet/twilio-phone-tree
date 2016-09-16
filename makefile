build:
	docker build -t magahet/twilio-phone-tree:latest .
test:
	docker run -i magahet/twilio-phone-tree nosetests
dev:
	docker run -d -p 5000:5000 -v conf:/etc/phone-tree -v webapp:/webapp magahet/twilio-phone-tree
prod:
	docker run -d -p 5000:5000 -v conf:/etc/phone-tree magahet/phone-tree
