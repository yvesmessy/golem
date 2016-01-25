from gnrstartapp import start_app, config_logging
from renderingapplicationlogic import RenderingApplicationLogic
from gnr.ui.renderingmainwindow import RenderingMainWindow
from gnr.application import GNRGui
from gnr.customizers.renderingmainwindowcustomizer import RenderingMainWindowCustomizer


def main():
    config_logging()

    logic = RenderingApplicationLogic()
    app = GNRGui(logic, RenderingMainWindow)
    gui = RenderingMainWindowCustomizer

    start_app(logic, app, gui, rendering=True)


from multiprocessing import freeze_support

if __name__ == "__main__":
    freeze_support()
    main()