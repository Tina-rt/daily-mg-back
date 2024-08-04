from scraper import midimdgscraper, expressmadascraper, lemondescraper, lefigaroscraper

JOURNAL_LIST = {
    '0': expressmadascraper,
    '1': midimdgscraper,
    '2': lefigaroscraper,
    '3': lemondescraper,
}