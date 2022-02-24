def process_meeting_chat():
  file_path = input("加工するチャットファイルへのpathを入力: ")
  extension = input("拡張子を入力 csv or txt: ")
  join_mark = ""
  if extension == 'csv':
    writeFile = file_path[:-4] + "_processed.csv"
    join_mark = ","
  elif extension == 'txt':
    writeFile = file_path[:-4] + "_processed.txt"
    join_mark = ": "
  else:
    print('extension_nameは csv か txt でお願いします')
    exit()
  
  with open(file_path, mode="r", encoding='utf-8') as f:
    for line in f:
      if ":" in line:
        line = (line[12:-8]).strip()
        with open(writeFile, mode="a", encoding='utf-8') as fw:
          fw.write(line + join_mark)
      else:
        with open(writeFile, mode='a', encoding='utf-8') as fw:
          fw.write(line.strip()+"\n")

if __name__ == '__main__':
  process_meeting_chat()
