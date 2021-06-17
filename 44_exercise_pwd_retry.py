# 44. [程式練習] 密碼重試程式
# 先在程式碼中 設定好密碼 password = 'a123456'
# 讓使用者[最多輸入3次密碼]
# 不對的話, 就印出"密碼錯誤! 還有__次機會"
# 對的話, 就印出"登入成功!"
# 剩餘0次的時候不要印

import time

str_correct_password = 'a123456'
int_retry = 3

while int_retry > 0:
    password = input('請輸入密碼: ')
    if password != str_correct_password:
        int_retry = int_retry - 1
        if int_retry > 0:
            print('密碼錯誤! 還有 ', int_retry, ' 次機會')
        else:
            print('密碼已錯誤3次 !')
            break
    else:
        print('登入成功 !')
        break 
