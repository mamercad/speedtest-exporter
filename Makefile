.PHONY: build
build:
	docker build -t speedtest-exporter:latest .

.PHONY: run
run:
	docker run --rm -p 10101:10101/tcp speedtest-exporter:latest

.PHONY: install
install:
	cp speedtest-exporter.py /usr/local/bin/
	cp speedtest-exporter.service /etc/systemd/system/
	systemctl daemon-reload
	systemctl enable speedtest-exporter
	systemctl start speedtest-exporter
