class Ordena:

    def __init__(self):
        pass

    def merge_sort_v1(self, A, ini, fim):
        if ini < fim:
            #Divisao
            q = int((ini + fim) / 2)
            #Conquista
            self.merge_sort_v1(A, ini, q)
            self.merge_sort_v1(A, q + 1, fim)
            #Combinação
            return self.intercala(A, ini, q, fim)

    def merge_sort_v2(self, A,  ini,  fim):
        n = fim - ini + 1
        if n >= 4:
            med = int((ini + fim) / 2)
            q1 = int((ini+med)/2)
            q3 = int((med+1+fim)/2)
            self.merge_sort_v2(A, ini, q1)
            self.merge_sort_v2(A, q1+1, med)
            self.merge_sort_v2(A, med+1, q3)
            self.merge_sort_v2(A, q3+1, fim)
            self.intercala(A, ini, q1, med)
            self.intercala(A, med+1, q3, fim)
            return self.intercala(A, ini, med, fim)
        else:
            return self.selection_sort(A, ini, fim)


    def selection_sort(self, A, ini, fim):
        for i in range(ini, fim):
            min_idx = i
            for j in range(i + 1, fim):
                if A[min_idx] > A[j]:
                    min_idx = j

            A[i], A[min_idx] = A[min_idx], A[i]

        return A

    def intercala(self, A, ini, q, fim):
        B = {}
        for i in range(ini, q+1):
            B[i] = A[i]
        for j in range(q+1, fim+1):
            B[fim+q+1-j] = A[j]
        i = ini
        j = fim
        for k in range(ini, fim+1):
            if B[i] <= B[j]:
                A[k] = B[i]
                i = i+1
            else:
                A[k] = B[j]
                j = j-1

        return A
if __name__ == "__main__":
    ordena = Ordena()
    A = [5,4,3,2,1]
    ini = 0
    fim = len(A)-1
    n = fim - ini
    print(A)
    #A = ordena.merge_sort_v1(A, ini, fim)
    A = ordena.merge_sort_v2(A, ini, fim)
    print(A)


