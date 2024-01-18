class Application:
    blocked = False

    def __init__(self, name) -> None:
        self.name = name


class AppStore:
    apps = []

    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        self.apps.remove(app)

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        return len(self.apps)


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
