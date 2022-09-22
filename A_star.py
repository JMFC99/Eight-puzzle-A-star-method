class A_star:
    '''
    |7|2|4|   
    |5|*|6|
    |8|3|1|
    '''
    


    def __init__(self,initial_state):
        self.states=initial_state
        self.space_position = []
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
    
    def up(self,states,number):
        space_position=self.find_position()
        number_position=self.find_position(value=number)
        pass

    def down(self,states,number):
        space_position=self.find_position()
        number_position=self.find_position(value=number)
        pass

    def conditions_movement(type=''):
        pass

initial_state= [[7,2,4],[5,'*',6],[8,3,1]]
# initial_state= [[7,2,4],[5,6,'*'],[8,3,1]]
# initial_state= [[7,2,4],['*',5,6],[8,3,1]]



example = A_star(initial_state=initial_state)
example.print_statement()
example.right(number=6)
example.print_statement()


### find in which line is the *
# find = list(filter(lambda x:'*' in x,initial_state)) ## regresa el string


# for i in range(3):
#     if initial_state[i] == find[0]:
#         j = find[0].index('*')
#         print([i,j])
# print(initial_state.index['*'])