from flask import Flask, render_template, request, redirect, url_for, session
from database import df

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_password'


@app.route('/', methods=['GET', 'POST'])
def index():
    # fields = {}
    data = df.copy()
    if request.method == 'POST':
        recommended_build_surfaces = ["ABS Slurry", "Kapton Tape", "PEI",
                                      "Painter's Tape", "Glue Stick", "Glass Plate", "Commercial Adhesive", "Polypropylene Sheet",
                                      "Packing Tape"
                                      ]

        build_surface = request.form.get('build_surface')

        if build_surface == "":
            data = df.copy()
        else:
            for item in recommended_build_surfaces:

                if build_surface == item:

                    data = df[df['recommended_build_surfaces'].str.contains(
                        item)]

        ultimate_strength = request.form.get('ultimate_strength')
        stiffness = request.form.get('stiffness')
        durability = request.form.get('durability')
        printability = request.form.get('printability')
        density = request.form.get('density')



        if not request.form.get('ultimate_strength') == '':

            data = data[data['ultimate_strength'] <= float(ultimate_strength)]

        if not request.form.get('stiffness') == '':

            data = data[data['stiffness'] <= float(stiffness)]

        if not request.form.get('durability') == '':

            data = data[data['durability'] <= float(durability)]

        if not request.form.get('printability') == '':

            data = data[data['printability'] <= float(printability)]

        if not request.form.get('density') == '':

            data = data[data['density'] < float(density)]

        flexible = request.form.get('flexible')
        if flexible == 'yes':
            data = data[data['flexibility'] == 1]
        elif flexible == 'no':
            data = data[data['flexibility'] == 0]

        flexible = request.form.get('impact_resistant')
        if flexible == 'yes':
            data = data[data['impact_resistant'] == 1]
        elif flexible == 'no':
            data = data[data['impact_resistant'] == 0]

        flexible = request.form.get('impact_resistant')
        if flexible == 'yes':
            data = data[data['impact_resistant'] == 1]
        elif flexible == 'no':
            data = data[data['impact_resistant'] == 0]

        flexible = request.form.get('uv_resistant')
        if flexible == 'yes':
            data = data[data['uv_resistant'] == 1]
        elif flexible == 'no':
            data = data[data['uv_resistant'] == 0]

        flexible = request.form.get('water_resistant')
        if flexible == 'yes':
            data = data[data['water_resistant'] == 1]
        elif flexible == 'no':
            data = data[data['water_resistant'] == 0]

        flexible = request.form.get('dissolvable')
        if flexible == 'yes':
            data = data[data['dissolvable'] == 1]
        elif flexible == 'no':
            data = data[data['dissolvable'] == 0]

        flexible = request.form.get('chemically_resistant')
        if flexible == 'yes':
            data = data[data['chemically_resistant'] == 1]
        elif flexible == 'no':
            data = data[data['chemically_resistant'] == 0]

        data = data.loc[:, ['item_name', 'recommended_build_surfaces',
                            'ultimate_strength', 'stiffness', 'durability', 'min_price', 'max_price']]

        html = data.to_html()

        return render_template('form.html', tables=[data.to_html(classes='data')], titles=data.columns.values)
    return render_template('form.html')



if __name__ == "__main__":
    app.run(debug=True)
