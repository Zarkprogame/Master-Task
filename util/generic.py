from PIL import ImageTk, Image

def read_img(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))

def root_center(root, app_width, app_height):
    x = int((root.winfo_screenwidth() - app_width) / 2)
    y = int((root.winfo_screenheight() - app_height) / 2)
    return root.geometry(f"{app_width}x{app_height}+{x}+{y}")