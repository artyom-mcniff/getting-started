import json

import requests
#
#

headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE2Njg2MTA1MzQsIm5iZiI6MTY2ODYxMDUzNCwiZXhwIjoxNjY4NjE1MDk1LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBR1ppNFdVaWRCbU4zRURJK2t5UExYc2ZXVTJoT25ieWpJUStweTFhaDg4UVpvbm4zT0d5NklYckxPcWw3ZklJNE93Tk0vNTlHdElzWVZBREplNTU5dmlTaktxaDErbjJCd0JncUJLcmJkYTQ9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTWNOaWZmIiwiZ2l2ZW5fbmFtZSI6IkFydHlvbSIsImdyb3VwcyI6WyJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCIxMjVjYWI3Yy1mOWViLTQzZTUtOWUyMS01ZTNiNWRkZDA1YmEiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiXSwiaXBhZGRyIjoiMTQ3LjI1Mi4yMi4xMzMiLCJuYW1lIjoiQzIwMzk0MzAxIEFydHlvbSBNY05pZmYiLCJvaWQiOiIwMzFlYTgxMi1mNWEwLTRjNWQtODdmYS00ZjJmZTU4ZWM2NTEiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjAyNTQyOTI2NS0xOTU4MzY3NDc2LTcyNTM0NTU0My0zMjYyODMiLCJwdWlkIjoiMTAwMzIwMDBFNEFFOTRFRCIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBQTAuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoidDBfaXVpRWxraTBGdlN5WGNiNUxsYzhNbUdkYjk4M29hUkFrM2RfN043VSIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiQzIwMzk0MzAxQG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJDMjAzOTQzMDFAbXl0dWR1Ymxpbi5pZSIsInV0aSI6InVaV2FUak1LSTBhNncyV0dGZk9IQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.WkrmPRTpk-G3RQGUsC0jK0U5DTrVWLcGgZgpOW__TiMqsdE9mh7Fad6lHh7NMedBW88WDtIIBHTA_1DuFO8rKF-hWQiD67rMwfNYNblGGCdVAiqalrLIFL9_GDX7XvDnLdOHmkGiwboS4jFpW17fIlKpuaZcN41JH5OeVrF79mRgw15Xr03LSfywEaFFK1VwtZqzOK2nJ46zON53fhxoc5Zw2GmTxeDexzZRyorYGFgcaZ41Afx76dyQyujhldTTBpBHYb-YAVNJPkyRkOHqf7m7MNxkEAYq6Kt3yMNMKymZ-SwC5b3SCJITaSCKPZfXRQ6HC8m9oJFniGWXvcRNGQ",
    "Content-type": "application/json"}
data = json.dumps({
"properties": {
    "publicIPAllocationMethod": "Static",
    "idleTimeoutInMinutes": 10,
    "publicIPAddressVersion": "IPv4"
},
"sku": {
    "name": "Basic"
},
"location": "eastus"
})

url = "https://management.azure.com/subscriptions/919c8687-e465-499f-a96b-75ce67da421e/resourceGroups/cc1/providers/Microsoft.Network/publicIPAddresses/testip2?api-version=2022-05-01"

resp=requests.put(url, data=data, headers=headers)
print(resp.status_code)

headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE2Njg2MTA1MzQsIm5iZiI6MTY2ODYxMDUzNCwiZXhwIjoxNjY4NjE1MDI1LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBbTY2TlBQQ3E5NWpsK2QzZFl1NXlRQ3Z3dDQ1ZHhmVFBuNndycS8rWE5kR2c5b2RVYjU5cTZHeC9QcytkNXZvNC9TckkvSmxlMXcrU2JtK2hTM0haWHdwSnFoWVd6VTNIczFNV0t3QTVLTjg9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTWNOaWZmIiwiZ2l2ZW5fbmFtZSI6IkFydHlvbSIsImdyb3VwcyI6WyJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCIxMjVjYWI3Yy1mOWViLTQzZTUtOWUyMS01ZTNiNWRkZDA1YmEiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiXSwiaXBhZGRyIjoiMTQ3LjI1Mi4yMi4xMzMiLCJuYW1lIjoiQzIwMzk0MzAxIEFydHlvbSBNY05pZmYiLCJvaWQiOiIwMzFlYTgxMi1mNWEwLTRjNWQtODdmYS00ZjJmZTU4ZWM2NTEiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjAyNTQyOTI2NS0xOTU4MzY3NDc2LTcyNTM0NTU0My0zMjYyODMiLCJwdWlkIjoiMTAwMzIwMDBFNEFFOTRFRCIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBQTAuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoidDBfaXVpRWxraTBGdlN5WGNiNUxsYzhNbUdkYjk4M29hUkFrM2RfN043VSIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiQzIwMzk0MzAxQG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJDMjAzOTQzMDFAbXl0dWR1Ymxpbi5pZSIsInV0aSI6ImlkbEdZdXJ0N2tLYUgzTTJ2QTRWQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.QGmn2_O0jentsUaDrCd9h7VBqgIqG9FUH9SiaQsQxvxEKJEaWgUuy6sJkOD9EnDmsRoTS9JnHVPYgqPf8FitgFGCPSR3Y5vy8q21TLVjWshal-6hu6dvJF4jbE_ZbD1fcIXLGtKbVGKsRXOAdhena9aOaP9kupQBLEV9JC3tSMcijRKai61qXQRNtz1QQgW0zKg_buVqOB7v5hEhS10GZ7_y9x9G-UEsFkXxCowAarKa_2GLS-Q1PWcG3RTLQMUfg50aVVmN4WLaU8ua_ZQbe3ssqgzNl1Rs5uFTwjH7SKham2lbdY8LnihFK6pUBVz5K0SFpGJw0guZr8AxYF3HCg",
           "Content-type": "application/json"}

data = json.dumps(
    {
        "properties": {
            "enableAcceleratedNetworking": False,
            "disableTcpStateTracking": False,
            "ipConfigurations": [
                {
                    "name": "ipconfig1",
                    "properties": {
                        "publicIPAddress": {
                            "id": "/subscriptions/919c8687-e465-499f-a96b-75ce67da421e/resourceGroups/cc1/providers/Microsoft.Network/publicIPAddresses/testip2"
                        },
                        "subnet": {
                            "id": "/subscriptions/919c8687-e465-499f-a96b-75ce67da421e/resourceGroups/cc1/providers/Microsoft.Network/virtualNetworks/cc1-vnet/subnets/default"
                        }
                    }
                }
            ]
        },
        "location": "eastus"
    }
)

url = "https://management.azure.com/subscriptions/919c8687-e465-499f-a96b-75ce67da421e/resourceGroups/cc1/providers/Microsoft.Network/networkInterfaces/cloudnw2?api-version=2022-05-01"
resp=requests.put(url, data=data, headers=headers)
print(resp.status_code)

headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE2Njg2MTA1MzksIm5iZiI6MTY2ODYxMDUzOSwiZXhwIjoxNjY4NjE0ODcxLCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBYnF5WkxSdXhqVUljbWYvcWhoMnBFOWFYVXRRL3lNazVsQzRaMG5qM2pFR3NINGIzbEM2Y29EKzFNRGMrZHc2SVBwbFljQW85bnBiaDBWelpnS3ZTRUZTUGtRc1I3YW16bFZJRk43d3dKNWM9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTWNOaWZmIiwiZ2l2ZW5fbmFtZSI6IkFydHlvbSIsImdyb3VwcyI6WyJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCIxMjVjYWI3Yy1mOWViLTQzZTUtOWUyMS01ZTNiNWRkZDA1YmEiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiXSwiaXBhZGRyIjoiMTQ3LjI1Mi4yMi4xMzMiLCJuYW1lIjoiQzIwMzk0MzAxIEFydHlvbSBNY05pZmYiLCJvaWQiOiIwMzFlYTgxMi1mNWEwLTRjNWQtODdmYS00ZjJmZTU4ZWM2NTEiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjAyNTQyOTI2NS0xOTU4MzY3NDc2LTcyNTM0NTU0My0zMjYyODMiLCJwdWlkIjoiMTAwMzIwMDBFNEFFOTRFRCIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBQTAuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoidDBfaXVpRWxraTBGdlN5WGNiNUxsYzhNbUdkYjk4M29hUkFrM2RfN043VSIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiQzIwMzk0MzAxQG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJDMjAzOTQzMDFAbXl0dWR1Ymxpbi5pZSIsInV0aSI6IkFLUGl0U2Q3RlVtc2ZVQnZtUDh2QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.ZBBMmsa1v_MpdYqHqcPzkHSWqMWxXGvEayk8Hdzm3Mo-bq11x5TG3jSZBYVtgDRdsHpbdVW4xBSMNuVUGm0EUt4ZVs4aywMjLigvO_C5vOOyoF-nU_HaCCI0sI60-TbQdvTTBKu8_UrkZQdB-EpNWxsSs-UBQnNUWgnW5oANwK_SvvrauDm-n1YawEikrV_Wn_pVpZMxn1ArroujgkKJ8GmRcX5GBaSIeXez6PpdCTqX61gLGo6yHAOegc3DtfqW-xroZh-07wa9alVqDTLN42hOWKvh46rG-kcdTQXe93Z5d_fQ85psMq68RRNo-oHUVCahI8t43_wCVs-YhxiFvg",
"Content-type": "application/json"}

url = "https://management.azure.com/subscriptions/919c8687-e465-499f-a96b-75ce67da421e/resourceGroups/cc1/providers/Microsoft.Compute/virtualMachines/myVM?api-version=2022-08-01"



data = json.dumps(
    {
        "id": "/subscriptions/919c8687-e465-499f-a96b-75ce67da421e/resourceGroups/cc1/providers/Microsoft.Compute/virtualMachines/myVM",
        "type": "Microsoft.Compute/virtualMachines",
        "properties": {
            "osProfile": {
                "adminUsername": "amcniff",
                "secrets": [

                ],
                "computerName": "myVM",
                "linuxConfiguration": {
                    "ssh": {
                        "publicKeys": [
                            {
                                "path": "/home/amcniff/.ssh/authorized_keys",
                                "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDUMPIhwsrVlHKuUxpR1Woe0kNYjM955EndsYMPmrbkgILD4ezC7C9H0GZOSVWaL+O6+rhXvTPAgj+B3/pju1gd05f3q85wyS1VV7wPvjDoAwBRMfX4NNNRVx23J7Y7cq5zC4Vysk5nOHn4k6Kn8GXlA9FmjWP35CpUUANvKl4BfIg38moidNdWFcJz8/b4kAJNryOCqD5jpYrLvA0ExDxG6onBcw9y9b6j/GXyrmHMtfu/9/VwHl+Oj3r6rQ7Os8EAHMazdXFVfigAsVsNf2Kt+XCOg24E2iEo6nnmJtb7uYwJP9lAEhfPxmzcZvzZRdAhI+cqMLIV4LlxqrX2CE28IcaG4Z6uHHRnEkpMBhTrjmLV8xSVsOxqHr8XoUFNUU7lr1o8L57292iP/xZPBJzYcczVhwdXqrEYfZOcRqTTK0XyF/hzzDhJXTfi4r0Ffdq/9uPijjjuRPikPmyL6d93KcWYOFNHaSSU4nJY58CjWdtEPpirFa25R7gkwJPmwQs= amcniff@LAPTOP-CVQ2PDG3"
                            }
                        ]
                    },
                    "disablePasswordAuthentication": True
                }
            },
            "networkProfile": {
                "networkInterfaces": [
                    {
                        "id": "/subscriptions/919c8687-e465-499f-a96b-75ce67da421e/resourceGroups/cc1/providers/Microsoft.Network/networkInterfaces/cloudnw2",
                        "properties": {
                            "primary": True
                        }
                    }
                ]
            },
            "storageProfile": {
                "imageReference": {
                    "sku": "16.04-LTS",
                    "publisher": "Canonical",
                    "version": "latest",
                    "offer": "UbuntuServer"
                },
                "dataDisks": [

                ]
            },
            "hardwareProfile": {
                "vmSize": "Standard_D1_v2"
            },
            "provisioningState": "Creating"
        },
        "name": "myVM",
        "location": "eastus"
    }
)



## data = body
# header = dictionary