import os
from html.parser import HTMLParser

# The elements are of the structure ["", []].
# The first is the title, the second is the text.
documents = {}

current_file = None
set_title = False
in_content = False

class SearchIndexParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global in_content, set_title

        if tag == "title":
            set_title = True
        else:
            set_title = False

        for att in attrs:
            if att[0] == "class" and att[1] == "content":
                in_content = True

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if data.strip() == "":
            return

        global documents, in_content, set_title

        strip = data.strip()
        if set_title:
            documents[current_file]["title"] = strip
        
        if in_content:
            documents[current_file]["text"].append(strip)

parser = SearchIndexParser()

files_folder = r"upload\v-dala"

documents_list = [
    r"sources\history.html.page",
    r"sources\event.html.page",
    r"sources\contact.html.page",
    r"sources\alumnus.html.page",
    r"sources\index.html.page",
    r"sources\leaving_nation.html.page",
    r"sources\membership.html.page",
    r"sources\history.html.page",
    r"sources\opening_hours.html.page",
    r"sources\honorary_members.html.page",
    r"sources\pay_membership_fee.html.page"
]

def main():
    global current_file, documents, in_content

    files = os.listdir(files_folder)
    for fi in documents_list:
        current_file = fi
        documents[current_file] = {"title": "", "text": []}
        with open(fi, encoding="utf-8") as fo:
            parser.feed(fo.read())
        in_content = False

    json = []
    for filename, data in documents.items():
        json.append({filename[8:-5]: data})

    with open("search_index.json", "w", encoding="utf-8") as fo:
        print(json, file=fo)

if __name__ == '__main__':
    main()