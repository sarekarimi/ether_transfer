# # یک فانکشن داریم که از کاربر نام دوتا فایل رو دریافت میکند.
# # در هر فایلی که کاربر نام آن را به ما میدهد یک دیکشنری داریم.
# # در فایل اول دیکشنری ما به این صورت است که :
# # Name : ID

# # و در فایل دوم دیکشنری ما این شکلی است :
# # ID : Color 

# # در خروجی از شما فایلی میخواهیم که دیکشنری درون آن به این صورت باشد :
# # Name : Color 

# # اگر ID اسم در فایل اول با ID رنگ در فایل دوم برابر باشد.


# # به مثال زیر توجه کنید :

# # First_File :

# # Dara : 1
# # Sara : 2

# # Second_File :

# # 1 : Blue 
# # 2 : Red 

# # Output_File :

# # Dara : Blue 
# # Sara : Red



# import json


# _file_baz_shode = open("sample_name.json", mode='r')

# _tmp_str = _file_baz_shode.read()
# print(_tmp_str)
# print(type(_tmp_str))
# _file_baz_shode.close()

# print("**************")
# # print(_file_baz_shode.read())
# _file_baz_shode = open("sample_name.json", mode='r')

# _tmp = json.load(_file_baz_shode)
# print(_tmp)
# print(type(_tmp))

# print("**************")
# print(_tmp['navid'])
# print(type(_tmp['navid']))


# # _file_baz_shode = open("sample_name.json", mode='r')

## Error Handeling .... 
# Crash ... 
import json



def ajib(vorodi):
    '''
    sen e hama ro ye sal ziad mikonm
    {"name" : age}
    age > 20 
    '''   
    try:
        
        for key in vorodi:
            if vorodi[key] >  20 or  vorodi[key] <  0:
                raise ValueError("moshkel ro")
            # raise TypeError
            # raise NameError
            
                # exit(0)
                # raise ValueError("adami pey da kardm ba sene bala ye 20")
            vorodi[key] += 1
        
    except TypeError :
        return {}
    return vorodi
    

d = {"navid" : 15, "ajib khan" : 534}
# d = 15
try:
    print(
        ajib(d)
        )
except ValueError as e:
    print('ye khari')
# try:
#     print("man injam ... ^___^")
#     f2 = open("names.json" , mode='r')
#     # print(json.load(f2))
    
#     print(age + 1)
    

# # except SyntaxError as e:
# #     print('tokenstam rad sham azash')

# except FileNotFoundError as e:
#     print('ko file')
# except json.decoder.JSONDecodeError as e:
#     print('json e irad dasht')
    
# except (NameError , TypeError):
#     print('sen ziad nashod')
    
# except Exception as e:
#     print("nemidonam dg chi shod")
    
    
# f1 = open("sample_name.json", mode="r")
# print(f1.read())


# try -> سعی کنیم یه کاری که ممکنه به مشکل بخوره رو انحام بدیم
# raise -> بگیم به مشکل خوردیم 
# except -> سعی کنیم با مشکل بوحود اومده برخورد کیم
# finally -> در نهایت

# Error Types
# NameError
# TypeError
# FileNotFoundError
# KeyError
# ValueError
# ....