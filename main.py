from pygame import mixer  # Load the popular external library
import arcade
import http.client as httplib

#mixer.init()
#mixer.music.load('j:\Prv\Filee\Beraghsa.mp3')
#mixer.music.play()

# Creating MainGame class       
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, title="Player Movement")
  
        # Initializing the initial x and y coordinated
        self.x = 250 
        self.y = 250
  
        # Initializing a variable to store
        # the velocity of the player
        self.vel = 300
  
    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()
  
        # Drawing the rectangle using
        # draw_rectangle_filled function
        arcade.draw_rectangle_filled(self.x, self.y,50, 50,
                                     arcade.color.GREEN )
    # Creating on_update function to
    # update the x coordinate
    def on_update(self,delta_time):
        self.x += self.vel * delta_time
  
        # Changing the direction of
        # movement if player crosses the screen
        if self.x>=550 or self.x<=50:
            self.vel *= -1
  
            # Loading the audio file
            audio = arcade.load_sound('j:\Prv\Filee\Beraghsa.mp3',False)
  
            # Printing "Playing Audio"
            print("Playing Audio.mp File")
  
            # Playing the audio
            arcade.play_sound(audio,1.0,-1,False)
              
          
# Calling MainGame class       
def checkInternetHttplib(url="www.geeksforgeeks.org",
                         timeout=3):
    connection = httplib.HTTPConnection(url,
                                        timeout=timeout)
    try:
        # only header requested for fast operation
        while True:
            connection.request("HEAD", "/")
            connection.close()  # connection closed
            print("Internet On")
        return True
    except Exception as exep:
        print(exep)
        MainGame()
        arcade.run()
        return False
 
 
checkInternetHttplib("www.geeksforgeeks.org", 3)
#MainGame()
#arcade.run()