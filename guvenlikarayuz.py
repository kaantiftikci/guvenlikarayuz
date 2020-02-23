login=["kaan","kaan1","kaan2"] #kullanıcı adı
loginpass="123456" #şifre
login_hak=3

print('''
************************************************    
*                                              *
*           Sisteme Giriş Paneli               *
*                                              *
*                                              *
************************************************

''')
while True:
    login_name=input("Kullanıcı Adınızı Giriniz : ")
    login_pswrd=input("Şifrenizi Giriniz : ")
    if (login_name != login and login_pswrd == loginpass):
        print("Kullanıcı Adınız Yanlış ")
        login_hak -= 1
        print("{} Deneme Hakkınız Kaldı" .format(login_hak))  
    elif (login_name == login and login_pswrd != loginpass):
        print("Şifreniz Yanlış")
        login_hak -=1
        print("{} Deneme Hakkınız Kaldı" .format(login_hak))
    elif (login_name != login and login_pswrd != loginpass):
        print("Kullanıcı Adı Ve Şifreniz Yanlış")
        login_hak -=1
        print("{} Deneme Hakkınız Kaldı " .format(login_hak))
    else:
        print("Sisteme Hoşgeldiniz")
        break
    if (login_hak == 0) :
        print("Deneme Hakkınız Kalmadı! 15 Dakika Sonra Tekrar Deneyiniz")
        exit()
        