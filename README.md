# ocr_verify_bom

# Purpose of the program
This project's aims to assist the end user to verify the "bill of material" of finished products. 
By providing a screenshot of the bill of material, the program finds the article components and draws a rectangle around the detected article numbers.
This helps relieve the user from the tidious task of checking every article line by line and helps reduce error.

# How to use this program
The user is able to take a screenshot by pressing the "screenshot" button, this function opens a transparent window defining the position and size of the screenshot.
Once the screenshot has been taken, it is displayed in the main window and can be "analyzed".
The numbers get detected with pytesseract.

# Futur improvements/addon's
* Store the data in a database instead of a json file.
* Visualize the saved "bill of materials" in a treeview
