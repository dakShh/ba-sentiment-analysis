
import sys
from app import scrapper

if __name__ == "__main__":
    try:
        scrapper.start_scraping()
        print("Done!")
        scrapper.view_all_reviews()
        scrapper.save_to_csv()
    except Exception as e:
          # Get exception info
        exc_type, exc_obj, exc_tb = sys.exc_info()

        # Extract line number, function name, and error message
        line_number = exc_tb.tb_lineno
        function_name = exc_tb.tb_frame.f_code.co_name
        error_message = str(exc_obj)  # Get the error message

        # Print the detailed information
        print(f"Error occurred at line {line_number} in function '{function_name}':", error_message)
