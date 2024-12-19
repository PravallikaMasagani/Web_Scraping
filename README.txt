# OCR and Sports Data Scraper

This project consists of two Python scripts:
1. **OCR Script**: Extracts text from an image using Tesseract OCR and counts the frequency of words.
2. **Sports Data Scraper**: Scrapes sports-related content from Wikipedia's Current Events portal.

## Files Overview
- **image.py**: Contains the code for OCR functionality.
- **sports.py**: Contains the code for scraping sports data.
- **requirements.txt**: Lists the Python packages required to run the scripts.

## Instructions

### Prerequisites
1. Install Python (>=3.7).
2. Install pip (Python package manager).
3. Install Tesseract OCR and configure its path if not already installed. On Windows, set the `tesseract_cmd` variable in the script to the location of `tesseract.exe`.

### Setup
1. Clone or download this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### OCR Script
1. Place the input image file in the project directory.
2. Update the `image_path` variable in the script with the name of your image file.
3. Run the OCR script:
   ```bash
   python image.py
   ```
4. The script will extract text from the image, process it, and display a word count map.

#### Sports Data Scraper
1. Ensure your machine has an active internet connection.
2. Update the `url` variable in the script if scraping from a different webpage.
3. Run the scraper:
   ```bash
   python sports.py
   ```
4. The script will scrape sports-related content from the specified webpage and display it.

## Notes
- Make sure the image file is clear and properly formatted for accurate OCR results.
- The scraper is designed for Wikipedia's Current Events page but can be adjusted for other websites.

---


