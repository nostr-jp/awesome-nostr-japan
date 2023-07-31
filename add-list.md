# リストへの追加方法
リストに追加するには、以下の手順を踏んでください。
README.md と README-ja.md を直接編集しないで下さい。

## awesome-nostr-japan.tomlを編集する
リストの本体は、awesome-nostr-japan.tomlです。

以下のような書式で並んでいます。

アイテムは、この書式で追加してください。  
カテゴリも同様の形で追加することができます。

```toml
[内部カテゴリ名]
caption = "カテゴリの表示名"

  [内部カテゴリ名.内部アイテム名]
  name = "表示名"
  address = "https://example.com/"
  description = "English description"
  description_ja = "日本語の説明文"
  author_name = ["制作者名"]
  author_url = ["https://example.com/"]

　# 必要な数だけ並べていく

[WebServices]
caption = "Web Services"

  [WebServices.Nostrends]
  name = "Nostrends"
  address = "https://nostrends.vercel.app"
  description = "Trending posts on nostr."
  description_ja = "nostrのトレンド表示サイト"
  author_name = ["akiomik"]
  author_url = ["https://github.com/akiomik"]
```

内部カテゴリ名、内部アイテム名はどんな名前をつけても表示上の名前には影響しません。  
プログラム上での識別でのみ使用します。

# toml2md.pyを実行する。
事前に toml ファイルの正当性を確認されたい場合は以下を実行して下さい。
python 3.11以降を導入してください。

`python toml2md.py`

で実行します。

+ README.md
+ README-ja.md

が生成されます。README.md と README-ja.md の変更はコミットに含まないで下さい。

# プルリクエストする
プルリクエストを作成してください。
