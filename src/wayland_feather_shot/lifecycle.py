"""Pair manual application holds with GTK window removal."""


def release_on_window_removed(app, window):
    """Release a caller-owned hold once *window* leaves *app*.

    GTK holds the application for registered windows, but a separate manual
    hold needs its own release.  Widget disposal can happen after the window
    has closed, so the widget's ``destroy`` signal is too late for this job.
    """

    def on_removed(_app, removed):
        if removed is not window:
            return
        app.disconnect(handler_id)
        app.release()

    handler_id = app.connect("window-removed", on_removed)
