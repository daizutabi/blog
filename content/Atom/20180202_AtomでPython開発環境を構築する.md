AtomテキストエディタにPython開発環境を構築します．

<!-- PELICAN_END_SUMMARY -->

## `init.coffee`

[File] > [Init Script...]を選択して，`init.coffee`を開き，次の行を追加します．

```coffee
process.env.PYTHONIOENCODING = "utf-8";
```


## MagicPython

MagicPythonのシンタックスカラーを`styles.less`に追加します．

```less
atom-text-editor .syntax--source.syntax--python {
  .syntax--keyword.syntax--control,
  .syntax--keyword.syntax--operator.syntax--logical,
  .syntax--storage.syntax--type {
    // font-weight: bold;
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

## autocomplete-python

## Hydrogen

## terminal

## ide-python

## atom-beautify

##
