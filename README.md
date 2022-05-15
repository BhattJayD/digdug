# digdug

a tryhackme simple ctf (url:https://tryhackme.com/room/digdug)
where we have got dns server and we need to get recon for _givemetheflag.com_
host contain the flag

###### run with

```
python3 digdug.py <ip>
```

###### response

```
$python3 digdug.py 10.10.192.156
"flag{0767ccd06e79853318f25aeb08ff83e2}"
```

##### same output with bash

```
dig @10.10.192.156 givemetheflag.com |grep -oE "flag{.*}"
```
