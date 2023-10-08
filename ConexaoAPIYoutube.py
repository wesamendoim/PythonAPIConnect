from googleapiclient.discovery import build

from tkinter.commondialog import Dialog

#2. Criar conexão com API do Youtube 

#URL PLaylist = "https://www.youtube.com/watch?v=hnAn1mbEWPM&list=PLY5t6Ut9HKFenI3a_yfOvcmjb-iO_oZPl"

#"tokenAPI" AIzaSyDnHOCvqpzxMz8QH88yEtutIqfwMm0qHMI

tokenAPI = "AIzaSyDnHOCvqpzxMz8QH88yEtutIqfwMm0qHMI" 

youtube = build('youtube','v3',developerKey=tokenAPI)

#Dados da Playlist para extração de dados
idPlaylist = "hnAn1mbEWPM&list=PLY5t6Ut9HKFenI3a_yfOvcmjb-iO_oZPl"
namePlaylist = "SAGA DO TIME SEM FP!"
nextPage_token = "None" 

playlist_FIFA = []
while True:
    res = youtube.playlistItems().list(part='snippet',playlistId = idPlaylist).execute()