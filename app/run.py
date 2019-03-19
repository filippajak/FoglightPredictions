from flask import request, Flask, jsonify

from app.model.historical_datapath import HistoricalDatapath
from app.plotting.stacked_area_plotter import StackedAreaPlotter
from app.predictionmodels.prophet_predictor import ProphetPredictor
from app.remote.request_body_builder import RequestbodyBuilder
from app.remote.request_sender import RequestSender
from app.transform.dataframe_converter import DataframeConverter

main_url = 'http://localhost:8080/foglight/predictions'

app = Flask(__name__)

def send_request_for_oss(request):
    desktop_operating_systems_url = main_url + '/desktop-operating-systems'

    contents = request.json

    countries = contents['countries']
    oss = contents['oss']
    threshold = request.args.get('threshold')
    min_date = request.args.get('min_date')
    max_date = request.args.get('max_date')

    request_body = RequestbodyBuilder().build_request_body_for_desktop_operating_systems(countries, oss)

    dat = RequestSender().send_request(desktop_operating_systems_url, request_body, threshold, min_date, max_date)
    print(dat)

    # list of lists of all paths (multiple OSs --- multiple countries)
    all_paths = list()
    for country in countries:
        # list of paths (multiple OSs --- single country)
        paths = list()
        for data in dat:
            if data['country'] == country:
                # single path (single OS --- single country)
                # path = HistoricalDatapath(data['historicalMarketshares'], data['handset'], data['country'])
                path = HistoricalDatapath(data['historicalMarketshares'], data['desktopOperatingSystem'], data['country'])
                paths.append(path)
        all_paths.append(paths)

    return all_paths

@app.route('/')
def yo():
    return 'yo'

@app.route('/desktop-operating-systems/stacked-area-graph', methods=['POST'])
def draw_stacked_area_graph_for_desktop_operating_systems():

    all_paths = send_request_for_oss(request)

    for paths in all_paths:
        country = paths[0].country
        dataframe = ProphetPredictor().predict(paths)
        StackedAreaPlotter().draw(dataframe, country)

    # DeviceMarketsharePlotter().draw_plot_for_all_devices(paths)

    return 'fo shizz'

@app.route('/desktop-operating-systems/predictions', methods=['POST'])
def get_predicted_values_for_desktop_operating_systems():
    all_paths = send_request_for_oss(request)

    response = list()

    # iterate over countries
    for paths in all_paths:
        country = paths[0].country
        # predict paths for a single country
        dataframe = ProphetPredictor().predict(paths)
        p = DataframeConverter().get_future_datapaths(dataframe, country) 
        response.extend(p)

    json = jsonify([e.serialize() for e in response])

    url = main_url + '/future-datapaths/desktop-operating-systems'
    RequestSender().send_request_with_future_datapath(url, json.json)

    return json

    