from arche.interfaces import IBaseView
from arche.interfaces import IViewInitializedEvent
from fanstatic import Library
from fanstatic import Resource

from voteit.irl.fanstaticlib import voteit_irl_print_css

library = Library('rfsu_app', 'static')

rfsu_app_css = Resource(library, 'css/main.css', depends = (voteit_irl_print_css,))


def need_subscriber(view, event):
    rfsu_app_css.need()


def includeme(config):
    config.add_subscriber(need_subscriber, [IBaseView, IViewInitializedEvent])
