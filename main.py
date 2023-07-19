import ftplib
def anonLogin(hostname):
    try:
        ftp=ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+]' + str(hostname) + ' FTP Anonyous Login Succeded')
        ftp.quit()
        return True
    except Exception:
          print(('\n [+]' + str(hostname) + ' FTP Anonyous Login Fails'))
          return False
if __name__ == '__main__':
     anonLogin('90.130.70.74')
        
