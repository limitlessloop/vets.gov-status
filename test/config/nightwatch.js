/* eslint-disable camelcase, strict */
'use strict';

const fs = require('fs-extra');
const chromedriver = require('chromedriver');
const seleniumServer = require('selenium-server');

require('@babel/register');
require('@babel/polyfill');

const selenium_logs = './logs/selenium';
const selenium_server_port = process.env.SELENIUM_PORT || 4444;

fs.ensureDirSync(selenium_logs);

module.exports = {
  output_folder: './logs/nightwatch',
  src_folders: './',
  live_output: true,
  parallel_process_delay: 10,
  disable_colors: process.env.BUILDTYPE === 'production',
  test_workers: false,
  test_settings: {
    default: {
      launch_url: `localhost:4000`,
      filter: '**/*.e2e.spec.js',
      selenium_host: 'localhost',
      selenium_port: selenium_server_port,
      use_ssl: false,
      silent: true,
      output: true,
      screenshots: {
        enabled: true,
        on_failure: true,
        path: 'logs/screenshots',
      },
      desiredCapabilities: {
        browserName: 'chrome',
        javascriptEnabled: true,
        acceptSslCerts: true,
        webStorageEnabled: true,
        chromeOptions: {
          args: ['--window-size=1024,768'],
          w3c: false
        },
      },
      selenium: {
        cli_args: {
          'webdriver.chrome.driver': chromedriver.path,
        },
        start_process: true,
        server_path: seleniumServer.path,
        log_path: selenium_logs,
        host: '127.0.0.1',
        port: selenium_server_port,
      },
      test_workers: {
        enabled: false,
        workers: parseInt(process.env.CONCURRENCY || 1, 10),
      },
    },
    headless: {
      desiredCapabilities: {
        chromeOptions: {
          args: ['--headless', '--window-size=1024,768'],
        },
      },
    },
    bestpractice: {
      globals: {
        rules: ['section508', 'wcag2a', 'wcag2aa', 'best-practice'],
      },
    },
  },
};