[Happy Hacking Keyboard Professional2 Type-S](https://www.pfu.fujitsu.com/hhkeyboard/type-s/)英語配列モデルを購入しました．より快適に使うための設定をまとめておきます．



以下の記事を参考にしました．

+ [[Windows 8/10] 日本語キーボードのノートPCで外付け英語キーボードを使用する方法](http://blog.shos.info/archives/2012/11/windows_8_pc.html)
+ [【HHKB】英語キーボードの右Altキーに［全角／半角］キーを割り当てる](http://evacore.info/hardware-hhkb-alt/)

## 背面スイッチ

以下の設定にしています．

+ Lite拡張モード（PC）: SW1 ON, SW2 OFF
+ 左◇ ⇒ Fn: SW4 ON

## レジスタの設定

+ LayerDriver JPN: kbdax2.dll
+ OverrideKeyboardIdentifier: AX_105KEY
+ OverriedKeyboardSubtype: 2

![png]({static}/images/20180211/reg.png)


## 言語の追加

「英語(米国)」を追加しました．

![png]({static}/images/20180211/lang.png)


## 設定状況

以上の設定で以下のような動作になります．

+ 左◇キー ⇒ Fnキー
+ 右◇キー ⇒ Windowsキー
+ 右Altキー ⇒［全角／半角］キー
+ ノートPCのキー配列は日本語のまま
