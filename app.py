from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import json

app = Flask(__name__)

# Datos de ejemplo (simulando una base de datos)
def get_data():
    return pd.DataFrame({
        'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
        'Ventas': [200, 220, 250, 300, 400, 350],
        'Gastos': [150, 160, 170, 180, 190, 200]
    })

@app.route('/')
def dashboard():
    df = get_data()
    
    # Crear gráficos con Plotly
    fig1 = px.bar(df, x='Mes', y='Ventas', title='Ventas por Mes')
    fig2 = px.line(df, x='Mes', y=['Ventas', 'Gastos'], title='Comparativo')
    fig3 = px.pie(df, values='Ventas', names='Mes', title='Distribución')
    
    # Convertir gráficos a JSON para JavaScript
    graphs = [
        json.loads(fig.to_json()) for fig in [fig1, fig2, fig3]
    ]
    
    return render_template(
        'dashboard.html',
        graphs=graphs,
        table=df.to_html(classes='table table-striped')
    )

if __name__ == '__main__':
    app.run(debug=True)
