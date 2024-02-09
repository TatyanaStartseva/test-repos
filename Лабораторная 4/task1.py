if __name__ == "__main__":
    # Write your solution here
    class Mythological_creatures:
        """ Basic class.
            We can create a creature, which has name, ability, live in the certain place and has some intelligence.
            In this class, we use a property for an attribute of our class.
            For instance: dragon = Mythological_creatures("Dragon", "Make fire", "A cave", 150).
            name - "Dragon" , ability - "Make fire", live -"A cave", intelligence - 150
            And we have methods that show information about the class.
        """

        def __init__(self, name: str, ability: str, live: str, intelligence: int):
            self.name = name
            self.ability = ability
            self.live = live
            self.intelligence = intelligence

        """Creating properties to protect our attributes. Make it so that users aren't able to change our attributes and 
        include the extra checks. The result of the call( in our example) : Dragon (for name)"""

        @property
        def name(self) -> str:
            return self._name
        """The result of the call( in our example) : Make fire (for ability)"""
        @property
        def ability(self) -> str:
            return self._ability

        """The result of the call( in our example) : A cave (for live)"""
        @property
        def live(self) -> str:
            return self._live

        """The result of the call( in our example) : 150 (for intelligence)"""
        @property
        def intelligence(self) -> int:
            return self._intelligence

        """Creating setters to protect our attributes. And added checks.
        For instants: dragon.name = "Dragon-Zizi" and etc """

        @name.setter
        def name(self, new_name) -> None:
            if not isinstance(new_name, str):
                raise TypeError("A name must be a string")
            else:
                self._name = new_name

        @ability.setter
        def ability(self, ability: str) -> None:
            if not isinstance(ability, str):
                raise TypeError("A ability must be a string")
            else:
                self._ability = ability

        @live.setter
        def live(self, live: str) -> None:
            if not isinstance(live, str):
                raise TypeError("Live must be a string")
            else:
                self._live = live

        @intelligence.setter
        def intelligence(self, intelligence: int) -> None:
            if not isinstance(intelligence, int) or intelligence < 0:
                raise TypeError("Intelligence must be an integer and be greater more than zero")
            else:
                self._intelligence = intelligence
        """In the basic class we have a method that shows the creature's ability """
        def Show_ability(self) -> str:
            return self.ability
        """A method which improves the creature's wisdom"""
        def improve_intelligence(self) -> None:
            self.intelligence += 5

        """ A magic method, which shows information about class for users. The result in our example will be 
        A name Dragon.A Power Make fire. Live A cave. Intelligence 150"""

        def __str__(self):
            return f"A name {self.name}.A Power {self.ability}. Live {self.live}. Intelligence {self.intelligence}"

        """A magic method, which shows information about class for programmers. The result in our example will be 
        Mythological_creatures(name='Dragon', ability='Make fire',live='A cave', intelligence=150)"""

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, ability={self.ability!r},live={self.live!r}, " \
                   f"intelligence={self.intelligence!r})"


    class Phoenix(Mythological_creatures):
        """ An inherited class. Has the same as the class 'Mythological_creatures', except for the attribute 'revival' """

        def __init__(self, name: str, ability: str, live: str, intelligence: int, revival: int):
            super().__init__(name, ability, live, intelligence)
            self.revival = revival

        """ A getter for revival """

        @property
        def revival(self) -> int:
            return self._revival

        """ A setter for safe a revival. The setter has check ( that the number of revival is more than zero and that type is int)
        """

        @revival.setter
        def revival(self, new_revival: int) -> None:
            if not isinstance(new_revival, int) or new_revival < 0:
                raise TypeError("The number of revival must be an integer and more than zero")
            else:
                self._revival = new_revival
        """A method that make a phoenix to die and increases the attribute 'revival' """
        def fire(self) -> int:
            self.revival += 1
            print("Fire")
        """A overloaded method. In the base class it shows the creature's ability, but in an inherited write 'Flight'"""
        def Show_ability(self) -> str:
            abi = "Flight"
            return abi

        """ In the methods 'str' and 'repr' added 'revival' """

        def __str__(self):
            return f"A name {self.name}.A Power {self.ability}. Live {self.live}. Intelligence {self.intelligence}. A revival {self.revival}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, ability={self.ability!r},live={self.live!r}, " \
                   f"intelligence={self.intelligence!r}, revival={self.revival})"


    class Sirens(Mythological_creatures):
        """ An inherited class.Has the same as the class ''Mythological_creatures', except the method "Show_ability" """

        def __init__(self, name: str, ability: str, live: str, intelligence: int):
            super().__init__(name, ability, live, intelligence)

        """A overloaded method. In the base class it shows the creature's ability, but in an inherited write 'Seducing sailors'"""
        def Show_ability(self) -> str:
            return "Seducing sailors"

        def Sing(self) -> None:
            print("\t", "While up aloft in storm", "\n\t", "From me his absence mourn", "\n\t", "And firmly pray arrive the day",
                  "\n", "\t", "He's never more to roam.")


    dragon = Mythological_creatures("Dragon", "Make fire", "A cave", 150)
    print(dragon.name)
    print(dragon.ability)
    print(dragon.live)
    print(dragon.intelligence)
    dragon.name = "Dragon-Zizi"
    print(dragon.Show_ability())
    dragon.improve_intelligence()
    print(dragon.intelligence)
    print(dragon.__str__())
    print(dragon.__repr__())
    print("_________________________________________", '\n')
    phoenix = Phoenix("Phy", "Die", "A desert", 150, 2)
    print(phoenix.name)
    print(phoenix.revival)
    print(phoenix.ability)
    print(phoenix.live)
    print(phoenix.Show_ability())
    phoenix.fire()
    print(phoenix.__str__())
    print(phoenix.__repr__())
    print("_________________________________________", '\n')
    siren = Sirens("Samanta", "Sing", "sea", 90)
    print(siren.Show_ability())
    siren.Sing()
    print(siren.__str__())
    print(siren.__repr__())
    pass
