#!/usr/bin/env python3

from __future__ import annotations

import sys
from typing import Any, cast

try:
    import tomllib  # type: ignore[import-not-found, import-untyped]
except ImportError:
    import toml as tomllib  # type: ignore[import-untyped]


def convert(ja: bool) -> None:
    filename = "README-ja.md" if ja else "README.md"

    with open(filename, "w", encoding="utf-8", newline="\n") as o:

        mode = "rb" if sys.version_info >= (3, 11) else "r"
        encoding = None if mode == "rb" else "utf-8"

        with open("awesome-nostr-japan.toml", mode, encoding=encoding) as toml_in:
            toml_data: dict[str, Any] = cast(Any, tomllib.load(toml_in))

            for section_key in toml_data:
                section = toml_data[section_key]

                caption = cast(str, section.get("caption", ""))
                if caption == "awesome-nostr-japan":
                    o.write(f"# {caption}\n\n")  # pyright: ignore[reportUnusedCallResult]
                else:
                    o.write(f"## {caption}\n\n")  # pyright: ignore[reportUnusedCallResult]

                if ja:
                    desc = (
                        section.get("description_ja", "")
                        or section.get("description", "")
                    )
                else:
                    desc = section.get("description", "")

                if desc:
                    o.write(f"{desc}\n")  # pyright: ignore[reportUnusedCallResult]

                o.write("\n")  # pyright: ignore[reportUnusedCallResult]

                for item_key in section:
                    item = section[item_key]
                    if not isinstance(item, dict):
                        continue

                    line = "* "
                    name = cast(str, item.get("name", ""))
                    address = cast(str, item["address"])

                    if not name:
                        line += f"`{address}`"
                    else:
                        line += f"[{name}]({address})"

                    if ja:
                        item_desc = (
                            item.get("description_ja", "")
                            or item.get("description", "")
                        )
                    else:
                        item_desc = item.get("description", "")

                    if item_desc:
                        line += f" - {item_desc}"

                    author_names = item.get("author_name", [])
                    author_urls = item.get("author_url", [])

                    if len(author_names) != len(author_urls):
                        print(
                            f"警告: 作者名とURLの数が一致しません (name: {len(author_names)}, url: {len(author_urls)})",
                            file=sys.stderr
                        )
                        print(f"  対象項目: {name or address}", file=sys.stderr)
                        min_len = min(len(author_names), len(author_urls))
                        author_names = author_names[:min_len]
                        author_urls = author_urls[:min_len]

                    if isinstance(author_names, str):
                        author_names = [author_names]
                    if isinstance(author_urls, str):
                        author_urls = [author_urls]

                    for name_part, url_part in zip(author_names, author_urls):
                        if name_part:
                            line += f" by [{name_part}]({url_part})"

                    o.write(line + "\n")  # pyright: ignore[reportUnusedCallResult]

                o.write("\n")  # pyright: ignore[reportUnusedCallResult]


if __name__ == "__main__":
    convert(False)  # README.md
    convert(True)   # README-ja.md
