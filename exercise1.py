#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first few lines for you as an example


'''
import sys, logging, pygame	# imports the sys, logging, and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

screen_size = (800,600) #Sets the size of the screen that the animations will be playing on.
FPS = 60 #Defining FPS as 60s to be used later as the frame rate
red = (255,0,0) #Color to be used as the block colour.
black = (0,0,0) #Color of the background/screen

class Block(pygame.sprite.Sprite): #Creating a class called Block, which will include all the properties of the block that appears on screen
	def __init__(self, position, direction): #defining a function that will run automatically called __init__ that has th parameters self, position and direction relating to the block and the screen.
		pygame.sprite.Sprite.__init__(self) #The sprite will appear automatically in the program
		self.image = pygame.Surface((50, 50)) #sets the size of the block
		self.image.fill(red) #sets the color of the block
		self.rect = self.image.get_rect() #Gives the Block the same attributes as a rectangle sprite in pygames.
		(self.rect.x,self.rect.y) = position #Sets a direction in relation to the Block
		self.direction = direction #Defining the direction in relation to the the Block

	def update(self): #Further expanding an the attributes of 'self'
		(dx,dy) = self.direction #setting direction to a tuple so that it relates to the coordinates on the screen
		self.rect.x += dx #
		self.rect.y += dy
		(WIDTH,HEIGHT) = screen_size #Sets screen size to a tuple so that it can be easily related to the Block.
		if self.rect.left > WIDTH: #If the value for the sprite starting at the left is greater than the width:
			self.rect.right = 0 #It will move right
		if self.rect.right < 0: #If the value for the sprite starting right is less than 0:
			self.rect.left = WIDTH #The rectangle will go back to the edge of the screen
		if self.rect.top > HEIGHT: #If the rectangle is starting at the top
			self.rect.bottom = 0 #Then the sprite will not start at the bottom
		if self.rect.bottom < 0: #If the sprite reaches the bottom
			self.rect.top = HEIGHT # It will go back to the top


def main():
	pygame.init() #Makes sure this line of code runs automatically
	screen = pygame.display.set_mode(screen_size) #defines screen as the function that draws the screen
	clock = pygame.time.Clock() #This is the function that controls the framerate of the program/game being run

	blocks = pygame.sprite.Group() #A container that holds and manages multiple blocks within the program
	block = Block((200,200),(-1,1)) #Defines block as the Block class that was created earlier
	blocks.add(block) #Adds blocks to the group of sprites

	while True: #This is the game loop
		clock.tick(FPS) #Ensures that the program does
		screen.fill(black) #Colours the screen black

		for event in pygame.event.get():
			if event.type == pygame.QUIT: #condition of if the event is QUIT
				pygame.quit() #Quits the pygame module
				sys.exit(0) #quits the program at the system level

		blocks.update() #Continuously runs the loop, the blocks will update with a new value and move across the screen accordingly
		blocks.draw(screen) #Draws the blocks on the screen
		pygame.display.flip() #The picture on the screen that is set to change is automatically flipped all at once on the screen

if __name__ == '__main__': #If you recall as a .py file, it will run the program, if it is recalled as a module (imported) it won't automatically run.
	main() #runs the program