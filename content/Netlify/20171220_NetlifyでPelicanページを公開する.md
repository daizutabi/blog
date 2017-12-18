（編集中）

これまで[GitHub Pages](https://pages.github.com)でブログを公開していましたが，[Netlify](https://www.netlify.com)に移行します．とても簡単に独自ドメインを使うことができます．

## お名前.comで独自ドメインの取得

[お名前.com](https://www.onamae.com)で独自ドメインを取得します．金額に関しては，初年度だけでなく２年目以降の金額についてもチェックしておきましょう．また，「1.お申込み内容」のところで，

+ Whois情報公開代行（新規登録と同時なら無料）

は，個人情報を公開したくない場合にはチェックを入れておきます．


## Pelicanプロジェクトの作成

Pelicanプロジェクトを作成して，GitHubレポジトリにPushしておきます．

## Netifyでサイトの作成

[Netlify](https://www.netlify.com)にはGitHubアカウント使ってログインします．ログイン後に，[https://app.netlify.com](https://app.netlify.com/)を開き，右上のNew Site From Gitをクリックします．GitHubを選ぶと，自分のレポジトリ一覧が表示されるので，公開したいレポジトリを選択します．（以下はblogレポジトリを選択した前提です．）

Deploy settings for daizutabi/blogで，次の選択をします．

+ Branch to deploy: master
+ Build commant: (何も入力しない)
+ Publish directory: /output

Deply siteをクリックすると（すでに生成されていた）サイトが公開されます．

## Custom domain

編集中

## HTTPS

Verify DNS configurationをクリック．うまくいけば，Let's Encrypt certificateに代わるのでもう一度クリック．

Automatic TLS setupダイアログで Provision certificateをクリック

Force HTTPSもクリック
