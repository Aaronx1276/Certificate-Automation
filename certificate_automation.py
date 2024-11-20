from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import os

def generate_certificate(name, event, template_path, output_folder):
    # Open the template image
    img = Image.open(template_path)
    
    # Create a draw object to add text to the image
    draw = ImageDraw.Draw(img)
    
    # Load a font
    font_path = "C:/Windows/Fonts/arial.ttf"  # Update with the correct font path on your machine
    try:
        font = ImageFont.truetype(font_path, 65)
    except OSError:
        font = ImageFont.load_default()
    
    # Add the student's name to the certificate
    text_position_name = (100, 200)  # Adjust the position as needed
    draw.text(text_position_name, name, font=font, fill=(0, 0, 0))
    
    # Add the event name to the certificate
    font_event = ImageFont.truetype(font_path, 40)  # Smaller font for the event
    text_position_event = (100, 300)  # Adjust the position as needed
    draw.text(text_position_event, event, font=font_event, fill=(0, 0, 0))
    
    # Save the generated certificate to the output folder
    output_path = os.path.join(output_folder, f"{name}_certificate.jpg")
    img.save(output_path)
    print(f"Certificate saved for {name} at {output_path}")

def main():
    # Tkinter window setup
    root = Tk()
    root.title("Certificate Automation")
    root.geometry("400x300")
    
    # Input for the event name
    event_label = Label(root, text="Enter the event name:")
    event_label.pack()
    event_entry = Text(root, height=2, width=30)
    event_entry.pack()

    def start_generation():
        # Use the 'requirements.txt' file in the same folder
        names_file_path = "input_names.txt"
        try:
            with open(names_file_path, 'r') as file:
                names = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"File {names_file_path} not found.")
            return
        
        # Get the event name from the entry
        event = event_entry.get("1.0", "end-1c")
        
        # The output folder is fixed as 'certificates' in the project folder
        output_folder = "certificates"
        
        # Make sure the output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Template path is fixed as 'template.jpg' in the project folder
        template_path = "template.jpg"
        
        # Generate certificates for all names
        for name in names:
            generate_certificate(name, event, template_path, output_folder)
        
        print("All certificates have been generated.")

    # Start button to trigger certificate generation
    start_button = Button(root, text="Generate Certificates", command=start_generation)
    start_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
