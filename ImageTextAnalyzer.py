import pyautogui
import pytesseract
import cv2


class ImageTextAnalyzer:

    # uncomment out first line of each method to run on windows, you must install pytesseract first, please see
    # install_instructions.txt for detailed instructions

    #TODO add more comments


    #takes 4 values which define rectangle and then scans text within that rectangle to see if specifiend text is found
    #returns True if found and False if not
    def is_text_in_rectangle(self, left_x, top_y, right_x, bottom_y, text: str):
        # pytesseract.pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        text_found = False
        image = pyautogui.screenshot(region=(left_x, top_y, right_x, bottom_y))
        image_text = pytesseract.image_to_string(image)
        if image_text.__contains__(text):
            text_found = True

        return text_found

    #takes screenshot of screen and returns all text found on the screen
    def scan_text_on_screen(self):
        # pytesseract.pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

        image = pyautogui.screenshot()
        image_text = pytesseract.image_to_string(image)

        return image_text

    #takes 4 values which define rectangle and then scans text within that rectangle
    #return all text found
    def scan_text_in_rectangle(self, left_x, top_y, right_x, bottom_y):
        # pytesseract.pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

        image = pyautogui.screenshot(region=(left_x, top_y, right_x, bottom_y))
        image_text = pytesseract.image_to_string(image)

        return image_text

    #takes path for image to scan
    #returns all text found within image
    def scan_text_in_image(self, image_path):
        # pytesseract.pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

        image = cv2.imread(image_path)
        image_text = pytesseract.image_to_string(image)

        return image_text

#uncomment below for simple test
#ita= ImageTextAnalyzer()
#result =ita.scan_text_in_image("test_image.png")
#print(result)




