from pymongo import MongoClient

# MongoDB connection URI
uri = "mongodb://127.0.0.1:36002/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.3"

# Connect to the MongoDB client
client = MongoClient(uri)

# Access the specific database and collection
db = client['petrus']  # Replace with your actual database name
forms_collection = db['forms']  # Replace with the name of your collection

# List of form updates (index = name, value = id)
form_updates = [
  {
    "index": "StageInspection 1",
    "value": "78014f82-2228-4949-9620-3e5a87dc5699"
  },
  {
    "index": "StageInspection 2",
    "value": "12f8e790-2280-43b4-b6a0-87627a88adf8"
  },
  {
    "index": "StageInspection 3",
    "value": "bcfa92cb-c54e-435a-9830-971881bb76a7"
  },
  {
    "index": "StageInspection 4",
    "value": "aabd3714-01ac-448d-9108-1b46a3dca4ec"
  },
  {
    "index": "StageInspection 5",
    "value": "4c03f877-dc95-4ef5-97e7-12c23cf490e5"
  },
  {
    "index": "StageInspection 6",
    "value": "d8a6fee4-3048-4b36-8aea-9f8231bd6194"
  },
  {
    "index": "StageInspection 7",
    "value": "894455c2-3777-4587-8094-ae232acbe6b6"
  },
  {
    "index": "StageInspection 8",
    "value": "9cc89239-410f-4158-94ff-35d8542ef679"
  },
  {
    "index": "StageInspection 9",
    "value": "a2721c65-3a58-47ec-bd85-91f9f0491272"
  },
  {
    "index": "StageInspection 10",
    "value": "64ad969e-6928-4efd-9d45-dbac6d625a72"
  },
  {
    "index": "StageInspection 11",
    "value": "c4986086-92aa-4110-b25d-515a6d01cd68"
  },
  {
    "index": "StageInspection 12",
    "value": "9d7188b7-7e86-47eb-bd0c-d312df77c2ff"
  },
  {
    "index": "StageInspection 13",
    "value": "58cc506a-5024-43eb-a827-f203603822bc"
  },
  {
    "index": "StageInspection 14",
    "value": "15754db4-919b-4e39-b6e6-842c2a173eeb"
  },
  {
    "index": "StageInspection 15",
    "value": "74d42d4f-e815-45b1-8375-efb12bb010d5"
  },
  {
    "index": "StageInspection 16",
    "value": "95a04eba-4f68-43e7-91ad-c9770fc69ef7"
  },
  {
    "index": "StageInspection 17",
    "value": "9caa7908-a537-4d88-9fe5-0ea04d4a11a6"
  },
  {
    "index": "StageInspection 18",
    "value": "bcdc1836-6a67-4dcd-b7b1-7c0317f365ab"
  },
  {
    "index": "StageInspection 19",
    "value": "d879f895-6e76-4a05-bb90-60488bbac051"
  },
  {
    "index": "StageInspection 20",
    "value": "360ed52c-9a7e-4a16-9d09-7bd45fd083d9"
  },
  {
    "index": "StageInspection 21",
    "value": "474ffec5-85b6-4989-a472-17fb6ff2a958"
  },
  {
    "index": "StageInspection 22",
    "value": "155f3d7f-9cd1-499a-9cbc-bca4a54fd615"
  },
  {
    "index": "StageInspection 23",
    "value": "db12ce44-c2db-4c2a-89ad-c6eb867c397f"
  },
  {
    "index": "StageInspection 24",
    "value": "ab1b0af1-9e4e-4e11-b96a-e8128c04ab9f"
  },
  {
    "index": "StageInspection 25",
    "value": "e593bd5b-f2f1-45bb-9748-c3f36af0c3c0"
  },
  {
    "index": "StageInspection 26",
    "value": "9abfbda0-a6a6-4403-8527-6196d8920698"
  },
  {
    "index": "StageInspection 27",
    "value": "354ea912-604d-4846-b139-9c7064388390"
  },
  {
    "index": "StageInspection 28",
    "value": "5359b3db-dd70-4ed6-8aa6-839b737a828e"
  },
  {
    "index": "StageInspection 29",
    "value": "fe65f44d-d53d-4c48-9066-e0ab93a74be0"
  },
  {
    "index": "StageInspection 30",
    "value": "4b8c7bc7-0682-446e-be6d-0a0a8db1066a"
  },
  {
    "index": "StageInspection 31",
    "value": "177cb66f-33f3-45d8-833c-fd9a2c6e8d86"
  },
  {
    "index": "StageInspection 32",
    "value": "34a94aa9-64d5-4470-8e74-e5867077b822"
  },
  {
    "index": "StageInspection 33",
    "value": "d3accbd2-4238-495f-a346-6fc3780eb991"
  },
  {
    "index": "StageInspection 34",
    "value": "e83a0ab3-8ae2-4133-9128-31a9244d9d1d"
  },
  {
    "index": "StageInspection 35",
    "value": "2ae56318-7649-49cc-9521-269fac8a09db"
  },
  {
    "index": "StageInspection 36",
    "value": "ee144a70-598c-482f-bb42-2182aaa21e6e"
  },
  {
    "index": "StageInspection 37",
    "value": "aad00fe7-1a6b-40ad-9456-7fbda33786ae"
  },
  {
    "index": "StageInspection 38",
    "value": "603e8ddc-5560-4427-9146-7fccdbce544f"
  },
  {
    "index": "StageInspection 39",
    "value": "718e51c1-e584-4f55-9c60-fa7f940650bc"
  },
  {
    "index": "StageInspection 40",
    "value": "113c3bee-183d-45d2-9dc1-aa6e16fdb2bb"
  },
  {
    "index": "StageInspection 41",
    "value": "ffa98e31-f4d4-4bb6-b329-69f22191f08d"
  },
  {
    "index": "StageInspection 42",
    "value": "43a69b86-781c-4470-9017-f35a981902cb"
  },
  {
    "index": "StageInspection 43",
    "value": "c95f9124-711b-4e62-9900-d93e2700d0fe"
  },
  {
    "index": "StageInspection 44",
    "value": "a78f9475-e566-4e51-8b76-ddad406ad70d"
  },
  {
    "index": "StageInspection 45",
    "value": "fe549e39-82a4-4d4b-824f-cce5b5f0d6b3"
  },
  {
    "index": "StageInspection 46",
    "value": "05011b04-eb1f-49e2-84e9-4c8004991dfd"
  },
  {
    "index": "StageInspection 47",
    "value": "94f2b502-c198-4163-bc41-0c10ccb2b5a9"
  },
  {
    "index": "StageInspection 48",
    "value": "3f216be7-f5f9-461f-a78a-34e7df410b14"
  },
  {
    "index": "StageInspection 49",
    "value": "a116d724-f479-4e4d-8e41-931e57727509"
  },
  {
    "index": "StageInspection 50",
    "value": "86b7404c-0434-49ec-a6da-a0bc13de0381"
  },
  {
    "index": "StageInspection 51",
    "value": "5a01a40a-59d2-4805-9c01-e596a82a2f3b"
  },
  {
    "index": "StageInspection 52",
    "value": "b5455e71-8e2f-4237-949b-1f3fc56dd88c"
  },
  {
    "index": "StageInspection 53",
    "value": "19662b29-f9f1-4bed-a191-46e236ae2d7f"
  },
  {
    "index": "StageInspection 54",
    "value": "b3752c0e-f85e-4b61-9c17-191a9feae741"
  },
  {
    "index": "StageInspection 55",
    "value": "2f3e79f5-b634-401f-89ba-2c5da978b93c"
  },
  {
    "index": "StageInspection 56",
    "value": "868fc7f8-3f24-4915-bd36-5ded9913a981"
  },
  {
    "index": "StageInspection 57",
    "value": "d8d254ae-9976-438e-b50e-40381c513edb"
  },
  {
    "index": "StageInspection 58",
    "value": "cfce5672-2ae3-4812-8cca-84eed717cda5"
  },
  {
    "index": "StageInspection 59",
    "value": "5c2e4840-c25d-4e58-a869-f83fc88bcbf7"
  },
  {
    "index": "StageInspection 60",
    "value": "bbd5a997-b9d0-4154-8fdf-94ad6dc51543"
  },
  {
    "index": "StageInspection 61",
    "value": "42bb31d1-8a6a-4811-a206-6b448b06c78d"
  },
  {
    "index": "StageInspection 62",
    "value": "f8756c67-09dc-4125-86bc-7496b9a275ea"
  },
  {
    "index": "StageInspection 63",
    "value": "748d73ee-835f-4920-b80d-9d3978d8efd5"
  },
  {
    "index": "StageInspection 64",
    "value": "dffd5c1a-2581-415e-8c4d-16287003f6a6"
  },
  {
    "index": "StageInspection 65",
    "value": "05ed148e-7149-473f-a15a-45054b2ab344"
  },
  {
    "index": "StageInspection 66",
    "value": "d8324d0a-c222-4874-b82b-d12940ca9308"
  },
  {
    "index": "StageInspection 67",
    "value": "2801e4ac-f100-420f-b97b-dc2bd49efe1f"
  },
  {
    "index": "StageInspection 68",
    "value": "cdd0c2e1-f9b5-4474-abc5-3c07dc6471ef"
  },
  {
    "index": "StageInspection 69",
    "value": "b760ecdf-1581-4e01-80aa-d2bd18131d64"
  },
  {
    "index": "StageInspection 70",
    "value": "2317f569-bd90-47a5-b225-b6f83bfb13e0"
  },
  {
    "index": "StageInspection 71",
    "value": "ec7c9afa-706b-4d7f-b56e-63acb9211fb0"
  },
  {
    "index": "StageInspection 72",
    "value": "bcb816c8-5ebf-4961-87d4-45c91a4263c4"
  },
  {
    "index": "StageInspection 73",
    "value": "5e26abe1-1220-4db5-af23-ce06a80e7fa1"
  },
  {
    "index": "StageInspection 74",
    "value": "74928ae4-4e73-4078-8ac2-51be64afd3ef"
  },
  {
    "index": "StageInspection 75",
    "value": "202b5a9b-05d7-4e72-8899-66253ca64c5a"
  }
]

# Iterate over each update in the list
for form in form_updates:
    # Update the 'name' field based on the 'value' (id)
    result = forms_collection.update_one(
        {"id": form["value"]},  # Find document by id
        {"$set": {"name": form["index"]}}  # Set the new name
    )
    
    # Check if the update was successful
    if result.modified_count > 0:
        print(f"Updated form {form['value']} with name '{form['index']}'")
    else:
        print(f"Form {form['value']} not updated or already has the name '{form['index']}'")

# Close the connection
client.close()
