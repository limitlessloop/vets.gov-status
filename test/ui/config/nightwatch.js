/* eslint-disable camelcase, strict */
"use strict";
const path = require('path');

module.exports = {
    output_folder: "./logs/nightwatch",
    src_folders: "./",
    custom_commands_path: "./nightwatch-commands/",
    live_output: true,
    parallel_process_delay: 10,
    disable_colors: process.env.BUILDTYPE === "production",
    test_workers: false,
    webdriver: {
        start_process: true,
        server_path: "node_modules/.bin/chromedriver",
        cli_args: [
          "--verbose"
        ],
        port: 9515,
        log_path: "./logs"
    },
    test_settings: {
        default: {
            launch_url: `file://${path.resolve(__dirname, '../../../_site/index.html')}`,
            filter: "**/*.e2e.spec.js",
            use_ssl: false,
            silent: true,
            output: true,
            screenshots: {
                enabled: true,
                on_failure: true,
                path: "logs/screenshots"
            },
            desiredCapabilities: {
                browserName: "chrome",
                javascriptEnabled: true,
                acceptSslCerts: true,
                webStorageEnabled: true,
                chromeOptions: {
                    args: ["--window-size=1024,768", "no-sandbox", "disable-gpu"],
                    w3c: false
                }
            },
        },
        headless: {
            desiredCapabilities: {
                chromeOptions: {
                    args: ["--headless", "--window-size=1024,768"]
                }
            }
        }
    }
};