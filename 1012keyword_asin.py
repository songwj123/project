from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_amazon_asins(search_query):
    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 如果不需要可视化界面，取消注释

    # 启动浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # 打开亚马逊搜索页面
        driver.get("https://www.amazon.com")

        # 输入搜索关键词
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(search_query)
        search_box.submit()

        # 等待页面加载
        time.sleep(5)

        # 获取前 10 个 ASIN
        asins = []
        products = driver.find_elements(By.XPATH, "//div[@data-asin and @data-asin!='']")
        for product in products[:10]:  # 只取前10个
            asin = product.get_attribute("data-asin")
            if asin and len(asin) == 10:
                asins.append(asin)

        return asins

    finally:
        driver.quit()


def main():
    search_query = input("请输入关键词: ").strip().replace(" ", "+")
    asins = get_amazon_asins(search_query)

    if asins:
        print(f"关键词'{search_query}'前十个为:")
        for idx, asin in enumerate(asins, 1):
            print(f"{idx}. {asin}")
    else:
        print("No ASINs found.")


if __name__ == "__main__":
    main()
