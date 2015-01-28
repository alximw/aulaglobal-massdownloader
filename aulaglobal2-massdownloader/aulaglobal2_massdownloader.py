__author__ = "Jorge Rodriguez Canseco"
__version__ = "1.0b"


import include.requests, getpass, os, include.bs4, include.unidecode, time

_DOCFILE_BASE_STRING = "https://aulaglobal.uc3m.es/mod/resource/view.php?id="
_DOCFILE_BASE_TAG_NAME = '<span class="instancename">'
_DOWNLOAD_FOLDER = "DOWNLOADS/"

def getDocsFrom(url, course_name, connection):

    print("\n --- Downloading from %s ---" % course_name)
    try:
        os.mkdir(_DOWNLOAD_FOLDER)
    except OSError:
        pass
    response = connection.get(url)
    tousefolder = course_name.replace(' ', '_').replace('/', '_').replace('.', '-')
    ordinal = 0

    try:
        os.mkdir(_DOWNLOAD_FOLDER+tousefolder)
    except OSError:
        pass

    for line in response.iter_lines():
        startindex = line.find(_DOCFILE_BASE_STRING)

        if startindex is not -1:
            time.sleep(1)
            endindex = line.find('"', startindex)
            subaddress = line[startindex:endindex]

            try:
                thefileResponse = connection.get(subaddress)
            except:
                print("Connection ratio bypassed. Sleeping 10s")
                time.sleep(10)
                thefileResponse = connection.get(subaddress)

            # Find name of doc
            startindex_name = line.find(_DOCFILE_BASE_TAG_NAME, endindex) + len(_DOCFILE_BASE_TAG_NAME)
            object_url = thefileResponse.url.split('/')
            object_name_temp = object_url[-1]
            if object_name_temp.find('?') is not -1:
                object_name = object_name_temp[:object_name_temp.find('?')+1]
            else:
                object_name = object_name_temp

            print("Downloading ... %s" % object_name)
            with open(_DOWNLOAD_FOLDER + tousefolder + "/" + str(ordinal) + "-" + object_name, 'w+') as fd:
                for chunk in thefileResponse.iter_content():
                    fd.write(chunk)
            ordinal+=1


username = raw_input("USERNAME: ")
password = getpass.getpass("PASSWORD: ")

attributes = "?adAS_i18n_theme=es&adAS_mode=authn&adAS_username=%s&adAS_password=%s" % (username, password)
courses = []

connection = requests.Session()
homepage_html = connection.post(
    "https://sir.uc3m.es/CAS/index.php/login?service=https%3A%2F%2Faulaglobal.uc3m.es%2Flogin%2Findex.php&gateway=true" + attributes)

# Get the elements from the page
number = 0

htmlparsed = bs4.BeautifulSoup(homepage_html.text)
found = htmlparsed.findAll('a', attrs={'class': 'course_link'})
for a in found:
    courses.append( [str(a['href']), unidecode.unidecode(a.contents[0])] )

end = False
while not end:

    # Prompt
    for i, mycourse in zip(range(len(courses)), courses):
        print("%s) %s" % (str(i), mycourse[1]))
    print("%s) ALL" % str(len(courses)))
    print("%s) EXIT" % str(len(courses)+1))
    input = int(raw_input("\nSELECT AN OPTION TO DOWNLOAD THE FILES\n   > "))

    if input is not len(courses) and input is not len(courses)+1:
        # Get the page of the selected course
        getDocsFrom(courses[input][0], courses[input][1].replace(' ', '_'), connection)

    elif input is len(courses):
        for course in courses:
            getDocsFrom(course[0], course[1].replace(' ', '_'), connection)

    elif input is len(courses)+1:
        end=True

exit()