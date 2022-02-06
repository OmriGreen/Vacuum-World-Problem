#Enter A/B in capital letters for location_input and complement_input
#0 means clean space, 1 means a dirty space
class vacuumCheck:
    
    def __init__(self, location_input, location_status, complement_status):
        #Initialize all Variables
        
        #Creates the pieces of the Object        
        goal_state = {"A":"0", "B":"0"}
        cost = 0

        #Checks if the starting location is in A
        if location_input == "A":
            #if A is dirty
            if location_status == 1:
                goal_state["A"] = "0"
                cost+= 1 #The cost to clean the dirt

                #if B is dirty
                if complement_status == 1:
                    cost+=1 #Cost for moving to B
                    goal_state["B"] = "0"
                    cost +=1 #Cost for cleaning the dirt
                #If B is not dirty no action is taken
            #If A isn't dirty
            else:
                #if B is dirty
                if complement_status == 1:
                    cost+=1 #Cost for moving to B
                    goal_state["B"] = "0"
                    cost +=1 #Cost for cleaning the dirt
                #If B is not dirty no action is taken
                
        #If the starting location is in B
        else:
            if location_status == 1:
                goal_state["B"] = "0"
                cost+= 1 #The cost to clean the dirt

                #if A is dirty
                if complement_status == 1:
                    cost+=1 #Cost for moving to A
                    goal_state["A"] = "0"
                    cost +=1 #Cost for cleaning the dirt
                #If A is not dirty no action is taken
            #If B isn't dirty
            else:
                #if A is dirty
                if complement_status == 1:
                    cost+=1 #Cost for moving to B
                    goal_state["A"] = "0"
                    cost +=1 #Cost for cleaning the dirt
                #If A is not dirty no action is taken            
        self.cost = cost;
        
                    
                
                    
                    
                    
                    
            
        
    
        
    