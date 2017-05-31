
def includeme(config):
    config.include('.fanstatic_lib')
    #Static dir
    config.add_static_view('static_rfsu_app', 'static', cache_max_age=3600*5)
    #Override print template
    config.override_asset(to_override='voteit.irl:templates/',
                          override_with='rfsu_app:templates/overrides/')
