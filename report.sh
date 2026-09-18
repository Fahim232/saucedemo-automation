#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
allure generate allure-results --clean -o allure-report
allure open allure-report