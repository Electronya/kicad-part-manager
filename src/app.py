from logger import initLogging

from pkgs.appComposer import AppComposer


def main():
    """
    Application main.
    """
    initLogging()
    app = AppComposer()
    app.run()


if __name__ == '__main__':
    main()
