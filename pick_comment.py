#!/usr/bin/python
# -*- Coding: utf-8 -*-
import CsvAnalyze as ca
import oseti2 
import MeCab


#data = ca.AllBooks("../zzz")
data = ca.AllBooks("comments")

uniq_titles = data["opus"].unique()

dict_title_value = {}

#uniq_titles = ["遊☆戯☆王"]
uniq_titles = ["ドラゴンボール超"]

for i_title in uniq_titles:
  counter_comments = 0.0
  #print(i_title)
  comments = ca.OutCommnet(data, i_title) 
  #print( i_comment )
  ave_title = 0.0
  comment_value = {}
  for i_comment in comments:
    analyzer = oseti2.Analyzer()
    #print (i_comment)
    if i_comment == i_comment : # if comment != nan  
      list_value = analyzer.analyze(i_comment)
      #print(i_comment,", ", list_value, ", ", len(list_value) )
      
      tmp_sum = 0.0
      for i in list_value:
        ave_title += i
        counter_comments += 1
        tmp_sum += i
        #print("DEBUG: sum_value, counter ", ave_title, counter_comments)
      if len(list_value) == 0:
        comment_value[i_comment] = 0
      else :
        comment_value[i_comment] = tmp_sum / len(list_value)
  ave_title = ave_title / counter_comments
  dict_sorted = sorted( comment_value.items(), key=lambda x: -x[1])
  ii = 0
  for i,j in dict_sorted:
    ii += 1
    print(ii ,", ", i ,", " , j)
  print ("Average Score: " ,ave_title )
  
  #print("DEBUG: # analyzed sentences: ", counter_comments)
  #print("TITLE: ",i_title, ", VALUE: ", ave_title) 
  #dict_title_value[i_title] = ave_title

quit()

#print (dict_title_value) 
dict_sorted = sorted(dict_title_value.items(), key=lambda x: -x[1])
#print (dict_sorted)

ii = 0
for i,j in dict_sorted:
  ii += 1
  print(ii ,", ", i ,", " , j)
  


