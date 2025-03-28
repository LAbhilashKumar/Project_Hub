# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pyautogui as py
# import time
# def internet(x,speak):
#     # chrome_opened= False
#     # options.add_argument("--headless")
#     driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
#     global chrome_opened
#     chrome_opened = True
#     driver.get("https://www.blackbox.ai/")
#
#     speak("1st time completed ")
#     # try:
#     #     speak("in try block ")
#     #     blackbox_textarea = driver.find_element(By.CLASS_NAME, "resize-none")
#     # except:
#     speak("in except block ")
#     time.sleep(5)
#     blackbox_textarea = driver.find_element(By.XPATH,'//*[@id="chat-input-box"]')
#     time.sleep(5)
#     speak("2 time completed ")
#     template= "in need in short paragraph wise"
#     if "weather" in x:
#         x+="in hyderabad"
#         blackbox_textarea.send_keys(x, " ", template)
#     else:
#         blackbox_textarea.send_keys(x," ",template )
#     time.sleep(5)
#     py.press("enter")
#
#     # py.press("enter")
#     xpath = "/html/body/div[2]/main/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[1]/div"
#     # xpath= "/html/body/div[2]/main/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[6]/div[1]/div/div/div[4]"
#     try:
#         time.sleep(10)
#         # Wait until at least one element with the class name 'prose' is present
#         WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath)))
#
#         # Fetch all elements with the class name 'prose'
#         elements = driver.find_elements(By.XPATH, xpath)
#         # time.sleep(20)
#         # Debug: speak the number of elements found
#         speak(f"Number of elements with class 'prose': {len(elements)}")
#
#         # Access the last element's text if the list is not empty
#         if elements:
#             speak("in if block ")
#             last_element = elements[-1]  # Get the last element in the list
#             # speak("Last Element Text:", last_element.text)
#             speak(type(last_element.text))
#         #     add speak function here
#             last=last_element.text.strip("BLACKBOXAI")
#             # last=last_element.text.strip("\n")[8:]
#             # speak("speaking last element",last)
#             speak(last)
#         else:
#             speak("unable to fetch the content.")
#
#     except Exception as e:
#         speak( "unknown error has occurred, could you please say that again.")
#         # driver.quit()
# #
# speak(internet("who scored most runs in the ipl"))


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)


def internet():
    print("accessing website")
    driver.get("https://www.blackbox.ai/")
    print("accessed website")


a = 0


def sendkeys(x,speak):
    speak("Analyzing... Give me a second.")
    # time.sleep(2)

    # Locate the input box
    blackbox_textarea = driver.find_element(By.XPATH, '//*[@id="chat-input-box"]')

    template = "in short !"
    if "weather" in x:
        x += " in Hyderabad"
        blackbox_textarea.send_keys(x, " " + template)
    else:
        blackbox_textarea.send_keys(x, " " + template)

    speak("Processing your request... ")
    time.sleep(3)

    # Locate and click the submit button instead of pressing Enter
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    speak(" On it,... Give me a moment to process")

    time.sleep(2)
    # Wait for response to appear
    global a
    b = a + 2
    a = b
    # response_xpath = f"/html/body/div[2]/main/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[{b}]/div[1]/div/div"
    response_xpath =f"/html/body/div[2]/main/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[1]/div/div"

    # time.sleep(5)
    time.sleep(2)
    speak("Processing, boss... Remember, this is still a prototype.")
    try:
        WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, response_xpath)))

        elements = driver.find_elements(By.XPATH, response_xpath)
        print(f"Number of elements found: {len(elements)}")
        speak("Almost there, boss... Just a few more seconds")

        if elements:
            speak("Fetching response...")
            last_element = elements[-1]
            last = last_element.text.strip("BLACKBOXAI")
            int_re = "here is what i found from  : " + last
            speak(int_re)
        else:
            speak("Unable to fetch the content.")

    except Exception as e:
        speak("Unknown error occurred, could you please say that again.")

# internet()
# sendkeys("what is ml")
# sendkeys("if dinosaurs would exists now? how would humans adopt to it?")
# sendkeys("todays weather")
# sendkeys("todays special")
