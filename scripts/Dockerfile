FROM python:3.6.8

WORKDIR application

ENV DATA_DIR="/application/data"
ENV CONFIG_DIR="/application"
# Store credentials in /tmp to avoid possibility of them being checked in
ENV GA_SERVICEACCOUNT="/tmp/serviceaccount.json"

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir --require-hashes --no-deps -r requirements.txt

COPY . .

CMD ["/application/fetch-data.sh"]
