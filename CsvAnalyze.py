#!/usr/bin/python
# -*- Coding: utf-8 -*-
import glob
import pandas as pd

'''
csvファイルが入っているディレクトリ名を入れて呼び出してください
ex) AllBolls("comments")
'''
def AllBooks(dir):
  Dic = glob.glob(dir + "/*")

  #pandasファイルを一時的に格納
  tmp = []

  for File in Dic:
    df = pd.read_csv(File, encoding='cp932')
    tmp.append(df)


  ## 配列の数(ファイル数)
  DataSize = len(tmp)

  #csvファイルの連結
  result = tmp[0]
  for i in range(1, DataSize):
    pd.concat([ result, tmp[i]])
  
  result = result.rename(columns={
                  "#コメントID":"comment_id", 
                  "状態 ('未承認：unapproved、承認済み：approved、ゴミ箱：trash、投稿者にのみ表示：show_only_owner'のいずれか)":"status", 
                  "作成日時 (読取り専用)":"create_date",
                  "アプリ名 (読取り専用)":"app_name",
                  "デバイスID (読取り専用)":"device_id",
                  "メールアドレス (読取り専用)": "mail",
                  "作品ID (読取り専用)": "opus_id",
                  "作品タイトル (読取り専用)": "opus",
                  "コンテンツID (読取り専用)": "contents_id",
                  "コンテンツ名 (読取り専用)": "conntens_name",
                  "メッセージ (読取り専用)": "comments",
                  "いいね数 (読取り専用)": "good_value",
                  "通報件数 (読取り専用)": "report_value"
                  })

  result = result.replace( '\n', ' ', regex=True)

  return result


'''
Sortするやつ

panda: panda型のデータ
header: ソートしたいヘッダー
ascending:  昇順と降順

ascending=Falseに変更すると降順
ascending=Falseに変更すると昇順
'''
def CsvSort(panda, header, ascending):
  return panda.sort_values(by=[header], ascending=ascending)


'''
欲しいヘッダーを連結して返すもの
panda:panda型のデータ
ExtArray:欲しいヘッダーの配列
'''
def CsvExtraction(panda, ExtAray):
  return CsvSort( panda[ExtAray], ExtAray[0], True)


def OutCommnet(df, title):
  df = df[df["opus"] == title]

  return df["comments"]