"""1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]"""

normal_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flatten_list = []


def nestedtoflatten(normal):
    for e in normal:
        if type(e) == list:
            nestedtoflatten(e)
        else:
            flatten_list.append(e)


nestedtoflatten(normal_list)
print(flatten_list)

"""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]"""

list1 = [[1, 2], [3, 4], [5, 6, 7]]

def ultra_reverse(listt):
    listt.reverse()
    listt= list(map(lambda x: x[::-1], listt))
    print(listt)

ultra_reverse(list1)