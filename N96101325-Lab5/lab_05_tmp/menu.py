import pygame
import os
MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        
        self.image = pygame.transform.scale(MENU_IMAGE, (150, 150)) 
        self.sell_image = pygame.transform.scale(SELL_IMAGE, (50, 50))
        self.upgrade_image = pygame.transform.scale(UPGRADE_IMAGE, (75, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.__buttons = [Button(self.upgrade_image,"upgrade",self.rect.centerx,self.rect.centery-55)
                          ,Button(self.sell_image,"sell",self.rect.centerx,self.rect.centery+60)]
        # (Q2) Add buttons here

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.image,(self.rect.x,self.rect.y))
        # draw button
        # (Q2) Draw buttons here
        #win.blit(())
        #win.blit(self.sell_image,(self.rect.x+50,self.rect.y+100))
        #win.blit(self.upgrade_image,(self.rect.x+37,self.rect.y))
        for btn in self.__buttons:
            win.blit(btn.image,btn.rect)

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons
        


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #pygame.transform.scale(image, (60, 40))
        

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if self.rect.collidepoint( x, y):
            return True 
        else:
            return False 

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name 






