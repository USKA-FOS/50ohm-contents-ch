const { defineConfig } = require("@playwright/test");

module.exports = defineConfig({
  testDir: "./tests",
  outputDir: "./work/drawing_svg_review/playwright-results",
  reporter: "line",
  use: {
    baseURL: "http://127.0.0.1:8765",
    browserName: "chromium",
    screenshot: "only-on-failure",
  },
  webServer: {
    command: "python tools/serve_drawing_svg_review.py --port 8765",
    url: "http://127.0.0.1:8765/api/drawings",
    reuseExistingServer: true,
    timeout: 15_000,
  },
});
