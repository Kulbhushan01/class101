import dropbox


class TrasferData:
    def __init__(self,access_token): 
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)


def main():
    access_token ="sl.Bzj54QRo1XzyZJsPHco-mWlDL3Yql_w-r-OTHweYAIM8uUDSTi94AxAB-i8aQ1nA15dnrCFIdYAYLicJVPiAUyYIZk8RYTZLvRPcZ2SSl2eiUUl7Z1cZpiQR__9xPdb7sUiigqQeqmFp"
    trasferData=TrasferData(access_token)
    file_from = input("Enter the file path to transfer: ").strip().strip('"')
    file_to = input("Enter the full path to upload to Dropbox: ").strip().strip('"')
    trasferData.upload_file(file_from,file_to)
    print("file is moved")

main()