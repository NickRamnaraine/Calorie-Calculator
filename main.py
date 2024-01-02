from tkinter import *
from tkinter import messagebox

# Calorie calculator for the gym based on your specific goals
root = Tk()
root.title("Calorie Calculator")
root.geometry("400x150")


# Define submit button
def submit():
    # GUI that asks questions about lifestyle and what the user wants to accomplish
    submit_gui = Tk()
    submit_gui.title("Questions")
    submit_gui.geometry("1100x450")

    # Getting the user's height, weight, age, etc.
    height_feet = height_ft_label_box.get()
    height_inch = height_inch_label_box.get()
    weight = weight_label_box.get()
    age = age_label_box.get()
    sex = sex_label_box.get()

    # Creating error messages for incorrect responses
    if not height_feet.isdigit() or not height_inch.isdigit() or not weight.isdigit() or not age.isdigit():
        messagebox.showerror("ERROR", "Inputs cannot \nbe a word, or have decimals")
    if int(height_inch) < 0 or int(height_feet) < 0 or int(weight) < 0 or int(age) < 0:
        messagebox.showerror("ERROR", "Inputs cannot \nbe negative")
    if str(sex.lower()) != "female" and str(sex.lower()) != "male":
        messagebox.showerror("ERROR", "Must be male or female")

    # Creating activity level for calculations
    activity_level = {
        "1. Sedentary (little to no exercise)": 1,
        "2. Lightly active (light exercise 1 to 3 days a week)": 2,
        "3. Moderately active (moderate exercise 6 to 7 days a week)": 3,
        "4. Very active (hard exercise every day or exercising twice a day)": 4,
        "5. Extra active (very hard exercise, training, or a physical job. Ex: construction)": 5
    }

    # Creating goals for the gym to determine how many calories are needed to be added or subtracted
    gym_goals = {
        "1. Loose weight": 6,
        "2. Gain weight": 7,
        "3. Loose weight while gaining muscle": 8,
        "4. Gain weight and gain muscle": 9,
        "5. Maintain weight while gaining muscle ": 10,
    }

    # Creating variables for the values of the questions
    act_lvl = IntVar(submit_gui, 0)
    gym_lvl = IntVar(submit_gui, 0)

    # Creating a for loop to place multiple questions
    for text, lvl in activity_level.items():
        Radiobutton(submit_gui, text=text, variable=act_lvl, value=lvl).pack(anchor=W)

    gym_labelf = LabelFrame(submit_gui, text="")
    gym_labelf.pack(pady=3)
    gym_label = Label(gym_labelf, text="Goals for the gym")
    gym_label.pack()

    # Same process as above
    for text, lvl, in gym_goals.items():
        Radiobutton(submit_gui, text=text, variable=gym_lvl, value=lvl).pack(anchor=W)

    # Creating a function for calculating and outputting the goals for the user
    def clicked(activity_lvl, goals_lvl):
        # BMR(Basal Metabolic Rate), the calories you burn for the bodies daily functions
        global new_bmr

        if sex == "male":
            bmr = round((10 * weight_in_kg) + (6.25 * height_in_cm) - 5 * float(age) + 5)
        else:
            bmr = round((10 * weight_in_kg) + (6.25 * height_in_cm) - 5 * float(age) - 161)

        if activity_lvl == 1:
            new_bmr = round(bmr * 1.2)
        if activity_lvl == 2:
            new_bmr = round(bmr * 1.375)
        if activity_lvl == 3:
            new_bmr = round(bmr * 1.55)
        if activity_lvl == 4:
            new_bmr = round(bmr * 1.725)
        if activity_lvl == 5:
            new_bmr = round(bmr * 1.9)

        # Calories and protein calculated for gym goals
        if goals_lvl == 6:
            goals_lvl_6 = Label(submit_gui, text="Your target calories each day is around " + str(new_bmr - 500) +
                                                 ". With this amount, you should lose around 1 pound per week ")
            goals_lvl_6.pack(anchor=W)

        if goals_lvl == 7:
            goals_lvl_7 = Label(submit_gui, text="Your target calories each day is around " + str(new_bmr + 500) +
                                                 ". With this amount, you should gain around 1 pound per week.")
            goals_lvl_7.pack(anchor=W)

        if goals_lvl == 8:
            goals_lvl_8 = Label(submit_gui, text="Your target calories each day is around " + str(new_bmr - 300) +
                                                 " and around " + str(round(weight_in_kg * 0.7 * 2.204623)) +
                                                 " grams of protein each day. With these goals for each day you should lose around half a"
                                                 " pond to 1 pound a week, and you will gain some muscle.")
            goals_lvl_8.pack(anchor=W)

        if goals_lvl == 9:
            goals_lvl_9 = Label(submit_gui, text="Your target calories each day is around " + str(new_bmr + 500) +
                                                 " and around " + str(round(weight_in_kg * 0.7 * 2.204623)) +
                                                 " grams of protein each day. With these goals for each day you should gain about 1 pound of muscle"
                                                 " each week and gain muscle.")
            goals_lvl_9.pack(anchor=W)

        if goals_lvl == 10:
            goals_lvl_10 = Label(submit_gui, text="Your target calories for each day is around " + str(new_bmr) +
                                                  " and eating around " + str(round(weight_in_kg * 0.7 * 2.204623)) +
                                                  " grams of protein each day. This will ensure you stay at your weight while gaining muscle.")
            goals_lvl_10.pack(anchor=W)

    button = Button(submit_gui, text="Confirm", command=lambda: clicked(act_lvl.get(), gym_lvl.get()))
    button.pack()

    # Converts height into centimeters for calculations
    height_in_cm = float(height_feet) * 30.48 + float(height_inch) * 2.54
    # Converts weight into kilograms for calculations
    weight_in_kg = float(weight) * 0.45359237


# Creating labels for user information
height_ft_label = Label(root, text="Enter your height: ")
height_ft_label.grid(row=0, column=0, pady=(10, 0), ipadx=5)
height_ft_2_label = Label(root, text="ft")
height_ft_2_label.grid(row=0, column=2, pady=(10, 0))
height_inch_label = Label(root, text="in")
height_inch_label.grid(row=0, column=4, pady=(10, 0))
weight_label = Label(root, text="Enter your weight: ")
weight_label.grid(row=1, column=0)
lbs_label = Label(root, text="lbs")
lbs_label.grid(row=1, column=2)
age_label = Label(root, text="Enter your age: ")
age_label.grid(row=2, column=0)
sex_label = Label(root, text="Enter your sex: ")
sex_label.grid(row=3, column=0)

# Creating boxes for user to enter information
height_ft_label_box = Entry(root, width=15)
height_ft_label_box.grid(row=0, column=1, sticky=W, pady=(10, 0))
height_inch_label_box = Entry(root, width=15)
height_inch_label_box.grid(row=0, column=3, sticky=W, pady=(10, 0))
weight_label_box = Entry(root, width=15)
weight_label_box.grid(row=1, column=1)
age_label_box = Entry(root, width=15)
age_label_box.grid(row=2, column=1)
sex_label_box = Entry(root, width=15)
sex_label_box.grid(row=3, column=1)

# Submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=1, columnspan=3, pady=10, padx=10)

new_bmr = 0

root.mainloop()
