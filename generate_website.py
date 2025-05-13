import os, shutil, hashlib
from html.parser import HTMLParser


# The current file output.
file_output = None

def get_hash(file):
	with open(file, 'rb') as fo:
		data = fo.read()
		file_hash = hashlib.sha256(data).hexdigest()
	return file_hash


stylesheet_hash = get_hash(r"sources\styles.css")
scripts_hash = get_hash(r"sources\scripts.js")
lunr_hash = get_hash(r"sources\lunr.js")
lunr_documents_hash = get_hash(r"sources\lunr_documents.js")
lunr_documents_id_map_hash = get_hash(r"sources\lunr_documents_id_map.js")


class VDalaHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag == "include":
			filename = attrs[0][1].strip("\"")
			with open(filename, "r", encoding="utf-8") as include:
				part = include.read()
				if "statics.html.part" in filename:
					part = part.replace("$stylesheet_hash", stylesheet_hash)
					part = part.replace("$scripts_hash", scripts_hash)
					part = part.replace("$lunr_hash", lunr_hash)
					part = part.replace("$lunr_documents_hash", lunr_documents_hash)
					part = part.replace("$lunr_documents_id_map_hash", lunr_documents_id_map_hash)
				file_output.write(part)
				file_output.flush()
		else:
			file_output.write("<%s" % tag)
			for attr_name, attr_value in attrs:
				file_output.write(" %s=\"%s\"" % (attr_name, attr_value))
			file_output.write(">")
			file_output.flush()

	def handle_endtag(self, tag):
		file_output.write("</%s>" % tag)

	def handle_data(self, data):
		file_output.write(data)

parser = VDalaHTMLParser()

pages = [
	("sources", "index.html.page"),
	("sources", "event.html.page"),
	("sources", "opening_hours.html.page"),
	("sources", "contact.html.page"),
	("sources", "membership.html.page"),
	("sources", "pay_membership_fee.html.page"),
	("sources", "alumnus.html.page"),
	("sources", "honorary_members.html.page"),
	("sources", "leaving_nation.html.page"),
	("sources", "history.html.page"),
	("sources", "sister_nations.html.page"),
	("sources", "documents.html.page"),
	("sources", "landskap.html.page"),
	("sources", "news.html.page"),
	("sources", "safety.html.page"),
	("sources", "accommodation.html.page")
]

image_files = [
	(r"sources\images", "huset.jpg"),
	(r"sources\images", "engagera_dig.jpg"),
	(r"sources\images", "v_dala.png")
]

icon_files = [
	(r"sources\images\google-materials", "search_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg")
]

contact_images = [
	# Images on people for the contact page.
	(r"sources\images\contact", "adrian_pfeffer.png"),
	(r"sources\images\contact", "johan_tysk.png"),
	(r"sources\images\contact", "josefina_jonsson.png"),
	(r"sources\images\contact", "adrian_pfeffer_2.png"),
	(r"sources\images\contact", "joel_redner.jpg"),
	(r"sources\images\contact", "rolf_kroon.png"),
	(r"sources\images\contact", "helene_erbing_backstrom.png"),
	(r"sources\images\contact", "linn_tagerud.png"),
	(r"sources\images\contact", "veronica_ekholm.png"),
	(r"sources\images\contact", "hans_petersson.png"),
	(r"sources\images\contact", "katarina_barrling.png"),
	(r"sources\images\contact", "charlii_engstrom.png"),
	(r"sources\images\contact", "vera_sintorn.jpg"),
	(r"sources\images\contact", "sofia_toll.png"),
	(r"sources\images\contact", "marlene_burwik.png"),
	(r"sources\images\contact", "karin_karlsson.png"),
	(r"sources\images\contact", "adam_tunner_weiderud.png")

]

mixed_files = [
	("sources", "styles.css"),
	("sources", "scripts.js"),
	("sources", "lunr_documents.js"),
	("sources", "lunr.js"),
	("sources", "lunr_documents_id_map.js")
]

mixed_files_mobile = [
	(r"sources\mobile", "styles.css"),
	(r"sources\mobile", "scripts.js")
]

mobile_pages = [
	(r"sources\mobile", "index.html.page"),
	(r"sources\mobile", "accommodation.html.page")
]

output_folder = "upload"

def render_page_to_file(pages, output_folder):
	global file_output

	for path, filename in pages:
		source = os.path.join(path, filename)
		dest = os.path.join(output_folder, filename.rstrip(".page"))
		file_output = open(dest, "w", encoding="utf-8")
		with open(source, "r", encoding="utf-8") as part:
			parser.feed(part.read())
		file_output.close()

def main():
	global output_folder

	render_page_to_file(pages, output_folder)
	
	mobile_pages_dest = os.path.join(output_folder, "mobile")
	render_page_to_file(mobile_pages, mobile_pages_dest)

	for path, filename in image_files:
		source = os.path.join(path, filename)
		dest = os.path.join(output_folder, "images", filename)
		shutil.copy(source, dest)

	for path, filename in mixed_files:
		source = os.path.join(path, filename)
		dest = os.path.join(output_folder, filename)
		shutil.copy(source, dest)

	for path, filename in mixed_files_mobile:
		source = os.path.join(path, filename)
		dest = os.path.join(output_folder, "mobile", filename)
		shutil.copy(source, dest)

	for path, filename in contact_images:
		source = os.path.join(path, filename)
		dest = os.path.join(output_folder, r"images\contact", filename)
		shutil.copy(source, dest)

	for path, filename in icon_files:
		source = os.path.join(path, filename)
		dest = os.path.join(output_folder, r"images\google-materials", filename)
		shutil.copy(source, dest)
			

if __name__ == '__main__':
	main()