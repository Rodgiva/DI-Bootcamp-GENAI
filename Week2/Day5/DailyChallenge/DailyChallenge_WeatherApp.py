from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

api_key = "20c7245b0724f685ac04fb70ce8fae2d"
config_dict = get_default_config()
config_dict['language'] = 'fr'
owm = OWM(api_key)

mgr = owm.weather_manager()
observation = mgr.weather_at_place('Paris, FR')
print(observation.weather.detailed_status)  # Nuageux