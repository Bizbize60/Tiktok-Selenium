from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

# **Appium Sunucu Bağlantısı**
appium_server_url = 'http://127.0.0.1:4723'

# **TikTok İzleyici Botu Ayarları**
options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "deviceName": "127.0.0.1:5555",
    "automationName": "UiAutomator2",
    "appPackage": "com.zhiliaoapp.musically",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "noReset": True,
    "adbExecTimeout": 60000
})

# **Appium WebDriver Bağlantısı Yap**
driver = webdriver.Remote(command_executor=appium_server_url, options=options)

time.sleep(5)

# **TikTok Açılınca, Canlı Yayına Girme**
def join_live():
    print("✅ TikTok açıldı, şimdi yayına giriyoruz...")

    try:
        # **1. Arama butonunu bul ve tıkla**
        search_button = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.zhiliaoapp.musically:id/gm1"]')
        search_button.click()
        time.sleep(2)

        # **2. Arama kutusuna kullanıcı adı yaz**
        search_input = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.zhiliaoapp.musically:id/euf"]')
        search_input.send_keys("@whiysssude")
        time.sleep(2)

        # **3. İlk sonucu seç ve tıkla**
        driver.execute_script("mobile: shell", {
        "command": "input keyevent 66"
    }   )
        time.sleep(5)

        # **4. Canlı yayına gir**
        live_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Live")]')
        live_button.click()
        print("🎥 Canlı yayına başarıyla girildi!")

    except Exception as e:
        print("🚨 Canlı yayına girerken hata oluştu:", e)

# **Fonksiyonu çalıştır**
join_live()

# **Sonsuz döngü, sürekli canlı yayında kalır**
while True:
    time.sleep(60)
