import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from MediPlot import BodyMap
import matplotlib.pyplot as plt

def save_bodymap_image(age, sex, sport):
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv('sports-dataset.csv')

    # Filter the data based on the given age, sex, and body part
    filtered_df = df[(df['Age'] == age) & (df['Sex'] == sex) & (df['Sport'] == sport)]

    # Count the unique product titles in the filtered data
    injury_counts = filtered_df['Body'].value_counts()

    # create empty lists to hold the columns
    body_parts = []
    counts = []

    # loop through the dictionary and add keys and values to the lists
    for body, count in injury_counts.items():
        body_parts.append(body)
        counts.append(count)
    
    print(body_parts, counts)  
    ax = BodyMap().generate(areas=body_parts,values=counts,cmap='YlOrRd',background='white')
    plt.savefig('image.png')
    return body_parts, counts

'''class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x400')
        self.root.configure(bg='white')

        # Create a frame to hold the controls on the right side
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the sport dropdown
        sport_label = tk.Label(controls_frame, text='Sport')
        sport_label.pack()
        self.sport_var = tk.StringVar()
        sport_options = ['Soccer', 'Baseball', 'Football', 'Basketball', 'Volleyball', 'Softball', 'Tennis', 'Badminton']
        self.sport_dropdown = tk.OptionMenu(controls_frame, self.sport_var, *sport_options)
        self.sport_dropdown.pack()

        # Create the gender dropdown
        gender_label = tk.Label(controls_frame, text='Gender')
        gender_label.pack()
        self.gender_var = tk.StringVar()
        gender_options = ['Male', 'Female']
        self.gender_dropdown = tk.OptionMenu(controls_frame, self.gender_var, *gender_options)
        self.gender_dropdown.pack()

        # Create the age group dropdown
        age_label = tk.Label(controls_frame, text='Age Group')
        age_label.pack()
        self.age_var = tk.StringVar()
        age_options = ['18-30', '30-45', '45+']
        self.age_dropdown = tk.OptionMenu(controls_frame, self.age_var, *age_options)
        self.age_dropdown.pack()

        # Create the Show and Clear buttons
        self.show_button = tk.Button(controls_frame, text='Show Image', command=self.show_image)
        self.show_button.pack(pady=10)
        self.clear_button = tk.Button(controls_frame, text='Clear Image', command=self.clear_image)
        self.clear_button.pack()

        # Create a canvas to display the image in the center
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack(side=tk.LEFT, padx=50, pady=50)

        self.image = None
'''

class App:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='white')

        # Create a frame to hold the controls on the right side
        controls_frame = tk.Frame(self.root, bg='white')
        controls_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=30, pady=30)

        # Create the sport dropdown
        sport_label = tk.Label(controls_frame, text='Sport', bg='white', font=('Arial', 20))
        sport_label.pack(pady=(50, 10))
        self.sport_var = tk.StringVar()
        sport_options = ['Soccer', 'Baseball', 'Football', 'Basketball', 'Volleyball', 'Softball', 'Tennis', 'Badminton']
        self.sport_dropdown = tk.OptionMenu(controls_frame, self.sport_var, *sport_options)
        self.sport_dropdown.config(font=('Arial', 18), bg='white')
        self.sport_dropdown.pack(pady=(0, 50))

        # Create the gender dropdown
        gender_label = tk.Label(controls_frame, text='Gender', bg='white', font=('Arial', 20))
        gender_label.pack(pady=(50, 10))
        self.gender_var = tk.StringVar()
        gender_options = ['Male', 'Female']
        self.gender_dropdown = tk.OptionMenu(controls_frame, self.gender_var, *gender_options)
        self.gender_dropdown.config(font=('Arial', 18), bg='white')
        self.gender_dropdown.pack(pady=(0, 50))

        # Create the age group dropdown
        age_label = tk.Label(controls_frame, text='Age Group', bg='white', font=('Arial', 20))
        age_label.pack(pady=(50, 10))
        self.age_var = tk.StringVar()
        age_options = ['0-18', '18-30', '30-45', '45+']
        self.age_dropdown = tk.OptionMenu(controls_frame, self.age_var, *age_options)
        self.age_dropdown.config(font=('Arial', 18), bg='white')
        self.age_dropdown.pack(pady=(0, 50))

        # Create the Show and Clear buttons
        self.show_button = tk.Button(controls_frame, text='Show Image', font=('Arial', 18), command=self.show_image, bg='white')
        self.show_button.pack(pady=(0, 10))
        self.clear_button = tk.Button(controls_frame, text='Clear Image', font=('Arial', 18), command=self.clear_image, bg='white')
        self.clear_button.pack()

        self.sport_var.set('Baseball')
        self.gender_var.set('Male')
        self.age_var.set('18-30')

        # Create a canvas to display the image in the center
        self.canvas = tk.Canvas(self.root, bg='white')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.create_text((850, 30), text="Human Anatomy plot Showing Sports related Injuries", font=("Arial", 44, "bold"), fill="black")

        self.image = None

    def show_image(self):
        if self.image is not None:
            self.canvas.create_text((850, 30), text="Human Anatomy plot Showing Sports related Injuries", font=("Arial", 44, "bold"), fill="black")
            self.canvas.delete('all')
            self.image = None
        self.canvas.create_text((850, 30), text="Human Anatomy plot Showing Sports related Injuries", font=("Arial", 44, "bold"), fill="black")    
        age = self.age_var.get()
        gender = self.gender_var.get()
        sport = self.sport_var.get()
        
        bp, cnts = save_bodymap_image(age, gender, sport)

        img = Image.open('image.png')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        img = img.resize((int(0.8*screen_height), int(0.9*screen_height)))
        self.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(screen_width/2.5, screen_height/2, anchor='center', image=self.image)

    def clear_image(self):
        if self.image is not None:
            self.canvas.delete('all')
            self.image = None

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()