import asyncio
import logging
from datetime import datetime
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
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
        
    async def scrape_cause_list(self, court_complex, court_number, date, case_type):
        """
        Automated form filling with iframe handling
        Manual captcha solving still required
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=False,
                slow_mo=500  # Slower for visibility
            )
            
            context = await browser.new_context()
            page = await context.new_page()
            
            try:
                print("\n" + "="*70)
                print("  COURT CAUSE LIST SCRAPER - AUTO FILL MODE")
                print("="*70)
                print(f"\n  Court Complex: {court_complex}")
                print(f"  Court Number: {court_number}")
                print(f"  Date: {date}")
                print(f"  Case Type: {case_type}")
                print("="*70)
                
                # Navigate to the page
                self.logger.info("Loading page...")
                await page.goto(BASE_URL, wait_until='domcontentloaded')
                await asyncio.sleep(3)
                
                form_frame = None
                try:
                    # A more direct way to find the iframe containing the form
                    self.logger.info("Looking for iframe with form...")
                    # Locate an iframe that contains our form's unique ID
                    iframe_locator = page.frame_locator('iframe:has(#ecourt-services-cause-list-cause-list)')
                    # Give it a moment to ensure it's there
                    await iframe_locator.locator('#ecourt-services-cause-list-cause-list').wait_for(timeout=5000)
                    form_frame = iframe_locator.frame
                    self.logger.info("Found form inside an iframe.")
                except PlaywrightTimeout:
                    # If the iframe isn't found within the timeout, assume the form is on the main page
                    self.logger.info("No iframe found, trying direct page access...")
                    form_frame = page
                
                # Wait for form to be ready
                await form_frame.wait_for_selector('#ecourt-services-cause-list-cause-list', timeout=10000)
                await asyncio.sleep(2)
                
                # Step 1: Select "Court Complex" radio button
                self.logger.info("Selecting Court Complex radio...")
                await form_frame.check('#chkYes')
                await asyncio.sleep(1)
                
                # Step 2: Select Court Complex from dropdown
                self.logger.info(f"Selecting court complex: {court_complex}")
                
                # Map court complex name to value
                court_complex_values = {
                    "District Court, Gurugram": "HRGR01,HRGR02,HRGR03",
                    "Judicial Complex, Sohna": "HRGRA0,HRGRA1",
                    "Judicial Complex, Pataudi": "HRGRB0,HRGRB1"
                }
                
                complex_value = court_complex_values.get(court_complex, "HRGR01,HRGR02,HRGR03")
                await form_frame.select_option('#est_code', value=complex_value)
                
                # Instead of a fixed sleep, wait intelligently for the dropdown to be populated.
                # This is more robust against network/server delays.
                self.logger.info("Waiting for court list to populate...")
                await form_frame.wait_for_selector('#court:not([disabled])', timeout=30000)
                await form_frame.wait_for_function("document.querySelectorAll('#court option').length > 1", timeout=30000)
                
                # Step 3: Select Court Number
                self.logger.info(f"Selecting court number: {court_number}")
                await asyncio.sleep(1)
                
                # Get all options from the court dropdown
                options = await form_frame.query_selector_all('#court option')
                target_option_value = None
                full_court_name = None
                for option in options:
                    option_text = await option.inner_text()
                    # Find the option that starts with the court number (e.g., "1 ", "2 ", etc.)
                    if option_text.strip().startswith(f"{court_number} "):
                        target_option_value = await option.get_attribute('value')
                        full_court_name = option_text.strip()
                        self.logger.info(f"Found matching court: '{full_court_name}'")
                        await form_frame.select_option('#court', value=target_option_value)
                        break
                
                if not target_option_value:
                    self.logger.error(f"Could not find a court matching number '{court_number}'. Please check the number and try again.")
                    raise Exception(f"Court number '{court_number}' not found in dropdown.")
                await asyncio.sleep(1)
                
                # Step 4: Set date
                self.logger.info(f"Setting date: {date}")
                
                # Use keyboard navigation for the date picker, as it's more reliable.
                # 1. Calculate day difference between today and target date.
                today = datetime.now().date()
                target_date_obj = datetime.strptime(date, "%d/%m/%Y").date()
                delta_days = (target_date_obj - today).days
                
                # 2. Click the calendar icon to open the date picker. It will focus on today's date.
                self.logger.info("Opening calendar widget...")
                await form_frame.click('button[aria-label="Choose Date"]')
                await asyncio.sleep(1) # Wait for dialog to appear
                
                # 3. Navigate using arrow keys.
                self.logger.info(f"Navigating {abs(delta_days)} days from today using arrow keys...")
                if delta_days > 0: # Future date
                    for _ in range(delta_days):
                        await form_frame.press('.datepickerDialog', 'ArrowRight')
                        await asyncio.sleep(0.1) # Small delay between key presses
                elif delta_days < 0: # Past date
                    for _ in range(abs(delta_days)):
                        await form_frame.press('.datepickerDialog', 'ArrowLeft')
                        await asyncio.sleep(0.1)
                
                # 4. Press Enter to confirm the date selection.
                self.logger.info("Confirming date with 'Enter' key...")
                await form_frame.press('.datepickerDialog', 'Enter')
                await asyncio.sleep(1)

                # Step 5: Select case type
                self.logger.info(f"Selecting case type: {case_type}")
                
                if case_type.lower() == "civil":
                    await form_frame.check('#chkCauseTypeCivil')
                else:
                    await form_frame.check('#chkCauseTypeCriminal')
                
                await asyncio.sleep(1)
                
                # Step 6: CAPTCHA - Manual solving
                print("\n" + "🔴"*35)
                print("⚠️  CAPTCHA SOLVING REQUIRED")
                print("🔴"*35)
                print("\n  The form has been filled automatically!")
                print(f"  Court: {court_complex}")
                print(f"  Court Number: {court_number}")
                print(f"  Date: {date}")
                print(f"  Case Type: {case_type}")
                print("\n  👉 Please solve the CAPTCHA in the browser")
                print("  👉 Then press ENTER here to continue...")
                print("🔴"*35 + "\n")
                
                # Wait for user to solve captcha
                input("  >>> Press ENTER after solving captcha <<<\n")
                
                # Step 7: Submit form
                self.logger.info("Submitting form...")
                await form_frame.click('input[type="submit"][value="Search"]')
                await asyncio.sleep(5)
                
                # Wait for results to load
                self.logger.info("Waiting for results...")
                await asyncio.sleep(3)
                
                # Step 8: Save as PDF
                # Use the full court name for a more descriptive filename.
                # Sanitize the name to make it safe for a filename.
                court_name_clean = full_court_name.replace(' - ', '_').replace(' ', '_').replace('.', '')
                court_name_clean = "".join(c for c in court_name_clean if c.isalnum() or c in ('_', '-'))
                
                date_clean = date.replace('/', '-')
                pdf_filename = f"{OUTPUT_DIR}/CauseList_{court_name_clean}_{case_type}_{date_clean}.pdf"
                
                self.logger.info(f"Saving as PDF: {pdf_filename}")
                
                # Save the entire page as PDF
                await page.pdf(
                    path=pdf_filename,
                    format='A3', # Use A3 for wider court lists
                    print_background=True,
                    margin={
                        'top': '20px',
                        'right': '20px',
                        'bottom': '20px',
                        'left': '20px'
                    }
                )
                
                # Also save screenshot
                screenshot_path = f"{OUTPUT_DIR}/screenshot_{court_name_clean}_{case_type}_{date_clean}.png"
                await page.screenshot(path=screenshot_path, full_page=True)
                
                print("\n" + "✓"*70)
                print(f"  ✅ SUCCESS!")
                print(f"  📄 PDF: {pdf_filename}")
                print(f"  📸 Screenshot: {screenshot_path}")
                print("✓"*70 + "\n")
                
                self.logger.info(f"Successfully saved: {pdf_filename}")
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
        Run multiple scrapes sequentially
        """
        total = len(court_numbers) * len(case_types)
        completed = 0
        successful = 0
        
        print(f"\n{'='*70}")
        print(f"  BATCH SCRAPE MODE")
        print(f"  Total: {total} scrapes")
        print(f"{'='*70}\n")
        
        for court_number in court_numbers:
            for case_type in case_types:
                completed += 1
                print(f"\n{'='*70}")
                print(f"  SCRAPE {completed} of {total}")
                print(f"{'='*70}")
                
                success = await self.scrape_cause_list(
                    court_complex=court_complex,
                    court_number=court_number,
                    date=date,
                    case_type=case_type
                )
                
                if success:
                    successful += 1
                
                if completed < total:
                    print(f"\n  ⏳ Next scrape in 3 seconds...")
                    await asyncio.sleep(3)
        
        print(f"\n{'='*70}")
        print(f"  BATCH COMPLETE")
        print(f"  ✅ Successful: {successful}/{total}")
        print(f"{'='*70}\n")
