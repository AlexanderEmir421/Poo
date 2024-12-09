class Cliente:
    def __init__(self,nom,ap,email,contra,dir,tel):
        self.__nombre=nom
        self.__apellido=ap
        self.__contra=contra
        self.__dir=dir
        self.__email=email
        self.__tel=tel
    def __str__(self):
        return f"\n Cliente:{self.__nombre}"