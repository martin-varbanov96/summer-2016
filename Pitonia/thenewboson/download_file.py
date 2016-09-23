from urllib import request
CSV_URL = "https://vincentarelbundock.github.io/Rdatasets/csv/datasets/HairEyeColor.csv"
CSV_FILE_NAME = "hair_eyes_color.csv"

def download_csv(csv_url):
	response = request.urlopen(csv_url)
	csv_format = str(response.read())
	csv_arr=csv_format.split("\\n")
	write_to_file = open(CSV_FILE_NAME, "w")
	for line in csv_arr:
		print(line)
		print("*"*30)
		write_to_file.write(line + "\n")
		write_to_file.close()
download_csv(CSV_URL)