from core.utility_functions import resource_path


LIGHT = {
    "txt_color": "#2b2b2b",
    "btn_background_color": "#ffffff",
    "close_btn_background_color": "#ff0000",
    "close_btn_text_color": "#ffffff",
    "close_btn_background_color_hover": "#ffffff",
    "close_btn_text_color_hover": "#ff0000",
    "universal_btn_background_color": "#ffffff",
    "universal_btn_background_color_hover": "#242f60",
    "universal_btn_text_color_hover": "#ffffff",
    "universal_btn_link_color": "#0000ff",
    "logo": resource_path("assets/SU_Logo_Light.png"),
}

DARK = {
    "txt_color": "#ededed",
    "btn_background_color": "#535454",
    "close_btn_background_color": "#ff0000",
    "close_btn_text_color": "#ededed",
    "close_btn_background_color_hover": "#ffffff",
    "close_btn_text_color_hover": "#ff0000",
    "universal_btn_background_color": "#535454",
    "universal_btn_background_color_hover": "#30cbff",
    "universal_btn_text_color_hover": "#ededed",
    "universal_btn_link_color": "#30cbff",
    "logo": resource_path("assets/SU_Logo_Dark.png"),
}

THEMES = {
    "LIGHT": LIGHT,
    "DARK": DARK,
}
