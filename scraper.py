import asyncio
import logging
from datetime import datetime
from playwright.async_api import async_playwright
import os
from config import *

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'{LOG_DIR}/scraper.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class CourtCauseListScraper:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    async def scrape_and_save_as_pdf(self, court_complex, court_number, date, case_type):
        """
        Opens browser, you fill form manually, script saves result page as PDF
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=False,
                slow_mo=100
            )
            
            context = await browser.new_context()
            page = await context.new_page()
            
            try:
                print("\n" + "="*70)
                print("  COURT CAUSE LIST SCRAPER")
                print("="*70)
                print(f"\nTarget:")
                print(f"  Court Complex: {court_complex}")
                print(f"  Court Number: {court_number}")
                print(f"  Date: {date}")
                print(f"  Case Type: {case_type}")
                print("="*70)
                
                # Navigate to the page
                self.logger.info("Opening cause list page...")
                await page.goto(BASE_URL, wait_until='domcontentloaded')
                await asyncio.sleep(3)
                
                # Instructions for manual filling
                print("\n" + ">"*70)
                print("  PLEASE COMPLETE THE FOLLOWING STEPS:")
                print(">"*70)
                print(f"\n  1. Select Court Complex: {court_complex}")
                print(f"  2. Select Court Number: {court_number}")
                print(f"  3. Enter Date: {date}")
                print(f"  4. Select Case Type: {case_type}")
                print("  5. Solve the CAPTCHA")
                print("  6. Click 'Search' button")
                print("\n" + ">"*70)
                
                # Wait for user input to continue
                print("\n  Waiting for you to complete the form...")
                input("\n  >>> Press ENTER after you click Search and see the results table <<<\n")
                
                # Give time for page to load results
                print("\n  Waiting for results to load...")
                await asyncio.sleep(5)
                
                # Take screenshot for verification
                screenshot_path = f"{OUTPUT_DIR}/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                await page.screenshot(path=screenshot_path, full_page=True)
                self.logger.info(f"Screenshot saved: {screenshot_path}")
                
                # Save the page as PDF
                court_num_clean = str(court_number).replace(' ', '_').replace('.', '').replace(',', '')
                date_clean = date.replace('/', '-')
                pdf_filename = f"{OUTPUT_DIR}/CauseList_Court{court_num_clean}_{case_type}_{date_clean}.pdf"
                
                self.logger.info(f"Saving page as PDF: {pdf_filename}")
                
                # Save as PDF with proper formatting
                await page.pdf(
                    path=pdf_filename,
                    format='A4',
                    print_background=True,
                    margin={
                        'top': '20px',
                        'right': '20px',
                        'bottom': '20px',
                        'left': '20px'
                    }
                )
                
                print("\n" + "✓"*70)
                print(f"  SUCCESS! PDF saved: {pdf_filename}")
                print("✓"*70 + "\n")
                self.logger.info(f"PDF saved successfully: {pdf_filename}")
                
                return True
                
            except Exception as e:
                self.logger.error(f"Error: {str(e)}")
                
                # Save error screenshot
                try:
                    error_screenshot = f"{OUTPUT_DIR}/error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    await page.screenshot(path=error_screenshot, full_page=True)
                    self.logger.info(f"Error screenshot: {error_screenshot}")
                except:
                    pass
                
                return False
                
            finally:
                print("\n  Keeping browser open for 5 seconds...")
                await asyncio.sleep(5)
                await browser.close()
                self.logger.info("Browser closed.")
    
    async def run_batch_scrape(self, court_complex, court_numbers, date, case_types):
        """
        Run multiple scrapes (one at a time, with manual filling)
        """
        total = len(court_numbers) * len(case_types)
        completed = 0
        successful = 0
        
        print(f"\n{'='*70}")
        print(f"  BATCH SCRAPE MODE")
        print(f"  Total scrapes: {total}")
        print(f"{'='*70}\n")
        
        for court_number in court_numbers:
            for case_type in case_types:
                completed += 1
                print(f"\n{'='*70}")
                print(f"  SCRAPE {completed} of {total}")
                print(f"{'='*70}")
                
                success = await self.scrape_and_save_as_pdf(
                    court_complex=court_complex,
                    court_number=court_number,
                    date=date,
                    case_type=case_type
                )
                
                if success:
                    successful += 1
                
                if completed < total:
                    print(f"\n  Next scrape starting in 3 seconds...")
                    await asyncio.sleep(3)
        
        print(f"\n{'='*70}")
        print(f"  BATCH COMPLETE")
        print(f"  Successful: {successful}/{total}")
        print(f"{'='*70}\n")
