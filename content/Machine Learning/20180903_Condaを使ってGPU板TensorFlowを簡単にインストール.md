[2018/9/1の記事](../../../2018/09/01/)では，CUDA Toolkitなどをインストールした上で，pip経由でTensorFlowおよびKerasをインストールしました．実は，Condaを使うと，CUDAを手動でインストールする必要がなくなります．実際に検証してみました．

<!-- PELICAN_END_SUMMARY -->


## 準備

まず，コントロールパネルのプログラムのアンインストールで，CUDA関連のアプリを全て消去します．再起動後に，以下を実行してみます．

```bash
(base) > activate ml
(ml) > python mnist_cnn.py
(中略)
ImportError: Could not find 'cudart64_90.dll'. TensorFlow requires that this DLL be installed in a directory that is named in your %PATH% environment variable. Download and install CUDA 9.0
 from this URL: https://developer.nvidia.com/cuda-90-download-archive
```

当然エラーが出ます．

Condaでインストールしていきます．

```bash
(ml) > activate base
(base) > conda remove -y -n ml --all
(base) > conda create -y -n ml python=3.6
(base) > conda activate ml
(ml) > conda install tensorflow-gpu keras
```

## 動作確認

Kerasの動作確認をします． [MNIST_CNN](https://raw.githubusercontent.com/keras-team/keras/master/examples/mnist_cnn.py)のサンプルをダウンロードし，実行します．

```bash
(ml) > python mnist_cnn.py
(中略)
 GPU (device: 0, name: GeForce GTX 1050, pci bus id: 0000:01:00.0, compute capability: 6.1)
60000/60000 [==============================] - 13s 208us/step - loss: 0.2567 - acc: 0.9233 - val_loss: 0.0768 - val_acc: 0.9760
Epoch 2/12
60000/60000 [==============================] - 10s 159us/step - loss: 0.0875 - acc: 0.9740 - val_loss: 0.0398 - val_acc: 0.9873
Epoch 3/12
60000/60000 [==============================] - 10s 159us/step - loss: 0.0669 - acc: 0.9805 - val_loss: 0.0326 - val_acc: 0.9886
Epoch 4/12
60000/60000 [==============================] - 10s 159us/step - loss: 0.0536 - acc: 0.9842 - val_loss: 0.0311 - val_acc: 0.9894
Epoch 5/12
60000/60000 [==============================] - 10s 159us/step - loss: 0.0466 - acc: 0.9856 - val_loss: 0.0321 - val_acc: 0.9891
Epoch 6/12
33536/60000 [===============>..............] - ETA: 4s - loss: 0.0416 - acc: 0.9874
```

問題なく動作しています．

他のパッケージもインストールしておきます．

```bash
(ml) > conda install ipykernel scikit-learn seaborn
```
