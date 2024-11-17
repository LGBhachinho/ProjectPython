## AIde d installation dependance

pip install python-dotenv
pip install requests
pip install watchdog

#Lancement sous console 
python scriptFolderTransferEmby.py

##Pour exécuter ce script dans Docker :

apres avoir fait le dockerfile --> docker build -t scriptfiletransferemby .
docker run --name monconteneur scriptfiletransferemby pour l executer
docker run -v /mnt/mouflosyno/Downloads/Radarr-Sonarr/Radarr.NOK:/app/source \
           -v /mnt/mouflosyno/Emby-Media/Film\ 4K:/app/destination \
           -v $(pwd)/log:/app/log \
           -it scriptfiletransferemby

docker run -v D:\Ditch\Dev\script\testPython\source:/app/source \
           -v D:\Ditch\Dev\script\testPython\destination:/app/destination \
           -v $(pwd)/log:/app/log \
           -it scriptfiletransferemby

           docker run -v D:/Ditch/Dev/script/testPython/source:/app/source `
           -v D:/Ditch/Dev/script/testPython/destination:/app/destination `
           -v D:/Ditch/Dev/script/testPython/log:/app/log `
           -it --name scriptEmby-container scriptfiletransferemby



docker build -t file_watcher .
docker run -v /chemin/local/source:/path/to/source -v /chemin/local/destination:/path/to/destination file_watcher
