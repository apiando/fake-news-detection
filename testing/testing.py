import subprocess 
import pytest
import time
from playwright.async_api import async_playwright, expect
import sys




@pytest.fixture(scope="session", autouse=True)
def flask_server():
    # Start Flask in the background
    flask_process = subprocess.Popen(["python", "app.py"])
    
    yield
    flask_process.terminate()  # Cleanup
    flask_process.wait()



#Real news from our True.csv
@pytest.mark.asyncio
async def test_true():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        print("reached tests")
        
        try:
            await page.goto("http://127.0.0.1:5000/")
            print("opened homepage")

            print("Locating Inspect Page")
            await page.get_by_role("link", name="Inspect", exact=True).click()
            print("putting fake article text")
            await page.locator("textarea").fill("The conversation between Papadopoulos and the diplomat, " \
                                                "Alexander Downer, in London was a driving factor behind the " \
                                                "FBI’s decision to open a counter-intelligence investigation " \
                                                "of Moscow’s contacts with the Trump campaign, the Times reported. " \
                                                "Two months after the meeting, Australian officials passed the information " \
                                                "that came from Papadopoulos to their American counterparts when leaked " \
                                                "Democratic emails began appearing online, according to the newspaper, which" \
                                                " cited four current and former U.S. and foreign officials. Besides the information " \
                                                "from the Australians, the probe by the Federal Bureau of Investigation was also propelled " \
                                                "by intelligence from other friendly governments, including the British and Dutch," \
                                                " the Times said. Papadopoulos, a Chicago-based international energy lawyer, " \
                                                "pleaded guilty on Oct. 30 to lying to FBI agents about contacts with people who claimed" \
                                                " to have ties to top Russian officials.")
            print("clicking to submit")
            await page.locator("button:has-text('Inspect')").click()
            print("looking for predictions")
            # Wait for results to appear - adjust selector as needed
            result_section = page.locator('div.result')
            await expect(result_section).to_be_visible()
            
        except Exception as e:
            print(f"Test failed: {e}")
            raise
        finally:
            await browser.close()
            



#Real news from outside source: World Health Organization
#gets to inspector via Try Inspector Link
@pytest.mark.asyncio
async def test_real(): 
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        print("reached tests")
        
        try:
            await page.goto("http://127.0.0.1:5000/")
            print("opened homepage")
            inspect_link = page.get_by_text("Try the Inspector", exact=True)
            await expect(inspect_link).to_be_visible()
            await inspect_link.click()
            print("Clicked 'Try the Inspector'")
            
            
            
            # 3. Wait for textarea to be ready
            textarea = page.locator("textarea")
            await expect(textarea).to_be_editable()
            
            
            
            # 4. Fill the form
            await page.locator("textarea").fill("Most people infected with the virus will experience" \
                                                " mild to moderate respiratory illness and recover without" \
                                                " requiring special treatment. However, some will become" \
                                                " seriously ill and require medical attention. Older peopl" \
                                                "e and those with underlying medical conditions like cardiovascular" \
                                                " disease, diabetes, chronic respiratory disease, or cancer" \
                                                " are more likely to develop serious illness. Anyone can get sick" \
                                                " with COVID-19 and become seriously ill or die at any age")
            print("clicking to submit")
            await page.locator("button:has-text('Inspect')").click()
            print("looking for predictions")
            # Wait for results to appear - adjust selector as needed
            result_section = page.locator('div.result')
            await expect(result_section).to_be_visible()
            
        except Exception as e:
            print(f"Test failed: {e}")
            raise
        finally:
            await browser.close()
           


    

 #Fake news from our Fake.csv
 #also clicks the Demo Page
@pytest.mark.asyncio
async def test_fake(): 
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        print("reached tests")
        
        try:
            await page.goto("http://127.0.0.1:5000/")
            print("opened homepage")

            print("attempt to go to demo page")
            await page.get_by_role("link", name="Demo", exact=True).click()
            print("reached demo")

            print("Locating Inspect Page")
            await page.get_by_role("link", name="Inspect", exact=True).click()
            print("putting fake article text")
            await page.locator("textarea").fill("An Alabama woman by the name of Angela Williams " \
                                                "shared a graphic photo of her son, lying in a " \
                                                "hospital bed with a beaten and fractured face, on " \
                                                "Facebook. It needs to be shared far and wide, because this is unacceptable." \
                                                "It is unclear why Williams  son was in police custody or what sort of " \
                                                "altercation resulted in his arrest, but when you see the photo you will realize" \
                                                " that these details matter not. Cops are not supposed to beat and brutalize " \
                                                "those in their custody. In the post you are about to see, Ms. Williams expresses " \
                                                "her hope that the cops had their body cameras on while they were beating her son," \
                                                " but I think we all know that there will be some kind of convenient  malfunction "\
                                                "to explain away the lack of existence of dash or body camera footage of what was "\
                                                "clearly a brutal beating.")
            print("clicking to submit")
            await page.locator("button:has-text('Inspect')").click()
            print("looking for predictions")
            # Wait for results to appear - adjust selector as needed
            result_section = page.locator('div.result')
            await expect(result_section).to_be_visible()
            
        except Exception as e:
            print(f"Test failed: {e}")
            raise
        finally:
            await browser.close()
            



#Real news from outside source: New York Times
@pytest.mark.asyncio
async def test_false():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        print("reached tests")
        
        try:
            await page.goto("http://127.0.0.1:5000/")
            print("opened homepage")

            print("Locating Inspect Page")
            await page.get_by_role("link", name="Inspect", exact=True).click()
            print("putting fake article text")
            await page.locator("textarea").fill("Covid irritates the lungs and can cause long-term issues, like" \
                                                " persistent shortness of breath and coughing. In rare cases, Covid " \
                                                "can lead patients to develop pneumonia and leave scarring and small" \
                                                " masses of tissue, called nodules, throughout the lungs. Those scars " \
                                                "can make it harder to breathe. Small studies have suggested that over" \
                                                " 10 percent of people hospitalized with a Covid infection had lung scarring"
                                                " and other issues two years later.")
            print("clicking to submit")
            await page.locator("button:has-text('Inspect')").click()
            print("looking for predictions")
            # Wait for results to appear - adjust selector as needed
            result_section = page.locator('div.result')
            await expect(result_section).to_be_visible()
            
        except Exception as e:
            print(f"Test failed: {e}")
            raise
        finally:
            await browser.close()
           



 