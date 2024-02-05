import calendar




class Brain:
    materialTextures = ["Biological/Flesh", "Mechanical", "Spiritual", "Psychological", "Digital", "Cultural", "Delusional"] #List of textures I am aware of.
    def __init__(self, sample_name) -> None: 
        self.texture = None #Later method will change the value of this variable.
        self.__condition = "Undefined" #Will set to Healthy or Uhealthy by the scientist.
        self.sample_name = sample_name
    
    #Defining texture of the brain
    def define_texture(self, texture: int) -> None:
        """
        This is method to define texture of brain.

        Parameters:
        texture (int): A int parameter. From 0 to 6.
        
        Thorws error if: 
        parameter given is other than integer type,
        or
        parameter is out of bound from 0-6.
        """
        Options = self.materialTextures.copy()
        if type(texture) == int and texture in range(len(Options)): #Checks if texture is in the possible list.
            if self.texture != None:
                choice = input(f'Texture is already set to {self.texture}, are you willing to change it Y/N?: ')
                if choice == "Y" or choice == "y":
                    self.texture = Options[texture]
                elif choice == "N" or choice == "n":
                    return
                else:
                    raise ValueError("Out of definition.")
            self.texture = Options[texture] 
        elif type(texture) != int:
            raise AttributeError("Value must be of an integer type!")
        else:
            raise AttributeError("Value out of boundaries!")
    
    def get_texture(self):
        texture = self.texture
        return texture