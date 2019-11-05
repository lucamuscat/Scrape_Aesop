from requests_html import HTMLSession


session = HTMLSession()
r = session.get("https://aesopsfables.org/")
sidebar = r.html.find("#sidebar")
sidebar_links = sidebar[0].absolute_links
unwanted_links = [
    "https://aesopsfables.org/",
    "https://aesopsfables.org/randomfable.php",
]
for link in unwanted_links:
    sidebar_links.discard(link)

fable_text = list()

for fable_catagory in sidebar_links:
    temp_sesh = session.get(fable_catagory)
    main_body = temp_sesh.html.find("#mainbody")
    fables = main_body[0].absolute_links
    for fable in fables:
        temp_sesh2 = session.get(fable)
        main_body = temp_sesh2.html.find("#mainbody")
        fable_text.append(main_body[0].text)

"""
EOF = End of fable. This is going to be used to get rid of the
excess google ads data which comes with the scraped data
"""
EOF_string = "&lt;!--"
fable_text_cleaned = [x[:x.find(EOF_string)] for x in fable_text]


with open("test_text.txt", "w") as file:
    file.write("\n".join(fable_text_cleaned))


print("Done")
