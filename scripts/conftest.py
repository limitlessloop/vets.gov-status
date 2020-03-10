import pytest


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('DATA_DIR', 'data')
    monkeypatch.setenv('CONFIG_DIR', '')
    monkeypatch.setenv('GA_SERVICEACCOUNT', 'serviceaccount.json')
    monkeypatch.setenv('MARKDOWN_DIR', 'migration_status')
