import ssl
import pymongo

connection = pymongo.MongoClient(
    "mongodb+srv://Jomondi:FidelliaAdhiambo@cluster0.lbtqn.mongodb.net/Hospital?retryWrites=true&w=majority",
    ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

database = connection['Hospital']
doc_col = database['Doctors']
hos_col = database['Hospital']
patient_col = database['Patient']

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

pat_data = [{'patient_id': 827, 'patient_name': 'John Rustu', 'age': 28, 'gender': 'M', 'Inpatient/Outpatient': 'Y',
             'hospital_id': 324},
            {'patient_id': 567, 'patient_name': 'Aggrey Mukwambo', 'age': 35, 'gender': 'M',
             'Inpatient/Outpatient': 'N', 'hospital_id': 120},
            {'patient_id': 901, 'patient_name': 'Lucy Ochieng', 'age': 19, 'gender': 'F', 'Inpatient/Outpatient': 'Y',
             'hospital_id': 892},
            {'patient_id': 820, 'patient_name': 'Gaudencia Oirere', 'age': 24, 'gender': 'F',
             'Inpatient/Outpatient': 'N', 'hospital_id': 891}]


def insert_data():
    x = doc_col.insert_many(docs_data)
    y = hos_col.insert_many(hosp_data)
    z = patient_col.insert_many(pat_data)
    print('Data successfully entered!')


# insert_data()


def join_collections():
    cursor = database.Hospital.aggregate([
        {
            "$lookup":
                {
                    "from": "Doctors",
                    "localField": "hospital_id",
                    "foreignField": "hospital_id",
                    "as": "hospital_info"
                }},
        {"$unwind": "$hospital_info"},
        {"$lookup": {
            "from": "Patient",
            "localField": "hospital_id",
            "foreignField": "hospital_id",
            "as": "hospital_info2"}},
        {"$unwind": "$hospital_info2"},
        {"$project": {
            "_id": 0,
            "hospital_id": 1,
            "hospital_name": 1,
            "patient_name": "$hospital_info2.patient_name",
            "doctor_name": "$hospital_info.doctor_name",
            "Inpatient/Outpatient": "$hospital_info2.Inpatient/Outpatient"

        }}

    ])

    for values in cursor:
        print(values)


join_collections()
