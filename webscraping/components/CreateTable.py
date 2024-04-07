class CreateTables:
    def __init__(self,data):
        self.data=data

    def Supplier(self) :
        command='INSERT INTO supplier VALUES'
        for productItem in self.data:

            command+=f"({productItem['supplierID']},{productItem['brand']}),"
              
        return command[0:-1]

# data=[{'supplierID': '1054', 'productID': '97683', 'title': 'SteelSeries USB Apex 5 Hybrid Mechanical Gaming Keyboard – Per-Key RGB Illumination – Aircraft Grade Aluminum Alloy Frame – OLED Smart Display (Hybrid Blue Switch)', 'stock:': 818826, 'price': '89', 'productType': 'gaming keyboard', 'brand': 'SteelSeries'},
# {'supplierID': '1057', 'productID': '89801', 'title': 'ASUS ROG Strix Scope II 96 Wireless Gaming Keyboard, Tri-Mode Connection, Dampening Foam & Switch-Dampening Pads, Hot-Swappable Pre-lubed ROG NX Snow Switches, PBT Keycaps, RGB-Black', 'stock:': 815971, 'price': '144', 'productType': 'gaming keyboard', 'brand': 'ASUS'},
# {'supplierID': '1054', 'productID': '92223', 'title': 'SteelSeries Apex 3 RGB Gaming Keyboard – 10-Zone RGB Illumination – IP32 Water Resistant – Premium Magnetic Wrist Rest (Whisper Quiet Gaming Switch)', 'stock:': 803390, 'price': '45', 'productType': 'gaming keyboard', 'brand': 'SteelSeries'}]

# table=CreateTable(data)
# table.Supplier()
