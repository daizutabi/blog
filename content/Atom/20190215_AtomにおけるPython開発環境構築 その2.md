AtomテキストエディタにPython開発環境を構築します。細かい設定を丁寧に説明し、快適な開発環境を整備することを目指します。

<!-- PELICAN_END_SUMMARY -->

それでは，Python開発に役立つパッケージを紹介していきます．各節のヘッダがパッケージ名になっているので，特に記載のない限り，その名前でパッケージを検索してインストールしてください．その後，Settings，Keymap，Stylesheetの各項目を必要に応じて設定していきます．

## platformio-ide-terminal

Atom内でターミナルを実行します．

### Settings

* Auto Run Command: C:\Users\daizu\Miniconda3\Scripts\activate.bat base
* Shell Override: C:\Windows\System32\cmd.exe


## vim-mode-plus, ex-mode, vim-mode-plus-keymaps-for-surround, cursor-history, quick-highlight

 AtomでVimキーバインドを実現します。

### Settings

vim-mode-plusで、以下のキーマップを有効にします．

* `Y`: 'yank-to-last-character-of-line'
* `_`: 'replace-with-register'
* `c c`: 'change inner-smart-word'
* `;`: 'inner-any-pair' in 'operator-pending-mode'
* `;`: 'inner-any-pair' in 'visual-mode'

以下の設定を有効にします．

* Automatically Escape Insert Mode On Activate Pane Item Change

### Keymap

```cson
'atom-text-editor.vim-mode-plus:not(.insert-mode)':
  'j': 'vim-mode-plus:move-down-screen'
  'k': 'vim-mode-plus:move-up-screen'
  'g j': 'vim-mode-plus:move-down'
  'g k': 'vim-mode-plus:move-up'
  'ctrl-m': 'vim-mode-plus-user:quick-highlight-word'
  'g m': 'vim-mode-plus-user:quick-highlight'
  'space m': 'quick-highlight:clear'
  'space space': 'command-palette:toggle'

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
  'g >': 'vim-mode-plus:rotate-arguments-of-inner-pair'
  'g <': 'vim-mode-plus:rotate-arguments-backwards-of-inner-pair'
  'ctrl-i': 'cursor-history:next'
  'ctrl-o': 'cursor-history:prev'

'.tree-view':
  's f': 'tree-view:toggle-focus'
```

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


## atom-ide-ui, ide-python

Minicondaの仮想環境`atom`を作成します。

```bash
(base) > conda create -n atom python
(base) > activate atom
(atom) > pip install python-language-server[all]
(atom) > pip install pyls-isort pyls-mypy
```

Atom実行時のパスに、Pythonの仮想環境を追加します。AtomのFile->Init Script...でinit.coffeeを開き、

```javascript
process.env.PATH = ["C:\\Users\\daizu\\Miniconda3\\envs\\atom;C:\\Users\\daizu\\Miniconda3\\envs\\atom\\Library\\bin;C:\\Users\\daizu\\Miniconda3\\envs\\atom\\Scripts", process.env.PATH].join(";")
```

を追加します。

[キーマッピング](
https://github.com/facebookarchive/atom-ide-ui/blob/master/docs/keybindings.md)


## Hydrogen

Jupyter clientを使って，Atom上でPythonコードの実行ができます．インタラクティブな実行が可能なので，非常に重宝します．Hydrogenを使う仮想環境下(仮に`example`とします)で，以下を実行します。

```bash
(base) > conda create -n daizu python
(base) > active daizu
(daizu) > conda install jupyter
(daizu) > python -m ipykernel install --user --name daizu
```

Atom実行時のパスに、Pythonの仮想環境を追加します。AtomのFile->Init Script...でinit.coffeeを開き、以下のように変更します。

```javascript
process.env.PATH = ["C:\\Users\\daizu\\Miniconda3\\envs\\atom;C:\\Users\\daizu\\Miniconda3\\envs\\atom\\Library\\bin;C:\\Users\\daizu\\Miniconda3\\envs\\atom\\Scripts;C:\\Users\\daizu\\Miniconda3\\envs\\daizu;C:\\Users\\daizu\\Miniconda3\\envs\\daizu\\Library\\bin;C:\\Users\\daizu\\Miniconda3\\envs\\daizu\\Scripts", process.env.PATH].join(";")
```

### Keymap

```cson
'atom-text-editor':
  'f8': 'hydrogen:clear-results'
  'f9': 'hydrogen:run-all-above'
  'f10': 'hydrogen:run-all'
```

## autocomplete-python

## その他のパッケージ

Pythonとは直接関係ないですが，以下のパッケージもインストールするとよいでしょう．

* tab-numbers
* busy-signal
* git-plus
* file-icons
* minimap系


以上で，開発環境が整いました．
