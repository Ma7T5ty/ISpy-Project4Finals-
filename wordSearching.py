from PIL import Image
import pyscreenshot
import pytesseract
from pytesseract import Output
import cv2  



def word_search(word_list):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    screenshot = pyscreenshot.grab()
    screenshot.save('sample_image.png')
    img = cv2.imread('sample_image.png')
    fixed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    data = pytesseract.image_to_data(
        processed_img,
        lang="eng",
        output_type=Output.DICT
    )

    word_found = False
    for i, word in enumerate(data["text"]):
        word = word.strip()
        
        if not word:
            continue

        word_matches = False
        for candidate in word_list:
            #print(candidate.lower() +" == "+ word.lower())
            if candidate.lower() == word.lower():
                word_found = True
                word_matches = True
        
        if not word_matches:
            continue

        try:
            confidence = float(data["conf"][i])
        except (TypeError, ValueError):
            continue

        if confidence < 0:
            continue

        x = int(data["left"][i])
        y = int(data["top"][i])
        w = int(data["width"][i])
        h = int(data["height"][i])

        cv2.rectangle(
            fixed_img,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2
        )

    if word_found == True:
        regular_image = Image.fromarray(fixed_img)
        return regular_image
    else:
        return
#key words