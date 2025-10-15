import asyncio
import os
from datetime import datetime
from scraper import CourtCauseListScraper
from config import *

def setup_directories():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)

def get_date_input():
    today = datetime.now().strftime("%d/%m/%Y")
    print(f"\n  Today's date: {today}")
    date_input = input(f"  Enter date (dd/mm/yyyy) or press Enter for today: ").strip()
    return date_input if date_input else today

async def main():
    setup_directories()
    
    print("\n" + "="*70)
    print("  COURT CAUSE LIST SCRAPER")
    print("  Gurugram District Courts")
    print("="*70)
    print("\n  How it works:")
    print("  1. Script opens browser to the cause list page")
    print("  2. YOU manually fill the form and solve captcha")
    print("  3. YOU click Search and press ENTER in terminal")
    print("  4. Script saves the results page as PDF")
    print("="*70)
    
    scraper = CourtCauseListScraper()
    
    print("\n  Options:")
    print("    1. Single Scrape (Quick - Best for demo)")
    print("    2. Batch Scrape (Multiple courts)")
    print("    3. Exit")
    print("="*70)
    
    choice = input("\n  Your choice (1-3): ").strip()
    
    if choice == "1":
        print("\n" + "="*70)
        print("  SINGLE SCRAPE MODE")
        print("="*70)
        
        court_number = input("\n  Court number (e.g., 1): ").strip()
        
        print("\n  Case Type:")
        print("    1. Civil")
        print("    2. Criminal")
        case_choice = input("  Your choice (1 or 2): ").strip()
        case_type = "Civil" if case_choice == "1" else "Criminal"
        
        date = get_date_input()
        
        print("\n  Starting scrape...")
        await scraper.scrape_and_save_as_pdf(
            court_complex=DEFAULT_COURT_COMPLEX,
            court_number=court_number,
            date=date,
            case_type=case_type
        )
        
    elif choice == "2":
        print("\n" + "="*70)
        print("  BATCH SCRAPE MODE")
        print("="*70)
        
        court_numbers_input = input("\n  Court numbers (comma-separated, e.g., 1,2,3): ").strip()
        court_numbers = [num.strip() for num in court_numbers_input.split(',')]
        
        print("\n  Case Types:")
        print("    1. Civil only")
        print("    2. Criminal only")
        print("    3. Both")
        case_choice = input("  Your choice (1-3): ").strip()
        
        if case_choice == "1":
            case_types = ["Civil"]
        elif case_choice == "2":
            case_types = ["Criminal"]
        else:
            case_types = CASE_TYPES
        
        date = get_date_input()
        
        total = len(court_numbers) * len(case_types)
        print(f"\n  Total PDFs to create: {total}")
        
        confirm = input("\n  Continue? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("\n  Cancelled.")
            return
        
        await scraper.run_batch_scrape(
            court_complex=DEFAULT_COURT_COMPLEX,
            court_numbers=court_numbers,
            date=date,
            case_types=case_types
        )
        
    elif choice == "3":
        print("\n  Goodbye!")
        return
    
    else:
        print("\n  Invalid choice!")
        return
    
    print("\n" + "="*70)
    print("  ALL DONE!")
    print(f"  PDFs saved in: {OUTPUT_DIR}/")
    print(f"  Logs saved in: {LOG_DIR}/")
    print("="*70 + "\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n  Interrupted by user")
    except Exception as e:
        print(f"\n  Error: {str(e)}")
