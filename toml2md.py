import tomllib

# python toml2md.py


def convert(ja):
    filename = "README.md"
    if ja:
        filename = "README-ja.md"

    o = open(filename, "w", encoding="utf-8", newline="\n")

    with open("awesome-nostr-japan.toml", "rb") as toml_in:
        toml = tomllib.load(toml_in)

        for section_key in toml:
            section = toml[section_key]
            if section["caption"] == "awesome-nostr-japan":
                o.write("# " + section["caption"]+"\n\n")
            else:
                o.write("## " + section["caption"]+"\n\n")

            if ja:
                if "description_ja" in section and \
                        section["description_ja"] != "":
                    o.write(section["description_ja"]+"\n")
                elif "description" in section:
                    o.write(section["description"]+"\n")
            else:
                if "description" in section:
                    o.write(section["description"]+"\n")

            for item_key in section:
                item = section[item_key]
                if not isinstance(item, dict):
                    continue

                line = "* "
                if item["name"] == "":
                    line += "`" + item["address"] + "`"
                else:
                    line += "[" + item["name"] + "]"
                    line += "(" + item["address"] + ")"

                if ja:
                    if item["description_ja"] != "":
                        line += " - " + item["description_ja"]
                    elif item["description"] != "":
                        line += " - " + item["description"]
                else:
                    if item["description"] != "":
                        line += " - " + item["description"]

                if len(item["author_name"]) > 0:
                    for i in range(len(item["author_name"])):
                        if item["author_name"][i] != "":
                            line += " by [" + item["author_name"][i] + \
                                "]("+item["author_url"][i]+")"

                o.write(line+"\n")
            o.write("\n")


convert(False)
convert(True)
