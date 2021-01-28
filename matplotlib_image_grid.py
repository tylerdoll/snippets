def plot_image_grid(images, cols=10, width=3):
    n = len(images)
    cols = min(n, cols)
    rows = math.ceil(n / cols)
    
    fig, axs = plt.subplots(rows, cols, figsize=(cols * width, rows * width), squeeze=False)
    for i, image in enumerate(images):
        axs[i // cols][i % cols].imshow(image)
        
    plt.show()
