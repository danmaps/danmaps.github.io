import arcpy
from datetime import date

months = {1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"}

mxd = arcpy.mapping.MapDocument(r"") # path to MXD

print "Scanning ",mxd

for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
    if elm.text == '<dyn type="date" format="MMMM"/>': # text = this month
        elm.text = months[date.today().month-1] # set text to previous month
        print "Changed from "+months[date.today().month]+" to "+months[date.today().month-1]
    elif (months[date.today().month] == "January") and elm.text == '<dyn type="date" format="MMMM"/>':
        elm.text = "December"
        print "Changed from January to December"
    else: print "Found "+ elm.text+"... No changes to make."

mxd.save()
print "MXD saved"
del mxd
print "Done!"
