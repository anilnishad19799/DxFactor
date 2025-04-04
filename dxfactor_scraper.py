from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager

class DXFactorScraper:
    def __init__(self, base_url="https://www.dxfactor.com/"):
        """Initialize the scraper with the website URL and Selenium configurations."""
        self.base_url = base_url
        self.options = Options()
        self.options.add_argument("--headless")  # Run in headless mode
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        
        # Setup WebDriver
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def get_internal_links(self):
        """Extract all internal links from the homepage."""
        self.driver.get(self.base_url)
        time.sleep(5)  # Wait for page to load
        
        links = set()
        elements = self.driver.find_elements(By.TAG_NAME, "a")
        
        for elem in elements:
            link = elem.get_attribute("href")
            if link and "dxfactor.com" in link:  # Only consider internal links
                links.add(link)
        
        return links

    def scrape_content(self):
        """Scrape text content from all collected internal pages."""
        links = self.get_internal_links()
        print(f"Found {len(links)} internal links to scrape.")

        all_content = ""
        for link in links:
            print(f"Scraping {link}...")
            self.driver.get(link)
            time.sleep(3)  # Wait for page to load
            
            try:
                page_content = self.driver.find_element(By.TAG_NAME, "body").text
                all_content += f"Content from {link}:\n{page_content}\n\n"
            except Exception as e:
                print(f"Error scraping {link}: {e}")

        self.driver.quit()
        return all_content

    def save_content(self, filename="dxfactor_data.txt"):
        """Save scraped content to a text file."""
        content = self.scrape_content()
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        
        print(f"✅ Website data scraped successfully and saved to {filename}.")

# Example Usage
if __name__ == "__main__":
    scraper = DXFactorScraper()
    scraper.save_content()
