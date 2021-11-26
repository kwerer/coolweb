from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
class FeatureInput(FlaskForm):
    New_Cases_Smoothed_Per_Million = StringField("New Cases Smoothed Per Million", validators=[DataRequired()])
    Total_Cases_Per_Million = StringField("Total Cases Per Million", validators=[DataRequired()])
    New_Deaths_Smoothed_Per_Million = StringField("New Deaths Smoothed Per Million", validators=[DataRequired()])
    Reproduction_Rate = StringField("Reproduction Rate", validators=[DataRequired()])
    New_Tests_Smoothed_Per_Thousand = StringField("New Tests Smoothed Per Thousand", validators=[DataRequired()])
    People_Fully_Vaccinated_Per_Hundred = StringField("People Fully Vaccinated Per Hundred", validators=[DataRequired()])
    Positive_Rate = StringField("Positive Rate", validators=[DataRequired()])
    submit = SubmitField("Submit")
