# -*- coding: utf-8 -*-
import os

class fold:

    # クラスが生成されるときに呼び出される
    def __init__(self, pa1, pa2):
        self.pa1 = pa1
        self.pa2 = pa2

    # フォルダが存在するかチェック
    def chkfold(self):
        try:
          ck1=os.path.exists(self.pa1)
          ck2=os.path.exists(self.pa1+'\\')
          # 存在しているかチェック
          if ck1>0 or ck2>0:
            if os.path.exists(self.pa2) == 0:
              return False
            else:
              return True
        except:
            print('Error:chkfold')
            return True

    # フォルダを作成
    def chknewfold(self):
        try:
          cky=''
          pop=self.pa2.split('\\') #\で分割
          for i in range(0,len(pop)):
              cky+=pop[i]+'\\' #パスを作成
              if os.path.exists(cky) == 0: #パスが存在するかチェック
                  os.mkdir(cky) #フォルダを作成
        except:
            print('Error:chknewfold')
            return 0
