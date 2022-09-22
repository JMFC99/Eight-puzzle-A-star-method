class A_star:
    '''
    |7|2|4|   
    |5|*|6|
    |8|3|1|
    '''
    


    def __init__(self,initial_state):
        self.states=initial_state
        self.final_goal = [[1,2,3],[4,5,6],[7,8,'*']]
        
        pass

    def print_statement(self):
        for i,j,k in self.states:
            print(f'|{i}|{j}|{k}|')
    
    def find_position(self,value='*'):## por default es *, pero puede buscar cualquier valor
        find = list(filter(lambda x:value in x,self.states)) ### regresa en que linea de encuentra el asterisco
        '''
            |7|2|4| <- This or   
            |5|*|6| <-  this or 
            |8|3|1| <-   this
        '''
        for i in range(3):
            if initial_state[i] == find[0]:
                j = find[0].index(value) ### esta nos da la posición de la columna 
                return [i,j]

    def right(self,number):
        space_position=self.find_position()
        print('asterisco posicion:',space_position)
        number_position=self.find_position(value=number)
        print('numero posicion:',space_position)
        row,column = number_position ### tener la fila y columna
        
        if (space_position[0] == row) and (space_position[1]-1 ==column):
            print('puedo moverlo a la derecha')
            self.states[space_position[0]][space_position[1]] = self.states[number_position[0]][number_position[1]]
            self.states[number_position[0]][number_position[1]] = '*'

    def left(self,number): #### simplificar derecha e izquierda
        space_position=self.find_position()
        print('asterisco posicion:',space_position)
        number_position=self.find_position(value=number)
        print('numero posicion:',space_position)
        row,column = number_position ### tener la fila y columna
        
        if (space_position[0] == row) and (space_position[1]+1 ==column):
            print('puedo moverlo a la izquierda')
            self.states[space_position[0]][space_position[1]] = self.states[number_position[0]][number_position[1]]
            self.states[number_position[0]][number_position[1]] = '*'
    
    def up(self,number):
        space_position=self.find_position()
        print('asterisco posicion:',space_position)
        number_position=self.find_position(value=number)
        print('numero posicion:',space_position)
        row,column = number_position ### tener la fila y columna
        
        if (space_position[0]+1 == row) and (space_position[1] ==column):
            print('puedo moverlo arriba')
            self.states[space_position[0]][space_position[1]] = self.states[number_position[0]][number_position[1]]
            self.states[number_position[0]][number_position[1]] = '*'
        

    def down(self,number):
        space_position=self.find_position()
        print('asterisco posicion:',space_position)
        number_position=self.find_position(value=number)
        print('numero posicion:',space_position)
        row,column = number_position ### tener la fila y columna
        
        if (space_position[0]-1 == row) and (space_position[1] ==column):
            print('puedo moverlo abajo')
            self.states[space_position[0]][space_position[1]] = self.states[number_position[0]][number_position[1]]
            self.states[number_position[0]][number_position[1]] = '*'

    def surrondings(self,value): ### alrededores
        value_position=self.find_position(value=value) #valor que se desea buscar
        row,column = value_position  #fila y columna 
        surrondings_positions = [] #posiciones de los alrededores
        surrondings_values=[] # valores de los alrededores
        
        for i in [1,-1]: ### suma y resta 1 posicion en fila y columna para encontrar los alrededores
            if (column+i>=0 and column+i<=2): ### los valores no pueden pasar de 2 ni ser menores de 0 ya que esto son las posiciones en las listas
                surrondings_positions.append([row,column+i])
            if (row+i>=0 and row+i<=2):
                surrondings_positions.append([row+i,column])
    
        for i,j in surrondings_positions:
                surrondings_values.append(self.states[i][j])
        print(surrondings_values)
        return surrondings_values ## regresa los valores de los alrededores

            
        #if (space_position[0]-1 == row) and (space_position[1] ==column): down
        #if (space_position[0]+1 == row) and (space_position[1] ==column): up
        #  if (space_position[0] == row) and (space_position[1]+1 ==column): left
        #if (space_position[0] == row) and (space_position[1]-1 ==column): right

        

initial_state= [[7,2,4],[5,'*',6],[8,3,1]]
# initial_state= [[7,2,4],[5,6,'*'],[8,3,1]]
# initial_state= [[7,2,4],['*',5,6],[8,3,1]]



example = A_star(initial_state=initial_state)
example.print_statement()
# example.right(number=6)
# example.left(number=6)
# example.up(number=1)
# example.down(number=2)
# example.print_statement()
# example.surrondings(value='*')


### find in which line is the *
# find = list(filter(lambda x:'*' in x,initial_state)) ## regresa el string


# for i in range(3):
#     if initial_state[i] == find[0]:
#         j = find[0].index('*')
#         print([i,j])
# print(initial_state.index['*'])