# -*- coding: utf-8 -*-
import datetime
import os

class time:


    # クラスが生成されるときに呼び出される
    def __init__(self):
        self.file = ""
        self.pa1 = ""
        self.pa2 = ""

    def setSelf(self, file, pa1, pa2):
        self.file = file
        self.pa1 = pa1
        self.pa2 = pa2


    # 今日の日付
    def chktimenow(self):
        try:
            now = datetime.datetime.now()
            # 書式を変換
            pa = now.strftime(self.pa2)
            # 不要な文字列を削除
            pa = pa.replace('<now:','')
            return pa.replace('>','')
        except:
            print('Error:chktimenow')
            return 0

    # タイムスタンプ
    def chktimestamp(self):
        try:
            path = os.path.join(self.pa1,self.file)
            stat = os.stat(path)
            last_modified = stat.st_mtime
            dt = datetime.datetime.fromtimestamp(last_modified)
            # 書式を変換
            st = dt.strftime(self.pa2)
            # 不要な文字列を削除
            st = st.replace('<stamp:','')
            return st.replace('>','')
        except:
            print('Error:chktimestamp')
            return 0
