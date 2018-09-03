この記事では，[JupyterLab](https://jupyterlab.readthedocs.io/en/latest/)をカスタマイズする方法を説明します．

<!-- PELICAN_END_SUMMARY -->

## JupyterLab

JupyterLabを実行する仮想環境を作成し，必要なパッケージをインストールします．

```bash
(base) conda create -y -n jupyter python=3.6 jupyterlab nodejs
```
## jupyterlab-vim

VIMを使えるようにします．

```bash
(base) > activate jupyter
(jupyter) > jupyter labextension install jupyterlab_vim
```

以下に設定＆拡張機能について執筆したい．
