from flask import Flask, request, render_template, Response
import plotly.graph_objects as go
#import plotly.express as px
import json
import plotly


Data = [[1,5,3,8],[2,4,6,5]]
Labels = ['a', 'b','c','d']
Legend = ['City1','City2']
LineColor = ['green','orange']
LineOpacity = [0.5,1]

app = Flask(__name__)

@app.route('/test', methods=['POST', 'GET'])
def index():
    # Create a figure to which I'll add plots
    fig = go.Figure()
    
    for i in range(0,len(Data)):
        fig.add_trace(go.Scatter(
                                x= Labels, 
                                y= Data[i], 
                                marker=dict(
                                    symbol='square',
                                    size=20,
                                    color='red',
                                    line=dict(
                                        color='blue',
                                        width=4
                                    )),
                                name = Legend[i],
                                line=dict(
                                        color=LineColor[i],
                                        width=2
                                    ),  
                                line_shape = 'spline',
                                opacity = LineOpacity[i],
                                mode = 'markers+lines+text',
                                text =  Legend[i],
                                textposition = 'top center'  
                                ))

    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(debug=True)