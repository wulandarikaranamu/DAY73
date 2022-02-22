#manipulasi data

data = ["merry","wiwi","lisa","marwa","diva"]

data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")
data_1 = data[1]
print(f"data kedua (index 1) = {data_1}")
data_2 = data[2]
print(f"data pertama (index 2) = {data_2}")
data_3 = data[3]
print(f"data kedua (index 3) = {data_3}")
data_4 = data[4]
print(f"data kedua (index 4) = {data_4}")

print("------------------batas--------------")

data_terakhir = data[-1]
print(f"data terakhir = {data_terakhir}")
data_marwa = data[-2]
print(f"data marwa = {data_marwa}")
data_lisa = data[-3]
print(f"data lisa = {data_lisa}")
data_wiwi = data[-4]
print(f"data wiwi = {data_wiwi}")
data_merry = data[-5]
print(f"data merry= {data_merry}")

print("--------------mencari panjang data---------------")

jumlah_data  = len(data)
print(f"total keseluruhan data = {jumlah_data}")


print("----------------manipulasi data ------------------")

print(f"data sebelum ditambah = {data}")
data.insert(3,"virna")
print(f"data setelah ditambah = {data}")

#jika ingin menambah item diakhir list

data.append("herawati")
print(f"item baru diakhir list = \n{data}")

#menambah list dengan list
data_baru = ["sakina","inun","wajida"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

#merubah data
data[3] = "naya"
print(f"data yang sudah diubah = \n{data}")

#meremove data
data.remove("wajida")
print(f"data yang sudah diremove = \n{data}")

#menghapus data dengan fungsi pop
data_akhir = data.pop()
print(f"data yang sudah dihapus diakhir list  = \n{data}")
print(data_akhir)




