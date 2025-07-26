from html.parser import HTMLParser


# The current file output.
file_output = None


class VDalaHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "include":
        	filename = attrs[0][1].strip("\"")
        	with open(filename, "r", encoding="utf-8") as include:
        		part = include.read()
        		file_output.write(part)
        		file_output.flush()
        else:
        	file_output.write("<%s" % tag)
        	for attr_name, attr_value in attrs:
        		file_output.write(" %s=\"%s\"" % (attr_name, attr_value))
        	file_output.write(">")

    def handle_endtag(self, tag):
        file_output.write("</%s>" % tag)

    def handle_data(self, data):
        file_output.write(data)

parser = VDalaHTMLParser()

pages = [
	r"public_html\index.html.page",
	r"public_html\event.html.page"
]


def main():
	global file_output

	for filename in pages:
		output_filename = filename[0:-5]
		file_output = open(output_filename, "w", encoding="utf-8")
		with open(filename, "r", encoding="utf-8") as part:
			parser.feed(part.read())
		file_output.close()
			

if __name__ == '__main__':
	main()