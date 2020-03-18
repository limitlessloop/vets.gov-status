/* eslint-disable camelcase, strict */
"use strict";
require("@babel/register");
require("@babel/polyfill");

const selenium_server_port = 4444;
const selenium_host = process.env.selenium_host || "localhost";
const jekyll_port = 4000;
const jekyll_host = process.env.jekyll_host || "localhost";

module.exports = {
    output_folder: "./logs/nightwatch",
    src_folders: "./",
    custom_commands_path: "./nightwatch-commands/",
    live_output: true,
    parallel_process_delay: 10,
    disable_colors: process.env.BUILDTYPE === "production",
    test_workers: false,
    test_settings: {
        default: {
            launch_url: `http://${jekyll_host}:${jekyll_port}/scorecard/`,
            filter: "**/*.e2e.spec.js",
            selenium_host: selenium_host,
            selenium_port: selenium_server_port,
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
                    args: ["--window-size=1024,768"],
                    w3c: false
                }
            },
            selenium: {
                start_process: false,
                host: selenium_host,
                port: selenium_server_port
            },
            test_workers: {
                enabled: false,
                workers: parseInt(process.env.CONCURRENCY || 1, 10)
            }
        },
        headless: {
            desiredCapabilities: {
                chromeOptions: {
                    args: ["--headless", "--window-size=1024,768"]
                }
            }
        },
        bestpractice: {
            globals: {
                rules: ["section508", "wcag2a", "wcag2aa", "best-practice"]
            }
        }
    }
};