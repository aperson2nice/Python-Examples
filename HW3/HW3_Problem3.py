#Sheila Robles
#Assignment 3 Problem 3
#Python Version 3.0.1

class Actor(object):
    def __init__(self, name):
        self.name = name
    def act(self):
        raise NotImplementedError("Act method not implemented.")
    def act(self,actor):
        self.actor = actor

class Robber(Actor):
    def __init__(self, name):
        Actor.__init__(self,name)
        
    def act(self, other_actor="None"):
        if other_actor == "None":
            print(self.name,"is Sneaking around")
        elif not isinstance(other_actor,Actor):
            raise TypeError("Must be of type Actor")
        elif isinstance(other_actor, Cop):
            print(self.name,"is running away from",other_actor.name)
        elif isinstance(other_actor, Pedestrian):
            print(self.name,"snatches wallet from",other_actor.name)
        else:
            print("Ignored")

class Cop(Actor):
    def __init__(self, name):
        Actor.__init__(self,name)
        
    def act(self, other_actor="None"):
        if other_actor == "None":
            print(self.name,"is patrolling the area")
        elif not isinstance(other_actor,Actor):
            raise TypeError("Must be of type Actor")
        elif isinstance(other_actor, Robber):
            print(self.name,"is arresting",other_actor.name)
        elif isinstance(other_actor,Pedestrian):
            print(self.name,"greets with a smile",other_actor.name)
        else:
            print("Ignored")

class Pedestrian(Actor):
    def __init__(self, name):
        Actor.__init__(self,name)
        
    def act(self, other_actor="None"):
        if other_actor == "None":
            print(self.name,"is walking downtown")
        elif not isinstance(other_actor,Actor):
            raise TypeError("Must be of type Actor")
        elif isinstance(other_actor, Robber):
            print(self.name,"is calling the cops on",other_actor.name)
        elif isinstance(other_actor,Cop):
            print(self.name,"greets with a smile",other_actor.name)
        else:
            print("Ignored")
            
            
if __name__ == "__main__":
    # Error cases were commented out in each objects
    # test block

    actor1 = Actor("Mr. Actor")
    robber1 = Robber("Mr. Robber")
    cop1 = Cop("Mrs. Cop")
    pedestrian1 = Pedestrian("Ms. Pedestrian")
    
    # Test Robber Interactions
    robber1.act()
    robber1.act(cop1)
    robber1.act(pedestrian1)
    robber1.act(actor1)
    #robber1.act("This is not a cop.")
    
    # Test Cop Interractions
    cop1.act()
    cop1.act(robber1)
    cop1.act(pedestrian1)
    cop1.act(actor1)
    #cop1.act("This is not a cop.")
    
    # Test Pedestrian Interrations
    pedestrian1.act()
    pedestrian1.act(cop1)
    pedestrian1.act(robber1)
    pedestrian1.act(actor1)
    #pedestrian1.act("This is not a cop.")