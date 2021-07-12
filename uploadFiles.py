import dropbox 

class TransferData:
    def __init__ (self,accesstoken):
        self.accesstoken = accesstoken

    def upload_file(self,filefrom,fileto):
        

        dbx = dropbox.Dropbox(self.accesstoken)

        with open(filefrom,'rb') as f:
            dbx.files_upload(f.read(),fileto)

def main():
    accesstoken = 'sl.Az_w6e5DcuZVxKAOSVfLzU17qN3IKq86jk6eKfa7i7AHzfix5xPdFxS0jspC0CufpqcPtUp11JiT8jR1EnrX0TXHoeplnRJqvyTEHQlhvHYSAYuszWqhmtIQn7HepWFAc6Nqf0A'
    data1 = data(accesstoken)

    filefrom = input("ENTER THE FILE TO UPLOAD")
    fileto = input("ENTER THE COMPLET DROPBOX PATH")

    data1.upload_file(filefrom,fileto)
    print("FILE UPLOADED")

main()
