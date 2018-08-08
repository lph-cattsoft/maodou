# -*- coding: utf-8 -*-
#created by liph
#usually password

import os
import os.path


most_use=["11111111","0000000","11223344","0123456789","147258369","6666666","888888888",
          "12341234","88889999","a2b2c3d4","22222222","999999999","9999999","11111111111",
          "7777777","23456789","1122334455","55555555","qwertyuiop","8888888","111111111",
          "12345678","012345678","abcd1234","a123456789","000000000","1234","12345","123456","12345678",
          "12345890","54321","654321","754321","8754321","9754321","12344321","121314","8888888",
          "666666","666","abc","admin","asd","super","xyz","0101","01023","love","6868","110",
          "fuck","1111","568","up","china",'111222333'
          ]

year=["1970","1971","1972","1973","1974","1975","1976","1977","1978","1979",
      "1980","1981","1982","1983","1984","1985","1986","1987","1988","1989",
      "1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
      "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009",
      "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"
      ]

month =["01","02","03","04","05","06","07","08","09","10","11","12"]

day =["01","02","03","04","05","06","07","08","09","10","11","12",
     "13","14","15","16","17","18","19","20","21","22","23","24","25",
      "26","27","28","29","30","31"
      ]

#常用姓氏
surn=["li","wang","ma","wu","xu","hu","yu","he","liu","sun","gao","luo","cai","guo","zhu","zhao"
      "yang","song","zhou","meng","deng","zhang","huang","liang","lin","zheng","xie","tang","han",
      "cao","xu","feng","zeng","cheng","ye","wei","yuan","du","kong","mao","su","fan","pan","cai",
      "cui","jin","qin","xue","tan","lei","shi"
      ]

# 所有可以组成名字首字母的字母

fname=["b","c","d","f","g","h","j","k","l","m","n","p","q","s","t","w","x","y","z"]

#包括名字的所有字的拼音

b_sub=["bo","bi","bai","bei","bao","ban","ben","bin","bang","bing","biao"]
c_sub=["ci","cai","can","cen","cun","cent","cong"]
d_sub=["de","di","du","dai","dao","dan","deng","ding","dong"]
f_sub=["fa","fu","fei","fan","fen","feng","fang","fing"]
g_sub=["gu","gui","gao","gan","gen","guo","gang","geng","guan","guang"]
h_sub=["hu","hui","hao","han","hen","huo","hang","heng","huan","huang"]
j_sub=["ji","ju","jiu","jie","jin","jun","jue","jing","jia","jiao","jian","juan"]
k_sub=["kai","kui","kan","kun","kuo","kang","kong","kuan","kuang"]
l_sub=["le","li","lu","lai","lei","lie","lan","lin","lun","lang","ling","long","liao","lian","luan"]
m_sub=["mi","mu","mai","mei","mao","miu","man","min","mang","meng","ming","miao","mian"]
n_sub=["na","ni","niu","nie","nan","nuo","neng","ning"]
p_sub=["pi","pu","pai","pei","pan","pin","pang","peng","ping","pian"]
q_sub=["qi","qiu","qing","qiang","quan","qian"]
s_sub=["sa","so","se","si","su","sai","suo","sang","song"]
t_sub=["ta","to","te","ti","tu","tai","tao","tan","tuo","tang","teng","ting","tong","tian"]
w_sub=["wa","wo","wai","wei","wang","wan"]
x_sub=["xi","xu","xv","xie","xin","xue","xing","xiang","xiong","xia","xian","xuan"]
y_sub=["ya","yi","yu","yao","you","yan","yun","yue","ying","yang","yong","yia","yuan"]
z_sub=["zu","zao","zan","zun","zuo","zeng","zong"]
zh_sub=["zhi","zhou","zhan","zhen","zhong","zhuan"]
ch_sub=["cha","che","chi","chu","chai","chao","chan","chen","chong","chuang"]
sh_sub=["sha","shi","shu","shuo","shou","shan","shen","shuo","shuang"]
#特殊字符
most_sin=["!","*","#","_","@","%","$"]


def makepsd(var1=[]):
    psdfile(var1)

def makepsd2(var1=[],var2=[]):
    new_psd=[]
    for param in var1 :
        for param2 in var2:
           new_psd.append(str(param)+str(param2))
    psdfile(new_psd)

def makepsd3(var1=[],var2=[],var3=[]):
    new_psd=[]
    for param in var1 :
        for param2 in var2:
            for param3 in var3:
                 new_psd.append(str(param)+str(param2)+str(param3))
    psdfile(new_psd)
def makepsd4(var1=[],var2=[],var3=[],var4=[]):
    new_psd=[]
    for param in var1 :
        for param2 in var2:
            for param3 in var3:
                for param4 in var4:
                    new_psd.append(str(param)+str(param2)+str(param3)+str(param4))
    psdfile(new_psd)
def makepsd5(var1=[],var2=[],var3=[],var4=[],var5=[]):
    new_psd=[]
    for param in var1 :
        for param2 in var2:
            for param3 in var3:
                for param4 in var4:
                    for param5 in var5:
                        new_psd.append(str(param)+str(param2)+str(param3)+str(param4)+str(param5))
    psdfile(new_psd)
def makepsd6(var1=[],var2=[],var3=[],var4=[],var5=[],var6=[]):
    new_psd=[]
    for param in var1 :
        for param2 in var2:
            for param3 in var3:
                for param4 in var4:
                    for param5 in var5:
                        for param6 in var6:
                            new_psd.append(str(param)+str(param2)+str(param3)+str(param4)+str(param5)+str(param6))
                            if len(new_psd)>=1000:
                                psdfile(new_psd)
                                new_psd=[]
    psdfile(new_psd)

def psdfile(psd_list=[]):
    psd_file="d:\password.txt"
    fb=open(psd_file, "a+")

    for psd in psd_list:
        fb.write(psd)
        fb.write("\n")
    fb.close()

#常用数字组合
makepsd(most_use)
print "step 1"
#  常用数字组合+特殊字符
makepsd2(most_use,most_sin)
print "step 2"
#姓+年+特殊符号
makepsd3(surn,year,most_sin)
print "step 3"

#  #姓+常用数字
makepsd2(surn,most_use)
print "step 4"

# 姓+常用数字+特殊字符
makepsd3(surn,most_use,most_sin)
print "step 5"
# 姓+年+月+日
makepsd4(surn,year,month,day)
print "step 6"
# 姓+月+日+特殊字符
makepsd4(surn,month,day,most_sin)
print "step 7"
# 2字母+常用数字组合
makepsd3(fname,fname,most_use)
print "step 8"
#2字母+常用数字+特殊字符
makepsd4(fname,fname,most_use,most_sin)
print "step 9"
#2字母+年
makepsd3(fname,fname,year)
print "step 10"
#2字母+年+特殊字符
makepsd4(fname,fname,year,most_sin)
print "step 11"

#2字母+月+日
makepsd4(fname,fname,month,day)
print "step 12"

#2字母+月+日+特殊字符
makepsd5(fname,fname,month,day,most_sin)
print "step 13"
#2字母+年+月+日
makepsd5(fname,fname,year,month,day)
print "step 14"
#3字母+常用数字组合
makepsd4(fname,fname,fname,most_use)
print "step 15"
#3字母+常用数字组合+特殊字符
makepsd5(fname,fname,fname,most_use,most_sin)
print "step 16"
#3字母+年
makepsd4(fname,fname,fname,year)
print "step 17"
#3字母+年+特殊字符
makepsd5(fname,fname,fname,year,most_sin)
print "step 18"
#3字母+月+日
makepsd5(fname,fname,fname,month,day)
print "step 19"
#3字母+月+日+特殊字符
makepsd6(fname,fname,fname,month,day,most_sin)
print "step 20"
#3字母+年+月+日
makepsd6(fname,fname,fname,year,month,day)
print "step 21"