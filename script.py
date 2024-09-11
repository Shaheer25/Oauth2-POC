import requests

# List of form IDs
form_ids = ['78014f82-2228-4949-9620-3e5a87dc5699', '12f8e790-2280-43b4-b6a0-87627a88adf8', 'bcfa92cb-c54e-435a-9830-971881bb76a7', 'aabd3714-01ac-448d-9108-1b46a3dca4ec', '4c03f877-dc95-4ef5-97e7-12c23cf490e5', 'd8a6fee4-3048-4b36-8aea-9f8231bd6194', '894455c2-3777-4587-8094-ae232acbe6b6', '9cc89239-410f-4158-94ff-35d8542ef679', 'a2721c65-3a58-47ec-bd85-91f9f0491272', '64ad969e-6928-4efd-9d45-dbac6d625a72', 'c4986086-92aa-4110-b25d-515a6d01cd68', '9d7188b7-7e86-47eb-bd0c-d312df77c2ff', '58cc506a-5024-43eb-a827-f203603822bc', '15754db4-919b-4e39-b6e6-842c2a173eeb', '74d42d4f-e815-45b1-8375-efb12bb010d5', '95a04eba-4f68-43e7-91ad-c9770fc69ef7', '9caa7908-a537-4d88-9fe5-0ea04d4a11a6', 'bcdc1836-6a67-4dcd-b7b1-7c0317f365ab', 'd879f895-6e76-4a05-bb90-60488bbac051', '360ed52c-9a7e-4a16-9d09-7bd45fd083d9', '474ffec5-85b6-4989-a472-17fb6ff2a958', '155f3d7f-9cd1-499a-9cbc-bca4a54fd615', 'db12ce44-c2db-4c2a-89ad-c6eb867c397f', 'ab1b0af1-9e4e-4e11-b96a-e8128c04ab9f', 'e593bd5b-f2f1-45bb-9748-c3f36af0c3c0', '9abfbda0-a6a6-4403-8527-6196d8920698', '354ea912-604d-4846-b139-9c7064388390', '5359b3db-dd70-4ed6-8aa6-839b737a828e', 'fe65f44d-d53d-4c48-9066-e0ab93a74be0', '4b8c7bc7-0682-446e-be6d-0a0a8db1066a', '177cb66f-33f3-45d8-833c-fd9a2c6e8d86', '34a94aa9-64d5-4470-8e74-e5867077b822', 'd3accbd2-4238-495f-a346-6fc3780eb991', 'e83a0ab3-8ae2-4133-9128-31a9244d9d1d', '2ae56318-7649-49cc-9521-269fac8a09db', 'ee144a70-598c-482f-bb42-2182aaa21e6e', 'aad00fe7-1a6b-40ad-9456-7fbda33786ae', '603e8ddc-5560-4427-9146-7fccdbce544f', '718e51c1-e584-4f55-9c60-fa7f940650bc', '113c3bee-183d-45d2-9dc1-aa6e16fdb2bb', 'ffa98e31-f4d4-4bb6-b329-69f22191f08d', '43a69b86-781c-4470-9017-f35a981902cb', 'c95f9124-711b-4e62-9900-d93e2700d0fe', 'a78f9475-e566-4e51-8b76-ddad406ad70d', 'fe549e39-82a4-4d4b-824f-cce5b5f0d6b3', '05011b04-eb1f-49e2-84e9-4c8004991dfd', '94f2b502-c198-4163-bc41-0c10ccb2b5a9', '3f216be7-f5f9-461f-a78a-34e7df410b14', 'a116d724-f479-4e4d-8e41-931e57727509', '86b7404c-0434-49ec-a6da-a0bc13de0381', '5a01a40a-59d2-4805-9c01-e596a82a2f3b', 'b5455e71-8e2f-4237-949b-1f3fc56dd88c', '19662b29-f9f1-4bed-a191-46e236ae2d7f', 'b3752c0e-f85e-4b61-9c17-191a9feae741', '2f3e79f5-b634-401f-89ba-2c5da978b93c', '868fc7f8-3f24-4915-bd36-5ded9913a981', 'd8d254ae-9976-438e-b50e-40381c513edb', 'cfce5672-2ae3-4812-8cca-84eed717cda5', '5c2e4840-c25d-4e58-a869-f83fc88bcbf7', 'bbd5a997-b9d0-4154-8fdf-94ad6dc51543', '42bb31d1-8a6a-4811-a206-6b448b06c78d', 'f8756c67-09dc-4125-86bc-7496b9a275ea', '748d73ee-835f-4920-b80d-9d3978d8efd5', 'dffd5c1a-2581-415e-8c4d-16287003f6a6', '05ed148e-7149-473f-a15a-45054b2ab344', 'd8324d0a-c222-4874-b82b-d12940ca9308', '2801e4ac-f100-420f-b97b-dc2bd49efe1f', 'cdd0c2e1-f9b5-4474-abc5-3c07dc6471ef', 'b760ecdf-1581-4e01-80aa-d2bd18131d64', '2317f569-bd90-47a5-b225-b6f83bfb13e0', 'ec7c9afa-706b-4d7f-b56e-63acb9211fb0', 'bcb816c8-5ebf-4961-87d4-45c91a4263c4', '5e26abe1-1220-4db5-af23-ce06a80e7fa1', '74928ae4-4e73-4078-8ac2-51be64afd3ef', '202b5a9b-05d7-4e72-8899-66253ca64c5a']

# The payload
payload = {
    "summary": "",
    "assignee_level_type": "singlelevel",
    "matrix": [
        {
            "name": "string",
            "assign_to": [
                {
                    "id": "USR0700430797e71d0e1",
                    "name": "Digital Inspection Team",
                    "type": "user"
                }
            ],
            "map_to": [
                {
                    "id": "string",
                    "name": "string",
                    "type": "part_no"
                }
            ]
        }
    ],
    "others": {
        "priority": "high"
    },
    "validations": {
        "enabled": True,
        "asset_id": "",
        "validation_type": "qr_code"
    },
    "geofencing": {
        "enabled": False,
        "location_type": "latitude_and_longitude",
        "location": "",
        "radius": 200,
        "lattitude": "",
        "longitude": ""
    },
    "advanced_settings": {
        "enabled": False,
        "count_type": "count_up",
        "count_down_values": ""
    },
    "shuffle_questions": False,
    "submission_approvals": {
        "enabled": True,
        "summary": "",
        "approval_type": "singlelevel",
        "levels": [
            {
                "name": "level1",
                "sublevel": [
                    {
                        "name": "sublevel1",
                        "matrix": [
                            {
                                "id": "USR0700430797e71d0e1",
                                "name": "Digital Inspection Team",
                                "type": "user"
                            }
                        ],
                        "condition": "or"
                    }
                ],
                "sub_level_condition": []
            }
        ]
    }
}

# Headers
headers = {
    'accept': 'application/json',
    'sub-tenant-id': 'BSN10404719064601a01',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ0b2tlbklkIjoiVE9LMDUwODA3NjQxNTliN2VkMTAiLCJ0ZW5hbnRJZCI6IlROVDA5NDI0OTIxMDEzZjg0ZTUxIiwidXNlclJvbGUiOlsiUk9MMDgwOTM5NjUyYjQ0YTZiMWMiXSwidXNlcklkIjoiVVNSMDcwMDQzMDc5N2U3MWQwZTEiLCJkZXZpY2VJZCI6IjEwOjIxMzQ6U0QiLCJwbGF0Zm9ybSI6IndlYiIsInVzZXJuYW1lIjoiZGl0dXNlciIsInN1YiI6IlVTUjA3MDA0MzA3OTdlNzFkMGUxIiwiaWF0IjoxNzI1OTQ0ODg3LCJleHAiOjE3MjU5NzcyODd9.AERMxblEGYlnZ9yZwgwkg0yCmHR5bjq_gTnmWI0FCYQ'
}

# URL base
base_url = "https://api2.fflow.app.lghive.com/api/v1/forms/{form_id}/assignment"

# Iterate over form IDs and send PATCH requests
for form_id in form_ids:
    url = base_url.format(form_id=form_id)
    response = requests.patch(url, json=payload, headers=headers)

    # Print the response for each request
    print(f"Response for form {form_id}: {response.status_code} - {response.text}")
