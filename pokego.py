from bs4 import BeautifulSoup
import os


##will return the pokemon go hub html page 
def getFileName():
    fileName = "pokemongohub.html"

    if os.path.isfile( fileName ):
        return fileName
    else:
        print("file not found...")
        exit()

##open file
def openFile( fileName ):
    fin = open( fileName )

    return fin

##returns links to all pokemon pictures
def getLinks( soup ):
    pghLinks = []

    for link in soup.find_all( 'a' ):
        if 'amazonaws' in link.get('href'):
            pghLinks.append( link.get('href') )
    
    return pghLinks

##downloads all pokemon images
def getImages( pghLinks ):
    template = "{}.png"
    x = 1

    for i in pghLinks:
        r = requests.get( i )
        open( template.format(x) , 'wb').write(r.content)
        x += 1

##get lines of data ( needs filter )
def getData( soup ):
    table = soup.find('table')

    tableRows = table.find_all('tr')

    data = []
    pokeNames = []                  #list of all pokemon names ( pokedex number is index + 1 )

    for tr in tableRows:
        td = tr.find_all('td')
        row = [ i.text for i in td ]
        #print( row )
        data.append( row[1] )

    for i in data:
        getName( i , pokeNames )

    #for i in pokeNames:
    #    print( i )

##filter for name
def getName( i , pokeNames ):

    if "name" in i:
        if "class" in i:
            ##splice data to get names
            name = i[19:]
            name = name[:-7]
            pokeNames.append( name )





##main
fileName = getFileName()                        #get fileName
fin = openFile( fileName )                      #get html source


soup = BeautifulSoup( fin , 'html.parser' )     #create soup object


pghLinks = getLinks( soup )                     #gets links for pokemon pictures


#getImages( pghLinks )                           #downloads all images


getData( soup )                                 #gets all the lines with pokemon names , numbers , types

