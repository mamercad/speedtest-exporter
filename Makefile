.PHONY: build
build:
	docker build -t speedtest-exporter:latest .

.PHONY: run
run:
	docker run --rm -p 10101:10101/tcp speedtest-exporter:latest
