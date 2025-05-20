class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]

    def __init__(self,name,pet_type , owner=None):
        self.name=name
        self.pet_type=pet_type
        self.owner=owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self,pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type=pet_type
        else:
            raise Exception("Input a valid pet type ")
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self,name):
        if isinstance(name, Owner)or name is None:
            self._owner=name
        else:
            raise Exception("Object is not of type Owner")


class Owner:
    def __init__(self,name):
        self.name=name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise Exception("Input must be an instance on Pet")
        pet.owner=self
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

    
