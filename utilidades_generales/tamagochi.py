import tkinter as tk
from tkinter import messagebox

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.thirst = 0
        self.happiness = 100
        self.health = 100
        self.need_to_pee = 0
        self.alive = True
    
    def feed(self):
        if self.hunger > 0:
            self.hunger -= 40
            self.thirst += 10
            self.need_to_pee += 10
        else:
            messagebox.showinfo("Tamagotchi", f"{self.name} no tiene hambre.")
    
    def drink(self):
        if self.thirst > 0:
            self.thirst -= 20
            self.need_to_pee += 50
        else:
            messagebox.showinfo("Tamagotchi", f"{self.name} no tiene sed.")
    
    def play(self):
        if self.happiness < 100:
            self.happiness += 20
            self.hunger += 10
            self.thirst += 5
        else:
            messagebox.showinfo("Tamagotchi", f"{self.name} está muy feliz ahora mismo.")
    
    def got_to_bathroom(self):
        if self.need_to_pee > 0:
            self.need_to_pee = 0
        else:
            messagebox.showinfo("Tamagotchi", f"{self.name} no necesita ir al baño.")
    
    def check_status(self):
        return f"Estado de {self.name}: Hambre {self.hunger}, Sed {self.thirst}, Felicidad {self.happiness}, Salud {self.health}, Necesidad de ir al baño {self.need_to_pee}"
    
    def time_passes(self):
        self.hunger += 5
        self.thirst += 5
        self.happiness -= 5
        self.need_to_pee += 5
        if self.hunger > 100 or self.thirst > 100 or self.need_to_pee > 100:
            self.health -= 20
        if self.health <= 0:
            self.alive = False

class TamagotchiApp:
    def __init__(self, master):
        self.master = master
        master.title("Tamagotchi")
        self.initialize_pet()
        self.initialize_ui()
    
    def initialize_pet(self):
        self.pet = Tamagotchi("Pet")
    
    def initialize_ui(self):
        self.status_font = ("Arial", 14)
        self.load_images()
        self.create_widgets()
        self.auto_update_status()

    def load_images(self):
        self.images = {
            'normal': tk.PhotoImage(file='imagenes/idle-happy.gif'),
            'hungry': tk.PhotoImage(file='imagenes/tired-sad.gif'),
            'thirsty': tk.PhotoImage(file='imagenes/sleeping-zzz.gif'),
            'happy': tk.PhotoImage(file='imagenes/wave-waving.gif'),
            'bathroom': tk.PhotoImage(file='imagenes/run-walk.gif'),
            'sad': tk.PhotoImage(file='imagenes/tired-sad.gif'),
            'dead': tk.PhotoImage(file='imagenes/rip-deadpool.gif')
        }
    
    def create_widgets(self):
        self.image_label = tk.Label(self.master, image=self.images["normal"])
        self.image_label.pack()

        self.status_label = tk.Label(self.master, text=self.pet.check_status(), font=self.status_font)
        self.status_label.pack()

        self.feed_button = tk.Button(self.master, text="Alimentar", command=self.feed)
        self.feed_button.pack()

        self.drink_button = tk.Button(self.master, text="Dar de beber", command=self.drink)
        self.drink_button.pack()

        self.play_button = tk.Button(self.master, text="Jugar", command=self.play)
        self.play_button.pack()

        self.bathroom_button = tk.Button(self.master, text="Ir al baño", command=self.go_to_bathroom)
        self.bathroom_button.pack()
    
    def pet_action(self, action):
        message = getattr(self.pet, action)()
        if message:
            messagebox.showinfo("Tamagotchi", message)
        self.update_status()
    
    def feed(self):
        self.pet_action("feed")

    def drink(self):
        self.pet_action('drink')

    def play(self):
        self.pet_action('play')

    def go_to_bathroom(self):
        self.pet_action('go_to_bathroom')

    def update_status(self):
        self.status_label.config(text=self.pet.check_status())
        self.update_image()

    def update_image(self):
        if not self.pet.alive:
            self.image_label.config(image=self.images['dead'])
            self.show_death_message()
        elif self.pet.hunger >= 80:
            self.image_label.config(image=self.images['hungry'])
        elif self.pet.thirst >= 80:
            self.image_label.config(image=self.images['thirsty'])
        elif self.pet.happiness > 80:
            self.image_label.config(image=self.images['happy'])
        elif self.pet.need_to_pee >= 80:
            self.image_label.config(image=self.images['bathroom'])
        elif self.pet.health < 20:
            self.image_label.config(image=self.images['sad'])
        else:
            self.image_label.config(image=self.images['normal'])
        
    def auto_update_status(self):
        if self.pet.alive:
            self.pet.time_passes()
            self.update_status()
            self.master.after(5000, self.auto_update_status)
        else:
            self.update_status()
    
    def show_death_message(self):
        messagebox.showinfo("Tamagotchi", f"Oh no, {self.pet.name} ha fallecido. :(")
        self.disable_buttons()

    def disable_buttons(self):
        self.feed_button.config(state='disabled')
        self.drink_button.config(state='disabled')
        self.play_button.config(state='disabled')
        self.bathroom_button.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = TamagotchiApp(root)
    root.mainloop()