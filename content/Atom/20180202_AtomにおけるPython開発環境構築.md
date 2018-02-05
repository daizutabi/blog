Modified: 2018-02-05

AtomテキストエディタにPython開発環境を構築します．細かい設定を丁寧に説明し，快適な開発環境を整備することを目指します．

<!-- PELICAN_END_SUMMARY -->

それでは，Python開発に役立つパッケージを紹介していきます．各節のヘッダがパッケージ名になっているので，特に記載のない限り，その名前でパッケージを検索してインストールしてください．その後，Settings，Keymap，Stylesheetの各項目を必要に応じて設定していきます．

## vim-mode-plus

AtomでVimキーバインドを実現します．このパッケージがなかったら，Atomを使っていないでしょう．

### Settings

以下のキーマップを有効にします．

* `Y`: 'yank-to-last-character-of-line'
* `_`: 'replace-with-register'
* `c c`: 'change inner-smart-word'
* `;`: 'inner-any-pair' in 'operator-pending-mode'
* `;`: 'inner-any-pair' in 'visual-mode'

以下の設定を有効にします．

* Automatically Escape Insert Mode On Activate Pane Item Change

### Keymap

Markdownなどのファイルを編集するときには，ソフトラップを有効にするので，論理行の移動キーと物理行の移動キーをスワップします．

[File] > [Keymap...]を選択して，`keymap.cson`を開き，次の行を追加します．好みに応じて変更してください．

```cson
# keymap.cson
'atom-text-editor.vim-mode-plus:not(.insert-mode)':
  'j': 'vim-mode-plus:move-down-screen'
  'k': 'vim-mode-plus:move-up-screen'
  'g j': 'vim-mode-plus:move-down'
  'g k': 'vim-mode-plus:move-up'
```

（以下のキーマップの設定では，同様に`keymap.cson`を編集します．）

`s`キーに，ツリービュー，ペーン，タブ間の移動のプレフィックスの役割を割り当てます．

```cson
'atom-text-editor.vim-mode-plus.normal-mode':
  's': 'vim-mode-plus:nop'
  's f': 'tree-view:toggle-focus'
  's v': 'pane:split-left-and-copy-active-item'
  's s': 'pane:split-up-and-copy-active-item'
  's j': 'window:focus-pane-below'
  's k': 'window:focus-pane-above'
  's h': 'window:focus-pane-on-left'
  's l': 'window:focus-pane-on-right'
  's n': 'window:focus-next-pane'
  's p': 'window:focus-previous-pane'
  's 1': 'pane:show-item-1'
  's 2': 'pane:show-item-2'
  's 3': 'pane:show-item-3'
  's 4': 'pane:show-item-4'
  's 5': 'pane:show-item-5'
  's 6': 'pane:show-item-6'
  's 7': 'pane:show-item-7'
  's 8': 'pane:show-item-8'
  's 9': 'pane:show-item-9'
  's c': 'pane:close'

'.tree-view':
  's f': 'tree-view:toggle-focus'
```

関数内で，引数の位置をローテーションします．

```cson
'atom-text-editor.vim-mode-plus.normal-mode':
  'g >': 'vim-mode-plus:rotate-arguments-of-inner-pair'
  'g <': 'vim-mode-plus:rotate-arguments-backwards-of-inner-pair'
```

## ex-mode

`:w`などのコマンドを使えるようにします．

## vim-mode-plus-keymaps-for-surround

サラウンド機能のキーマップ設定です．たとえば，ある単語にカーソルを合わせて，`y s i w (`と入力すると，その単語をカッコでくくります．他に`c s`，`d s`などもあります．

## cursor-history

オリジナルのVimと同様にカーソルのジャンプ履歴に素早くアクセスします．

### Keymap

```cson
'atom-text-editor.vim-mode-plus.normal-mode':
  'ctrl-i': 'cursor-history:next'
  'ctrl-o': 'cursor-history:prev'
```

## quick-highlight

コードを編集するときに，同じ文字列をハイライトすると，どこで再利用されているか一目でわかります．

### Keymap

```cson
'atom-text-editor.vim-mode-plus.normal-mode, atom-text-editor.vim-mode-plus.visual-mode':
  'ctrl-m': 'vim-mode-plus-user:quick-highlight-word'
  'g m': 'vim-mode-plus-user:quick-highlight'
  'space m': 'quick-highlight:clear'
```

## tab-numbers

タブの横にタブの番号を表示します．この数値をもとに`s <number>`で移動できます．

## MagicPython

Pythonコードのシンタックスハイライターに，MagicPythonを使います．コアパッケージのlanguage-pythonはdisableにします．

### Settings

* Tab Type: soft

### Stylesheet

色の設定を追加します．[File] > [Stylesheet]を選択して，`styles.less`を開き，次の行を追加します．好みに応じて変更してください．

```css
/* styles.less */
atom-text-editor .syntax--source.syntax--python {
  .syntax--keyword.syntax--control,
  .syntax--keyword.syntax--operator.syntax--logical,
  .syntax--storage.syntax--type {
    /* font-weight: bold; */
  }

  .syntax--entity.syntax--name.syntax--function.syntax--decorator {
    color: #6590FF;
  }

  .syntax--self {
    font-style: italic;
    color: #A57083;
  }

  .syntax--fstring {
    color: #6c65ff;
  }

  .syntax--function.syntax--magic,
  .syntax--magic {
    color: #63AA63;
  }

  .syntax--docstring,
  .syntax--docstring .syntax--punctuation {
    color: #666666;
  }

  .syntax--import.syntax--keyword.syntax--control {
    color: #A69646;
  }

  .syntax--support.syntax--function.syntax--builtin {
    color: #A69666;
  }

  .syntax--support.syntax--type.syntax--python {
    color: #A696A6;
  }

  .syntax--arithmetic.syntax--operator,
  .syntax--keyword.syntax--unpacking {
    color: #76A6A6;
  }

  .syntax--numeric {
    color: #D69696;
  }

  .syntax--constant.syntax--other {
    color: #D69696;
  }
}
```

（以下のスタイルシートの設定では，同様に`styles.less`を編集します．）

## autocomplete-plus

コアパッケージに含まれているので，インストールの必要はありません．

### Settings

補完の方法，カーソル移動の方法などを設定します．

* Keymap For Confirming A Suggestion: tab always, enter when suggestion explicitly selected
* Use Core Movement Commands: false
* Suppress Activation For Editor Classes: vim-mode-plus.normal-mode, vim-mode-plus.visual-mode, vim-mode-plus.operator-pending-mode, vim-mode-plus.insert-mode.replace

### Keymap

Vimライクなキー操作で補完候補間を移動できるようにします．この設定を有効にするには，上のUse Core Movement Commandsを非選択にする必要があります．

```cson
'atom-text-editor.autocomplete-active':
  'ctrl-k': 'autocomplete-plus:move-up'
  'ctrl-j': 'autocomplete-plus:move-down'
  'ctrl-h': 'autocomplete-plus:move-to-top'
  'ctrl-l': 'autocomplete-plus:move-to-bottom'
  'pageup': 'autocomplete-plus:page-up'
  'pagedown': 'autocomplete-plus:page-down'
```

### Stylesheet

補完リストのフォントサイズを小さめに設定します．

```css
.autocomplete-plus li {
  font-size: 11pt;
}
```

## ide-python

Atom IDE を使ってPython開発をするためのパッケージです．言語サーバーが必要なので，Condaの`base`環境下にインストールします：

```bash
(base) > pip install python-language-server
```

### Settings

Condaの`base`環境にインストールされた`pyls.exe`をフルパスで指定します．

* Python Language Server Path: C:\Users\daizu\Miniconda3\Scripts\pyls.exe

## autocomplete-python

autocomplete-plusのPython拡張です．本パッケージで提供される機能は， ide-pythonと重複します．しかし，`base`環境以外の仮想環境下にインストールされたPythonパッケージへのジャンプなどがide-pythonではできない（or 設定方法がわからない）ので，autocomplete-plusも同時に入れておきます．

### Settings

* Use Kite-powered Completions: false
* Python Executable Paths: C:\Users\daizu\Miniconda3\python.exe
* Extra Paths For Packages: C:\Users\daizu\Miniconda3\envs\example\Lib\site-packages
* Case Insensitive Completion: false
* Use Fussy Matcher For Completions: false

上のExtra Paths For Packagesの設定は一例です．Condaの`example`環境を登録しています．他にも登録したい仮想環境がある場合には，セミコロンで区切って追記します．

## python-ident

Pythonコード入力時にインデントを自動で調整します．

## atom-beautify

Pythonコードを整形します．ide-pythonでも整形はできますが，atom-beautifyでは，`import`の並び替えができます．整形するためのPythonパッケージをインストールします：

```bash
(base) > pip install autopep8 isort
```

### Settings

* Executables > autopep8: C:\Users\daizu\Miniconda3\Scripts\autopep8.exe
* Executables > isort: C:\Users\daizu\Miniconda3\Scripts\isort.exe
* Sort imports: true

## Hydrogen

Jupyter clientを使って，Atom上でPythonコードの実行ができます．インタラクティブな実行が可能なので，非常に重宝します．Hydrogenを使う仮想環境下で，以下を実行します：

```bash
(example) > conda install jupyter
(example) > python -m ipykernel install --user --name example
```

### Settings

* Language Mappings: {"python": "magicpython"}

### Keymap

```cson
'atom-text-editor':
  'f8': 'hydrogen:clear-results'
  'f9': 'hydrogen:run-all-above'
  'f10': 'hydrogen:run-all'
```

## platformio-ide-terminal

Atom内でターミナルを実行します．

### Settings

* Auto Run Command: C:\Users\daizu\Miniconda3\Scripts\activate.bat base
* Shell Override: C:\Windows\System32\cmd.exe

## hydrogen-launcher

Hydrogenで実行中のカーネルに接続されたJupyterコンソールを表示します．

### Keymap

```cson
'atom-text-editor':
  'ctrl-alt-j': 'hydrogen-launcher:launch-jupyter-console-in-platformio-terminal'
```

## その他のパッケージ

Pythonとは直接関係ないですが，以下のパッケージもインストールするとよいでしょう．

* git-plus
* file-icons
* minimap系

## 初期化スクリプト

パッケージではありませんが，文字化けを防ぐために，[File] > [Init Script...]を選択して，`init.coffee`を開き，次の行を追加します．

```coffee
# init.coffee
process.env.PYTHONIOENCODING = "utf-8";
```

以上で，開発環境が整いました．
