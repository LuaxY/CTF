```
mkdir /tmp/luax && cp data.txt /tmp/luax && cd /tmp/luax
xxd -r data.txt > data.bin
file data.bin
zcat data.bin > data2.bin
file data2.bin
bunzip2 data2.bin
mv data2.bin.out data3.bin
file data3.bin
zcat data3.bin > data4.bin
file data4.bin
tar -xf data4.bin
file data5.bin
tar -xf data5.bin
file data6.bin
bunzip2 data6.bin
mv data6.bin.out data7.bin
file data7.bini
tar -xf data7.bin
file data8.bin
zcat data8.bin > data9.bin
file data9.bin
cat data9.bin
```
