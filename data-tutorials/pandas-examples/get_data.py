import requests

url = "https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-1000.csv"
response = requests.get(url)

if response.status_code == 200:
    csv_file_path = "../../sample-data/organisations.csv"

    with open(csv_file_path, "wb") as csv_file:
        csv_file.write(response.content)
    print(f"CSV file saved successfully: {csv_file_path}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
