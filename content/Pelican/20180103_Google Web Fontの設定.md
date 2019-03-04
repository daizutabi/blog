[Google Fonts + 日本語早期アクセス](https://googlefonts.github.io/japanese/)の設定を行います．今回は，さわらびゴシックを使ってみます．本ブログのPelicanテーマである[VoidyBootstrap](http://www.voidynullness.net/page/voidy-bootstrap-pelican-theme/)での設定方法になります．



`pelicanconf.py`に以下を追加します．

``` python
THEME = 'voidy-bootstrap/'
STYLESHEETS = (
    'custom/custom.css',
    # other stylesheets
)

STYLESHEET_URLS = (
    'https://fonts.googleapis.com/earlyaccess/sawarabigothic.css',
    # other stylesheet_urls
)
```

`voidy-bootstrap`ディレクトリ下に`static/css/custom.css`を作成し，以下を追加します．

```css
body {
  font-family: 'Sawarabi Gothic';
}
```

簡単に設定できました．
