# -*- coding: utf-8 -*-

import sys
import glob
import csv
import os
import shutil
import codecs
import re
import dircache
import lib.time
import lib.fold
import lib.name
import lib.filemove

# fuwファイルを読み込む
def chkcsv(s_file):
    fopen=open(s_file, 'rb')
    try:
     #fuwファイルの設定を読み込む
     for row in csv.reader(fopen):
         key=row[0].decode('utf-8') #移動キーワード
         ren=row[1].decode('utf-8') #リネームキーワード
         pa1=row[2].decode('utf-8') #移動元
         pa2=row[3].decode('utf-8') #移動先
         #print key
         #print ren
         #print pa1
         #print pa2
         # ファイルの検索
         chkfilesort(key,ren,pa1,pa2)
    except:
     print('Error:chkcsv')
    finally:
     fopen.close()

# ファイルを正規表現で取得
def chkfilesort(key,ren,pa1,pa2):
    try:
        cm = re.compile(key)
        for file in dircache.listdir(pa1):
            #正規表現でファイルをフィルタ
            if cm.search(file):
                #print '=== FILE: %s ==='  %(file)
                # 移動元フォルダ
                #print 'MovingSource: %s' %(pa1)
                # 移動先フォルダ
                moveDes = chktimeformatif(file, pa1, pa2)
                #print 'moveDes: %s' %(moveDes)

                # フォルダチェック
                chkfold = Idawof.fold.fold(pa1, moveDes)
                if (chkfold.chkfold() == False): chkfold.chknewfold()

                #リネーム
                reName = Idawof.name.name(file, ren)
                #print 'reName: %s' %(reName.chkrename())

                #ファイル移動
                MovingSource = os.path.join(pa1, file)
                Destination = os.path.join(moveDes, reName.chkrename())
                #fiMove = Idawof.filemove.filemove(MovingSource, \
                #        Destination)
                #fiMove.chkfilremove()
                chkfilemove(MovingSource, Destination)
    except:
        print('Error:chkfilesort')
        return 0

# 取得日付判別
def chktimeformatif(file,pa1,pa2):
    # パスに指定の文字列が含まれているか判断するために大文字に変換
    ItisConvertedToUppercase=pa2.upper()

    time = Conversion.time.time()
    time.setSelf(file, pa1, pa2)

    if 'NOW' in ItisConvertedToUppercase: #今日の日付
        return time.chktimenow()
    elif 'STAMP' in ItisConvertedToUppercase: #ファイルのタイムスタンプ
        return time.chktimestamp()
    else: # そのまま出力
        return pa2

# ファイル移動
def chkfilemove(file,moveFilePath):
    try:
      if os.path.exists(file) == 1:
         #移動先に同じファイルがあると移動しない
         if os.path.exists(moveFilePath)==0:
            #リネームで移動できるかテスト
            os.rename(file,moveFilePath)
    except:
        print('Error:chkfilremove')
        return 0

if __name__ == '__main__':
    # 作業フォルダを変更
    os.chdir(os.path.dirname(sys.argv[0]) or '.')
    # 起動パラメーターチェック
    argvs = sys.argv
    if len(argvs) == 1: #パラメーターがない場合
       chkcsv('sorting.fuw')
    else: #パラメーターがある場合
       if '.fuw' in argvs[1]:
          chkcsv(argvs[1])
       else:
           print 'Not fuw File'
