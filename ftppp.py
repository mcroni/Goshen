from ftplib import FTP

#domain name or server ip:
ftp = FTP('ftp.goshen.heliohost.org')
#ftp = FTP('ftp.point3hub.com')
ftp.login(user='mcroni', passwd = 'paloma')

print('connected')
ftp.cwd('/public_html/albums/menz')
print('changed')

files = ftp.dir()
#print(files)
data = []
ftp.dir(data.append)
ftp.quit()



for line in data:
    if line[-3] == 'mp3':
        print(line)
    #print(data)
    #print(line[62:])
    





##import ftplib
##import os
##
##def upload(ftp, file):
##    ext = os.path.splitext(file)[1]
##    if ext in (".txt", ".htm", ".html"):
##        ftp.storlines("STOR " + file, open(file))
##    else:
##        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
##
##ftp = ftplib.FTP("ftp.fbi.gov")
##ftp.login("mulder", "trustno1")
##
##upload(ftp, "trixie.zip")
##upload(ftp, "file.txt")
##upload(ftp, "sightings.jpg")
