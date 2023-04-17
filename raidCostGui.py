import tkinter as tk

# Gets input from the user on what objects they are trying to raid
def calculate_cost():
    sheet_door_num = float(sheetDoor_entry.get())
    wood_door_num = float(woodDoor_entry.get())
    arm_door_num = float(armDoor_entry.get())
    wooden_wall_num = float(woodWall_entry.get())
    stone_wall_num = float(stoneWall_entry.get())
    sheet_wall_num = float(sheetWall_entry.get())
    arm_wall_num = float(armWall_entry.get())
    garagedoor_num = float(garageDoor_entry.get())
    exStoneWall_num = float(exStoneWall_entry.get())
    exWoodWall_num = float(exWoodWall_entry.get())
    
    # Assigns the cost to raid each object depending on the explosive being used
    wall_cost = {
            "Sheet Metal Wall": {
                "Satchel Charge": 23,
                "Rocket": 8, 
                "Beancan": 112, 
                "C4": 4, 
                "HV": 67, 
                "Icen": 0, 
                "Explo": 400, 
                "Nade": 1000, 
            },
            "Armored Wall": {
                "Satchel Charge": 46,
                "Rocket": 15, 
                "Beancan": 223, 
                "C4": 8, 
                "HV": 134, 
                "Icen": 0, 
                "Explo": 834, 
                "Nade": 2000, 
            },
            "Stone Wall": {
                "Satchel Charge": 10,
                "Rocket": 4, 
                "Beancan": 46, 
                "C4": 2, 
                "HV": 34, 
                "Icen": 0, 
                "Explo": 209, 
                "Nade": 200, 
            },
            "High External Stone Wall": {
                "Satchel Charge": 10,
                "Rocket": 4, 
                "Beancan": 46, 
                "C4": 2, 
                "HV": 32, 
                "Icen": 0, 
                "Explo": 185, 
                "Nade": 182, 
            }, 
            "Wooden Wall": {
                "Satchel Charge": 3,
                "Rocket": 2, 
                "Beancan": 13, 
                "C4": 1, 
                "HV": 9, 
                "Icen": 1, 
                "Explo": 49, 
                "Nade": 63, 
            }, 
            "High External Wooden Wall": {
                "Satchel Charge": 6,
                "Rocket": 3, 
                "Beancan": 26, 
                "C4": 2, 
                "HV": 18, 
                "Icen": 1, 
                "Explo": 98, 
                "Nade": 118, 
            },
            "Wooden Door": {
                "Satchel Charge": 2,
                "Rocket": 1, 
                "Beancan": 6, 
                "C4": 1, 
                "HV": 4, 
                "Icen": 1, 
                "Explo": 19, 
                "Nade": 23, 
            }, 
            "Sheet Door": {
                "Satchel Charge": 4,
                "Rocket": 2, 
                "Beancan": 18, 
                "C4": 1, 
                "HV": 11, 
                "Icen": 0, 
                "Explo": 63, 
                "Nade": 50, 
            }, 
            "Arm Door": {
                "Satchel Charge": 15,
                "Rocket": 5, 
                "Beancan": 69, 
                "C4": 3, 
                "HV": 42, 
                "Icen": 0, 
                "Explo": 250, 
                "Nade": 200, 
            }, 
            "Garage Door": {
                "Satchel Charge": 9,
                "Rocket": 3, 
                "Beancan": 42, 
                "C4": 2, 
                "HV": 25, 
                "Icen": 0, 
                "Explo": 150, 
                "Nade": 120, 
            }
        }
    # Assigns the sulfur cost of crafting each explosive
    sulfur_cost = {
            "Satchel Charge":480,
            "Beancan": 120,
            "Nade": 60,
            "Rocket": 1400, 
            "C4": 2200,
            "Icen": 610,
            "Explo": 50,
            "HV": 200
        }



    # Calculate the sulfur cost of raiding sheet walls
    sheetWall_satchel = sheet_wall_num * (wall_cost["Sheet Metal Wall"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    sheetWall_beancan = sheet_wall_num * (wall_cost["Sheet Metal Wall"]["Beancan"] * sulfur_cost["Beancan"])
    sheetWall_nade = sheet_wall_num * (wall_cost["Sheet Metal Wall"]["Nade"] * sulfur_cost["Nade"])
    sheetWall_rocket = sheet_wall_num * (wall_cost["Sheet Metal Wall"]["Rocket"] * sulfur_cost["Rocket"])
    sheetWall_c4 = sheet_wall_num * (wall_cost["Sheet Metal Wall"]["C4"] * sulfur_cost["C4"])
    sheetWall_explo = sheet_wall_num * (wall_cost["Sheet Metal Wall"]["Explo"] * sulfur_cost["Explo"])
    sheetWall_HV = sheet_wall_num * (wall_cost["Sheet Metal Wall"]["HV"] * sulfur_cost["HV"])
    sheetWall_cost = min(sheetWall_satchel,sheetWall_beancan,sheetWall_nade,sheetWall_rocket,sheetWall_c4,sheetWall_explo,sheetWall_HV) 

    # Calculate the sulfur cost of raiding armoured walls
    armWall_satchel = arm_wall_num * (wall_cost["Armored Wall"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    armWall_beancan = arm_wall_num * (wall_cost["Armored Wall"]["Beancan"] * sulfur_cost["Beancan"])
    armWall_nade = arm_wall_num * (wall_cost["Armored Wall"]["Nade"] * sulfur_cost["Nade"])
    armWall_rocket = arm_wall_num * (wall_cost["Armored Wall"]["Rocket"] * sulfur_cost["Rocket"])
    armWall_c4 = arm_wall_num * (wall_cost["Armored Wall"]["C4"] * sulfur_cost["C4"])
    armWall_explo = arm_wall_num * (wall_cost["Armored Wall"]["Explo"] * sulfur_cost["Explo"])
    armWall_HV = arm_wall_num * (wall_cost["Armored Wall"]["HV"] * sulfur_cost["HV"])
    armWall_cost = min(armWall_satchel,armWall_beancan,armWall_nade,armWall_rocket,armWall_c4,armWall_explo,armWall_HV)

    # Calculate the sulfur cost of raiding stone walls
    stoneWall_satchel = stone_wall_num * (wall_cost["Stone Wall"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    stoneWall_beancan = stone_wall_num * (wall_cost["Stone Wall"]["Beancan"] * sulfur_cost["Beancan"])
    stoneWall_nade = stone_wall_num * (wall_cost["Stone Wall"]["Nade"] * sulfur_cost["Nade"])
    stoneWall_rocket = stone_wall_num * (wall_cost["Stone Wall"]["Rocket"] * sulfur_cost["Rocket"])
    stoneWall_c4 = stone_wall_num * (wall_cost["Stone Wall"]["C4"] * sulfur_cost["C4"])
    stoneWall_explo = stone_wall_num * (wall_cost["Stone Wall"]["Explo"] * sulfur_cost["Explo"])
    stoneWall_HV = stone_wall_num * (wall_cost["Stone Wall"]["HV"] * sulfur_cost["HV"])
    stoneWall_cost = min(stoneWall_satchel,stoneWall_beancan,stoneWall_nade,stoneWall_rocket,stoneWall_c4,stoneWall_explo,stoneWall_HV)

    # Calculate the sulfur cost of raiding wooden walls
    woodWall_satchel = wooden_wall_num * (wall_cost["Wooden Wall"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    woodWall_beancan = wooden_wall_num * (wall_cost["Wooden Wall"]["Beancan"] * sulfur_cost["Beancan"])
    woodWall_nade = wooden_wall_num * (wall_cost["Wooden Wall"]["Nade"] * sulfur_cost["Nade"])
    woodWall_rocket = wooden_wall_num * (wall_cost["Wooden Wall"]["Rocket"] * sulfur_cost["Rocket"])
    woodWall_c4 = wooden_wall_num * (wall_cost["Wooden Wall"]["C4"] * sulfur_cost["C4"])
    woodWall_explo = wooden_wall_num * (wall_cost["Wooden Wall"]["Explo"] * sulfur_cost["Explo"])
    woodWall_HV = wooden_wall_num * (wall_cost["Wooden Wall"]["HV"] * sulfur_cost["HV"])
    woodWall_Icen = wooden_wall_num * (wall_cost["Wooden Wall"]["Icen"] * sulfur_cost["Icen"])
    woodWall_cost = min(woodWall_satchel,woodWall_beancan,woodWall_nade,woodWall_rocket,woodWall_c4,woodWall_explo,woodWall_HV, woodWall_Icen)

    # Calculate the sulfur cost of raiding wooden door
    woodDoor_satchel = wood_door_num * (wall_cost["Wooden Door"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    woodDoor_beancan = wood_door_num * (wall_cost["Wooden Door"]["Beancan"] * sulfur_cost["Beancan"])
    woodDoor_nade = wood_door_num * (wall_cost["Wooden Door"]["Nade"] * sulfur_cost["Nade"])
    woodDoor_rocket = wood_door_num * (wall_cost["Wooden Door"]["Rocket"] * sulfur_cost["Rocket"])
    woodDoor_c4 = wood_door_num * (wall_cost["Wooden Door"]["C4"] * sulfur_cost["C4"])
    woodDoor_explo = wood_door_num * (wall_cost["Wooden Door"]["Explo"] * sulfur_cost["Explo"])
    woodDoor_HV = wood_door_num * (wall_cost["Wooden Door"]["HV"] * sulfur_cost["HV"])
    woodDoor_cost = min(woodDoor_satchel,woodDoor_beancan,woodDoor_nade,woodDoor_rocket,woodDoor_c4,woodDoor_explo,woodDoor_HV)


    # Calculate the sulfur cost of raiding sheet door
    sheetDoor_satchel = sheet_door_num * (wall_cost["Sheet Door"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    sheetDoor_beancan = sheet_door_num * (wall_cost["Sheet Door"]["Beancan"] * sulfur_cost["Beancan"])
    sheetDoor_nade = sheet_door_num * (wall_cost["Sheet Door"]["Nade"] * sulfur_cost["Nade"])
    sheetDoor_rocket = sheet_door_num * (wall_cost["Sheet Door"]["Rocket"] * sulfur_cost["Rocket"])
    sheetDoor_c4 = sheet_door_num * (wall_cost["Sheet Door"]["C4"] * sulfur_cost["C4"])
    sheetDoor_explo = sheet_door_num * (wall_cost["Sheet Door"]["Explo"] * sulfur_cost["Explo"])
    sheetDoor_HV = sheet_door_num * (wall_cost["Sheet Door"]["HV"] * sulfur_cost["HV"])
    sheetDoor_cost = min(sheetDoor_satchel,sheetDoor_beancan,sheetDoor_nade,sheetDoor_rocket,sheetDoor_c4,sheetDoor_explo,sheetDoor_HV)

    # Calculate the sulfur cost of raiding armoured door
    armDoor_satchel = arm_door_num * (wall_cost["Arm Door"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    armDoor_beancan = arm_door_num * (wall_cost["Arm Door"]["Beancan"] * sulfur_cost["Beancan"])
    armDoor_nade = arm_door_num * (wall_cost["Arm Door"]["Nade"] * sulfur_cost["Nade"])
    armDoor_rocket = arm_door_num * (wall_cost["Arm Door"]["Rocket"] * sulfur_cost["Rocket"])
    armDoor_c4 = arm_door_num * (wall_cost["Arm Door"]["C4"] * sulfur_cost["C4"])
    armDoor_explo = arm_door_num * (wall_cost["Arm Door"]["Explo"] * sulfur_cost["Explo"])
    armDoor_HV = arm_door_num * (wall_cost["Arm Door"]["HV"] * sulfur_cost["HV"])
    armDoor_cost = min(armDoor_satchel,armDoor_beancan,armDoor_nade,armDoor_rocket,armDoor_c4,armDoor_explo,armDoor_HV)

    # Calculate the sulfur cost of raiding External stone walls
    exStoneWall_satchel = exStoneWall_num * (wall_cost["High External Stone Wall"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    exStoneWall_beancan = exStoneWall_num * (wall_cost["High External Stone Wall"]["Beancan"] * sulfur_cost["Beancan"])
    exStoneWall_nade = exStoneWall_num * (wall_cost["High External Stone Wall"]["Nade"] * sulfur_cost["Nade"])
    exStoneWall_rocket = exStoneWall_num * (wall_cost["High External Stone Wall"]["Rocket"] * sulfur_cost["Rocket"])
    exStoneWall_c4 = exStoneWall_num * (wall_cost["High External Stone Wall"]["C4"] * sulfur_cost["C4"])
    exStoneWall_explo = exStoneWall_num * (wall_cost["High External Stone Wall"]["Explo"] * sulfur_cost["Explo"])
    exStoneWall_HV = exStoneWall_num * (wall_cost["High External Stone Wall"]["HV"] * sulfur_cost["HV"])
    exStoneWall_cost = min(exStoneWall_satchel,exStoneWall_beancan,exStoneWall_nade,exStoneWall_rocket,exStoneWall_c4,exStoneWall_explo,exStoneWall_HV)

    # Calculate the sulfur cost of raiding External wooden walls
    exWoodWall_satchel = exWoodWall_num * (wall_cost["High External Wooden Wall"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    exWoodWall_beancan = exWoodWall_num * (wall_cost["High External Wooden Wall"]["Beancan"] * sulfur_cost["Beancan"])
    exWoodWall_nade = exWoodWall_num * (wall_cost["High External Wooden Wall"]["Nade"] * sulfur_cost["Nade"])
    exWoodWall_rocket = exWoodWall_num * (wall_cost["High External Wooden Wall"]["Rocket"] * sulfur_cost["Rocket"])
    exWoodWall_c4 = exWoodWall_num * (wall_cost["High External Wooden Wall"]["C4"] * sulfur_cost["C4"])
    exWoodWall_explo = exWoodWall_num * (wall_cost["High External Wooden Wall"]["Explo"] * sulfur_cost["Explo"])
    exWoodWall_HV = exWoodWall_num * (wall_cost["High External Wooden Wall"]["HV"] * sulfur_cost["HV"])
    exWoodWall_cost = min(exWoodWall_satchel,exWoodWall_beancan,exWoodWall_nade,exWoodWall_rocket,exWoodWall_c4,exWoodWall_explo,exWoodWall_HV)

    # Calculate the sulfur cost of raiding garage door
    garageDoor_satchel = garagedoor_num * (wall_cost["Garage Door"]["Satchel Charge"] * sulfur_cost["Satchel Charge"])
    garageDoor_beancan = garagedoor_num * (wall_cost["Garage Door"]["Beancan"] * sulfur_cost["Beancan"])
    garageDoor_nade = garagedoor_num * (wall_cost["Garage Door"]["Nade"] * sulfur_cost["Nade"])
    garageDoor_rocket = garagedoor_num * (wall_cost["Garage Door"]["Rocket"] * sulfur_cost["Rocket"])
    garageDoor_c4 = garagedoor_num * (wall_cost["Garage Door"]["C4"] * sulfur_cost["C4"])
    garageDoor_explo = garagedoor_num * (wall_cost["Garage Door"]["Explo"] * sulfur_cost["Explo"])
    garageDoor_HV = garagedoor_num * (wall_cost["Garage Door"]["HV"] * sulfur_cost["HV"])
    garageDoor_cost = min(garageDoor_satchel,garageDoor_beancan,garageDoor_nade,garageDoor_rocket,garageDoor_c4,garageDoor_explo,garageDoor_HV)


    total_cost = (sheetWall_cost + armWall_cost + stoneWall_cost + woodWall_cost + woodDoor_cost + sheetDoor_cost + armDoor_cost + exStoneWall_cost + exWoodWall_cost + garageDoor_cost)
    cost_output.insert(tk.END, f"{total_cost:.2f}")
    
    node_cost = total_cost/300 
    node_output.insert(tk.END, f"{node_cost:.2f}")
    

# Create the main window
root = tk.Tk()
root.title("Rust Sulfur Cost Calculator")
root.geometry("300x300")
root.configure(bg='orange')


# Create the font
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 10)

# Set the background and foreground colors for the labels and buttons
label_color = "black"
button_color = "black"
label_font_color = "white"
button_font_color = "white"

# Create the labels and entry boxes with the updated appearance
woodDoor_label = tk.Label(root, text="Wooden Doors: ", bg=label_color, fg=label_font_color)
woodDoor_label.grid(row=0, column=0)
woodDoor_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
woodDoor_entry.grid(row=0, column=1)

sheetDoor_label = tk.Label(root, text="Sheet Doors: ", bg=label_color, fg=label_font_color)
sheetDoor_label.grid(row=1, column=0)
sheetDoor_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
sheetDoor_entry.grid(row=1, column=1)

armDoor_label = tk.Label(root, text="Armoured Doors: ", bg=label_color, fg=label_font_color)
armDoor_label.grid(row=2, column=0)
armDoor_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
armDoor_entry.grid(row=2, column=1)

woodWall_label = tk.Label(root, text="Wooden Walls: ", bg=label_color, fg=label_font_color)
woodWall_label.grid(row=3, column=0)
woodWall_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
woodWall_entry.grid(row=3, column=1)

stoneWall_label = tk.Label(root, text="Stone Wall: ", bg=label_color, fg=label_font_color)
stoneWall_label.grid(row=4, column=0)
stoneWall_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
stoneWall_entry.grid(row=4, column=1)

sheetWall_label = tk.Label(root, text="Sheet Walls: ", bg=label_color, fg=label_font_color)
sheetWall_label.grid(row=5, column=0)
sheetWall_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
sheetWall_entry.grid(row=5, column=1)

armWall_label = tk.Label(root, text="Armoured Walls: ", bg=label_color, fg=label_font_color)
armWall_label.grid(row=6, column=0)
armWall_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
armWall_entry.grid(row=6, column=1)

garageDoor_label = tk.Label(root, text="Garage Doors: ", bg=label_color, fg=label_font_color)
garageDoor_label.grid(row=7, column=0)
garageDoor_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
garageDoor_entry.grid(row=7, column=1)

exStoneWall_label = tk.Label(root, text="External Stone Walls: ", bg=label_color, fg=label_font_color)
exStoneWall_label.grid(row=8, column=0)
exStoneWall_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
exStoneWall_entry.grid(row=8, column=1)

exWoodWall_label = tk.Label(root, text="External Wood Walls: ", bg=label_color, fg=label_font_color)
exWoodWall_label.grid(row=9, column=0)
exWoodWall_entry = tk.Entry(root, bg=button_color, fg=button_font_color)
exWoodWall_entry.grid(row=9, column=1)

# Create the output box
cost_output_label = tk.Label(root, text="Total sulfur cost: ", bg=label_color, fg=label_font_color)
cost_output_label.grid(row=10, column=0)
cost_output = tk.Entry(root, bg=button_color, fg=button_font_color)
cost_output.grid(row=10, column=1)

# Create the output box
node_output_label = tk.Label(root, text="Number of Nodes: ", bg=label_color, fg=label_font_color)
node_output_label.grid(row=11, column=0)
node_output = tk.Entry(root, bg=button_color, fg=button_font_color)
node_output.grid(row=11, column=1)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_cost)
calculate_button.grid(row=11, column=1, columnspan=2)

# Start the GUI loop
root.mainloop()