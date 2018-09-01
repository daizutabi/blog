この記事では，[JupyterLab](https://jupyterlab.readthedocs.io/en/latest/)をカスタマイズする方法を説明します．

<!-- PELICAN_END_SUMMARY -->

## JupyterLab

```bash
(base) conda create -n jupyter python=3.6
(base) conda activate jupyter
(jupyter) conda install jupyterlab
```

## jupyterlab-vim

[Node.js](https://nodejs.org/ja/)のバージョン8.11.4 LTSをインストールする．


```bash
(jupyter) > conda install -c conda-forge nodejs==9.11.1
(jupyter) > npm install -g npm
(jupyter) > npm install -g --require webpack webpack-command
(jupyter) > jupyter labextension install jupyterlab_vim
```

## 拡張機能の有効化

`base`環境でJupyter Notebookを立ち上げます．Nbextensionsタブを開いて，以下の拡張をチェックして有効化します．

* Autopep8
* Codefolding
* ExecuteTime
* Table of Contents (2)
* VIM binding

一度Jupyter Notebookをシャットダウンして，再度立ち上げると拡張機能が使えるようになっているはずです．


## j, kキーのカスタマイズ

Notebookのセルのうち，Markdownセルはソフトラップで表示させるので，j, kキーで上下移動する際に，論理行ではなく，画面上の行で移動したほうが便利です．設定方法は，[公式ページ](https://github.com/lambdalisue/jupyter-vim-binding)で説明されています．

## スタイルシート

Notebookのスタイルを変更してみます．まずは設定ファイルを生成します．

```bash
(base) > jupyter notebook --generate-config
```

生成された`jupyter_notebook_config.py`をエディタで開いて，次の行を追加します．

``` python
c.NotebookApp.extra_static_paths = ['custom/custom.css']
```

スタイルシートは`~/.jupyter/custom/custom.css`に記載します．スタイルが変更されないようであれば，ブラウザのキャッシュをクリアするとよいでしょう．

スタイルシートの例を以下に示します．

```css
div.container {
    font-family: "Meiryo UI";
    font-size: 18px;
    line-height: 130%
}

pre {
    font-family:  "Migu 1M", "consolas", "IPAGothic";
    font-size: 16px;
}

div.CodeMirror {
    font-family:  "Migu 1M", "consolas", "IPAGothic";
    font-size: 16px;
}

div.cell {
    padding-top: 2px;
    padding-bottom: 2px;
}

div.inner_cell {
    margin: 0px;
}

div.prompt {
    padding-top: 8px;
    font-family: "Meiryo UI";
    font-size: 8px;
}

.cm-s-ipython span.cm-keyword {
  font-weight: normal;
}

#notebook {
    counter-reset: chapter;
}

.rendered_html h1 {
    font-size: 24px;
    padding: .55em 1em .55em 10px;
    border: 1px solid #ccc;
    border-top: 3px solid #3498db;
    background: -webkit-linear-gradient(top, #fff 0%, #f0f0fa 100%);
    background: linear-gradient(to bottom, #fff 0%, #f0f0fa 100%);
    box-shadow: 0 -1px 0 rgba(255, 255, 255, 1) inset;
    border-radius: 5px;
    color: #333366;
}

.rendered_html h2 {
    font-size: 20px;
    padding: .35em 1em .35em 10px;
    border: 1px solid #ccc;
    background: -webkit-linear-gradient(top, #fff 0%, #f0f0fa 100%);
    background: linear-gradient(to bottom, #fff 0%, #f0f0fa 100%);
    box-shadow: 0 -1px 0 rgba(255, 255, 255, 1) inset;
    border-radius: 5px;
    color: #333366;
}

.rendered_html h3 {
    font-size: 16px;
    margin: 10px 10px 0 0;
    padding: .15em 0em .15em 10px;
    border-bottom: 1px solid #d0d0fa;
    color: #333366;
    background: -webkit-linear-gradient(top, #fff 80%, #f0f0fa 100%);
    background: linear-gradient(to bottom, #fff 80%, #f0f0fa 100%);
}

.rendered_html h4 {
    font-size: 14px;
    margin: 8px 10px 0 0;
    padding: .15em 0px .15em 10px;
    border-bottom: 1px solid #d0d0fa;
    color: #333366;
}

.rendered_html h2:before {
    font-size: 14px;
    color: gray;
    content: counter(chapter)". ";
    counter-increment: chapter;
}

.rendered_html h3:before {
    font-size: 10px;
    color: gray;
    content: '■ '
}

.rendered_html h4:before {
    font-size: 8px;
    color: gray;
    content: '- '
}

div.text_cell_render {
    padding-left: 0px;
    padding-right: 0px;
}

div.text_cell_render p {
    margin-left: 20px;
}

div.output_subarea {
    padding-left: 20px;
}

div.timing_area {
	color: gray;
	font-size: 8px;
}

table.dataframe {
    border-collapse: collapse;
    border: none;
    font-size: 12px;
}

.dataframe thead tr,
.dataframe thead th,
.dataframe tbody tr,
.dataframe tbody th,
.dataframe tbody td {
    border: none;
    text-align: center;
    padding-left: 4px;
    padding-right: 4px;
    padding-top: 0px;
    padding-bottom: 0px;
}

.dataframe thead th {
    color: darkblue;
    background-color: lightcyan;
    border: 1px solid #333366;
}

.dataframe tbody th {
    color: black;
    background-color: #ffffee;
    border: 1px solid #666633;
}

.dataframe tbody td {
    color: black;
    background-color: #fcfcfc;
    border-bottom: 1px solid #b9b9b9;
    border-right: 1px solid #b9b9b9;
}

.dataframe tr th:last-child,
.dataframe tr td:last-child {
    border-right: 1px solid #555544;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
}

.dataframe tr:last-child td,
.dataframe tr:last-child th {
    border-bottom: 1px solid #555544;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
}

.dataframe tbody tr:nth-child(2n+1) td {
    background: #f1f6fc;
}
```
