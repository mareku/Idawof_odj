# -*- coding: utf-8 -*-
import os

class filemove:

    # クラスが生成されるときに呼び出される
    def __init__(self, MovingSource, Destination):
        self.MovingSource = MovingSource
        self.Destination = Destination

    def chkfilemove(self):
        try:
          # 移動元にファイルがあるか
          if os.path.exists(self.MovingSource) == 1:
             #移動先に同じファイルがあると移動しない
             if os.path.exists(self.Destination)==0:
                #リネームで移動
                os.rename(self.MovingSource, self.Destination)
        except:
            print('Error: chkfilremove')
            return 0
