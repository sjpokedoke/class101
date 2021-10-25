import dropbox

class TransferData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
    
    def files_upload(self, source, dest):
        dbx = dropbox.Dropbox(self.accesstoken)

        with open(source, 'rb') as f:
            dbx.files_upload(f.read(), dest)
    
def main():
    accesstoken = 'Pjm8Vgf7utEAAAAAAAAAAVhqn7-PLVuUMd3izZSwtpE4FiwvUoyZ-mxqeSoyyqkU'
    transfer = TransferData(accesstoken)

    source = input('Enter the file path to transfer: ')
    dest = input('Enter the full path to upload to dropbox: ')

    transfer.files_upload(source, dest)

    print('Transfer is successfull!')

main()