import pafy

#variable  selection

file = open('list.txt','r')

#boucle

for line in file:
    url = line
    
    
    try:
        #doner les lien a pafy
        video = pafy.new(url)
        
        bestaudio = video.getbestaudio()
        print(video.title)
        
        #telecharger 
        bestaudio.download()
        
        
    except:
        pass
    
    
    
file.close()
        
        
        
        