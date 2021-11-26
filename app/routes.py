from app import application
from flask import Flask, render_template, request
from app.forms import FeatureInput

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'lucky8'

@application.route("/", methods = ["POST", "GET"])
def home():
    beta_values = [52.73979899, -0.00207458, -6.91533959, 0.11199107, -0.8223395, 4.06842093, -0.83646151, 2.93171969]
    column_ave_values = [60.11932, 8814.446, 0.02173, 1.0859, 6.24012, 19.184,0.01912]
    column_std_values = [138.61, 4116.576, 0.04954, 0.3714, 4.08898, 29.919, 0.04558]
    features_names = ["Constant","New Cases Per Million", "Total Cases Per Million", "New Deaths Smoothed Per Million", " Repduction Rate", "New Tests Smoothed Per Thousand", "People Fully Vaccinated Per Hundered", "Positive Rate"]
    form = FeatureInput()
    if form.is_submitted():
        result = request.form
        value_ls = []
        for key, value in result.items():
            if value != "Submit":
                value_ls.append(float(value))
            else:
                value_ls.append(30)
        val_norm = []
        for index in range(0,7):
            val_norm.append((value_ls[index] - column_ave_values[index]) / (column_std_values[index]))
        sum = 0
        sum = beta_values[0]
        for c_index in range(1,7):
            sum += beta_values[c_index] * val_norm[c_index-1]
        val_norm.insert(0,"nil")
        value_ls.insert(0,"nil")
        return render_template("results.html", result = result, beta_values = beta_values, val_norm=val_norm, value_ls = value_ls, sum = sum, features_names=features_names)
    return render_template("home.html", form = form)