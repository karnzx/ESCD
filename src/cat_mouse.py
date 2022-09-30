def cat_mouse(cat_a, cat_b, mouse_c):
    dist_cat_b = abs(mouse_c - cat_b)
    dist_cat_a = abs(mouse_c - cat_a)
    if dist_cat_b < dist_cat_a:
        return "Cat B"
    elif dist_cat_a < dist_cat_b:
        return "Cat A"
    else:
        return "Mouse C"
