# リストへの追加方法

リストに項目を追加するには、以下の手順を踏んでください。
README.md と README-ja.md を直接編集しないで下さい。

## 環境を準備する

Python のバージョンが 3.11 以降であることを確認してください。もし 3.11 未満の場合は tomllib モジュールが標準で含まれていないため、手動で toml モジュールをインストールする必要があります。

既に環境構築が済んでいる場合、このステップはスキップしてください。

### 実行環境の準備

このリポジトリのスクリプトを実行する際には、**仮想環境(venv)** を使うことをおすすめします。
これにより、システム全体の Python 環境を汚さずに、プロジェクト専用の依存関係だけをインストールできます。

#### 1. リポジトリをクローン

```bash
git clone https://github.com/nostr-jp/awesome-nostr-japan.git
cd awesome-nostr-japan
```

#### 2. 仮想環境の作成

```
python -m venv venv
```

Windows の場合:

```
venv\Scripts\activate
```

Linux または macOS の場合:

```
source venv/bin/activate
```

有効化されたことを確認するには、コマンドラインのプロンプトに `(venv)` が表示されていることを確認してください。

#### 3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

#### 4. 仮想環境の無効化（作業終了後）

作業が終わったら、仮想環境を抜けます。

```bash
deactivate
```

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
