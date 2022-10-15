from Modules import Surface

def generateMap(width, height, format) -> list:
    Map = []
    with open('./src/data/glyph.txt', 'r') as Template:
        Glyph = [*Template.read()]
        #Remove \n from the list
        Glyph.pop(-1)

        for charcter in Glyph:
            # (charcter, surface)
            Map.append((charcter, Surface.Surface(width, height, format)))
    
    return Map

