from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
import time
import os


class DXFactorScraper:
    def __init__(self, base_url="https://www.dxfactor.com", output_file="dxfactor_data.txt", headless=True, sleep_time=2):
        self.base_url = base_url
        self.output_file = output_file
        self.sleep_time = sleep_time
        self.driver = self._init_driver(headless=headless)

    def _init_driver(self, headless=True):
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920x1080")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    ## function for cleaning the text having unwanted data
    def _clean_text(self, raw_text):
        lines = raw_text.split("\n")
        cleaned = []
        for line in lines:
            line = line.strip()
            if not line or len(line) < 20:
                continue
            if any(x in line.lower() for x in [
                "privacy policy", "terms", "cookie", "linkedin", "facebook", "instagram", "subscribe",
                "2024", "dx", "contact us", "home", "menu"
            ]):
                continue
            cleaned.append(line)
        return "\n".join(cleaned)

    ## function to get all the internal links from the website
    def _get_internal_links(self):
        self.driver.get(self.base_url)
        time.sleep(self.sleep_time)
        elements = self.driver.find_elements(By.TAG_NAME, "a")
        links = set()
        for elem in elements:
            href = elem.get_attribute("href")
            if href and "dxfactor.com" in href:
                parsed = urlparse(href)
                clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                links.add(clean_url)
        return links

    ## function to scrape the content from all links
    def scrape(self):
        all_content = ""
        links = self._get_internal_links()

        print(f"Found {len(links)} internal links to scrape.\n")

        for link in links:
            try:
                print(f"Scraping: {link}")
                self.driver.get(link)
                time.sleep(self.sleep_time)

                body_text = self.driver.find_element(By.TAG_NAME, "body").text
                cleaned_text = self._clean_text(body_text)

                if cleaned_text:
                    all_content += f"\n\n---\n{link}\n{cleaned_text}\n"
            except Exception as e:
                print(f"Failed to scrape {link}: {e}")

        self.driver.quit()

        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write(all_content)

        print(f"\nFinished scraping DXFactor. Clean content saved to '{self.output_file}'.")

# Example usage
if __name__ == "__main__":
    scraper = DXFactorScraper()
    scraper.scrape()
