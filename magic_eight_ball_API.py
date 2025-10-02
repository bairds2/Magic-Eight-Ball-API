"""
   Name: magic_eight_ball_API.py
   Author: Savannah Baird
   Created: 09/17/25
   Purpose: Get a random eight ball answer from API
"""
# define the main function
def main():
   print(magic())
   # Loop the function so you can ask as many questions as you want
   again = input("Do you have another question? [1. to quit]")
   while again != "1":
      print(magic())
      again = input("Do you have another question? [1. to quit] ")
   print("Thanks for playing!") 
         



# Import the requests module
def magic():
   import requests

   # URL for magic eight ball 
   URL = "https://eightballapi.com/api?locale=en"

   response = requests.get(URL)

   eight_ball = response.json()

   user_input = input("How can Magic Eight Ball serve you? ")
   shake = input("\nShAkE, sHaKe, ShAkE\n")
   return (eight_ball.get("reading"))
   

main()