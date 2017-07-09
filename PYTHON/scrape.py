import urllib2
import simplejson
import cStringIO

fetcher = urllib2.build_opener()
searchTerm = 'motorbikes in traffic 720p'
startIndex = 0
searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + startIndex
f = fetcher.open(searchUrl)
deserialized_output = simplejson.load(f)