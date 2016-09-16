build:
	docker build -t magahet/twilio-phone-tree .
test:
	docker run -i magahet/twilio-phone-tree nosetests
dev:
	docker run -d -p 5000:5000 -v ${CURDIR}/conf/phone-tree.yaml:/etc/phone-tree/phone-tree.yaml -v ${CURDIR}/webapp:/webapp magahet/twilio-phone-tree
prod:
	docker run -d -p 5000:5000 -v ${CURDIR}/conf/phone-tree.yaml:/etc/phone-tree/phone-tree.yaml magahet/twilio-phone-tree
