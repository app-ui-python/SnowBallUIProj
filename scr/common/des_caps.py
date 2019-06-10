# coding = utf-8


from appium import webdriver
import yaml
import logging

"""
 @Author: Allison Liu
 @Date: 07/06/2019
"""
def desired_caps():
    with open('../config/xueqiu_caps.yaml', 'r', encoding='utf-8') as f:
        data = yaml.load(f)

    des_caps = {
                'platformName': data['platformName'],
                'platformVersion': data['platformVersion'],
                'deviceName': data['deviceName'],
                'udid': data['udid'],
                'appPackage': data['appPackage'],
                'appActivity': data['appActivity']
                }

    logging.info("Start xueqiu app....")
    driver = webdriver.Remote("http://"+str(data['ip'])+':'+ str(data['port']) + '/wd/hub',des_caps)
    driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    desired_caps()