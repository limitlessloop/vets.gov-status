FROM python:3.6.8

WORKDIR application

ENV DATA_DIR="/application/data" \
    CONFIG_DIR="/application" \
    GA_SERVICEACCOUNT="/application/serviceaccount.json" \
    MARKDOWN_DIR="/application/migration_status"

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir --require-hashes --no-deps -r requirements.txt

COPY . .

CMD ["/application/updates.sh"]
