files_data = [['files/1.txt'],['files/2.txt'],['files/3.txt']]
for file_data in files_data:
  with open(file_data[0], encoding = "utf-8") as f:
    text = f.readlines()
    text[-1] += '\n'
    file_data += text
    file_data.insert(1,str(len(text)))
print(files_data)

files_data=sorted(files_data, key=lambda x:x[1])
ret = []
for file_data in files_data:
  file_data[0] += '\n'
  file_data[1] = f'{file_data[1]}\n'
  ret+=file_data

with open('files/res.txt', 'w', encoding = "utf-8" ) as f:
  f.writelines(ret)
