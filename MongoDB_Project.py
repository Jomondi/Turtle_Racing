import pymongo, ssl

page_title = "Hospital Information"

connection = pymongo.MongoClient(
    "mongodb+srv://<username>:<password>@cluster0.lbtqn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

# Create database and collections
database = connection["Healthcare"]
hosp_coll = database["Hospital"]
doc_coll = database["Doctors"]

hosp_data = [
    {'hospital_id': 324, 'hospital_name': 'Kenyatta National', 'bed_count': 78, 'address': '5612 Mbagathi Way'},
    {'hospital_id': 120, 'hospital_name': 'Nairobi National', 'bed_count': 100, 'address': '783 Uhuru  Highway'},
    {'hospital_id': 892, 'hospital_name': 'TUK Hospital', 'bed_count': 49, 'address': '42 City Block'},
    {'hospital_id': 891, 'hospital_name': 'Egerton University Hospital', 'bed_count': 94, 'address': '412 Moi Ave'}
    ]

docs_data = [{'doctor_id': 678, 'doctor_name': 'John Maina', 'hospital_id': 324, 'date_joined': '09/19/2012',
              'specialty': 'surgeon', 'salary': 100000, 'experience': '5 years'},
             {'doctor_id': 901, 'doctor_name': ' Robert Ochieng', 'hospital_id': 120, 'date_joined': '11/19/2003',
              'specialty': 'dentist', 'salary': 110000, 'experience': '5 years'},
             {'doctor_id': 481, 'doctor_name': 'Peter Maingi', 'hospital_id': 892, 'date_joined': '04/11/2009',
              'specialty': 'mortician', 'salary': 142000, 'experience': '5 years'},
             {'doctor_id': 561, 'doctor_name': 'Paul Embarambara', 'hospital_id': 891, 'date_joined': '01/30/2019',
              'specialty': 'neuro-surgeon', 'salary': 178000, 'experience': '5 years'}]


# Insert data into the collections
def insert_data():
    x = hosp_coll.insert_many(hosp_data)
    y = doc_coll.insert_many(docs_data)


insert_data()

# Join the collections
cursor = database.Hospital.aggregate([
    {
        "$lookup":
            {
                "from": "Doctors",
                "localField": "hospital_id",
                "foreignField": "hospital_id",
                "as": "hospital_info"
            }
    }])

for values in cursor:
    print(values)
