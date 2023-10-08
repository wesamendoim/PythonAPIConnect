from googleapiclient.discovery import build

from tkinter.commondialog import Dialog

#2. Criar conexão com API do Youtube 

#URL PLaylist = https://www.youtube.com/watch?v=a0nY4BQzxjA&list=PL5TJqBvpXQv7Xclsu6Y-YXBB0dlOqLvog

#"tokenAPI" AIzaSyDnHOCvqpzxMz8QH88yEtutIqfwMm0qHMI

tokenAPI = 'AIzaSyDnHOCvqpzxMz8QH88yEtutIqfwMm0qHMI'

youtube = build('youtube','v3',developerKey=tokenAPI)

print()

'''
#Dados da Playlist para extração de dados
idPlaylist = 'a0nY4BQzxjA&list=PL5TJqBvpXQv7Xclsu6Y-YXBB0dlOqLvog'
namePlaylist = 'SAGA DO TIME SEM FP!'
nextPage_token = 'None' 

playlist_FIFA = []
res = youtube.playlistItems().list(part='snippet',playlistId = idPlaylist).execute()
'''
