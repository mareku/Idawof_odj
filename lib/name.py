# -*- coding: utf-8 -*-
import os

class name:

    # クラスが生成されるときに呼び出される
    def __init__(self, file, ren):
        self.file = file
        self.ren = ren

    # リネーム
    def chkrename(self):
        try:
            dst=''
            file = self.file
            ren = self.ren
            FullFileName = os.path.basename(file) #pathからファイル名を取得
            #ファイルを名前と拡張子に分割
            name, ext = os.path.splitext(FullFileName)
            if self.ren: #リネーム文字列が含まれている
               #リネーム文字を置き換え
               if '<name>' in ren or '<ext>' in ren:
                  dst = ren.replace('<name>',name)
                  dst = dst.replace('<ext>',ext)
                  #リネーム
                  if file != dst: #ファイル名とren名が違う場合
                     return dst
                  else:
                      # 置き換えても変わらない
                     print('Error: It does not change')
                     return FullFileName
               else: #置き換え文字が含まれないていません
                  print('Error: The replacement does not does not contain the letter')
                  return FullFileName
            else:
              #renが設定されていません
              print('Error: ren has not been set')
              return FullFileName
        except:
            print('Error: chkrename')
            return FullFileName
