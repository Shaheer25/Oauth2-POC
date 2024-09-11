import requests
from fastapi import status


class ExternalRequests:
    def __init__(self):
        """
        Constants
        """
        self.tenant_id = "TNT09424921013f84e51"
        self.service_id = "SER0710550978dbb0f8d"
        self.app_id = "APP100202888cb618417"
        self.device_id = "10:2134:SD"

    def list_of_users(self, token , by_id = None , tenant = False , department = False):
        """
        Get List of users for approval
        """
        user_list = []
        skip = 0
        limit = 50
        if by_id is None:
            while True:
                response = requests.get(
                    url=f"http://platform-digitalinspection-591152774.ap-south-1.elb.amazonaws.com/v1/user-service/user/{self.tenant_id}/get?requestType=all&skip={skip}&limit={limit}",  # noqa
                    headers={
                        "Content-Type": "application/json",
                        "tenantId": self.tenant_id,
                        "serviceId": self.service_id,
                        "appId": self.app_id,
                        "deviceId": self.device_id,
                        "Authorization": token,
                    },
                )
                data = response.json().get("result", {}).get("data", [])
                if not data:
                    break
                for user in data:
                    user_info = {
                        "name": user.get("name"),
                        "id": user.get("id"),
                        "isActive": user.get("isActive", False),
                        "email": user.get("email"),
                    }
                    user_list.append(user_info)
                skip += 1
            return user_list
        else:
            response = requests.get(
                    url=f"http://platform-digitalinspection-591152774.ap-south-1.elb.amazonaws.com/v1/user-service/user/{self.tenant_id}/get?requestType=all&skip={skip}&limit={limit}&id={by_id.strip()}",  # noqa
                    headers={
                        "Content-Type": "application/json",
                        "tenantId": self.tenant_id,
                        "serviceId": self.service_id,
                        "appId": self.app_id,
                        "deviceId": self.device_id,
                        "Authorization": token,
                    },
                )
            data = response.json().get("result", {}).get("data", [])
            ids = []
            if department:
                # return data[0].get('departments',[]) if data[0]['departments'] else list()
                if data and data[0] and data[0]['departments'] and len(data[0]['departments']) > 0:
                    for department_id in data[0]['departments']:
                        ids.append(department_id['id'])
                    return ids
                else :
                    return list() 

            elif tenant:
                return data[0].get('businessId','') if data and data[0] and data[0]['businessId'] else None
            else:
                return data[0] if data and data[0] else []

    def list_of_departments(self, token: str) -> list[dict]:
        """
        Get List of Departments
        """
        department = requests.get(
            url=f"http://platform-digitalinspection-591152774.ap-south-1.elb.amazonaws.com/v1/site-service/department/{self.tenant_id}/get?requestType=all&skip=0&limit=50",  # noqa
            headers={
                "Content-Type": "application/json",
                "tenantId": self.tenant_id,
                "serviceId": self.service_id,
                "appId": self.app_id,
                "deviceId": self.device_id,
                "Authorization": token.strip(),
            },
        )
        department_list = []
        for response in department.json().get("result", {}).get("data", []):
            user_info = {
                "name": response.get("name"),
                "id": response.get("id"),
            }
            department_list.append(user_info)
        return department_list

    def list_of_sub_tenants(self, token: str) -> list[dict]:
        """
        Get List of Departments
        """
        sub_tenants = requests.get(
            url=f"http://platform-digitalinspection-591152774.ap-south-1.elb.amazonaws.com/v1/tenant-service/tenant/get/data?requestType=businessminimal&id={self.tenant_id}",  # noqa
            headers={
                "Content-Type": "application/json",
                "tenantId": self.tenant_id,
                "serviceId": self.service_id,
                "appId": self.app_id,
                "deviceId": self.device_id,
                "Authorization": token,
            },
        )
        sub_tenant_list = []
        for response in sub_tenants.json().get("result", {}):
            user_info = {
                "name": response.get("name"),
                "id": response.get("id"),
            }
            sub_tenant_list.append(user_info)
        return sub_tenant_list

    def permission_check(self, permission_to_check: str, token: str) -> bool:
        """
        Check the permission
        """
        response = requests.post(
            url=f"http://platform-digitalinspection-591152774.ap-south-1.elb.amazonaws.com/v1/user-service/authorization/{self.tenant_id}/check_permission",  # noqa
            headers={
                "Content-Type": "application/json",
                "tenantId": self.tenant_id,
                "serviceId": self.service_id,
                "appId": self.app_id,
                "Authorization": token,
            },
            json={"permissionToCheck": permission_to_check.strip()},
        )
        if (
            response.status_code == status.HTTP_200_OK
            and response.json()["result"]["isAuthorized"]
        ):
            return True
        else:
            False

    def list_of_roles(self, token) -> list[dict]:
        """
        Get List of roles for approval
        """
        role_list = []
        skip = 0
        limit = 50
        while True:
            response = requests.get(
                url=f"http://platform-digitalinspection-591152774.ap-south-1.elb.amazonaws.com/v1/user-service/role/{self.tenant_id}/get?requestType=all&skip={skip}&limit={limit}",  # noqa
                headers={
                    "Content-Type": "application/json",
                    "tenantId": self.tenant_id,
                    "serviceId": self.service_id,
                    "appId": self.app_id,
                    "deviceId": self.device_id,
                    "Authorization": token,
                },
            )
            data = response.json().get("result", {}).get("data", [])
            if not data:
                break
            for user in data:
                user_info = {
                    "name": user.get("name"),
                    "id": user.get("id"),
                }
                role_list.append(user_info)
            skip += 1
        return role_list



ext = ExternalRequests(
)

print(ext.list_of_users(token="eyJhbGciOiJIUzI1NiJ9.eyJ0b2tlbklkIjoiVE9LMDUyMDM3Mzk2M2U4NzliZGMiLCJ0ZW5hbnRJZCI6IlROVDA5NDI0OTIxMDEzZjg0ZTUxIiwidXNlclJvbGUiOlsiUk9MMDgwOTM5NjUyYjQ0YTZiMWMiXSwidXNlcklkIjoiVVNSMDcwMDQzMDc5N2U3MWQwZTEiLCJkZXZpY2VJZCI6IjEwOjIxMzQ6U0QiLCJwbGF0Zm9ybSI6IndlYiIsInVzZXJuYW1lIjoiZGl0dXNlciIsInN1YiI6IlVTUjA3MDA0MzA3OTdlNzFkMGUxIiwiaWF0IjoxNzIzMDk0NDM3LCJleHAiOjE3MjMxMjY4Mzd9.M0K44zGxMPfHdN-zToEkBpUlT8nFWyZE8uiOGl3bvOI",by_id='USR0700430797e71d01'))