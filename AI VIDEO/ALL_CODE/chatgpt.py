import pyautogui
import time
import random
import pyperclip
import subprocess
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to open Firefox browser
def open_firefox():
    time.sleep(5)
    # Open terminal and execute firefox command
    subprocess.Popen(['firefox'])
    time.sleep(4)

    # Maximize the window (adjust coordinates as needed for your screen resolution)
    pyautogui.hotkey('alt', 'space')
    time.sleep(2)
    pyautogui.press('f')
    time.sleep(2)

# Function to open a new tab in Firefox
def open_new_tab():
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.5)

# Function to switch between tabs in Firefox
def switch_tabs():
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(0.5)

# Function to close the current tab in Firefox
def close_tab():
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(0.5)

# Function to navigate to ChatGPT in Firefox
def navigate_to_chat_gpt():
    open_new_tab()
    switch_tabs()
    close_tab()
    time.sleep(2)
    url = "https://chat.openai.com/"
    pyautogui.typewrite(url, interval=0.01)
    pyautogui.press('enter')
    time.sleep(2)



 
    time.sleep(1)
    # Your list of 500 single-word keywords
    keywords_list = ["Love", "Technology", "Health", "Fashion", "Food", "Travel", "Fitness", "Business", "Money", "Education", "Music", "Art", "Design", "Photography", "Sports", "Gaming", "Nature", "Adventure", "Beauty", "Wellness", "DIY", "Cars", "Pets", "Books", "Movies", "Science", "Space", "Home", "Family", "Cooking", "Marketing", "Gardening", "History", "Architecture", "Leadership", "Writing", "Meditation", "Sustainability", "Spirituality", "Relationships", "Creativity", "Innovation", "Finance", "Motivation", "Happiness", "Communication", "Networking", "Inspiration", "Success", "Strategy", "Analytics", "Entrepreneurship", "Collaboration", "Automation", "Diversity", "Empowerment", "Mindfulness", "Productivity", "Resilience", "Trends", "Luxury", "Minimalism", "Veganism", "Vegetarianism", "Gluten-Free", "Organic", "Sustainable", "Ethical", "Recycling", "Upcycling", "Robotics", "Cybersecurity", "Virtual", "Augmented", "Blockchain", "Cryptocurrency", "Data", "Privacy", "E-commerce", "Startups", "Cryptography", "Cloud", "AI (Artificial Intelligence)", "Machine Learning", "Algorithms", "Gadgets", "Wearables", "Smartphones", "IoT (Internet of Things)", "Nanotechnology", "Biotechnology", "Vaccines", "Mental Health", "Yoga", "Nutrition", "Dieting", "Weightlifting", "Running", "Pilates", "Cycling", "Swimming", "Crossfit", "Bodybuilding", "Investing", "Stocks", "Budgeting", "Real Estate", "Retirement", "Frugality", "Passive Income", "Management", "Teamwork", "Branding", "SEO (Search Engine Optimization)", "Content", "Blogging", "Copywriting", "Storytelling", "Journalism", "Publishing", "Editing", "Podcasting", "Vlogging", "Filmmaking", "Acting", "Theater", "Painting", "Sculpture", "Drawing", "Pottery", "Calligraphy", "Couture", "Textiles", "Jewelry", "Footwear", "Accessories", "Handbags", "Watches", "Cosmetics", "Skincare", "Haircare", "Perfume", "Spa", "Herbalism", "Holistic", "Zen", "Chakras", "Crystals", "Astrology", "Tarot", "Feng Shui", "Green Living", "Renewable Energy", "Zero Waste", "Slow Fashion", "Decluttering", "Tiny Houses", "Permaculture", "Landscape Design", "Biodiversity", "Wildlife", "Conservation", "Environmentalism", "Hiking", "Camping", "Mountaineering", "Backpacking", "Trekking", "Kayaking", "Surfing", "Skiing", "Snowboarding", "Road Trips", "Cultural Experiences", "Historical Sites", "Museums", "Music Festivals", "Food Festivals", "Wine", "Craft Beer", "Mixology", "Cocktails", "Tea", "Coffee", "Chocolate", "Baking", "Fast Food", "Street Food", "Gourmet", "Vegetarian", "Vegan", "Superfoods", "Paleo", "Keto", "Intermittent Fasting", "Meal Planning", "Meal Prep", "Food Blogging", "Gastronomy", "Molecular Gastronomy", "Nutrition Science", "Workouts", "Fitness Training", "Cardio", "Strength Training", "HIIT (High-Intensity Interval Training)", "Yoga", "Pilates", "CrossFit", "Functional Training", "Bodyweight Training", "Gymnastics", "Running", "Cycling", "Swimming", "Martial Arts", "Football", "Soccer", "Basketball", "Baseball", "Tennis", "Golf", "Rugby", "Cricket", "Volleyball", "Wrestling", "Athletics", "Equestrian", "Archery", "Bowling", "Billiards", "Skateboarding", "Ice Skating", "Climbing", "Fishing", "Hunting", "Boating", "Sailing", "Diving", "Snorkeling", "Rafting", "Canoeing", "Extreme Sports", "Motorsports", "Racing", "Aviation", "Space Exploration", "Astronomy", "Astrophysics", "Planetary Science", "Cosmology", "Rockets", "Satellites", "Spacecraft", "Artificial Intelligence", "Robotics", "Nanotechnology", "Biotechnology", "Quantum", "Renewable Energy", "Climate", "Oceanography", "Geology", "Geography", "Chemistry", "Physics", "Biology", "Genetics", "Ecology", "Psychology", "Sociology", "Anthropology", "Archaeology", "Philosophy", "Ethics", "Religion", "Mythology", "Spirituality", "History", "Archaeology", "Linguistics", "Literature", "Poetry", "Fiction", "Nonfiction", "Fantasy", "Science Fiction", "Mystery", "Thriller", "Horror", "Romance", "Drama", "Comedy", "Action", "Adventure", "Animation", "Documentary", "Independent", "Blockbuster", "Cult", "Classics", "Hollywood", "Bollywood", "K-Pop", "J-Pop", "Hip-Hop", "Rock", "Pop", "Jazz", "Classical", "Folk", "Blues", "Reggae", "Metal", "EDM (Electronic Dance Music)", "R&B", "Soul", "Funk", "Country", "Latin", "World Music", "Instrumental", "Lyrics", "Vocals", "Melody", "Harmony", "Rhythm", "Composition", "Production", "Recording", "Performance", "Stage", "Dance", "Theater", "Film", "Visual Arts", "Digital Arts", "Fine Arts", "Applied Arts", "Performing Arts", "Contemporary", "Modern", "Traditional", "Abstract", "Realism", "Impressionism", "Cubism", "Surrealism", "Expressionism", "Renaissance", "Baroque", "Gothic", "Minimalism", "Postmodernism", "Architecture", "Design", "Fashion Design", "Graphic Design", "Interior Design", "Industrial Design", "Web Design", "User Experience", "User Interface", "Animation", "Illustration", "Typography", "Branding", "Advertising"]

    # Pick a word at random
    random_word = random.choice(keywords_list)

    # Display the randomly picked word
    print("Randomly picked word:", random_word)
    time.sleep(2)




    Niche = random_word
    text = "Write a Short Essay on " + Niche + " Max 100 words"
    pyautogui.typewrite(text, interval=0.01)  # Adjust the interval as needed (in seconds)
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.hotkey("ctrl", 'shift', 'c')
    time.sleep(1)




def SavingMaetialTotext():


    copied_text = pyperclip.paste()
    file_pathofmaterial = 'ALL_CODE/ChatGpttext/material.txt'

    with open(file_pathofmaterial, 'w') as file:
        file.write(copied_text)
    
        print(f"Material '{copied_text}' saved to '{file_pathofmaterial}'")
    


def AskingGPTFORTITLE():

    textoftile = "I know you are AI Now Give me title for video, i am making video on above topic and i want single title no extra information"
    pyautogui.typewrite(textoftile, interval=0.01)  # Adjust the interval as needed (in seconds)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.hotkey("ctrl", 'shift', 'c')
    time.sleep(1)


def SavingTitleToText():

    file_pathoftitle = "ALL_CODE/ChatGpttext/title.txt"

    copied_title = pyperclip.paste()

    with open(file_pathoftitle, 'w') as file:
        file.write(copied_title)
        print(f"Title '{copied_title}' saved to '{file_pathoftitle}'")
    time.sleep(1)
def c_losing():

    pyautogui.hotkey('ctrl','w')



'''

open_firefox()
open_new_tab()
switch_tabs()
close_tab()
navigate_to_chat_gpt()
SavingMaetialTotext()
AskingGPTFORTITLE()
SavingTitleToText()
c_losing()
# Perform other tasks here by calling respective functions


'''