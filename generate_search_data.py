import os
from html.parser import HTMLParser

# The elements are of the structure {"title": "", "text": [], "filename": ""}.
documents = []
current_document = {"text": ""}

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

        global current_document, in_content, set_title

        strip = data.strip()
        if set_title:
            # Strip the " | V-Dala nation" part from the HTML <title>.
            current_document["title"] = strip[:-16]
        
        if in_content:
            current_document["text"] += strip + " "

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
    global current_file, documents, in_content, current_document

    files = os.listdir(files_folder)
    for fi in documents_list:
        current_file = fi
        current_document["filename"] = fi[8:-5]
        with open(fi, encoding="utf-8") as fo:
            parser.feed(fo.read())
            documents.append(current_document)
            current_document = {"text": ""}
        in_content = False

    with open(r"sources\lunr_documents.js", "w", encoding="utf-8") as fo:
        print("var lunr_documents =", documents, ";", file=fo)

    documents_map = {}
    for doc in documents:
        documents_map[doc["filename"]] = doc["title"]
    with open(r"sources\lunr_documents_id_map.js", "w", encoding="utf-8") as fo:
        print("var lunr_documents_id_map =", documents_map, ";", file=fo)

if __name__ == '__main__':
    main()