
# import unittest
# from selenium import webdriver
# import page


# class AmazonTest(unittest.TestCase):
#     myName='com'
#     def setUp(self):
#         print('test_1 start',self.myName)
#         self.driver= webdriver.Chrome()
#         self.name='shelby 219803'
#         self.driver.get('https://www.amazon.'+self.myName)
        
#     def test_Search_Test(self):
#         mainpage= page.MainPage(self.driver)
#         self.assertTrue(mainpage.titleIsTrue)
#         key='gaming keyboard'

#         mainpage.SearchInput=key
#         mainpage.clickGoButton()
        
#         searchpage= page.SearchResultPage(self.driver)
#         productsDetail= searchpage.clickGoDetailProduct()
#         print(productsDetail)
        
#         # self.createtable= CreateTable.CreateTables(productsDetail)
#         # commandCreateSupplier= self.createtable.Supplier()
#         # print(commandCreateSupplier)


#     def tearDown(self):
#         print('success')
#         self.driver.quit()



# if __name__ == "__main__":
#     #  AmazonTest.setUp(unittest.TestCase)
#     #  AmazonTest.test_Search_Test()
#     AmazonTest.myName='com'
#     unittest.main() 
import numpy as np
a= np.arange(2,10,2)
print(a)
































# productList=[{'supplierID': '1053', 'productID': '20644', 'title': 'ASUS ROG Azoth 75% Wireless DIY Custom Gaming Keyboard, OLED Display, Three-Layer Dampening, Hot-Swappable ROG NX Red Switches & Keyboard Stabilizers, PBT Keycaps, RGB-Black', 'stock:': 728081, 'price': '199', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="2D01418AED40B2C2C59DF97CF1ED8E51_element_255")', 'brand': 'ASUS'},
# {'supplierID': '1073', 'productID': '18834', 'title': 'ROCCAT Magma Silent Membrane Switch PC Gaming Keyboard with 5 Zone/10 LED AIMO RGB Top Plate and Detachable Palm Rest - Black', 'stock:': 987300, 'price': '29', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="75F38DB9955B27F477FDED7DFB2A27A6_element_450")', 'brand': 'ROCCAT'},
# {'supplierID': '1016', 'productID': '99016', 'title': 'SteelSeries Apex 3 TKL RGB Gaming Keyboard – Tenkeyless Compact Form Factor - 8-Zone RGB Illumination – IP32 Water & Dust Resistant – Whisper Quiet Gaming Switch – Gaming Grade Anti-Ghosting,Black', 'stock:': 732893, 'price': '34', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="3B449906F4FE2DF461168E454ECB4CFF_element_656")', 'brand': 'SteelSeries'},
# {'supplierID': '1076', 'productID': '74102', 'title': 'Redragon S101 Gaming Keyboard, M601 Mouse, RGB Backlit Gaming Keyboard, Programmable Backlit Gaming Mouse, Value Combo Set [New Version]', 'stock:': 829047, 'price': '44', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="3539321ECEF3DA5ACE5E33D0C6733EA4_element_852")', 'brand': 'Redragon'},
# {'supplierID': '1100', 'productID': '43561', 'title': 'Corsair K70 RGB PRO Wired Mechanical Gaming Keyboard (Cherry MX RGB Red Switches: Linear and Fast, 8,000Hz Hyper-Polling, PBT Double-Shot PRO Keycaps, Soft-Touch Palm Rest) QWERTY, NA - Black', 'stock:': 39683, 'price': '109', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="A0784649B9C12617330FFBADBA60E0EA_element_1058")', 'brand': 'Corsair'},
# {'supplierID': '1016', 'productID': '37495', 'title': "SteelSeries Apex Pro TKL HyperMagnetic Gaming Keyboard - World's Fastest Keyboard - Adjustable Actuation - Esports Tenkeyless - OLED Screen - RGB - PBT Keycaps - USB-C - 2023 Edition,Black", 'stock:': 137306, 'price': '149', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="D227E5AABDA2F4A7A5A976BF0E7FB6FB_element_1233")', 'brand': 'SteelSeries'},
# {'supplierID': '1010', 'productID': '84116', 'title': 'Razer Ornata V3 X Gaming Keyboard: Low-Profile Keys - Silent Membrane Switches - Spill Resistant - Chroma RGB Lighting - Ergonomic Wrist Rest - Classic Black', 'stock:': 213080, 'price': '34', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="273B89B727E3882E34CF37E25D6FF245_element_1438")', 'brand': 'Razer'},
# {'supplierID': '1100', 'productID': '47988', 'title': 'Corsair K55 PRO LITE RG    B Wired Membrane Gaming Keyboard (5-Zone Dynamic RGB Backlighting, Six Macro Keys with Stream Deck Integration, IP42 Dust and Spill Resistant, Dedicated Media Keys) Black', 'stock:': 649843, 'price': '24', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="0701D54DC36675751EE6F14C3200A722_element_1643")', 'brand': 'Corsair'},
# {'supplierID': '1010', 'productID': '67047', 'title': 'Razer Huntsman Mini 60% Gaming Keyboard: Fast Keyboard Switches - Linear Optical Switches - Chroma RGB Lighting - PBT Keycaps - Onboard Memory - Mercury White', 'stock:': 124551, 'price': '79', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="C2D932E58B633F3C378FC86662F4D686_element_1843")', 'brand': 'Razer'},
# {'supplierID': '1025', 'productID': '33603', 'title': '8Bitdo Retro Mechanical Keyboard, Bluetooth/2.4G/USB-C Hot Swappable Gaming Keyboard with 87 Keys, Dual Super Programmable Buttons for Windows and Android - N Edition', 'stock:': 300846, 'price': '89', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="7808BAC22F0B64C1476F6E60EC6528C1_element_1908")', 'brand': '8Bitdo'},
# {'supplierID': '1010', 'productID': '40560', 'title': 'Razer Huntsman V2 TKL Tenkeyless Gaming Keyboard: Fastest Linear Optical Switches Gen2 w/Sound Dampeners & 8000Hz Polling Rate - Detachable TypeC Cable - Doubleshot PBT Keycaps - Ergonomic Wrist Rest', 'stock:': 145595, 'price': '99', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="A47D47E093247B357CAC998F71E1AA03_element_2102")', 'brand': 'Razer'},
# {'supplierID': '1053', 'productID': '30893', 'title': 'ASUS ROG Strix Scope NX TKL Moonlight White Wired Mechanical RGB Gaming Keyboard | ROG NX Brown Tactile Switches, Aluminum Frame, Aura Sync Lighting, Tenkeyless Design, Quick Toggle Media Keys', 'stock:': 457574, 'price': '99', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="C664468605825E17105DBCDD5B04EC34_element_2308")', 'brand': 'ASUS'},
# {'supplierID': '1084', 'productID': '84057', 'title': 'NZXT Function MiniTKL - Compact Tenkeyless Gaming Keyboard – Gateron Red Mechanical Switches: Linear, Fast, and Quiet – Hot-Swappable – RGB Backlit – Aluminum Top Plate – Sound Dampening Foam – Black', 'stock:': 478376, 'price': '49', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="E905C7E46D5C6081DF1FB9E468BB3EF0_element_2502")', 'brand': 'NZXT'},
# {'supplierID': '1016', 'productID': '13658', 'title': 'SteelSeries Apex 7 Mechanical Gaming Keyboard – OLED Smart Display – USB Passthrough and Media Controls – Tactile and Quiet – RGB Backlit (Brown Switch)', 'stock:': 770449, 'price': '134', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="91A9EA802DBF7053AF6AC0CC1AFB70CE_element_2719")', 'brand': 'SteelSeries'},
# {'supplierID': '1053', 'productID': '44840', 'title': 'ASUS ROG Azoth 75% Wireless DIY Custom Gaming Keyboard, OLED Display, Three-Layer Dampening, Hot-Swappable ROG NX Red Switches & Keyboard Stabilizers, PBT Keycaps, RGB-Black', 'stock:': 610831, 'price': '199', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="6614228828B197895E7DDABB929530B7_element_2897")', 'brand': 'ASUS'},
# {'supplierID': '1010', 'productID': '84415', 'title': 'Razer BlackWidow V3 Mechanical Gaming Keyboard: Green Mechanical Switches - Tactile & Clicky - Chroma RGB Lighting - Compact Form Factor - Programmable Macro Functionality - Quartz', 'stock:': 32803, 'price': '99', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="FB63B8EE37115BD0DC4D368EB43C8BBA_element_3092")', 'brand': 'Razer'},
# {'supplierID': '1053', 'productID': '51188', 'title': 'ASUS ROG Strix Scope II 96 Wireless Gaming Keyboard, Tri-Mode Connection, Dampening Foam & Switch-Dampening Pads, Hot-Swappable Pre-lubed ROG NX Snow Switches, PBT Keycaps, RGB-Black', 'stock:': 124817, 'price': '144', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="05234658092C6EFF5EEB62DA04EA15A5_element_3308")', 'brand': 'ASUS'},
# {'supplierID': '1053', 'productID': '64287', 'title': 'ASUS ROG Strix Scope II 96 Wireless Gaming Keyboard, Tri-Mode Connection, Dampening Foam & Switch-Dampening Pads, Hot-Swappable Pre-lubed ROG NX Snow Switches, PBT Keycaps, RGB-Black', 'stock:': 274170, 'price': '144', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="AD2286AB5BB80ECF6C4962652D8A9A5B_element_3488")', 'brand': 'ASUS'},
# {'supplierID': '1010', 'productID': '55766', 'title': 'Razer BlackWidow V3 Tenkeyless TKL Mechanical Gaming Keyboard: Yellow Mechanical Switches - Linear & Silent - Chroma RGB Lighting - Compact Form Factor - Programmable Macros - USB Passthrough', 'stock:': 554045, 'price': '76', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="66E18276375E097F7250EE90D4D13FB1_element_3684")', 'brand': 'Razer'},
# {'supplierID': '1010', 'productID': '26699', 'title': 'Razer ORNATA Expert: Mecha-Membrane - Individually Backlit Mid-Height Keys - Leatherette Wrist Rest - Gaming Keyboard - Gaming Keyboard (RZ03-02041800-R3U1)', 'stock:': 291923, 'price': '34', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="CF5E881932E46C9D5BDAD34742275C8C_element_3895")', 'brand': 'Razer'},
# {'supplierID': '1077', 'productID': '25848', 'title': 'IOGEAR Kaliber Gaming HVER Aluminum Gaming Keyboard, Black/Gray,GKB704L-BK', 'stock:': 389021, 'price': '33', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="303B1E729F26CC64339B6B56D80AF8CF_element_4079")', 'brand': 'IOGEAR'}   ,
# {'supplierID': '1030', 'productID': '68256', 'title': 'Cooler Master CK720 Hot-Swappable 65% Space Gray Mechanical Gaming Keyboard, Kailh Box V2 Tactile Brown Switches, Customizable RGB, USB-C Connectivity, 3-Way Dial, QWERTY (CK-720-GKKM1-US)', 'stock:': 544202, 'price': '99', 'productType': 'selenium.webdriver.remote.webelement.WebElement (session="de6ca9a64b797d9df554f5603e45fde4", element="463D46F99D80FA9872D40D11FA414618_element_4207")', 'brand': 'Cooler'}]

  


# data=[{'supplierID': '1054', 'productID': '97683', 'title': 'SteelSeries USB Apex 5 Hybrid Mechanical Gaming Keyboard – Per-Key RGB Illumination – Aircraft Grade Aluminum Alloy Frame – OLED Smart Display (Hybrid Blue Switch)', 'stock:': 818826, 'price': '89', 'productType': 'gaming keyboard', 'brand': 'SteelSeries'},
# {'supplierID': '1057', 'productID': '89801', 'title': 'ASUS ROG Strix Scope II 96 Wireless Gaming Keyboard, Tri-Mode Connection, Dampening Foam & Switch-Dampening Pads, Hot-Swappable Pre-lubed ROG NX Snow Switches, PBT Keycaps, RGB-Black', 'stock:': 815971, 'price': '144', 'productType': 'gaming keyboard', 'brand': 'ASUS'},
# {'supplierID': '1054', 'productID': '92223', 'title': 'SteelSeries Apex 3 RGB Gaming Keyboard – 10-Zone RGB Illumination – IP32 Water Resistant – Premium Magnetic Wrist Rest (Whisper Quiet Gaming Switch)', 'stock:': 803390, 'price': '45', 'productType': 'gaming keyboard', 'brand': 'SteelSeries'}]

# table=CreateTable.CreateTables(data)
# cmd= table.Supplier()
# print(cmd)