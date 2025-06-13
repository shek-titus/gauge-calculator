from flask import Flask, render_template, request
from gauge_calc import calculate_gauge, calculate_yardage, calculate_skeins, calculate_weight

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        stitches_per_inch  = float(request.form["stitches_per_inch"])
        rows_per_inch  = float(request.form["rows_per_inch"])
        swatch_width = float(request.form["swatch_width"])
        swatch_height = float(request.form["swatch_height"])
        swatch_weight = float(request.form["swatch_weight"])
        skein_yardage = float(request.form["skein_yardage"])
        skein_weight = float(request.form["skein_weight"])
        project_width = float(request.form["project_width"])
        project_height = float(request.form["project_height"])
        
        project_weight = calculate_weight(swatch_width, swatch_height, swatch_weight, project_width, project_height)

        stitches, rows = calculate_gauge(stitches_per_inch, rows_per_inch, project_width, project_height)
        yards = calculate_yardage(project_weight, skein_weight, skein_yardage)
        skeins = calculate_skeins(project_weight, skein_weight)

        return render_template(
            "results.html",
            stitches=int(stitches),
            rows=int(rows),
            yards=round(yards, 1),
            skeins =int(skeins),
            inputs=request.form
        )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
