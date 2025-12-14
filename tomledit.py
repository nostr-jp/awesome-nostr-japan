import tkinter as tk
from tkinter import messagebox
import tomllib

from toml2md import convert

hf_list = [
    "awesome-nostr-japan",
    "License",
    "Author"
]

toml_filename = "awesome-nostr-japan.toml"
toml_header = """\
[awesome-nostr-japan]

caption = "awesome-nostr-japan"
description = "Awesome [nostr](https://nostr.com/) in Japan. Software, Web service, Clients, Bots created by Japanese. [日本語版](README-ja.md)"
description_ja = "日本版Awesome [nostr](https://nostr.com/). 日本製のSoftware, Web service, Clients, Bots. [English version](README.md)"\
"""

toml_comment = """\
# Key is for reference only.\
"""

toml_footer = """\
[License]

caption = "License"
description = "MIT"

[Author]

caption = "Author"
description = "Yasuhiro Matsumoto (a.k.a. mattn)"\
"""

class Toml:
    def __init__(self):
        super().__init__()

    def open_toml(self, filename:str) -> dict:
        toml_data:dict = {}
        with open(filename, mode="rb") as f:
            toml_data = tomllib.load(f)
        
        return toml_data

    def save_toml(self, filename:str, toml_data:dict) -> None:
        # toml書式の生成
        with open(filename, mode="w", encoding="utf-8") as f:
            # ヘッダーの書き込み
            f.write(toml_header+"\n\n")

            # コメントの書き込み
            f.write(toml_comment+"\n\n")

            # 各項目の書き込み
            for genre, fields in toml_data.items():
                if genre in hf_list: continue
                f.write(f"[{genre}]\n\n")
                f.write(f"caption = \"{genre}\"\n\n")
                for field, value in fields.items():
                    if field == "caption": continue # ゴミデータ

                    if not any(c in field for c in [' ', '/']):
                        f.write(f"  [{genre}.{field}]\n")
                    else:
                        f.write(f"  [{genre}.\"{field}\"]\n")
                    for k, v in value.items():
                        if isinstance(v, list):
                            f.write(f"  {k} = {v}\n")
                        else:
                            f.write(f"  {k} = \"{v.replace('"', '\\"')}\"\n")
                    f.write("\n")
                f.write("\n")

            # フッターの書き込み
            f.write(toml_footer)

class App:
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.root.title("Tomlファイルエディタ")
        self.root.geometry("500x450")  # ウィンドウサイズを設定
        self.root.resizable(False, False)  # リサイズ不可能
        
        self.toml_data = Toml().open_toml(toml_filename)
        self.genre_list = []
        self.field_list = []

        print(self.toml_data)

        self.create_toolbar()
        self.create_widgets()
    
    def parse_genre_list(self, toml_data:dict) -> list:
        return [k for k in toml_data.keys()]
    
    def parse_field_list(self, key:str, toml_data:dict) -> list:
        return [v for k, v in toml_data.items() if k == key]
    
    def parse_field_items(self, field_list:list) -> list:
        return [k for e in field_list for k in e.keys()]

    def parse_field_values(self, key:str, field_list:list) -> list:
        return [v for e in field_list for k, v in e.items() if k == key]
    
    def delete_field_values(self, genre:str, field:str, toml_data:dict) -> dict:
        try:
            toml_data[genre] = {k:v for k,v in toml_data[genre].items() if k != field}
        except:
            pass
        return toml_data
    
    def add_field_values(self, genre:str, field:str, toml_data:dict) -> dict:
        if not isinstance(genre, str) or not isinstance(field, str): return toml_data
        if genre == "" or field == "": return toml_data

        field_dict = {
            "name":"",
            "address":"",
            "description":"",
            "description_ja":"",
            "author_name": [],
            "author_url": []
        }
        try:
            toml_data[genre].update({field:field_dict})
        except:
            pass

        return toml_data
    
    def update_field_values(self, genre:str, field:str, values:dict, toml_data:dict) -> dict:
        if not all((
            isinstance(genre, str), genre != "",
            isinstance(field, str), field != "",
            isinstance(values, dict),
        )): return toml_data
        keys = ["name", "address", "description", "description_ja", "author_name", "author_url"]
        if len(values) != 6: return toml_data
        if not all(tuple(True if e in keys else False for e in values.keys())): return toml_data
        if not all((
            isinstance(values["author_name"], list),
            isinstance(values["author_url"], list)
        )): return toml_data
        
        try:
            toml_data[genre].update({field:values})
        except:
            pass

        return toml_data

    def create_toolbar(self):
        # ツールバー用のフレームを作成
        self.toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        
        # 新規作成ボタンを作成
        create_button = tk.Button(self.toolbar, text="新規作成", command=self.create_form)
        create_button.grid(row=0, column=0, padx=2, pady=2)  # grid を使用

        # 削除ボタンを作成
        delete_button = tk.Button(self.toolbar, text="削除", command=self.delete_form)
        delete_button.grid(row=0, column=1, padx=2, pady=2)  # grid を使用

        # 変換ボタンを作成
        convert_button = tk.Button(self.toolbar, text="変換", command=self.convert_form)
        convert_button.grid(row=0, column=2, padx=2, pady=2)  # grid を使用

        # ツールバーをウィンドウに配置
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky=tk.W + tk.E)

    def create_widgets(self):
        # 各入力フィールドの作成

        # ジャンルのプルダウンメニューを作成
        tk.Label(self.root, text="ジャンル").grid(row=1, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.genre_var = tk.StringVar(self.root)
        self.genre_var.set("選択してください")  # デフォルトの値
        self.genre_list = self.parse_genre_list(self.toml_data)
        self.genre_list = [e for e in self.genre_list if e not in hf_list] # ヘッダーとフッターを取り除く
        self.genre_menu = tk.OptionMenu(self.root, self.genre_var, *self.genre_list)
        self.genre_menu.grid(row=1, column=1, sticky=tk.W + tk.E, padx=5, pady=5)
        
        # ジャンルの選択が変更されたときのトレースを設定
        self.genre_var.trace("w", self.update_genre)
        
        # 項目のプルダウンメニューを作成
        tk.Label(self.root, text="項目").grid(row=2, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.field_var = tk.StringVar(self.root)
        self.field_var.set("選択してください")  # デフォルトの値
        self.field_menu = tk.OptionMenu(self.root, self.field_var, "")
        self.field_menu.grid(row=2, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        # 項目が選択されたときのトレースを設定
        self.field_var.trace("w", self.update_field)

        tk.Label(self.root, text="表題").grid(row=3, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.title_var = tk.StringVar(self.root)
        self.title_entry = tk.Entry(self.root, textvariable=self.title_var)
        self.title_entry.grid(row=3, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        tk.Label(self.root, text="URL").grid(row=4, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.url_var = tk.StringVar(self.root)
        self.url_entry = tk.Entry(self.root, textvariable=self.url_var)
        self.url_entry.grid(row=4, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        tk.Label(self.root, text="概要(英語)").grid(row=5, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.summary_eng_entry = tk.Text(self.root, height=5, width=40)
        self.summary_eng_entry.grid(row=5, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        tk.Label(self.root, text="概要(日本語)").grid(row=6, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.summary_jpn_entry = tk.Text(self.root, height=5, width=40)
        self.summary_jpn_entry.grid(row=6, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        tk.Label(self.root, text="作者名").grid(row=7, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.author_name_var = tk.StringVar(self.root)
        self.author_name_entry = tk.Entry(self.root, textvariable=self.author_name_var)
        self.author_name_entry.grid(row=7, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        tk.Label(self.root, text="作者URL").grid(row=8, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.author_url_var = tk.StringVar(self.root)
        self.author_url_entry = tk.Entry(self.root, textvariable=self.author_url_var)
        self.author_url_entry.grid(row=8, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        # 完了ボタンの作成
        submit_button = tk.Button(self.root, text="入力完了", command=self.submit_form)
        submit_button.grid(row=9, columnspan=2, pady=10)

        # 各列の幅を設定
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)

    def update_genre(self, *args):
        selected_genre = self.genre_var.get()
        self.field_list = self.parse_field_list(selected_genre, self.toml_data)
        fields = self.parse_field_items(self.field_list)
        fields = [e for e in fields if e not in ["caption"]] # ゴミデータ

        self.field_menu["menu"].delete(0, "end")
        if fields:
            for field in fields:
                self.field_menu["menu"].add_command(label=field, command=tk._setit(self.field_var, field))
        else:
            self.field_menu["menu"].add_command(label="", command=tk._setit(self.field_var, ""))
        
        self.field_var.set("選択してください")
        self.title_var.set("")
        self.url_var.set("")
        self.summary_eng_entry.delete('1.0', 'end')
        self.summary_jpn_entry.delete('1.0', 'end')
        self.author_name_var.set("")
        self.author_url_var.set("")

    def update_field(self, *args):
        selected_field = self.field_var.get()
        field_values = self.parse_field_values(selected_field, self.field_list)

        if field_values:
            for value in field_values:
                self.title_var.set(value.get('name'))

                self.url_var.set(value.get('address'))
                
                self.summary_eng_entry.delete('1.0', 'end')
                self.summary_eng_entry.insert('end', value.get('description'))
                
                self.summary_jpn_entry.delete('1.0', 'end')
                self.summary_jpn_entry.insert('end', value.get('description_ja'))

                self.author_name_var.set(str.join("\n", value.get('author_name')))

                self.author_url_var.set(str.join("\n", value.get('author_url')))

    def submit_form(self):
        # ジャンルをプルダウンメニューから取得
        genre = self.genre_var.get()

        # その他の入力内容を取得
        title = self.title_entry.get()
        url = self.url_entry.get()
        summary_eng = self.summary_eng_entry.get("1.0", tk.END).replace('\r','').replace('\n','')
        summary_jpn = self.summary_jpn_entry.get("1.0", tk.END).replace('\r','').replace('\n','')
        author_name = self.author_name_entry.get()
        author_url = self.author_url_entry.get()

        # 入力内容の確認のために表示（デバッグ用）
        print(f"ジャンル: {genre}, 表題: {title}, URL: {url}, 概要(英語): {summary_eng.strip()}, 概要(日本語): {summary_jpn.strip()}, 作者名: {author_name}, 作者URL: {author_url}")

        values = {
            "name":title,
            "address":url,
            "description":summary_eng.strip(),
            "description_ja":summary_jpn.strip(),
            "author_name": [author_name.strip(",")],
            "author_url": [author_url.strip(",")]
        }

        self.toml_data = self.update_field_values(genre, self.field_var.get(), values, self.toml_data)

        # ファイルへの書き込み
        Toml().save_toml(toml_filename, self.toml_data)

        # メッセージボックスで表示（任意）
        messagebox.showinfo("完了", "入力が完了しました！")
    
    def create_form(self):
        # ポップアップウィンドウを作成
        popup = tk.Toplevel(self.root)
        popup.title("入力フォーム")

        # ジャンルの選択
        tk.Label(popup, text="ジャンル:").grid(row=0, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        genre_var = tk.StringVar(self.root)
        genre_var.set("")  # デフォルトの値
        genre_menu = tk.OptionMenu(popup, genre_var, *self.genre_list)
        genre_menu.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        # 項目の入力
        tk.Label(popup, text="項目:").grid(row=1, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        field_entry = tk.Entry(popup)
        field_entry.grid(row=1, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        # 確認ボタン
        confirm_button = tk.Button(popup, text="追加", command=lambda: self.add_entry(genre_var.get(), field_entry.get(), popup))
        confirm_button.grid(row=2, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

    def add_entry(self, genre, field, popup):
        # 入力されたジャンルと項目を処理する
        print(f"ジャンル: {genre}, 項目: {field}")
        self.toml_data = self.add_field_values(genre, field, self.toml_data)

        self.genre_var.set(genre)
        self.field_var.set(field)
        self.title_var.set("")
        self.url_var.set("")
        self.summary_eng_entry.delete('1.0', 'end')
        self.summary_jpn_entry.delete('1.0', 'end')
        self.author_name_var.set("")
        self.author_url_var.set("")

        # ポップアップを閉じる
        popup.destroy()

    def delete_form(self):
        genre = self.genre_var.get()
        field = self.field_var.get()
        self.delete_field_values(genre, field, self.toml_data)

        self.genre_var.set("選択してください")
        self.field_var.set("選択してください")
        self.title_var.set("")
        self.url_var.set("")
        self.summary_eng_entry.delete('1.0', 'end')
        self.summary_jpn_entry.delete('1.0', 'end')
        self.author_name_var.set("")
        self.author_url_var.set("")

        messagebox.showinfo("削除", "削除しました！")

    def convert_form(self):
        convert(False)  # README.md
        convert(True)   # README-ja.md

        messagebox.showinfo("変換", "変換しました！")

# メインループを開始
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
