build:
	docker build -t magahet/twilio-phone-tree .
test:
	docker run -i magahet/twilio-phone-tree nosetests
dev:
	docker run -d -p 5000:5000 -v ${CURDIR}/conf:/etc/phone-tree -v ${CURDIR}/webapp:/webapp magahet/twilio-phone-tree
prod:
	docker run -d -p 5000:5000 -v ${CURDIR}/conf:/etc/phone-tree magahet/twilio-phone-tree
