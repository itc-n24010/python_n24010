class Person:
    def __init__(self,
                name = '',
                nationality = '',
                birth = '',
                address = ''):

        self.name = name
        self.nationality =  nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生年月日:", self.birth)
        print("出身地:", self.address)

Author_of_jujuthu_kaisen = Person('芥見下々', '日本', '1999/2/26', '岩手県')
Author_of_jujuthu_kaisen.show_attributes()
