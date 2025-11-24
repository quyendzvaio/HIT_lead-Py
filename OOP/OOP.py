class Xe:
    id = 1
    toc_do = 400
    def __init__(self,ten :str,mau : str,version :str):
        self.ten = "Ten : " + ten
        self.mau = "Mau sac : " + mau
        self.version = "Phien ban : " + version
        
        self.id = Xe.id
        
        Xe.id += 1
        
    def xin_chao(self):
        return "Xin chao, toi la xe " + self.ten + " mau " + self.mau + " phien ban " + self.version

    @classmethod
    def clean(cls,ls : list,ms :str):
        chuoi = [s.strip() for s in ms.split()]
        new_val = [val for val in ls if val in chuoi]
        ten,mau,version = new_val
        return cls(ten,mau,version)
    
O_to = Xe("X","Xanh","VF8")
print(O_to)
print("ID cua xe : ", O_to.id)
print(O_to.ten)
print(O_to.mau)
print(O_to.version)
print(O_to.toc_do , "km/h")

O_to.ten = "Vin"
O_to.mau = "Do"
O_to.version = "VF3"

print("Ten : ", O_to.ten)
print("Mau sac : ",O_to.mau)
print("Phien ban : ",O_to.version)
print("Toc do : ",O_to.toc_do)

print(O_to.xin_chao())

Xe.toc_do = 500
print("Toc do moi : ",O_to.toc_do)
#thay doi thuoc tinh rieng doi tuong bang phep gan thuoc tinh chi rieng doi tuong do VD:Oto.toc_do = 600 

Xe_tai = Xe("Tai","Trang","TF8")
print("Id cua xe : ", Xe_tai.id)
print(Xe_tai.ten)
print(Xe_tai.mau)
print(Xe_tai.version)
print(Xe_tai.toc_do , "km/h")
print(Xe_tai.xin_chao())

ls = ["X","Do","VF8","Vin","Xanh","VF3","Tai","Trang","TF8"]
ms = "Toi co mot chiec xe ten Vin mau Xanh phien ban VF3"
Xe_moi = Xe.clean(ls,ms)
print(Xe_moi.xin_chao())
print(Xe_moi.__dict__)

#kethua
class Xe_dap(Xe):
    # toc_do = 80
    def __init__(self,ten :str,mau : str,version :str,so_banh : int):
        super().__init__(ten,mau,version)
        self.so_banh = so_banh
        
    def xin_chao(self):
        return super().xin_chao() + " co so banh la " + str(self.so_banh)

    def __str__(self):
        return "day la {} co mau {} phien ban {} va co toc do {} km/h".format(self.ten,self.mau,self.version,self.toc_do)

Xe_dap1 = Xe_dap("Dap","Den","DF1",2)
print(Xe_dap1.xin_chao())
print("ID cua xe dap : ", Xe_dap1.id)
print("So banh cua xe dap : ", Xe_dap1.so_banh)
print("Toc do cua xe dap : ", Xe_dap1.toc_do , "km/h")    #ke thua thuoc tinh toc_do cua lop cha Xe
print(Xe_dap1.__str__())