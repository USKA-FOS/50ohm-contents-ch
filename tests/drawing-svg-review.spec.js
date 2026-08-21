const { test, expect } = require("@playwright/test");

const screenshotDir = "work/drawing_svg_review/screenshots";

async function expectLoadedImages(page) {
  for (const language of ["de", "fr", "it"]) {
    const image = page.locator(`#image-${language}`);
    await expect(image).toBeVisible();
    await expect
      .poll(() => image.evaluate((element) => element.complete && element.naturalWidth > 0))
      .toBe(true);
  }
}

test("shows and navigates the trilingual drawing set", async ({ page, request }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  const response = await request.get("/api/drawings");
  expect(response.ok()).toBeTruthy();
  const payload = await response.json();
  expect(payload.drawings).toHaveLength(174);
  expect(payload.languages).toEqual(["de", "fr", "it"]);

  await page.goto("/#689");
  await expect(page.locator("#drawing-select")).toHaveValue("689");
  await expectLoadedImages(page);

  const index = payload.drawings.indexOf("689");
  const nextDrawing = payload.drawings[index + 1];
  await page.locator("#next").click();
  await expect(page.locator("#drawing-select")).toHaveValue(nextDrawing);
  await expectLoadedImages(page);

  await page.keyboard.press("ArrowLeft");
  await expect(page.locator("#drawing-select")).toHaveValue("689");
  await page.locator("#zoom-in").click();
  await expect(page.locator("#zoom-value")).toHaveText("110%");

  const panels = page.locator(".language-panel");
  await expect(panels).toHaveCount(3);
  for (let panelIndex = 0; panelIndex < 3; panelIndex += 1) {
    const box = await panels.nth(panelIndex).boundingBox();
    expect(box.width).toBeGreaterThan(400);
    expect(box.height).toBeGreaterThan(600);
  }

  await page.screenshot({
    path: `${screenshotDir}/drawing-review-desktop.png`,
    fullPage: true,
  });
});

test("keeps controls and drawings within a mobile viewport", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/#689");
  await expectLoadedImages(page);

  const dimensions = await page.evaluate(() => ({
    viewportWidth: window.innerWidth,
    documentWidth: document.documentElement.scrollWidth,
    panels: [...document.querySelectorAll(".language-panel")].map((panel) => {
      const box = panel.getBoundingClientRect();
      return { left: box.left, right: box.right, width: box.width };
    }),
  }));
  expect(dimensions.documentWidth).toBeLessThanOrEqual(dimensions.viewportWidth);
  for (const panel of dimensions.panels) {
    expect(panel.left).toBeGreaterThanOrEqual(0);
    expect(panel.right).toBeLessThanOrEqual(dimensions.viewportWidth);
  }

  await page.screenshot({
    path: `${screenshotDir}/drawing-review-mobile.png`,
    fullPage: true,
  });
});
