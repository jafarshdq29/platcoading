nama_saya = "Nama : Muhammad Jafar shidiq"
print (nama_saya, "bertipe", type (nama_saya)) 

NIM = "NIM : 230441100083"
print(NIM, "bertipe", type(NIM))

indeks = {
  " celcius     ": "c",
  " fahrenheit  ": "r",
  " kelvin      ": "k"
}

print("==========indeks satuan sekala suhu==========")
for i in indeks : 
    print("satuan suhu :", i ,"\t indeks : ", indeks [i])

suhu = float (input("masukan suhu : "))
satuan = input("masukan indeks satuan skala suhu : ")

if (satuan == "c"):
    print(suhu, "derajat celcius : ")
    print("fahrenheit = ",(suhu *9/5)+32, "derajat")
if (satuan == "f"):
    print(suhu, "derajat fahrenheit : ")
    print("celsius = ",(5/9)*(suhu-32),"derajat")
if (satuan == "k"):
    print(suhu, "derajat kelvin : ")
    print("celcius = ", suhu-273,"derajat") 
