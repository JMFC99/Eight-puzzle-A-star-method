class A_star:
    '''
    |7|2|4|   
    |5|*|6|
    |8|3|1|
    '''
    


    def __init__(self,initial_state):
        self.states=initial_state
        self.final_goal = [[1,2,3],[4,5,6],[7,8,'*']]
        self.changed_values=[]
        self.directions =['R','L','U','D'] ### right, left up and down
        self.no_reached_goal = True
        self.frontier = []
        self.explored = []
        self.cost = 1
        
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
            if self.states[i] == find[0]:
                j = find[0].index(value) ### esta nos da la posición de la columna 
                return [i,j]

    def right(self,number,frontier):
        space_position=self.find_position()
        # print('asterisco posicion:',space_position)
        number_position=self.find_position(value=number)
        # print('numero posicion:',space_position)
        row,column = number_position ### tener la fila y columna
        
        if (space_position[0] == row) and (space_position[1]-1 ==column):
            # print('puedo moverlo a la derecha')
            if frontier: ### solo saber si se puede hacer el movimiento
                return True
            #### esta sección de código realiza el movimiento de los estados
            self.states[space_position[0]][space_position[1]] = self.states[number_position[0]][number_position[1]]
            self.states[number_position[0]][number_position[1]] = '*'
            return
        return False

    def left(self,number,frontier): #### simplificar derecha e izquierda       
        space_position=self.find_position()
        # print('asterisco posicion:',space_position)
        number_position=self.find_position(value=number)
        # print('numero posicion:',space_position)
        row,column = number_position ### tener la fila y columna
        
        if (space_position[0] == row) and (space_position[1]+1 ==column):
            
            if frontier:### solo saber si se puede hacer el movimiento
                return True
         #### esta sección de código realiza el movimiento de los estados
            self.states[space_position[0]][space_position[1]] = self.states[number_position[0]][number_position[1]]
            self.states[number_position[0]][number_position[1]] = '*'
            return
            
        return False
    
    def up(self,number,frontier):
        space_position=self.find_position()
        # print('asterisco posicion:',space_position)
        number_position=self.find_position(value=number)
        # print('numero posicion:',space_position)
        row,column = number_position ### tener la fila y columna
        
        if (space_position[0]+1 == row) and (space_position[1] ==column):
            # print('puedo moverlo arriba')
            if frontier:
                return True
            self.states[space_position[0]][space_position[1]] = self.states[number_position[0]][number_position[1]]
            self.states[number_position[0]][number_position[1]] = '*'
                            
            return
        return False
        

    def down(self,number,frontier):
        space_position=self.find_position()
        # print('asterisco posicion:',space_position)
        number_position=self.find_position(value=number)
        # print('numero posicion:',space_position)
        row,column = number_position ### tener la fila y columna
        
        if (space_position[0]-1 == row) and (space_position[1] ==column):
            # print('puedo moverlo abajo')

            if frontier:
                return True
            self.states[space_position[0]][space_position[1]] = self.states[number_position[0]][number_position[1]]
            self.states[number_position[0]][number_position[1]] = '*'
            
            return
        return False

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
        # print(surrondings_values)
        return surrondings_values ## regresa los valores de los alrededores


    def calculate_distances(self,match_number_position,objective_position): #### esto será la heuristica y el numero de moviemientos el costo
        distance =(((match_number_position[0]-objective_position[0])**2) + ((match_number_position[1]-objective_position[1]))**2)**(1/2)
        return distance

    
    def movements(self,direction,value,frontier=False): ### valor por default de que nos estamos buscando frontiers sino que si se quiere hacer el cambio
        match direction:  ###['R','L','U','D']
            case 'R':
                return self.right(value,frontier)
            
            case 'L':
                return self.left(value,frontier)
            
            case 'U':
                return self.up(value,frontier)
            
            case 'D':
                return self.down(value,frontier)
        

    def frontier_method(self,objective):
        ##### esto obtenemos los alrededores del metodo
        ### obtener los valores alrededor del objetivo
            surrondings_values = self.surrondings(value=objective)
            surrondings_empty = self.surrondings(value='*')

            match_numbers = list(filter(lambda x:x in surrondings_empty,surrondings_values))
            #### son los numeros que conciden tanto en los alrededores del empty como del valor objetivo

            if len(match_numbers)<1:
                match_numbers = surrondings_empty ### los numeros match seran nombrados a los encontrados por surrondings_empty

            for match_number in match_numbers:
                for direction in self.directions:
                    # self.last_value = self.states
                    direction_value = self.movements(direction=direction,value=match_number,frontier=True)
                    if direction_value:
                        match_number_position= self.find_position(value=match_number)
                        objective_position = self.find_position(value=objective)
                        distance_number = self.calculate_distances(match_number_position,objective_position)+self.cost
                        value = [match_number,direction,distance_number]
                        movements_explored=[]
                        movements_frontier=[]
                        if len(self.explored)>0:
                            movements_explored = list(map(lambda x:x[:2],self.explored))
                        
                        if len(self.frontier)>0:
                            movements_frontier = list(map(lambda x:x[:2],self.frontier))

                        if (value not in movements_frontier) and (value[:2] not in movements_explored):
                            self.frontier.append(value)  ##### ['matched number/numero de los lados', 'Direccion',''f(n)']

                        # print(self.states)
                        # print(self.frontier)
                        break
            self.cost +=1

    def explorer_method(self):
        shorter_distance = sorted(list(map(lambda x:x[2],self.frontier))) ##### distancia más corta
        ordered_list = []
        for value in shorter_distance:
            ordered_list.append(list(filter(lambda x:value in x,self.frontier))[0])
        # del self.frontier
        self.frontier = ordered_list[1:]
        selected_movement = ordered_list[0]
        # selected_movement= list(filter(lambda x:shorter_distance in x,self.frontier))[0]
        self.explored.append(selected_movement)
        self.movements(selected_movement[1],selected_movement[0])
        print(self.explored)
        self.print_statement()
        #['matched number/numero de los lados', 'Direccion',''f(n)']

        # del self.frontier
        # self.frontier = []
        # print(frontier)
        # print(self.frontier)
        pass


    def main(self):
        objective = 1 
        while self.no_reached_goal:
            objective_position = self.find_position(value=objective)
            self.frontier_method(objective=1)
            self.explorer_method()
            if objective_position ==[0,0]:
                self.no_reached_goal=False



    # def method(self,objective):       


    #     distance_number = self.calculate_distances(coordinates_match_number,objective_position) + self.cost ### este 1 significa el numbero de movimientos
    #     ###
    #     if (len(distances)!=0): ### si no esta vacío
    #         if distance_number<distances[-1][1]:  ### diferenciar el tipo de distancia del ultimo dato dado
    #             distances.append([match_number,distance_number]) ## colocar en valores de nuevas distancias

    #     else:
    #         distances.append([match_numbers,distance_number])

    # ##### realizar los movimientos
    #     for direction in self.directions:
    #         move_done  = self.movements(direction=direction)
    #         if move_done:
    #             self.explored.append(f'{distances[0][0]}{direction}') ## sabemos la dirección inicial
    #             self.cost +=self.cost ### aumentamos el costo 
    #             break

            


                


    #     pass

       
# changed_value=[]
# initial_state= [[7,2,4],[5,'*',6],[8,3,1]]
# initial_state= [[7,2,4],[5,6,'*'],[8,3,1]]
initial_state= [[7,2,4],['*',5,6],[8,3,1]]



example = A_star(initial_state=initial_state)
example.print_statement()
# example.frontier_method(objective=1)
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
# print(example.frontier)
example.main()