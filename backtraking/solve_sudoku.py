


class SolveSudoku :


    def __init__(self, matriz) -> None:
        
        self.matriz = matriz
        self.long = len(matriz)
        self.rows = self.columns = len(matriz)
        self.nums = len(matriz) + 1



    def __str__(self) :

        if self.long % 2 == 0 :

            divisor = 2
            result = 1

        else :

            divisor = 3
            result = 2

        for i in range(self.rows) :

            if i != 0 and (i % divisor == 0) :

                print('-' + ' -' * (self.long ))
                print()

            for j in range(self.columns) :

                print(self.matriz[i][j], 
                    end= ' | ' if self.long -1 != j != 0 and (j % divisor == result) else ' '
                )

            print('\n') 

        return ''




    def en_column(self, columna, num) :

        for i in range(self.columns) :

            if self.matriz[i][columna] == num :

                return True

        return False




    def en_row(self, row, num) :

        for j in range(self.rows) :

            if self.matriz[row][j] == num :

                return True

        return False



    def en_box(self, row, column, num) :

        if self.long % 2 == 0 :

            row = row - row % 2
            column = column - column % 2
            sumar = 2

        else :

            row = row - row % 3
            column = column - column % 3
            sumar = 3


        for i in range(row, row + sumar ) :

            for j in range(column, column + sumar) :

                if self.matriz[i][j] == num :

                    return True

        return False



    def valido(self, row, column, num) :

        return not(
            self.en_row(row, num) or self.en_column(column, num) 
        )

    
    def vacio(self) :

        for i in range(self.rows) :

            for j in range(self.columns) :

                if self.matriz[i][j] == 0 :

                    return [i, j]

        return False



    def solve(self) :

        if self.vacio() :

            row, column = self.vacio()

        else :

            return True

        for num in range(1, self.nums) :

            if self.valido(row, column, num) :

                self.matriz[row][column] = num

                if self.solve() :

                    return True
                
                self.matriz[row][column] = 0

        return False

    
    

    def solve2(self) :

        for row in range(self.rows) :

            for column in range(self.columns) :

                if self.matriz[row][column] == 0 :

                    for num in range(1, self.nums) :

                        if self.valido(row, column, num) :

                            self.matriz[row][column] = num

                            self.solve2()

                            print(self)
                            input() 
                            
                    self.matriz[row][column] = 0

                    return False



    



sudoku1 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

sudoku1 = [
    [0, 0],
    [0, 0] 
]

solve_sudokus = SolveSudoku(sudoku1)



print(solve_sudokus)

