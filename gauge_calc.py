from math import ceil
def calculate_gauge(stitches_per_inch, rows_per_inch, project_width, project_height):
    project_stitches = stitches_per_inch*project_width
    project_rows = rows_per_inch*project_height
    return project_stitches, project_rows

def calculate_weight(swatch_width, swatch_height,swatch_weight, project_width, project_height):
    swatch_area = swatch_width * swatch_height
    project_area = project_width * project_height
    project_weight = swatch_weight * project_area/swatch_area
    return project_weight

def calculate_skeins(project_weight, skein_weight):
    return ceil(project_weight/skein_weight)

def calculate_yardage(project_weight, skein_weight, skein_yardage):
    return (project_weight/skein_weight)*skein_yardage