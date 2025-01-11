# furigana_info

`furigana_info` は、ふりがな情報サイト（[furigana.info](https://furigana.info/)）から指定した単語の読み仮名や例文を取得するための Python ライブラリです。このライブラリを使用すると、簡単に日本語単語の読み仮名やその使用例をプログラム内で利用できます。

## 特徴

- 指定した単語の読み仮名とその割合を取得
- 読み仮名ごとの例文を取得
- シンプルなAPIで簡単に使用可能

## インストール

1.リポジトリをクローンまたはZIPをダウンロードして解凍します。
```bash
git clone https://github.com/asfrgrtgd/furigana-info.git
```

2.クローンしたディレクトリに移動します。

```bash
cd furigana-info
```

3.pipを使用してインストールします。

```bash
pip install .
```

## 使い方

コード

```python
import furigana_info

def main():
    word = "濃黒"
    try:
        result = furigana_info.get_furigana(word)
        print(f"単語: {result['word']}")
        print("読み方と割合:")
        for reading in result["readings"]:
            print(f"  - {reading['yomi']}: {reading['percentage']}")
        
        print("\n例文:")
        for example in result["examples"]:
            print(f"  - 読み: {example['reading']}")
            print(f"    テキスト: {example['text']}\n")
    except furigana_info.FuriganaInfoError as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
```

実行例

```bash
$ python test_script.py
単語: 濃黒
読み方と割合:
  - どすぐろ: 50.0%
  - まつくろ: 50.0%

例文:
  - 読み: どすぐろ
    テキスト: 赭土色の膚で、髪の長い、手足の長い、爪の長い、人か猿か判らぬような怪物である。彼は市郎の靴で額の真向を蹴破られたと見えて、濃黒いような鮮血が其凄愴い半面を浸していた。
  
  - 読み: まつくろ
    テキスト: 其の鈍色を破ツて、處々に煤煙が上騰ツてゐる。眞直に衝騰る勢が、何か壓力に支へられて、横にも靡かず、ムツクラ／＼、恰で沸騰でもするやうに、濃黒になツてゐた。

```
