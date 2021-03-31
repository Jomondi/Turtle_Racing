import sqlite3
import pandas as pd
import webbrowser


conn = sqlite3.connect("School_System.db")
print('School database successfully created!')
print()
cursor = conn.cursor()

# Open the file
csv_doc = pd.read_csv('teacher_by_status_and_county_for_secondary.csv')


# Convert csv to dataframe and save it in sqlite3
def convert_to_df():
    csv_df = pd.DataFrame(csv_doc)
    csv_df.to_sql('School_Info', conn, if_exists='replace', index=False)


convert_to_df()

# Read and print database table data
table_data = cursor.execute("SELECT * FROM School_Info")


csv_doc.drop('County (centroid)', inplace=True, axis=1)
print(csv_doc.head(10))
print()
print()
print(csv_doc.tail(10))

html = csv_doc.to_html()


header = "<html><head><title>Kenya National Schools Heads</title><meta name='description'>" \
         "<center><img src='Shield.jpeg' alt='logo'/></center><h1>Kenya National Union of Teachers</h1>" \
         "<link rel='stylesheet' href='schools.css'/></head>"
with open('schools.html', 'w') as file_name:
    file_name.write(header)
    file_name.write(html)


webbrowser.open_new_tab("file_name")
