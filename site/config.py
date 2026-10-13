"""Site facts and shared lists: the one place for anything that appears on more than one page.

Change a value here, run `python site/build.py`, and every page that uses it updates.
"""
from datetime import date

COMPANY = 'Bolamudi Enterprise'
DOMAIN = 'bolamudi.com'
PHONE = '+91 91138 23687'            # shown as written; the tap-to-call link is derived from it
EMAIL = 'bolamudienergyinfra@gmail.com'
RESPONSE_TIME = 'one business day'   # the reply promise on the contact page, forms and footer bands
YEAR = date.today().year             # footer copyright

# Enquiry form: Web3Forms emails each submission to EMAIL (the key is tied to that inbox)
FORM_ENDPOINT = 'https://api.web3forms.com/submit'
FORM_KEY = '32504a9f-cbeb-47bb-bcf3-3b0c143a66e2'

# Web fonts. The families are also named in assets/tokens.css; keep the two in step.
FONTS_URL = ('https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600;700'
             '&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap')

# Header menu as (page, label), then the call-to-action button at its end
NAV = [('index.html', 'Home'), ('about.html', 'About'), ('services.html', 'Services'),
       ('sectors.html', 'Sectors'), ('karnataka.html', 'Karnataka')]
NAV_CTA = ('contact.html', 'Request a consultation')

# Footer "Company" column
FOOTER_COMPANY = [('about.html', 'About'), ('sectors.html', 'Sectors'),
                  ('karnataka.html', 'Karnataka coverage'), ('contact.html', 'Contact')]

# The five services, in order (footer, and previous/next links on the service pages).
# Each has a page services-<key>.html; its content is in pages/service_pages.py.
SERVICES = {
    'land-aggregation': dict(
        name='Land aggregation', title='Land Aggregation', photo='land-parcel.jpg',
        tagline='Contiguous, title-clean, registered land — assembled parcel by parcel.'),
    'government-liaison': dict(
        name='Government liaison', title='Government Liaison', photo='pavagada-satellite.jpg',
        tagline='Continuous, documented follow-through with the departments that decide.'),
    'statutory-approvals': dict(
        name='Statutory approvals', title='Statutory Approvals', photo='solar-plant-2.jpg',
        tagline='A project-specific statutory register, owned from application to closure.'),
    'transmission-row': dict(
        name='Transmission right of way', title='Transmission Right of Way', photo='almatti-dam.jpg',
        tagline='Corridor walked, optimised, compensated and cleared — span by span.'),
    'project-development-support': dict(
        name='Project development support', title='Project Development Support', photo='sharavathi.jpg',
        tagline='The Karnataka-side development desk — one interface, one register, one weekly report.'),
}

# Images in assets/img: alt text (empty = background only) and the Wikimedia Commons credit
# their licence requires, listed on the Terms page in this order.
PHOTOS = {
    'solar-plant.jpg': dict(alt='', by='Thomas Lloyd Group', licence='CC BY-SA 4.0',
                            source='Solar_Power_Plant_Karnataka_I_in_state_of_Karnataka,_India,_40.5-MWp_DC.jpg'),
    'solar-plant-2.jpg': dict(alt='Aerial view of a utility-scale solar plant in Karnataka', by='Thomas Lloyd Group',
                              licence='CC BY-SA 4.0',
                              source='Solar_Power_Plant_Karnataka_I_in_state_of_Karnataka,_India,_40.5-MWp_DCb.jpg'),
    'land-parcel.jpg': dict(alt='A marked land parcel in Karnataka before solar construction', by='Thomas Lloyd Group',
                            licence='CC BY-SA 4.0',
                            source='Solar_Power_Plant_Karnataka_II_in_state_of_Karnataka,_India,_27-MWp_DCb.jpg'),
    'wind-ridge.jpg': dict(alt='Wind turbines along a ridge in Karnataka', by='Ashwin Kumar', licence='CC BY-SA 2.0',
                           source='Wind_farm_(6586101583).jpg'),
    'wind-farmland.jpg': dict(alt='Wind turbines above farmland near Chikodi, Belagavi district', by='Hbkfromckd108',
                              licence='CC BY-SA 4.0', source='Wind_Turbines_Chikodi.jpg'),
    'almatti-dam.jpg': dict(alt='', by='Nvvchar', licence='CC BY-SA 3.0',
                            source='Upstream_view_of_dam_and_reservoir_-_Almatti_dam.JPG'),
    'sharavathi.jpg': dict(alt='Sharavathi valley and hydroelectric station, Western Ghats', by='Thangaraj Kumaravel',
                           licence='CC BY 2.0', source='Sharavathi_hydroelectric_power_plant_Karnataka_India.jpg'),
    'pavagada-satellite.jpg': dict(alt='', by='Copernicus Sentinel-2, ESA',
                                   licence='contains modified Copernicus Sentinel data 2020',
                                   source='Pavagada_Solar_Park_2020.jpg'),
    'karnataka-map.svg': dict(alt='Map of Karnataka showing all 31 districts', by='C1MM', licence='CC BY-SA 3.0',
                              source='Karnataka_districts_map_-_Updated.svg'),
}

# The seven-step development sequence: homepage "Our Approach" and the services hub both show it
DEV_SEQUENCE = [
    ('Site screening', 'Resource, terrain, evacuation proximity and land-tenure pattern assessed together.'),
    ('Land feasibility', 'Revenue records, classification, ceiling and tenancy constraints verified before commitment.'),
    ('Aggregation strategy', 'Parcel sequencing and negotiation order designed to prevent hold-out leverage.'),
    ('Acquisition &amp; conveyance', 'Negotiation, documentation, registration, mutation.'),
    ('Statutory clearances', 'Approvals filed in dependency order across district, state and utility authorities.'),
    ('Transmission &amp; RoW', 'Corridor alignment, landowner settlement, access arrangements.'),
    ('Handover &amp; support', 'Land schedules, diligence packs, continued support through construction.'),
]
