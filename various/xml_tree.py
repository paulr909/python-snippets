import requests
import xml.etree.ElementTree as Et
from decouple import config

# update variable values as needed
period_start = "202007210000"
period_end = "202007210100"
security_token = config("TOKEN")

# get xml data and save to data.xml
url = (
    f"https://transparency.entsoe.eu/api?securityToken={security_token}&documentType=A44&in_Domain=10YGB----------A"
    f"&out_Domain=10YGB----------A&periodStart={period_start}&periodEnd={period_end}"
)

r = requests.get(url)
root = Et.fromstring(r.text)
tree = Et.ElementTree(root)
tree.write("data.xml")

# import data.xml and transform tags
tree = Et.parse("data.xml")
root = tree.getroot()

name_space = "{urn:iec62325.351:tc57wg16:451-3:publicationdocument:7:0}"

for child in root.iter():
    if child.tag == f"{name_space}sender_MarketParticipant.mRID":
        child.tag = f"{name_space}sender_MarketParticipant_mRID"

    elif child.tag == f"{name_space}sender_MarketParticipant.marketRole.type":
        child.tag = f"{name_space}sender_MarketParticipant_marketRole_type"

    elif child.tag == f"{name_space}receiver_MarketParticipant.mRID":
        child.tag = f"{name_space}receiver_MarketParticipant_mRID"

    elif child.tag == f"{name_space}receiver_MarketParticipant.marketRole.type":
        child.tag = f"{name_space}receiver_MarketParticipant_marketRole_type"

    elif child.tag == f"{name_space}period.timeInterval":
        child.tag = f"{name_space}period_timeInterval"

    elif child.tag == f"{name_space}in_Domain.mRID":
        child.tag = f"{name_space}in_Domain_mRID"

    elif child.tag == f"{name_space}out_Domain.mRID":
        child.tag = f"{name_space}out_Domain_mRID"

    elif child.tag == f"{name_space}price.amount":
        child.tag = f"{name_space}price_amount"

# write data to output.xml
tree.write("output.xml")

print("Update complete, use output.xml")
