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
        elif isinstance(other_actor, Bystander):
            print(self.name,"glares at",other_actor.name)
        else:
            print("Ignored")
    def talk_to_rob(self):
        print(self.name,'says, "HEY YOU! This is a stick up!"')

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
        elif isinstance(other_actor, Bystander):
            print(self.name,"waves at",other_actor.name)
        else:
            print("Ignored")
    def talk_to_badguy(self):
        print(self.name,'says, "Hold it! Put your hands up!"')

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
        elif isinstance(other_actor, Bystander):
            print(self.name,"smiles at",other_actor.name)
        else:
            print("Ignored")
    def talk(self):
        print(self.name,'says, "Help me!"')
        
class Bystander(Actor):
    def __init__(self, name):
        Actor.__init__(self,name)      
    def act(self, other_actor="None"):
        if other_actor == "None":
            print(self.name,"is minding his own business")
        elif not isinstance(other_actor,Actor):
            raise TypeError("Must be of type Actor")
        elif isinstance(other_actor, Robber):
            print(self.name,"is fleeing from",other_actor.name)
        elif isinstance(other_actor,Cop):
            print(self.name,"waves at",other_actor.name)
        elif isinstance(other_actor,Pedestrian):
            print(self.name,"smiles at",other_actor.name)
        else:
            print("Ignored")
    def talk(self):
        print(self.name,'says, "What a lovely day."')
            
if __name__ == "__main__":
    # Error cases were commented out in each objects
    # test block
    actor1 = Actor("Mr. Actor")
    robber1 = Robber("Mr. Robber")
    cop1 = Cop("Mrs. Cop")
    pedestrian1 = Pedestrian("Mr. Pedestrian")
    bystander1 = Bystander("Kid eating ice cream")
    
    # Test Robber Interactions
    robber1.act()
    robber1.act(cop1)
    robber1.talk_to_rob()
    robber1.act(pedestrian1)
    robber1.act(bystander1)
    robber1.act(actor1)
    #robber1.act("This is not a cop.")
    
    # Test Cop Interractions
    cop1.act()
    cop1.talk_to_badguy()
    cop1.act(robber1)
    cop1.act(pedestrian1)
    cop1.act(bystander1)
    cop1.act(actor1)
    #cop1.act("This is not a cop.")
    
    # Test Pedestrian Interrations
    pedestrian1.act()
    pedestrian1.act(bystander1)
    pedestrian1.act(cop1)
    pedestrian1.talk()
    pedestrian1.act(robber1)
    pedestrian1.act(actor1)
    #pedestrian1.act("This is not a cop.")
    
    # Test Pedestrian Interrations
    bystander1.act()
    bystander1.act(cop1)
    bystander1.act(pedestrian1)
    bystander1.talk()
    bystander1.act(robber1)
    bystander1.act(actor1)
    #bystander1.act("This is not a cop.")