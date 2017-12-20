これまで[GitHub Pages](https://pages.github.com)をブログなどの公開に使っていましたが，[Netlify](https://www.netlify.com)に移行します．とても簡単に独自ドメインを使うことができます．

## お名前.comで独自ドメインの取得

[お名前.com](https://www.onamae.com)で独自ドメインを取得します．金額に関しては，初年度だけでなく２年目以降の金額についてもチェックしておきましょう．また，「1.お申込み内容」のところで，

+ Whois情報公開代行（新規登録と同時なら無料）

は，個人情報を公開したくない場合にはチェックを入れておきます．

お名前.comのサイト内ですることは，取得したドメインのネームサーバをNetlify DNSに設定することだけです．それ以外の設定はすべて，Netlify内で完結します．


## 静的サイトの作成

Pelicanを使ってサイトを作成し，GitHubレポジトリにPushしておきます．

## Netifyでサイトの作成

[Netlify](https://www.netlify.com)にはGitHubアカウント使ってログインします．ログイン後に，[https://app.netlify.com](https://app.netlify.com/)を開き，右上のNew Site From Gitをクリックします．GitHubを選ぶと，自分のレポジトリ一覧が表示されるので，公開したいレポジトリを選択します．（以下はblogレポジトリを選択した前提で進めます．）

"Deploy settings for daizutabi/iroha"で，次の選択をします．

+ Branch to deploy: master
+ Build commant: (何も入力しない)
+ Publish directory: output

"Deply site"をクリックすると（すでに生成されていた）サイトが公開されます．

## カスタムドメインの設定

"Add a custom domain"をクリックします．

"Your custom domain"に
`http://blog.daizutabi.net`を入力し，Saveをクリックします．

"Change your domain's name servers"を開くと，Netlify DNSが表示されるので，これをお名前.comのネームサーバーに設定します．

## HTTPS

画面の案内に従えばすんなり設定できます．
