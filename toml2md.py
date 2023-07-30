import sys
import tomllib

# python toml2md.py

o = open("README.md","w", encoding="utf-8")

with open("awesome-nostr-japan.toml", "rb") as toml_in:
    toml = tomllib.load(toml_in)

    for section_key in toml:
        section = toml[section_key]
        if section["caption"] == "awesome-nostr-japan":
            o.write("# " + section["caption"]+"\n\n")
        else:
            o.write("## " + section["caption"]+"\n\n")

        if "description" in section:
            o.write(section["description"]+"\n")

        for item_key in section:
            item = section[item_key]
            if not isinstance(item,dict):
                continue

            line = "* "
            if item["name"] == "":
                line += "`" +item["address"]+ "`"
            else:
                line += "[" +item["name"]+ "]"
                line += "(" +item["address"]+ ")"


            if item["description"] != "":
                line += " - " +item["description"]

            if len(item["author_name"]) > 0:
                for i in range(len(item["author_name"])):
                    if item["author_name"][i] != "":
                        line += " by [" +item["author_name"][i] + "]("+item["author_url"][i]+")"
                    
            o.write(line+"\n")
        o.write("\n")
