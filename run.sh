echo INICIANDO DOWNLOAD DAS URLS...
python DownloadUrls.py
echo DOWNLOAD FINALIZADO
echo INICIANDO AGRUPAMENTO DAS URLS...
python GroupUrls.py
echo AGRUPAMENTO FINALIZADO
cd BirdieChalenge
echo INICIO DO SCRAPING
python crawl.py
